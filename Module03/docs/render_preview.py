#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Approximate renderer for the generated PPTX (PIL based).
Purpose: visual QA - detect overflow / overlap / out-of-bounds elements.
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

from pptx import Presentation
from pptx.util import Emu
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.oxml.ns import qn

PX = 96.0 / 914400.0          # emu -> px at 96 dpi
SCALE = 1.0

FONTS = {
    ("Segoe UI", False, False): "/mnt/c/Windows/Fonts/segoeui.ttf",
    ("Segoe UI", True, False):  "/mnt/c/Windows/Fonts/segoeuib.ttf",
    ("Segoe UI", False, True):  "/mnt/c/Windows/Fonts/segoeuii.ttf",
    ("Segoe UI", True, True):   "/mnt/c/Windows/Fonts/segoeuiz.ttf",
    ("Segoe UI Semibold", False, False): "/mnt/c/Windows/Fonts/seguisb.ttf",
    ("Segoe UI Semibold", True, False):  "/mnt/c/Windows/Fonts/seguisb.ttf",
    ("Segoe UI Semibold", False, True):  "/mnt/c/Windows/Fonts/seguisbi.ttf",
    ("Segoe UI Semibold", True, True):   "/mnt/c/Windows/Fonts/seguisbi.ttf",
    ("Consolas", False, False): "/mnt/c/Windows/Fonts/consola.ttf",
    ("Consolas", True, False):  "/mnt/c/Windows/Fonts/consolab.ttf",
    ("Consolas", False, True):  "/mnt/c/Windows/Fonts/consolai.ttf",
    ("Consolas", True, True):   "/mnt/c/Windows/Fonts/consolaz.ttf",
    ("Arial", False, False): "/mnt/c/Windows/Fonts/arial.ttf",
    ("Arial", True, False):  "/mnt/c/Windows/Fonts/arialbd.ttf",
    ("Segoe UI Symbol", False, False): "/mnt/c/Windows/Fonts/seguisym.ttf",
    ("Segoe UI Symbol", True, False):  "/mnt/c/Windows/Fonts/seguisym.ttf",
    ("Segoe UI Symbol", False, True):  "/mnt/c/Windows/Fonts/seguisym.ttf",
    ("Segoe UI Symbol", True, True):   "/mnt/c/Windows/Fonts/seguisym.ttf",
}
_cache = {}


class _F(object):
    """PIL font wrapper that also carries the point size."""
    def __init__(self, f, size):
        self.f = f
        self.size = size

    def getlength(self, t):
        return self.f.getlength(t)

    def __getattr__(self, n):
        return getattr(self.f, n)


def font_for(name, size_pt, bold=False, italic=False):
    key = (name, bold, italic, round(size_pt, 1))
    if key in _cache:
        return _cache[key]
    path = FONTS.get((name, bold, italic)) or FONTS.get((name, False, False)) \
        or FONTS[("Segoe UI", False, False)]
    if not os.path.exists(path):
        path = "/mnt/c/Windows/Fonts/segoeui.ttf"
    try:
        f = ImageFont.truetype(path, max(1, int(round(size_pt * 96 / 72.0))),
                               layout_engine=ImageFont.Layout.BASIC)
    except Exception:
        f = ImageFont.truetype(path, max(1, int(round(size_pt * 96 / 72.0))))
    wrapped = _F(f, size_pt)
    _cache[key] = wrapped
    return wrapped


def solid_fill_rgb(shape):
    try:
        f = shape.fill
        if f.type is not None and f.type == 1:      # MSO_FILL.SOLID
            c = f.fore_color
            if c.type == 1:  # RGB
                return tuple(c.rgb)
    except Exception:
        pass
    return None


def line_rgb(shape):
    try:
        lf = shape.line.fill
        if lf.type == 1:
            c = shape.line.color
            if c.type == 1:
                return tuple(c.rgb)
    except Exception:
        pass
    return None


def shape_name(shape):
    try:
        return shape.shape_type
    except Exception:
        return None


def geom(shape):
    return shape._element.find(qn("p:spPr"))


def wrap_runs(runs, max_w):
    """runs: list of (text, font, colour). Returns list of lines, each a list of
    (text, font, colour)."""
    lines = [[]]
    cur = 0.0
    for text, fnt, col in runs:
        i = 0
        tokens = []
        buf = ""
        for ch in text:
            buf += ch
            if ch == " ":
                tokens.append(buf)
                buf = ""
        if buf:
            tokens.append(buf)
        for tok in tokens:
            w = fnt.getlength(tok)
            if cur + w > max_w and cur > 0:
                lines.append([])
                cur = 0.0
                tok_l = tok.lstrip(" ")
                w = fnt.getlength(tok_l)
                tok = tok_l
            lines[-1].append((tok, fnt, col))
            cur += w
    return lines


def para_lines(tf):
    """Yield lines for each paragraph, honouring <a:br/> line breaks."""
    from pptx.text.text import _Run
    for p in tf.paragraphs:
        cur = []
        for child in p._p.iterchildren():
            if child.tag == qn("a:r"):
                r = _Run(child, p)
                sz = r.font.size.pt if r.font.size else 18
                nm = r.font.name or "Segoe UI"
                bd = bool(r.font.bold)
                it = bool(r.font.italic)
                col = (0, 0, 0)
                try:
                    if r.font.color and r.font.color.type == 1:
                        col = tuple(r.font.color.rgb)
                except Exception:
                    pass
                cur.append((r.text, font_for(nm, sz, bd, it), col))
            elif child.tag == qn("a:br"):
                yield cur
                cur = []
        yield cur


def draw_tf(draw, shape, x, y, w, h, report, name):
    tf = shape.text_frame
    if not tf.text.strip():
        return
    try:
        ml = tf.margin_left.inches * 96 if tf.margin_left is not None else 0.1 * 96
        mr = tf.margin_right.inches * 96 if tf.margin_right is not None else 0.1 * 96
        mt = tf.margin_top.inches * 96 if tf.margin_top is not None else 0.05 * 96
    except Exception:
        ml = mr = 0.1 * 96
        mt = 0.05 * 96

    avail = max(10, w - ml - mr)
    cy = y + mt
    total = 0
    for runs in para_lines(tf):
        if not runs:
            cy += 10
            total += 10
            continue
        lines = wrap_runs(runs, avail)
        maxsz = max((f.size if hasattr(f, "size") else 18) for _, f, _ in runs)
        for _, f, _ in runs:
            try:
                maxsz = max(maxsz, f.size)
            except Exception:
                pass
        lh = 12
        for ln in lines:
            lx = x + ml
            for t, f, c in ln:
                draw.text((lx, cy), t, font=f, fill=c)
                lx += f.getlength(t)
            try:
                lh = max(f.size for _, f, _ in ln) * 1.28 * 96 / 72.0
            except Exception:
                lh = 12
            cy += lh
            total += lh
    if total > h + 12:
        report.append("  OVERFLOW %-28s box_h=%.0fpx text_h=%.0fpx  %r"
                      % (name, h, total, shape.text_frame.text[:60]))


def rot_pts(pts, cx, cy, deg):
    import math
    if not deg:
        return pts
    a = math.radians(deg)
    ca, sa = math.cos(a), math.sin(a)
    out = []
    for (px, py) in pts:
        dx, dy = px - cx, py - cy
        out.append((cx + dx * ca - dy * sa, cy + dx * sa + dy * ca))
    return out


def render(pptx_path, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    prs = Presentation(pptx_path)
    W = int(prs.slide_width * PX)
    H = int(prs.slide_height * PX)
    issues = []
    for idx, slide in enumerate(prs.slides, 1):
        img = Image.new("RGB", (W, H), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        rep = []
        for sh in slide.shapes:
            try:
                x = sh.left * PX
                y = sh.top * PX
                w = sh.width * PX
                h = sh.height * PX
            except Exception:
                continue
            if x < -2 or y < -2 or x + w > W + 2 or y + h > H + 2:
                rep.append("  OUT-OF-BOUNDS %s x=%.0f y=%.0f w=%.0f h=%.0f"
                           % (sh.shape_type, x, y, w, h))
            # crosses the footer rule (6.88in) ?
            if (y < 6.85 * 96 and y + h > 6.85 * 96 and h > 0.15 * 96
                    and not (w >= W - 4 and h >= H - 4)):
                rep.append("  CROSSES-FOOTER %s y=%.0f h=%.0f bottom=%.0f  %r"
                           % (sh.shape_type, y, h, y + h,
                              (sh.text_frame.text[:40] if sh.has_text_frame else "")))
            fill = solid_fill_rgb(sh)
            lcol = line_rgb(sh)
            st = shape_name(sh)
            if st == MSO_SHAPE_TYPE.TABLE:
                draw_table(draw, sh, x, y, w, h, rep)
                continue
            if st == MSO_SHAPE_TYPE.LINE:
                try:
                    draw.line([sh.begin_x * PX, sh.begin_y * PX,
                               sh.end_x * PX, sh.end_y * PX],
                              fill=lcol or (0, 0, 0), width=2)
                except Exception:
                    draw.line([x, y, x + w, y + h], fill=(0, 0, 0), width=2)
                continue
            if sh.has_text_frame and fill is None and lcol is None:
                pass
            else:
                if fill is not None or lcol is not None:
                    outline = lcol if lcol else None
                    width = 1
                    try:
                        if sh.line.width:
                            width = max(1, int(sh.line.width.pt * 96 / 72.0))
                    except Exception:
                        pass
                    pr = geom(sh)
                    gname = ""
                    if pr is not None:
                        pg = pr.find(qn("a:prstGeom"))
                        if pg is not None:
                            gname = pg.get("prst") or ""
                    rot = 0.0
                    try:
                        rot = sh.rotation or 0.0
                    except Exception:
                        rot = 0.0
                    if gname == "ellipse":
                        draw.ellipse([x, y, x + w, y + h], fill=fill, outline=outline,
                                     width=width)
                    elif gname == "triangle":
                        pts = [(x + w / 2, y), (x + w, y + h), (x, y + h)]
                        draw.polygon(rot_pts(pts, x + w / 2, y + h / 2, rot),
                                     fill=fill, outline=outline)
                    elif gname == "roundRect":
                        draw.rounded_rectangle([x, y, x + w, y + h], radius=min(w, h) * 0.12,
                                               fill=fill, outline=outline, width=width)
                    else:
                        draw.rectangle([x, y, x + w, y + h], fill=fill, outline=outline,
                                       width=width)
            if sh.has_text_frame:
                draw_tf(draw, sh, x, y, w, h, rep, str(st))
        img.save(os.path.join(out_dir, "slide_%02d.png" % idx))
        # overlap detection: a later opaque shape covering an earlier text shape
        boxes = []
        for sh in slide.shapes:
            try:
                boxes.append((sh, sh.left * PX, sh.top * PX, sh.width * PX, sh.height * PX,
                              solid_fill_rgb(sh) is not None,
                              sh.has_text_frame and bool(sh.text_frame.text.strip())))
            except Exception:
                pass
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                _, x1, y1, w1, h1, opaque1, txt1 = boxes[i]
                _, x2, y2, w2, h2, opaque2, txt2 = boxes[j]
                if not (opaque2 and txt1):
                    continue
                ox = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
                oy = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))
                area = ox * oy
                small = min(w1 * h1, w2 * h2)
                if small > 0 and area > 0.25 * small and area > 300:
                    rep.append("  OVERLAP  later-opaque covers earlier text  "
                               "overlap=%.0fpx  %r"
                               % (area, boxes[j][0].text_frame.text[:40]
                                  if boxes[j][0].has_text_frame else ""))
                # text drawn on top of an earlier opaque block
                if txt2 and opaque1:
                    ox2 = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
                    oy2 = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))
                    a2 = ox2 * oy2
                    s2 = min(w1 * h1, w2 * h2)
                    if s2 > 0 and a2 > 0.30 * s2 and a2 > 400:
                        rep.append("  OVERLAP  text drawn over an opaque block  "
                                   "overlap=%.0fpx  %r"
                                   % (a2, boxes[j][0].text_frame.text[:45]))
        if rep:
            issues.append("slide %d:" % idx)
            issues.extend(rep)
    print("\n".join(issues) if issues else "no geometry issues detected")
    return issues


def draw_table(draw, gf, x, y, w, h, rep):
    tbl = gf.table
    nrows = len(tbl.rows)
    ncols = len(tbl.columns)
    cw = [c.width * PX for c in tbl.columns]
    rh = [r.height * PX for r in tbl.rows]
    cy = y
    for r in range(nrows):
        cx = x
        for c in range(ncols):
            cell = tbl.cell(r, c)
            try:
                fc = tuple(cell.fill.fore_color.rgb) if cell.fill.type == 1 else None
            except Exception:
                fc = None
            draw.rectangle([cx, cy, cx + cw[c], cy + rh[r]], fill=fc,
                           outline=(217, 223, 234), width=1)
            tf = cell.text_frame
            ml = cell.margin_left * PX
            mr = cell.margin_right * PX
            mt = cell.margin_top * PX
            runs = []
            for p in tf.paragraphs:
                for run in p.runs:
                    sz = run.font.size.pt if run.font.size else 12
                    nm = run.font.name or "Segoe UI"
                    bd = bool(run.font.bold)
                    it = bool(run.font.italic)
                    col = (0, 0, 0)
                    try:
                        if run.font.color and run.font.color.type == 1:
                            col = tuple(run.font.color.rgb)
                    except Exception:
                        pass
                    runs.append((run.text, font_for(nm, sz, bd, it), col))
            if runs:
                lines = wrap_runs(runs, cw[c] - ml - mr)
                maxsz = max((run.font.size.pt if run.font.size else 12)
                            for p in tf.paragraphs for run in p.runs)
                lh = maxsz * 96 / 72.0 * 1.2
                ty = cy + max(mt, (rh[r] - len(lines) * lh) / 2)
                for ln in lines:
                    lx = cx + ml
                    for t, f, cc in ln:
                        draw.text((lx, ty), t, font=f, fill=cc)
                        lx += f.getlength(t)
                    ty += lh
                if ty > cy + rh[r] + 2:
                    rep.append("  TABLE CELL OVERFLOW r%d c%d  %r"
                               % (r, c, tf.text[:50]))
            cx += cw[c]
        cy += rh[r]


if __name__ == "__main__":
    pptx = sys.argv[1]
    out = sys.argv[2]
    render(pptx, out)
