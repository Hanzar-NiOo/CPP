import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ppt_theme import *  # noqa: F401,F403

OUT_NAME = os.environ.get("PPTX_OUT") or os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "Module03_CPP_Presentation.pptx"))


# ==========================================================================
# SLIDES
# ==========================================================================
def s_title(prs):
    s = blank(prs)
    bg_page(s, NAVY)
    rect(s, 0, 0, Inches(0.16), SH, fill=ORANGE)
    rect(s, SW - Inches(4.4), 0, Inches(4.4), SH, fill=NAVY_2)
    for i in range(5):
        for j in range(7):
            rect(s, SW - Inches(3.85) + Inches(0.46) * j,
                 Inches(1.05) + Inches(0.42) * i, Inches(0.1), Inches(0.1),
                 fill=NAVY_3, shape=MSO_SHAPE.OVAL)
    mx = SW - Inches(2.0)
    for (dx, dy) in ((0, 0), (-0.95, 0.95), (0.95, 0.95)):
        rect(s, mx + Inches(dx) - Inches(0.42), Inches(5.25) + Inches(dy),
             Inches(0.84), Inches(0.42),
             fill=ORANGE if (dx == 0 and dy == 0) else NAVY_3,
             shape=MSO_SHAPE.ROUNDED_RECTANGLE, adj=0.18)

    text(s, Inches(0.95), Inches(1.30), Inches(8.0), Inches(0.3),
         "42 SCHOOL  ·  C++ MODULE 03  ·  EVALUATION", size=12,
         color=ORANGE, font=FONT_B, bold=True)
    text(s, Inches(0.95), Inches(1.82), Inches(8.2), Inches(2.45),
         "Inheritance,\nInterfaces &\nPolymorphism", size=40, color=WHITE,
         font=FONT_B, bold=True, line_spacing=1.05)
    rect(s, Inches(0.95), Inches(4.32), Inches(1.3), Inches(0.06), fill=ORANGE)
    text(s, Inches(0.95), Inches(4.58), Inches(8.0), Inches(0.4),
         "ClapTrap  →  ScavTrap  →  FragTrap  →  DiamondTrap", size=16,
         color=RGBColor(0x9F, 0xB3, 0xCC), font=MONO)
    text(s, Inches(0.95), Inches(5.18), Inches(8.0), Inches(0.9),
         "Step-by-step implementation, design decisions and runtime proof\n"
         "of exercises ex00 – ex03", size=12.5,
         color=RGBColor(0x76, 0x8B, 0xA6), line_spacing=1.35)
    rect(s, Inches(0.95), Inches(6.30), Inches(6.2), Emu(9525), fill=NAVY_3)
    text(s, Inches(0.95), Inches(6.50), Inches(8.0), Inches(0.3),
         "Name: ____________     Promotion: ____________     Date: ________",
         size=11, color=RGBColor(0x5E, 0x73, 0x8C))
    PAGE_NO[0] += 1
    return s


def s_agenda(prs):
    s = content_slide(prs, "Agenda", "what this presentation covers")
    left = [
        (0, "**Part 1 — The subject**"),
        (1, "What Module 03 asks, in one slide"),
        (1, "The class hierarchy we are going to build"),
        (0, "**Part 2 — The knowledge you need**"),
        (1, "Inheritance, virtual functions, dynamic binding"),
        (1, "The Diamond problem and virtual inheritance"),
        (1, "Access specifiers, abstract classes, the Rule of Three"),
    ]
    right = [
        (0, "**Part 3 — Implementation, step by step**"),
        (1, "ex00 — ClapTrap: the base class"),
        (1, "ex01 — ScavTrap: the first inheritance"),
        (1, "ex02 — FragTrap: the second branch"),
        (1, "ex03 — DiamondTrap: the diamond"),
        (0, "**Part 4 — Proof and reflection**"),
        (1, "Runtime output, norms, pitfalls, conclusion"),
    ]
    bullets(s, ML, BODY_TOP, CW * 0.47, left, size=14, gap=0.13,
            max_h=Inches(3.9))
    bullets(s, ML + CW * 0.53, BODY_TOP, CW * 0.47, right, size=14, gap=0.13,
            max_h=Inches(3.9))
    callout(s, ML, Inches(5.55), CW, "The one-sentence version",
            "This module teaches how to **reuse** a class (inheritance), how to make one "
            "function behave differently depending on the real object (**polymorphism**), "
            "and how to solve the **Diamond problem** that appears as soon as two "
            "branches of a hierarchy meet.",
            accent=TEAL, bg=TEAL_L, size=12.5, h=Inches(1.0))
    return s


def s_subject(prs):
    s = content_slide(prs, "The Module 03 subject in one slide", "part 1 · the subject")
    rows = [
        ["Ex.", "Subject name", "What it asks for", "New concept"],
        ["ex00", "Aaaaand... OPEN!",
         "A `ClapTrap`: name, 10 HP, 10 energy, 0 damage; `attack()`, `takeDamage()`, "
         "`beRepaired()`; private attributes + getters/setters",
         "Class design,\nencapsulation"],
        ["ex01", "Serena, my love!",
         "A `ScavTrap` that **inherits** `ClapTrap`, overrides `attack()`, adds "
         "`guardGate()`; 100 HP / 50 energy / 20 damage",
         "Inheritance,\noverriding"],
        ["ex02", "Repetitive work",
         "A `FragTrap` that **also** inherits `ClapTrap`, adds `highFivesGuys()`; "
         "100 HP / 100 energy / 30 damage",
         "Code reuse,\nsub-classing"],
        ["ex03", "Now it's weird!",
         "A `DiamondTrap` inheriting **both** `ScavTrap` and `FragTrap`, with "
         "`whoAmI()` printing both names",
         "The Diamond,\nvirtual inheritance"],
    ]
    table(s, ML, BODY_TOP, CW, rows, col_w=[0.7, 1.7, 6.9, 1.9], size=11.5,
          row_h=0.92, head_h=0.40)
    callout(s, ML, Inches(5.85), CW * 0.485, "“Interfaces” in the title",
            "Not a Java-style `interface` keyword: it is the **set of public methods** "
            "(`attack`, `takeDamage`, `beRepaired`) shared by every trap, and that we "
            "use **polymorphically** through a `ClapTrap*`.",
            accent=TEAL, bg=TEAL_L, size=11.5, h=Inches(0.95))
    callout(s, ML + CW * 0.515, Inches(5.85), CW * 0.485, "Mandatory build flags",
            "`c++ -Wall -Wextra -Werror -std=c++98` — every warning is an **error**. "
            "C++98 means: no `nullptr`, no `override`, no `auto`, no range-`for`.",
            accent=ORANGE, bg=ORANGE_L, size=11.5, h=Inches(0.95))
    return s


def s_roadmap(prs):
    s = content_slide(prs, "The class hierarchy we are going to build",
                      "part 1 · roadmap")
    cx = SW / 2
    base_y = Inches(1.80)
    class_box(s, cx - Inches(1.55), base_y, Inches(3.1), Inches(1.25), "ClapTrap",
              ["name_, hitPoints_,", "energyPoints_, attackDamage_",
               "virtual void attack()"], head=NAVY, size=9.5, name_size=15)
    mid_y = Inches(3.75)
    class_box(s, cx - Inches(3.95), mid_y, Inches(3.0), Inches(1.00), "ScavTrap",
              ["guardGate()", "void attack()   // override"], head=TEAL, size=9.5)
    class_box(s, cx + Inches(0.95), mid_y, Inches(3.0), Inches(1.00), "FragTrap",
              ["highFivesGuys()"], head=ORANGE, size=9.5)
    low_y = Inches(5.40)
    class_box(s, cx - Inches(1.65), low_y, Inches(3.3), Inches(0.95), "DiamondTrap",
              ["whoAmI()  +  name_"], head=NAVY_3, size=9.5)
    arrow_to(s, cx - Inches(2.45), mid_y, cx - Inches(0.80), base_y + Inches(1.25))
    arrow_to(s, cx + Inches(2.45), mid_y, cx + Inches(0.80), base_y + Inches(1.25))
    arrow_to(s, cx - Inches(1.05), low_y, cx - Inches(2.00), mid_y + Inches(1.00),
             color=NAVY_3)
    arrow_to(s, cx + Inches(1.05), low_y, cx + Inches(2.00), mid_y + Inches(1.00),
             color=NAVY_3)
    text(s, ML, Inches(6.10), Inches(3.3), Inches(0.6),
         "One base class, two branches,\none shared base", size=12.5, color=GREY,
         line_spacing=1.3)
    for lbl, lx, ly in (("ex00", cx - Inches(2.35), base_y + Inches(0.09)),
                        ("ex01", cx - Inches(4.60), mid_y + Inches(0.09)),
                        ("ex02", cx + Inches(3.30), mid_y + Inches(0.09)),
                        ("ex03", cx - Inches(2.35), low_y + Inches(0.09))):
        text(s, lx, ly, Inches(0.7), Inches(0.25), lbl, size=10.5, color=GREY_L,
             font=FONT_B, bold=True)
    return s


def s_concept(prs, title, kicker, items, code, code_title, note=None):
    s = content_slide(prs, title, kicker, accent=TEAL)
    bullets(s, ML, BODY_TOP, CW * 0.45, items, size=13.5, gap=0.13,
            max_h=Inches(4.05))
    code_panel(s, ML + CW * 0.48, BODY_TOP, CW * 0.52, code, max_h=Inches(5.0),
               title=code_title)
    if note:
        callout(s, ML, Inches(5.72), CW * 0.45, note[0], note[1], accent=ORANGE,
                bg=ORANGE_L, size=11.5, h=Inches(0.95))
    return s


def s_ex00_intro(prs):
    s = content_slide(prs, "ex00 — Aaaaand... OPEN!", "part 3 · ex00 · the base class",
                      accent=ORANGE)
    items = [
        (0, "**The subject**"),
        (1, "A `ClapTrap` with a **private** name, **10 HP**, **10 energy**, **0 damage**."),
        (1, "Public: `attack()`, `takeDamage()`, `beRepaired()` + the getters."),
        (1, "The ctor, dtor, **copy ctor** and **`operator=`** all print a message."),
        (0, "**What I add on top**"),
        (1, "`attack()` is `virtual` from the very first exercise — the foundation of "
            "ex01 / ex02 / ex03."),
        (1, "The attributes stay `private`; the derived classes update them through "
            "`protected` setters — exactly *“update ClapTrap accordingly”*."),
    ]
    bullets(s, ML, BODY_TOP, CW * 0.42, items, size=13, gap=0.12,
            max_h=Inches(3.35))
    code = """class ClapTrap
{
private:
\tstd::string  name_;
\tunsigned int hitPoints_;
\tunsigned int energyPoints_;
\tunsigned int attackDamage_;

public:
\tClapTrap();
\tClapTrap(std::string const & name);
\tClapTrap(ClapTrap const & other);
\tClapTrap & operator=(ClapTrap const & other);
\tvirtual ~ClapTrap();

\tvirtual void attack(std::string const & target);
\tvoid takeDamage(unsigned int amount);
\tvoid beRepaired(unsigned int amount);

\tstd::string const & getName() const;
\tunsigned int getHitPoints() const;   // + the 3 other getters

protected:
\tvoid setHitPoints(unsigned int hitPoints);
\tvoid setEnergyPoints(unsigned int energyPoints);
\tvoid setAttackDamage(unsigned int attackDamage);
};"""
    code_panel(s, ML + CW * 0.45, BODY_TOP, CW * 0.55, code, max_h=Inches(5.0),
               title="include/ClapTrap.hpp", size=10)
    callout(s, ML, Inches(5.05), CW * 0.42, "Why `virtual` already in ex00?",
            "The subject does not require it in this exercise, but it is the "
            "**foundation** of the three next ones: without `virtual` on `attack()`, "
            "`ScavTrap` could not override it and no polymorphism would be possible.",
            accent=TEAL, bg=TEAL_L, size=11.5, h=Inches(1.25))
    return s


def s_ex00_ctor(prs):
    s = content_slide(prs, "ex00 — Constructors and the initializer list",
                      "ex00 · step 1", accent=ORANGE)
    code = """ClapTrap::ClapTrap(std::string const & name)
\t: name_(name),
\t  hitPoints_(10),
\t  energyPoints_(10),
\t  attackDamage_(0)
{
\tstd::cout << "ClapTrap: " << name_
\t\t\t  << " has been created." << std::endl;
}

ClapTrap::ClapTrap(ClapTrap const & other)
\t: name_(other.name_),
\t  hitPoints_(other.hitPoints_),
\t  energyPoints_(other.energyPoints_),
\t  attackDamage_(other.attackDamage_)
{
\tstd::cout << "ClapTrap: a copy of " << name_
\t\t\t  << " has been created." << std::endl;
}"""
    code_panel(s, ML, BODY_TOP, CW * 0.50, code, max_h=Inches(2.95),
               title="src/ClapTrap.cpp", size=10.5)
    items = [
        (0, "**Why the initializer list?**"),
        (1, "Members are initialised **before** the constructor body runs."),
        (1, "It avoids a temporary + an assignment, and it is the only way to "
            "initialise a `const` member."),
        (0, "**Order matters**"),
        (1, "Members are initialised in their **declaration** order — a different "
            "order triggers `-Wreorder`, and `-Werror` turns that into a build failure."),
        (0, "**The four special members (Rule of Three + default ctor)**"),
        (1, "Default ctor → the *“naked”* robot.   Copy ctor → copies the four members."),
        (1, "`operator=` → member by member, guarded by `if (this != &other)`."),
        (1, "Destructor → `virtual`, so `delete` through a base pointer is safe."),
    ]
    bullets(s, ML + CW * 0.53, BODY_TOP, CW * 0.47, items, size=13, gap=0.12,
            max_h=Inches(3.2))
    callout(s, ML, Inches(4.95), CW * 0.50, "Copy ctor vs. assignment operator",
            "The copy constructor **builds a new object** from an existing one; the "
            "assignment operator **overwrites** an existing object. The subject wants a "
            "message in both cases, so both print one.",
            accent=TEAL, bg=TEAL_L, size=11.5, h=Inches(1.05))
    callout(s, ML + CW * 0.53, Inches(4.95), CW * 0.47, "The self-assignment guard",
            "`if (this != &other)` avoids copying an object onto itself. Without it, "
            "`a = a;` could destroy the data before copying it. The operator also "
            "returns `*this` so that `a = b = c;` works.",
            accent=ORANGE, bg=ORANGE_L, size=11.5, h=Inches(1.05))
    return s


def s_ex00_attack(prs):
    s = content_slide(prs, "ex00 — attack(), takeDamage() and beRepaired()",
                      "ex00 · step 2", accent=ORANGE)
    code = """void ClapTrap::attack(std::string const & target)
{
\tif (!hasHitPoints())
\t{
\t\tstd::cout << "ClapTrap " << name_
\t\t\t\t  << " is out of hit points and cannot attack."
\t\t\t\t  << std::endl;
\t\treturn;
\t}
\tif (!hasEnergy())
\t{
\t\tstd::cout << "ClapTrap " << name_
\t\t\t\t  << " is out of energy and cannot attack."
\t\t\t\t  << std::endl;
\t\treturn;
\t}
\tconsumeEnergy();
\tstd::cout << "ClapTrap " << name_ << " attacks " << target
\t\t\t  << ", causing " << attackDamage_
\t\t\t  << " points of damage!" << std::endl;
}"""
    code_panel(s, ML, BODY_TOP, CW * 0.52, code, max_h=Inches(4.2),
               title="src/ClapTrap.cpp", size=10.2)
    items = [
        (0, "**The rules of the subject, in code**"),
        (1, "No hit points → nothing happens, we `return` early."),
        (1, "No energy → nothing happens, we `return` early."),
        (1, "Otherwise **1 energy point** is consumed and the damage is printed."),
        (1, "`takeDamage()` never goes below 0: `if (amount > hitPoints_) hitPoints_ = 0;`"),
        (1, "`beRepaired()` also costs **1 energy point** and **adds** hit points."),
        (0, "**Why the small protected helpers?**"),
        (1, "`hasHitPoints()`, `hasEnergy()` and `consumeEnergy()` are `protected`, so "
            "the derived classes reuse them instead of repeating the logic."),
    ]
    bullets(s, ML + CW * 0.55, BODY_TOP, CW * 0.45, items, size=13, gap=0.12,
            max_h=Inches(4.2))
    return s


def s_ex00_setter(prs):
    s = content_slide(prs, "ex00 — The `protected` setter pattern",
                      "ex00 · step 3 · a key design choice", accent=ORANGE)
    left = [
        (0, "**The problem**"),
        (1, "The subject says the attributes are **private** …"),
        (1, "… but ex01 / ex02 must give their robot **100 HP / 50 energy / 20 damage**."),
        (1, "A derived class **cannot** touch a `private` member of its base."),
        (0, "**Three possible solutions**"),
        (1, "**A.** Make them `protected` → breaks the subject (they must be private)."),
        (1, "**B.** Make them `public` → breaks encapsulation, forbidden."),
        (1, "**C.** Keep them `private` + add `protected` setters → **what I did**."),
    ]
    bullets(s, ML, BODY_TOP, CW * 0.44, left, size=13.5, gap=0.12,
            max_h=Inches(3.55))
    right = [
        (0, "**How it works**"),
        (1, "`private` data stays invisible to the outside world."),
        (1, "`protected` setters are reachable **only** by the class and its children."),
        (1, "The setter is the single controlled entry point — it can validate."),
        (1, "This is exactly the *“update ClapTrap accordingly”* of ex01 / ex02."),
    ]
    bullets(s, ML, Inches(5.35), CW * 0.44, right, size=13.5, gap=0.12,
            max_h=Inches(1.4))
    code = """//  header - the protected section
protected:
\tvoid setHitPoints(unsigned int hitPoints);
\tvoid setEnergyPoints(unsigned int energyPoints);
\tvoid setAttackDamage(unsigned int attackDamage);

//  implementation
void ClapTrap::setHitPoints(unsigned int hitPoints)
{
\thitPoints_ = hitPoints;
}

//  used by the derived classes (ex01 / ex02)
ScavTrap::ScavTrap(std::string const & name)
\t: ClapTrap(name)
{
\tsetHitPoints(100);
\tsetEnergyPoints(50);
\tsetAttackDamage(20);
}"""
    code_panel(s, ML + CW * 0.47, BODY_TOP, CW * 0.53, code, max_h=Inches(4.9),
               title="the pattern in action", size=10.5)
    return s


def s_ex00_main(prs):
    s = content_slide(prs, "ex00 — main.cpp: how I test", "ex00 · step 4", accent=ORANGE)
    code = """static void testCombat()
{
\tstd::cout << "--- testCombat: a ClapTrap fights ---" << std::endl;

\tClapTrap robot("Clappy");
\trobot.attack("target-1");
\trobot.attack("target-2");
\trobot.takeDamage(4);
\trobot.beRepaired(2);

\tstd::cout << "Clappy now has " << robot.getHitPoints()
\t\t\t  << " hit points, " << robot.getEnergyPoints()
\t\t\t  << " energy points and " << robot.getAttackDamage()
\t\t\t  << " attack damage." << std::endl;
}"""
    code_panel(s, ML, BODY_TOP, CW * 0.52, code, max_h=Inches(3.2),
               title="src/main.cpp", size=10.5)
    items = [
        (0, "**4 test functions, each in its own scope `{ }`**"),
        (1, "`testCombat()` — the nominal case: attack, take damage, repair."),
        (1, "`testNoEnergy()` — 12 attacks in a row: the 11th and 12th must fail."),
        (1, "`testDestruction()` — 50 damage on 10 HP → 0 HP → attacking refused."),
        (1, "`testCopy()` — copy constructor and assignment operator."),
        (0, "**Why it matters for the evaluation**"),
        (1, "It proves every rule of the subject, and the printed output is the "
            "**proof** that the implementation behaves as required."),
    ]
    bullets(s, ML + CW * 0.55, BODY_TOP, CW * 0.45, items, size=13, gap=0.12,
            max_h=Inches(3.4))
    return s


def s_ex00_proof(prs):
    s = content_slide(prs, "ex00 — Runtime proof", "ex00 · proof", accent=ORANGE)
    out = """=== Module 03 - ex00: Aaaaand... OPEN! ===
--- testCombat: a ClapTrap fights ---
ClapTrap: Clappy has been created.
ClapTrap Clappy attacks target-1, causing 0 points of damage!
ClapTrap Clappy attacks target-2, causing 0 points of damage!
ClapTrap Clappy takes 4 points of damage, it has 6 hit points left!
ClapTrap Clappy is repaired by 2 points, it has 8 hit points!
Clappy now has 8 hit points, 7 energy points and 0 attack damage.
ClapTrap: Clappy has been destroyed.
--- testNoEnergy: energy points are consumed ---
ClapTrap Energyless attacks a wall, causing 0 points of damage!   (x10)
ClapTrap Energyless is out of energy and cannot attack.
ClapTrap Energyless is out of energy and cannot attack.
Energyless has 0 energy points left.
--- testDestruction: no hit points left ---
ClapTrap Doomed takes 50 points of damage, it has 0 hit points left!
ClapTrap Doomed is out of hit points and cannot attack.
ClapTrap Doomed is repaired by 10 points, it has 10 hit points!
--- testCopy: copy constructor and assignment ---
ClapTrap: a copy of Original has been created.
copy is named Original and has 7 hit points.
ClapTrap: Original has been assigned from another ClapTrap.
assigned is named Original and has 7 hit points.
=== ex00 done ==="""
    code_panel(s, ML, BODY_TOP, CW * 0.55, out, max_h=Inches(4.9), term=True,
               title="terminal  ·  ./ex00", size=10)
    items = [
        (0, "**What the output proves**"),
        (1, "`Clappy` starts with 10 HP; −4 → 6; repaired by 2 → 8. ✔"),
        (1, "2 attacks + 1 repair consumed **3 energy** → 10 − 3 = 7. ✔"),
        (1, "10 attacks succeed, the 11th and 12th are refused → energy is consumed "
            "**one point at a time**. ✔"),
        (1, "50 damage on 10 HP leaves **exactly 0** HP, never negative. ✔"),
        (1, "The copy and the assignment both carry the **7 HP** of the original. ✔"),
        (1, "The destructor message proves the object is destroyed at the end of "
            "each scope. ✔"),
    ]
    bullets(s, ML + CW * 0.575, BODY_TOP, CW * 0.425, items, size=12.5, gap=0.11,
            max_h=Inches(4.9))
    return s


def s_ex01_intro(prs):
    s = content_slide(prs, "ex01 — Serena, my love!",
                      "part 3 · ex01 · the first inheritance", accent=TEAL)
    code = """#ifndef SCAVTRAP_HPP
#define SCAVTRAP_HPP

#include "ClapTrap.hpp"

class ScavTrap : public virtual ClapTrap
{
public:
\tScavTrap();
\tScavTrap(std::string const & name);
\tScavTrap(ScavTrap const & other);
\tScavTrap & operator=(ScavTrap const & other);
\tvirtual ~ScavTrap();

\tvirtual void attack(std::string const & target);
\tvoid guardGate();
};

#endif"""
    code_panel(s, ML, BODY_TOP, CW * 0.46, code, max_h=Inches(3.5),
               title="include/ScavTrap.hpp", size=10.5)
    items = [
        (0, "**The subject**"),
        (1, "`ScavTrap` **inherits** `ClapTrap` and adds a special ability."),
        (1, "It **overrides** `attack()` with its own message."),
        (1, "It is initialised with **100 HP / 50 energy / 20 damage**."),
        (1, "Its ctor and dtor print their **own** messages."),
        (0, "**Reading the class declaration**"),
        (1, "`public` → the inherited public methods stay **public**."),
        (1, "`virtual` → `ClapTrap` becomes a **virtual base**; this is what makes "
            "the diamond of ex03 possible."),
        (1, "`#include \"ClapTrap.hpp\"` → every header is **self-contained**."),
    ]
    bullets(s, ML + CW * 0.52, BODY_TOP, CW * 0.48, items, size=13, gap=0.12,
            max_h=Inches(4.0))
    callout(s, ML, Inches(5.35), CW * 0.46, "Why `virtual` already in ex01?",
            "Nothing forces it here — the behaviour is identical. But adding it now "
            "means ex03 only has to write `class DiamondTrap : public FragTrap, "
            "public ScavTrap` with **no change** to the existing classes.",
            accent=ORANGE, bg=ORANGE_L, size=11.5, h=Inches(1.05))
    return s


def s_ex01_ctor(prs):
    s = content_slide(prs, "ex01 — Constructor chaining", "ex01 · step 1", accent=TEAL)
    code = """ScavTrap::ScavTrap(std::string const & name)
\t: ClapTrap(name)
{
\tsetHitPoints(100);
\tsetEnergyPoints(50);
\tsetAttackDamage(20);
\tstd::cout << "ScavTrap: " << getName()
\t\t\t  << " is ready to fight!" << std::endl;
}

ScavTrap::ScavTrap(ScavTrap const & other)
\t: ClapTrap(other)
{
\tstd::cout << "ScavTrap: a copy of " << getName()
\t\t\t  << " is ready to fight!" << std::endl;
}"""
    code_panel(s, ML, BODY_TOP, CW * 0.50, code, max_h=Inches(3.1),
               title="src/ScavTrap.cpp", size=10.5)
    items = [
        (0, "**The mechanism**"),
        (1, "`: ClapTrap(name)` is the **initializer list**: it calls the base "
            "constructor *before* the body of `ScavTrap`'s constructor runs."),
        (1, "C++ has no `super` — the base is called **by name**."),
        (1, "The base is built first, so `getName()` already returns the right value "
            "inside the derived constructor."),
        (0, "**The order is guaranteed by the language**"),
        (1, "Construction: **base → derived**."),
        (1, "Destruction: **derived → base** (the exact reverse)."),
    ]
    bullets(s, ML + CW * 0.53, BODY_TOP, CW * 0.47, items, size=13, gap=0.12,
            max_h=Inches(3.2))
    callout(s, ML, Inches(4.95), CW, "Proof taken from the output",
            "Construction:   `ClapTrap: Scavvy has been created.`  →  "
            "`ScavTrap: Scavvy is ready to fight!`\n"
            "Destruction:   `ScavTrap: Scavvy has been destroyed.`  →  "
            "`ClapTrap: Scavvy has been destroyed.`",
            accent=TEAL, bg=TEAL_L, size=12, h=Inches(1.05))
    return s


def s_ex01_override(prs):
    s = content_slide(prs, "ex01 — Overriding attack(), adding guardGate()",
                      "ex01 · step 2", accent=TEAL)
    code = """//  in the header - same signature as the base
virtual void attack(std::string const & target);

//  in the .cpp - the override
void ScavTrap::attack(std::string const & target)
{
\tif (!hasHitPoints())
\t{
\t\tstd::cout << "ScavTrap " << getName()
\t\t\t\t  << " is out of hit points and cannot attack."
\t\t\t\t  << std::endl;
\t\treturn;
\t}
\tif (!hasEnergy())
\t{
\t\tstd::cout << "ScavTrap " << getName()
\t\t\t\t  << " is out of energy and cannot attack."
\t\t\t\t  << std::endl;
\t\treturn;
\t}
\tconsumeEnergy();
\tstd::cout << "ScavTrap " << getName() << " attacks " << target
\t\t\t  << ", causing " << getAttackDamage()
\t\t\t  << " points of damage!" << std::endl;
}

void ScavTrap::guardGate()
{
\tstd::cout << "ScavTrap " << getName()
\t\t\t  << " is now in Gate keeper mode!" << std::endl;
}"""
    code_panel(s, ML, BODY_TOP, CW * 0.53, code, max_h=Inches(4.5),
               title="src/ScavTrap.cpp", size=9.6)
    items = [
        (0, "**What an override is**"),
        (1, "The derived class declares a method with the **exact same signature** "
            "as a `virtual` base method."),
        (1, "The base method must be `virtual`, otherwise the base version always runs."),
        (1, "The override **replaces** the behaviour, it does not add to it."),
        (0, "**The three rules of an override**"),
        (1, "Same name, same parameters, same return type."),
        (1, "The base method is `virtual`."),
        (1, "The access level may differ — mine stays `public`."),
        (0, "**And a brand-new method**"),
        (1, "`guardGate()` simply does not exist in the base — a derived class can add "
            "new abilities too."),
    ]
    bullets(s, ML + CW * 0.56, BODY_TOP, CW * 0.44, items, size=12.5, gap=0.11,
            max_h=Inches(4.5))
    return s


def s_ex01_poly(prs):
    s = content_slide(prs, "ex01 — Polymorphism through a base pointer",
                      "ex01 · step 3", accent=TEAL)
    code = """static void testPolymorphism()
{
\tClapTrap *robot = new ScavTrap("Polymorph");
\trobot->attack("a target");
\trobot->takeDamage(10);
\tdelete robot;
}"""
    code_panel(s, ML, BODY_TOP, CW * 0.47, code, max_h=Inches(1.95),
               title="src/main.cpp", size=10.5)
    rows = [
        ["Call", "Without `virtual`", "With `virtual` (my code)"],
        ["`robot->attack(...)`\n(robot is a `ClapTrap*`)",
         "`ClapTrap::attack()` runs\n— the *static* type decides",
         "`ScavTrap::attack()` runs\n— the *real* type decides"],
        ["`robot->takeDamage(10)`", "same behaviour (not overridden)",
         "same behaviour (not overridden)"],
        ["`delete robot;`",
         "**UB** — the base destructor is not virtual,\nso the derived part is leaked",
         "safe — `virtual ~ClapTrap()` guarantees\nthe whole object is destroyed"],
    ]
    table(s, ML + CW * 0.50, BODY_TOP, CW * 0.50, rows, col_w=[2.0, 2.4, 2.6],
          size=11, row_h=0.9, head_h=0.40)
    items = [
        (0, "**The two bindings**"),
        (1, "**Static binding** — the compiler picks the function from the *type of "
            "the expression* (here `ClapTrap*`)."),
        (1, "**Dynamic binding** — with `virtual`, a hidden **vtable** pointer is "
            "added to the object and the *real* type decides at run time."),
        (0, "One interface, many behaviours — that is the whole point of the module."),
    ]
    bullets(s, ML, Inches(3.75), CW * 0.47, items, size=12.5, gap=0.12,
            max_h=Inches(2.9))
    callout(s, ML + CW * 0.50, Inches(4.85), CW * 0.50,
            "Why the destructor must be `virtual`",
            "When we `delete` through a `ClapTrap*`, the compiler must know whether a "
            "`ScavTrap` hides behind it. Without `virtual`, only the `ClapTrap` part is "
            "destroyed → memory leak. I declared `virtual ~ClapTrap();` in ex00 "
            "precisely for that reason.",
            accent=ORANGE, bg=ORANGE_L, size=11.5, h=Inches(1.65))
    return s


def s_ex01_proof(prs):
    s = content_slide(prs, "ex01 — Runtime proof", "ex01 · proof", accent=TEAL)
    out = """=== Module 03 - ex01: Serena, my love! ===
--- testConstructionChaining ---
ClapTrap: Scavvy has been created.
ScavTrap: Scavvy is ready to fight!
Scavvy has 100 hit points, 50 energy points and 20 attack damage.
ScavTrap: Scavvy has been destroyed.
ClapTrap: Scavvy has been destroyed.
--- testSpecialAbility ---
ScavTrap Gatekeeper is now in Gate keeper mode!
ScavTrap Gatekeeper attacks a target, causing 20 points of damage!
ClapTrap Gatekeeper takes 30 points of damage, it has 70 hit points left!
ClapTrap Gatekeeper is repaired by 20 points, it has 90 hit points!
--- testPolymorphism ---
ClapTrap: Polymorph has been created.
ScavTrap: Polymorph is ready to fight!
ScavTrap Polymorph attacks a target, causing 20 points of damage!  <-- override
ClapTrap Polymorph takes 10 points of damage, it has 90 hit points left.
ScavTrap: Polymorph has been destroyed.
ClapTrap: Polymorph has been destroyed.
--- testCopy ---
ClapTrap: a copy of Original has been created.
ScavTrap: a copy of Original is ready to fight!
the copy has 90 hit points.
ClapTrap: Original has been assigned from another ClapTrap.
ScavTrap: Original has been assigned from another ScavTrap.
=== ex01 done ==="""
    code_panel(s, ML, BODY_TOP, CW * 0.56, out, max_h=Inches(4.9), term=True,
               title="terminal  ·  ./ex01", size=9.6)
    items = [
        (0, "**What the output proves**"),
        (1, "**Construction order**: `ClapTrap` first, then `ScavTrap`. ✔"),
        (1, "**Destruction order**: the exact reverse. ✔"),
        (1, "**Values**: 100 HP / 50 energy / 20 damage — the `protected` setters worked. ✔"),
        (1, "**Override**: through a `ClapTrap*` the message says *“ScavTrap … 20 "
            "points of damage”* → the dynamic binding works. ✔"),
        (1, "**Copy**: the base and the derived both print, and the hit points are "
            "preserved (90). ✔"),
        (1, "**Inherited behaviour**: `takeDamage` still prints the `ClapTrap` message "
            "— it was not overridden. ✔"),
    ]
    bullets(s, ML + CW * 0.585, BODY_TOP, CW * 0.415, items, size=12.5, gap=0.11,
            max_h=Inches(4.9))
    return s


def s_ex02_intro(prs):
    s = content_slide(prs, "ex02 — Repetitive work",
                      "part 3 · ex02 · the second branch", accent=ORANGE)
    code = """#ifndef FRAGTRAP_HPP
#define FRAGTRAP_HPP

#include "ClapTrap.hpp"

class FragTrap : public virtual ClapTrap
{
public:
\tFragTrap();
\tFragTrap(std::string const & name);
\tFragTrap(FragTrap const & other);
\tFragTrap & operator=(FragTrap const & other);
\tvirtual ~FragTrap();

\tvoid highFivesGuys();
};

#endif"""
    code_panel(s, ML, BODY_TOP, CW * 0.46, code, max_h=Inches(3.4),
               title="include/FragTrap.hpp", size=10.5)
    items = [
        (0, "**The subject**"),
        (1, "`FragTrap` **also** inherits `ClapTrap` — a *sibling* of `ScavTrap`."),
        (1, "It adds the special ability `highFivesGuys()`."),
        (1, "Initialised with **100 HP / 100 energy / 30 damage**."),
        (1, "Its ctor / dtor messages differ from `ScavTrap`'s."),
        (0, "**The same pattern as ex01**"),
        (1, "`: ClapTrap(name)` in the initializer list."),
        (1, "`setHitPoints(100); setEnergyPoints(100); setAttackDamage(30);` in the body."),
        (1, "The `virtual` on the base is already there from ex01 — **nothing to change**."),
    ]
    bullets(s, ML + CW * 0.51, BODY_TOP, CW * 0.49, items, size=13, gap=0.12,
            max_h=Inches(4.0))
    callout(s, ML, Inches(5.30), CW * 0.46, "The point of ex02",
            "It creates the **second branch** of the hierarchy. After ex02 we have two "
            "classes inheriting the same base — which is exactly the shape of a "
            "**diamond**.",
            accent=ORANGE, bg=ORANGE_L, size=11.5, h=Inches(1.0))
    return s


def s_ex02_decision(prs):
    s = content_slide(prs, "ex02 — A deliberate decision: no override of attack()",
                      "ex02 · design decision", accent=ORANGE)
    code = """class FragTrap : public virtual ClapTrap
{
public:
\tFragTrap();
\tFragTrap(std::string const & name);
\tFragTrap(FragTrap const & other);
\tFragTrap & operator=(FragTrap const & other);
\tvirtual ~FragTrap();

\t//  no "virtual void attack(...)" here !
\tvoid highFivesGuys();
};"""
    code_panel(s, ML, BODY_TOP, CW * 0.46, code, max_h=Inches(3.2),
               title="include/FragTrap.hpp", size=10.5)
    items = [
        (0, "**The question**"),
        (1, "The subject does not forbid `FragTrap` from overriding `attack()`. "
            "Should it?"),
        (0, "**My answer: no — and here is why**"),
        (1, "In ex03, `DiamondTrap` inherits **both** `FragTrap` and `ScavTrap`."),
        (1, "If **both** declared `attack()`, the call `diamond.attack(...)` would have "
            "**two equally valid candidates** → the compiler refuses with *“request "
            "for member ‘attack’ is ambiguous”*."),
        (1, "If only `ScavTrap` overrides it, there is **exactly one** candidate → no "
            "ambiguity."),
        (1, "The subject of ex03 does not ask `FragTrap` for its own attack, so **not "
            "overriding it is both simpler and required**."),
        (0, "**Consequence in ex03**"),
        (1, "`DiamondTrap::attack()` resolves to **`ScavTrap::attack()`**."),
    ]
    bullets(s, ML + CW * 0.51, BODY_TOP, CW * 0.49, items, size=12.5, gap=0.11,
            max_h=Inches(4.3))
    callout(s, ML, Inches(5.15), CW * 0.46, "The general rule",
            "In a diamond, a method overridden in **every** branch becomes ambiguous. "
            "The standard fixes are a `using` declaration in the derived class, or "
            "overriding the method **in the derived class** itself.",
            accent=TEAL, bg=TEAL_L, size=11.5, h=Inches(1.1))
    return s


def s_ex02_proof(prs):
    s = content_slide(prs, "ex02 — Runtime proof", "ex02 · proof", accent=ORANGE)
    out = """=== Module 03 - ex02: Repetitive work ===
--- testConstructionChaining ---
ClapTrap: Fraggy has been created.
FragTrap: Fraggy has jumped into the battle!
Fraggy has 100 hit points, 100 energy points and 30 attack damage.
FragTrap: Fraggy has been destroyed.
ClapTrap: Fraggy has been destroyed.
--- testSpecialAbility ---
FragTrap Cheerful asks everybody for a high five! Let's go!
ClapTrap Cheerful attacks a target, causing 30 points of damage!  <-- inherited
ClapTrap Cheerful takes 30 points of damage, it has 70 hit points left!
ClapTrap Cheerful is repaired by 20 points, it has 90 hit points!
--- testPolymorphism ---
ClapTrap: Polymorph has been created.
FragTrap: Polymorph has jumped into the battle!
ClapTrap Polymorph attacks a target, causing 30 points of damage!
--- testCopy ---
ClapTrap: a copy of Original has been created.
FragTrap: a copy of Original has jumped into the battle!
the copy has 90 hit points.
ClapTrap: Original has been assigned from another ClapTrap.
FragTrap: Original has been assigned from another FragTrap.
=== ex02 done ==="""
    code_panel(s, ML, BODY_TOP, CW * 0.56, out, max_h=Inches(4.9), term=True,
               title="terminal  ·  ./ex02", size=9.6)
    items = [
        (0, "**What the output proves**"),
        (1, "**Different values than ex01**: 100 HP / **100 energy** / 30 damage — each "
            "class configures itself through the `protected` setters. ✔"),
        (1, "**Different messages**: *“has jumped into the battle!”* vs. *“is ready to "
            "fight!”*. ✔"),
        (1, "**`attack()` is inherited, not overridden** — the message says *“ClapTrap "
            "Cheerful attacks … 30 points of damage”*: the base implementation runs, "
            "but with the **derived** damage value (30, not 0). ✔"),
        (1, "**Same construction / destruction order** as ex01. ✔"),
        (1, "Through a `ClapTrap*`, the base message is used — correct, because "
            "`FragTrap` did not override it. ✔"),
    ]
    bullets(s, ML + CW * 0.585, BODY_TOP, CW * 0.415, items, size=12.5, gap=0.11,
            max_h=Inches(4.9))
    return s


def s_ex03_intro(prs):
    s = content_slide(prs, "ex03 — Now it's weird!",
                      "part 3 · ex03 · the diamond", accent=TEAL)
    code = """#ifndef DIAMONDTRAP_HPP
#define DIAMONDTRAP_HPP

#include "FragTrap.hpp"
#include "ScavTrap.hpp"

class DiamondTrap : public FragTrap, public ScavTrap
{
public:
\tDiamondTrap();
\tDiamondTrap(std::string const & name);
\tDiamondTrap(DiamondTrap const & other);
\tDiamondTrap & operator=(DiamondTrap const & other);
\tvirtual ~DiamondTrap();

\tvoid whoAmI();

private:
\tstd::string name_;
};

#endif"""
    code_panel(s, ML, BODY_TOP, CW * 0.47, code, max_h=Inches(4.0),
               title="include/DiamondTrap.hpp", size=10.2)
    items = [
        (0, "**The subject**"),
        (1, "`DiamondTrap` inherits **both** `FragTrap` **and** `ScavTrap`."),
        (1, "It must print **two different names**: its own, and its `ClapTrap` base's."),
        (1, "The `ClapTrap` base must exist **only once**."),
        (1, "Its ctor and dtor print their own messages."),
        (0, "**The inherited abilities**"),
        (1, "`guardGate()` comes from `ScavTrap`."),
        (1, "`highFivesGuys()` comes from `FragTrap`."),
        (1, "`attack()` comes from `ScavTrap` (the only one that overrides it)."),
        (1, "`takeDamage()` / `beRepaired()` come from `ClapTrap`."),
    ]
    bullets(s, ML + CW * 0.52, BODY_TOP, CW * 0.48, items, size=13, gap=0.12,
            max_h=Inches(4.6))
    return s


def s_ex03_problem(prs):
    s = content_slide(prs, "ex03 — The Diamond problem", "ex03 · the problem",
                      accent=RED)
    dx = ML + Inches(0.35)
    class_box(s, dx + Inches(1.55), Inches(1.70), Inches(2.5), Inches(0.95),
              "ClapTrap", ["name_, hitPoints_, energyPoints_"], head=NAVY, size=9)
    class_box(s, dx - Inches(0.60), Inches(3.40), Inches(2.2), Inches(0.90),
              "FragTrap", ["highFivesGuys()"], head=ORANGE, size=9)
    class_box(s, dx + Inches(3.30), Inches(3.40), Inches(2.2), Inches(0.90),
              "ScavTrap", ["guardGate()"], head=TEAL, size=9)
    class_box(s, dx + Inches(1.20), Inches(5.00), Inches(2.2), Inches(0.90),
              "DiamondTrap", ["whoAmI()"], head=NAVY_3, size=9)
    arrow_to(s, dx + Inches(0.50), Inches(3.40), dx + Inches(2.10), Inches(2.65),
             color=RED)
    arrow_to(s, dx + Inches(4.40), Inches(3.40), dx + Inches(2.80), Inches(2.65),
             color=RED)
    arrow_to(s, dx + Inches(1.50), Inches(5.00), dx + Inches(1.00), Inches(4.30),
             color=RED)
    arrow_to(s, dx + Inches(3.10), Inches(5.00), dx + Inches(3.60), Inches(4.30),
             color=RED)
    text(s, dx - Inches(0.5), Inches(5.95), Inches(6.3), Inches(0.5),
         "Two paths from DiamondTrap to the same ClapTrap  =  a diamond",
         size=11.5, color=GREY, align=PP_ALIGN.CENTER)

    right_x = ML + CW * 0.55
    items = [
        (0, "**Problem 1 — the base is built twice**"),
        (1, "Without `virtual`, `DiamondTrap` holds **two** `ClapTrap` sub-objects and "
            "the base constructor runs **twice**."),
        (0, "**Problem 2 — the member call is ambiguous**"),
        (1, "`diamond.attack(...)` has **two** candidates → the compiler refuses."),
        (0, "**Problem 3 — the state is duplicated**"),
        (1, "The hit points of the two copies are **different**; repairing one does "
            "not repair the other."),
    ]
    bullets(s, right_x, BODY_TOP, CW * 0.45, items, size=12.5, gap=0.11,
            max_h=Inches(2.8))
    code = """error: request for member 'f' is ambiguous
   17 |         d.f();
      |           ^
note: candidates are: 'virtual void Base::f()'
note: candidates are: 'virtual void Base::f()'"""
    code_panel(s, right_x, Inches(4.55), CW * 0.45, code, max_h=Inches(1.7),
               term=True, title="real compiler output", size=9.6)
    return s


def s_ex03_fix(prs):
    s = content_slide(prs, "ex03 — The fix: virtual inheritance",
                      "ex03 · the solution", accent=TEAL)
    code = """//  ex01 - ScavTrap.hpp
-class ScavTrap : public ClapTrap
+class ScavTrap : public virtual ClapTrap

//  ex02 - FragTrap.hpp
-class FragTrap : public ClapTrap
+class FragTrap : public virtual ClapTrap

//  ex03 - DiamondTrap.hpp
 class DiamondTrap : public FragTrap, public ScavTrap
 { ... };

//  ex03 - DiamondTrap.cpp
//  the most derived class owns the shared base
 DiamondTrap::DiamondTrap(std::string const & name)
 \t: ClapTrap(name + "_clap_name"),
 \t  FragTrap(name),
 \t  ScavTrap(name),
 \t  name_(name)
 {
 \tsetHitPoints(100);
 \tsetEnergyPoints(50);
 \tsetAttackDamage(30);
 }"""
    code_panel(s, ML, BODY_TOP, CW * 0.55, code, max_h=Inches(4.4),
               title="the diff and the constructor", size=10.2)
    items = [
        (0, "**What `virtual` changes**"),
        (1, "The base becomes a **virtual base**: only **one** shared sub-object, owned "
            "by the **most derived class**."),
        (1, "The base constructor runs **once**."),
        (1, "The member calls are **unambiguous** again."),
        (1, "The two branches now **share** the same data."),
        (0, "**Who initialises the virtual base?**"),
        (1, "**Only the most derived class** — here: `DiamondTrap`."),
        (1, "The `ClapTrap(name)` in `FragTrap`'s and `ScavTrap`'s initializer lists is "
            "**ignored** when a `DiamondTrap` is built."),
        (1, "That is why `DiamondTrap` **must** initialise `ClapTrap` itself — and it "
            "does, with `name + \"_clap_name\"`."),
        (0, "**The cost**"),
        (1, "One extra pointer per level of virtual inheritance, and a slightly slower "
            "access to the base members."),
    ]
    bullets(s, ML + CW * 0.58, BODY_TOP, CW * 0.42, items, size=12, gap=0.10,
            max_h=Inches(4.9))
    return s


def s_ex03_impl(prs):
    s = content_slide(prs, "ex03 — DiamondTrap implementation and whoAmI()",
                      "ex03 · step by step", accent=TEAL)
    code = """void DiamondTrap::whoAmI()
{
\tstd::cout << "My name is " << name_
\t\t\t  << " and my ClapTrap name is " << getName()
\t\t\t  << std::endl;
}

DiamondTrap::DiamondTrap(std::string const & name)
\t: ClapTrap(name + "_clap_name"),   // the virtual base, owned by us
\t  FragTrap(name),                   // ignored for the virtual base
\t  ScavTrap(name),                   // ignored for the virtual base
\t  name_(name)                       // our own attribute
{
\tsetHitPoints(100);
\tsetEnergyPoints(50);
\tsetAttackDamage(30);
\tstd::cout << "DiamondTrap: " << name_
\t\t\t  << " has been created!" << std::endl;
}"""
    code_panel(s, ML, BODY_TOP, CW * 0.54, code, max_h=Inches(4.3),
               title="src/DiamondTrap.cpp", size=9.8)
    items = [
        (0, "**Two names, one object**"),
        (1, "`name_` → the `DiamondTrap`'s **own** private attribute = *“Diamo”*."),
        (1, "`getName()` → the inherited getter of the shared `ClapTrap` base = "
            "*“Diamo_clap_name”*."),
        (1, "`whoAmI()` prints **both** — exactly what the subject asks."),
        (0, "**The values**"),
        (1, "100 HP and 30 damage come from the `FragTrap` configuration."),
        (1, "50 energy comes from the `ScavTrap` configuration."),
        (1, "I set them **explicitly** in the body of the constructor, because the "
            "sub-classes' settings are not applied to the shared base."),
    ]
    bullets(s, ML + CW * 0.57, BODY_TOP, CW * 0.43, items, size=12.5, gap=0.11,
            max_h=Inches(4.3))
    return s


def s_ex03_shadow(prs):
    s = content_slide(prs, "ex03 — The name shadowing trick, explained",
                      "ex03 · a subtle point", accent=RED)
    code = """//  ClapTrap  (the virtual base)
private:
\tstd::string name_;      //  "Diamo_clap_name"

//  DiamondTrap  (the most derived class)
private:
\tstd::string name_;      //  "Diamo"  <- shadows the base attribute

void DiamondTrap::whoAmI()
{
\tstd::cout << "My name is " << name_                // -> "Diamo"
\t\t\t  << " and my ClapTrap name is " << getName()  // -> "Diamo_clap_name"
\t\t\t  << std::endl;
}"""
    code_panel(s, ML, BODY_TOP, CW * 0.55, code, max_h=Inches(3.1),
               title="two attributes with the same name", size=10.2)
    items = [
        (0, "**Why does it compile?**"),
        (1, "Name lookup starts in the **most derived** class: `name_` is found in "
            "`DiamondTrap` and the search **stops**."),
        (1, "There is no ambiguity because the base's `name_` is **private**: it was "
            "never a candidate in that scope."),
        (0, "**Why is it legitimate?**"),
        (1, "The base's attribute is only reachable through `getName()`, so the two "
            "values never interfere."),
        (1, "Verified: the code compiles with `-Wall -Wextra -Werror -Wshadow "
            "-pedantic` — **no shadow warning is raised**."),
        (0, "**How I made it explicit**"),
        (1, "The base is initialised with `name + \"_clap_name\"`, so the two names are "
            "visibly different in the output."),
    ]
    bullets(s, ML + CW * 0.58, BODY_TOP, CW * 0.42, items, size=12.5, gap=0.11,
            max_h=Inches(3.2))
    callout(s, ML, Inches(4.95), CW * 0.55, "Honesty note — an alternative",
            "I could have renamed the derived attribute (`myName_`) and avoided the "
            "shadowing altogether. I kept `name_` because the subject mentions a "
            "*name attribute* for the `ClapTrap` base, and the shadowing is harmless "
            "here — but I can justify either choice.",
            accent=TEAL, bg=TEAL_L, size=11.5, h=Inches(1.15))
    return s


def s_ex03_order(prs):
    s = content_slide(prs, "ex03 — Construction and destruction order",
                      "ex03 · order of operations", accent=TEAL)
    rows = [
        ["#", "Event", "Who runs it", "Message printed"],
        ["1", "Construction", "`ClapTrap` (virtual base)",
         "`ClapTrap: Diamo_clap_name has been created.`"],
        ["2", "Construction", "`FragTrap`",
         "`FragTrap: Diamo_clap_name has jumped into the battle!`"],
        ["3", "Construction", "`ScavTrap`",
         "`ScavTrap: Diamo_clap_name is ready to fight!`"],
        ["4", "Construction", "`DiamondTrap`", "`DiamondTrap: Diamo has been created!`"],
        ["5", "Destruction", "`DiamondTrap`", "`DiamondTrap: Diamo has been destroyed!`"],
        ["6", "Destruction", "`ScavTrap`", "`ScavTrap: Diamo_clap_name has been destroyed.`"],
        ["7", "Destruction", "`FragTrap`", "`FragTrap: Diamo_clap_name has been destroyed.`"],
        ["8", "Destruction", "`ClapTrap`", "`ClapTrap: Diamo_clap_name has been destroyed.`"],
    ]
    table(s, ML, BODY_TOP, CW * 0.62, rows, col_w=[0.4, 1.5, 2.3, 6.0], size=10.5,
          row_h=0.42, head_h=0.38)
    items = [
        (0, "**The rule**"),
        (1, "The **virtual base** is constructed **first**."),
        (1, "Then the direct bases, **left to right** as declared: `FragTrap`, then "
            "`ScavTrap`."),
        (1, "Then the most derived class itself."),
        (1, "Destruction is the **exact reverse**."),
        (0, "**Notice**"),
        (1, "`FragTrap` and `ScavTrap` both print *“Diamo_clap_name”* — they read the "
            "**shared** base through `getName()`."),
        (1, "Only **one** `ClapTrap: … created` line → the virtual base was built once. ✔"),
    ]
    bullets(s, ML + CW * 0.645, BODY_TOP, CW * 0.355, items, size=12, gap=0.10,
            max_h=Inches(4.2))
    callout(s, ML, Inches(5.55), CW * 0.62, "Why is the base built first?",
            "A base class must exist before the derived class can use it. The standard "
            "orders the initialisation as: **virtual bases** → **direct bases (left to "
            "right)** → **members** → **the constructor body**.",
            accent=ORANGE, bg=ORANGE_L, size=11.5, h=Inches(1.0))
    return s


def s_ex03_values(prs):
    s = content_slide(prs, "ex03 — Where do the values come from?",
                      "ex03 · resolving the ambiguity", accent=TEAL)
    rows = [
        ["Member", "Inherited from", "Value", "Why"],
        ["`getName()`", "`ClapTrap` (the single shared virtual base)", "`\"Diamo_clap_name\"`",
         "The base is initialised with `name + \"_clap_name\"`"],
        ["`name_` (own)", "`DiamondTrap`", "`\"Diamo\"`", "Its own private attribute"],
        ["`getHitPoints()`", "the shared `ClapTrap` base", "**100**",
         "Set explicitly in `DiamondTrap`'s constructor"],
        ["`getEnergyPoints()`", "the shared `ClapTrap` base", "**50**",
         "Set explicitly in `DiamondTrap`'s constructor"],
        ["`getAttackDamage()`", "the shared `ClapTrap` base", "**30**",
         "Set explicitly in `DiamondTrap`'s constructor"],
        ["`attack()`", "`ScavTrap`", "the `ScavTrap` version",
         "The **only** branch that overrides it → no ambiguity"],
        ["`guardGate()`", "`ScavTrap`", "—", "Only `ScavTrap` declares it"],
        ["`highFivesGuys()`", "`FragTrap`", "—", "Only `FragTrap` declares it"],
        ["`whoAmI()`", "`DiamondTrap`", "—", "Declared only in `DiamondTrap`"],
    ]
    table(s, ML, BODY_TOP, CW, rows, col_w=[1.8, 3.3, 2.1, 5.0], size=10.5,
          row_h=0.36, head_h=0.38)
    callout(s, ML, Inches(5.70), CW, "Why set the values explicitly in `DiamondTrap`?",
            "The sub-classes set **their own** configuration on **their own** instance (a "
            "`FragTrap` alone gets 100/100/30). When a `DiamondTrap` is built there is "
            "only **one** shared base — so the most derived class decides the final "
            "values. I chose 100 HP / 50 energy / 30 damage, which combines the "
            "`FragTrap` HP and damage with the `ScavTrap` energy.",
            accent=TEAL, bg=TEAL_L, size=11.5, h=Inches(0.95))
    return s


def s_ex03_proof(prs):
    s = content_slide(prs, "ex03 — Runtime proof", "ex03 · proof", accent=TEAL)
    out = """=== Module 03 - ex03: Now it's weird! ===
--- testConstructionChaining ---
ClapTrap: Diamo_clap_name has been created.      <-- ONE single base
FragTrap: Diamo_clap_name has jumped into the battle!
ScavTrap: Diamo_clap_name is ready to fight!
DiamondTrap: Diamo has been created!
Diamo has 100 hit points, 50 energy points and 30 attack damage.
DiamondTrap: Diamo has been destroyed!
ScavTrap: Diamo_clap_name has been destroyed.
FragTrap: Diamo_clap_name has been destroyed.
ClapTrap: Diamo_clap_name has been destroyed.
--- testWhoAmI ---
My name is Diamo and my ClapTrap name is Diamo_clap_name
--- testInheritedAbilities ---
ScavTrap Diamo_clap_name is now in Gate keeper mode!
FragTrap Diamo_clap_name asks everybody for a high five! Let's go!
ScavTrap Diamo_clap_name attacks a target, causing 30 points of damage!
--- testPolymorphism ---
ClapTrap: Polymorph_clap_name has been created.
ScavTrap Polymorph_clap_name attacks a target, causing 30 points of damage!
--- testCopy ---
My name is Original and my ClapTrap name is Original_clap_name
=== ex03 done ==="""
    code_panel(s, ML, BODY_TOP, CW * 0.56, out, max_h=Inches(4.9), term=True,
               title="terminal  ·  ./ex03", size=9.4)
    items = [
        (0, "**What the output proves**"),
        (1, "**One** `ClapTrap: … created` line → the virtual base was built "
            "**once**. ✔"),
        (1, "Construction order: **ClapTrap → FragTrap → ScavTrap → DiamondTrap**; "
            "destruction is the **exact reverse**. ✔"),
        (1, "`whoAmI()` prints the two different names. ✔"),
        (1, "Both inherited abilities work: `guardGate()` and `highFivesGuys()`. ✔"),
        (1, "`attack()` resolves to the **`ScavTrap`** version (30 damage) — "
            "unambiguous. ✔"),
        (1, "Through a `ClapTrap*`, the dynamic binding still works. ✔"),
    ]
    bullets(s, ML + CW * 0.585, BODY_TOP, CW * 0.415, items, size=12.5, gap=0.11,
            max_h=Inches(4.9))
    return s


def s_design_map(prs):
    s = content_slide(prs, "The complete design map", "summary", accent=NAVY_3)
    code = """                      ClapTrap
               (private data + public API)
                    /            \\
           virtual/              \\virtual
                 /                \\
         ScavTrap                 FragTrap
     attack() [override]     highFivesGuys()
                 \\                /
                  \\              /
                   DiamondTrap
                  whoAmI() + name_"""
    code_panel(s, ML, BODY_TOP, CW * 0.42, code, max_h=Inches(4.2),
               title="the hierarchy", size=10.5)
    items = [
        (0, "**Who owns what**"),
        (1, "`ClapTrap` owns the **data** and the shared **behaviour** "
            "(`takeDamage`, `beRepaired`, the getters/setters)."),
        (1, "`ScavTrap` owns the **guard** ability and the **overridden** `attack()`."),
        (1, "`FragTrap` owns the **cheer** ability."),
        (1, "`DiamondTrap` owns the **second name**, the final values, and the "
            "construction of the shared base."),
        (0, "**The three techniques used**"),
        (1, "**Inheritance** to reuse the data and the behaviour."),
        (1, "**`virtual`** to make the behaviour depend on the real type."),
        (1, "**`virtual` inheritance** to share a single base between two branches."),
    ]
    bullets(s, ML + CW * 0.46, BODY_TOP, CW * 0.54, items, size=13, gap=0.12,
            max_h=Inches(4.6))
    return s


def s_cheatsheet(prs):
    s = content_slide(prs, "Cheat sheet — the C++ knowledge this module needs",
                      "summary · knowledge", accent=TEAL)
    rows = [
        ["Concept", "The syntax", "What it really does", "Where I used it"],
        ["Inheritance", "`class D : public B`",
         "`D` reuses and extends `B`; it gets `B`'s public and protected members",
         "ex01, ex02, ex03"],
        ["Constructor chaining", "`: B(args)` in the init list",
         "Calls the base constructor **before** the derived body", "every class"],
        ["Virtual function", "`virtual void f();`",
         "Allows a derived class to replace the behaviour (dynamic binding)",
         "`ClapTrap::attack()`"],
        ["Override", "same name & parameters", "Replaces the base implementation",
         "`ScavTrap::attack()`"],
        ["Virtual destructor", "`virtual ~D();`",
         "Makes `delete` through a base pointer safe", "`~ClapTrap()`"],
        ["Virtual inheritance", "`class D : public virtual B`",
         "One **shared** base instead of two copies", "ex01, ex02, ex03"],
        ["`protected`", "`protected:` section",
         "Visible to the class **and** its derived classes only", "the setters"],
        ["Pure virtual", "`virtual void f() = 0;`",
         "Makes the class **abstract** — an interface that cannot be instantiated",
         "not required by the subject"],
        ["Rule of Three", "copy ctor + `operator=` + dtor",
         "Correctly manages the resources of a class", "every class"],
    ]
    table(s, ML, BODY_TOP, CW, rows, col_w=[1.7, 2.6, 5.4, 2.3], size=11,
          row_h=0.45, head_h=0.40)
    callout(s, ML, Inches(6.00), CW, "If you remember only three things",
            "**1.** A `virtual` method is what makes the *real* type of the object decide "
            "at run time (polymorphism).   **2.** A **virtual base** is what makes two "
            "branches share **one** base (the diamond).   **3.** A `virtual` destructor "
            "is what makes `delete` through a base pointer safe.",
            accent=TEAL, bg=TEAL_L, size=11.5, h=Inches(0.8))
    return s


def s_pitfalls(prs):
    s = content_slide(prs, "Common pitfalls — and how I avoided them",
                      "summary · reflection", accent=RED)
    rows = [
        ["Pitfall", "What goes wrong", "How my code avoids it"],
        ["Non-virtual destructor", "`delete` through a base pointer → leak, undefined "
         "behaviour", "`virtual ~ClapTrap();` declared already in ex00"],
        ["Forgetting to call the base ctor", "The base members are left uninitialised",
         "`: ClapTrap(name)` in every initializer list"],
        ["Initialising members in the wrong order", "`-Wreorder` → with `-Werror`, the "
         "build fails", "The init lists follow the declaration order exactly"],
        ["Copying a class without a copy ctor", "Shallow copy → double free / leak",
         "Explicit copy ctor + `operator=` with `if (this != &other)`"],
        ["Forgetting `ClapTrap::operator=` in a derived class",
         "The base part is not copied → inconsistent object",
         "The derived `operator=` calls `ClapTrap::operator=(other);`"],
        ["Two overrides in a diamond", "*“request for member ‘attack’ is ambiguous”*",
         "`FragTrap` deliberately does **not** override `attack()`"],
        ["Two copies of the base", "The base is built twice, the state diverges",
         "`public virtual ClapTrap` in `ScavTrap` and `FragTrap`"],
        ["Accessing a `private` base member", "Compile error",
         "The `protected` setters (`setHitPoints`, …)"],
        ["Using C++11 features", "Does not compile with `-std=c++98`",
         "No `nullptr`, no `override`, no `auto`, no range-`for`"],
    ]
    table(s, ML, BODY_TOP, CW, rows, col_w=[3.0, 4.2, 4.8], size=10.5,
          row_h=0.45, head_h=0.40)
    return s


def s_norms(prs):
    s = content_slide(prs, "42 Norms — the rules I respected", "summary · norms",
                      accent=TEAL)
    left = [
        (0, "**Compilation**"),
        (1, "`-Wall -Wextra -Werror -std=c++98` — **zero warnings, zero errors**."),
        (1, "Also verified with `-Wshadow -pedantic` (no warning)."),
        (1, "Each exercise builds with its own `Makefile` (`make`, `make clean`, "
            "`make re`)."),
        (0, "**Coding standards**"),
        (1, "No `using namespace std;` — every call is fully qualified."),
        (1, "No `friend`, no `printf`, no `malloc` / `free`."),
        (1, "No STL containers and no algorithm (modules 08 / 09 only)."),
        (1, "Include guards on every header, and each header is **self-contained**."),
        (1, "All the implementation lives in the `.cpp` files, not in the headers."),
    ]
    right = [
        (0, "**Object oriented design**"),
        (1, "Encapsulation: the data stays `private`, access goes through getters and "
            "setters."),
        (1, "The **Orthodox Canonical Form** on every class: default ctor, copy ctor, "
            "`operator=`, destructor."),
        (1, "No memory leak — verified with `-fsanitize=address,undefined` "
            "(**0 errors**)."),
        (0, "**Project hygiene**"),
        (1, "One directory per exercise, each one self-contained."),
        (1, "A `README.md` documenting the module, the design notes and the rules "
            "followed."),
        (1, "Only the standard library is used — no external dependency."),
    ]
    bullets(s, ML, BODY_TOP, CW * 0.49, left, size=12.5, gap=0.10,
            max_h=Inches(4.2))
    bullets(s, ML + CW * 0.51, BODY_TOP, CW * 0.49, right, size=12.5, gap=0.10,
            max_h=Inches(4.2))
    callout(s, ML, Inches(5.85), CW, "One bug found and fixed during this presentation",
            "The `Makefile` of **ex03** was a copy of the one of ex02: it still built a "
            "binary named `ex02` and did not list `src/DiamondTrap.cpp` in `SRCS`, so the "
            "link failed with *“undefined reference to `DiamondTrap::~DiamondTrap()`”*. "
            "I corrected `NAME := ex03` and added the missing source file — ex03 now "
            "builds and runs.",
            accent=ORANGE, bg=ORANGE_L, size=11.5, h=Inches(0.95))
    return s


def s_testing(prs):
    s = content_slide(prs, "Testing & quality assurance", "summary · testing",
                      accent=TEAL)
    code = """#  build + run every exercise
cd ex00 && make && ./ex00
cd ex01 && make && ./ex01
cd ex02 && make && ./ex02
cd ex03 && make && ./ex03

#  strict warnings (must stay silent)
g++ -Wall -Wextra -Werror -Wshadow -pedantic \\
    -std=c++98 -I include src/*.cpp -o test

#  sanitizers: memory + undefined behaviour
g++ -fsanitize=address,undefined -std=c++98 \\
    -I include src/*.cpp -o test && ./test"""
    code_panel(s, ML, BODY_TOP, CW * 0.47, code, max_h=Inches(3.4),
               title="the commands I run", size=10.5)
    items = [
        (0, "**1 — Functional tests**"),
        (1, "4 `static` test functions per exercise, each in its own scope, covering "
            "the nominal case and the edge cases (0 HP, 0 energy, copy, assignment)."),
        (0, "**2 — Strict compilation**"),
        (1, "`-Wall -Wextra -Werror` catches almost everything; `-Wshadow -pedantic` "
            "confirms the code is clean beyond the required flags."),
        (0, "**3 — Sanitizers**"),
        (1, "`-fsanitize=address,undefined` → **no leak, no UB** on any exercise."),
        (0, "**4 — Manual inspection**"),
        (1, "The printed output is compared with what the subject asks for, "
            "message by message."),
    ]
    bullets(s, ML + CW * 0.52, BODY_TOP, CW * 0.48, items, size=12.5, gap=0.11,
            max_h=Inches(3.5))
    callout(s, ML, Inches(5.25), CW * 0.47, "Result",
            "ex00 ✔   ex01 ✔   ex02 ✔   ex03 ✔  — all four build without a single "
            "warning and produce the expected output.",
            accent=TEAL, bg=TEAL_L, size=12, h=Inches(0.9))
    return s


def s_makefile(prs):
    s = content_slide(prs, "The build system", "summary · makefile", accent=TEAL)
    code = """NAME      := ex03
CXX       := c++
CXXFLAGS := -Wall -Wextra -Werror -std=c++98
SRCS      := src/ClapTrap.cpp src/main.cpp \\
             src/ScavTrap.cpp src/FragTrap.cpp \\
             src/DiamondTrap.cpp
OBJS      := $(SRCS:.cpp=.o)

all: $(NAME)

$(NAME): $(OBJS)
\t$(CXX) $(CXXFLAGS) $(OBJS) -o $(NAME)

%.o: %.cpp
\t$(CXX) $(CXXFLAGS) -I include -c $< -o $@

clean:
\trm -f $(OBJS) $(NAME)

re: clean all

.PHONY: all clean re"""
    code_panel(s, ML, BODY_TOP, CW * 0.50, code, max_h=Inches(4.5),
               title="ex03/Makefile", size=9.8)
    items = [
        (0, "**How the Makefile works**"),
        (1, "`%.o: %.cpp` is a **pattern rule**: any `.cpp` becomes a `.o` in the same "
            "folder."),
        (1, "`-I include` tells the compiler where the headers live."),
        (1, "`$(SRCS:.cpp=.o)` derives the objects from the sources — no duplication."),
        (1, "`.PHONY` tells `make` that `all`, `clean` and `re` are not files."),
        (0, "**The targets**"),
        (1, "`make` → builds everything.   `make clean` → removes the objects and the "
            "binary.   `make re` → `clean` + `all`."),
        (0, "**Why a Makefile?**"),
        (1, "The 42 Norms ask for a `Makefile` that compiles with the right flags and "
            "cleans up after itself."),
    ]
    bullets(s, ML + CW * 0.53, BODY_TOP, CW * 0.47, items, size=12.5, gap=0.11,
            max_h=Inches(4.6))
    return s


def s_conclusion(prs):
    s = content_slide(prs, "Conclusion", "wrap-up", accent=ORANGE)
    items = [
        (0, "**What the module taught me**"),
        (1, "**Inheritance** lets me reuse a class instead of copying it: the data and "
            "the behaviour of `ClapTrap` are written **once** and shared by "
            "`ScavTrap`, `FragTrap` and `DiamondTrap`."),
        (1, "**`virtual`** turns a base class into a real interface: the same call "
            "`robot->attack(\"a target\")` produces a different behaviour depending on "
            "the real object — that is **polymorphism**."),
        (1, "**`virtual` inheritance** solves the **Diamond problem**: one shared "
            "base, one construction, no ambiguity."),
        (1, "**Encapsulation** stays intact: the data is `private`, the derived classes "
            "update it through `protected` setters, exactly as the subject asks."),
        (0, "**What I am proud of**"),
        (1, "Four exercises that compile with **zero warnings** under "
            "`-Wall -Wextra -Werror -std=c++98` and run clean under "
            "`-fsanitize=address,undefined`."),
        (1, "Each design decision is **explained and justified** — especially the two "
            "subtle ones: why `attack()` is `virtual` from ex00, and why `FragTrap` "
            "does not override it."),
    ]
    bullets(s, ML, BODY_TOP, CW * 0.60, items, size=13.5, gap=0.13,
            max_h=Inches(4.9))
    rect(s, ML + CW * 0.64, BODY_TOP, CW * 0.36, Inches(4.5), fill=NAVY,
         shape=MSO_SHAPE.ROUNDED_RECTANGLE, adj=0.03)
    text(s, ML + CW * 0.64 + Inches(0.32), BODY_TOP + Inches(0.32),
         CW * 0.36 - Inches(0.64), Inches(0.3), "THE MODULE IN ONE LINE",
         size=10.5, color=ORANGE, font=FONT_B, bold=True)
    text(s, ML + CW * 0.64 + Inches(0.32), BODY_TOP + Inches(0.85),
         CW * 0.36 - Inches(0.64), Inches(3.2),
         "One class,\nmany behaviours —\nand one shared base,\nhowever many branches "
         "need it.",
         size=20, color=WHITE, font=FONT_B, bold=True, line_spacing=1.22)
    return s


def s_thanks(prs):
    s = blank(prs)
    bg_page(s, NAVY)
    rect(s, 0, 0, Inches(0.16), SH, fill=ORANGE)
    rect(s, SW - Inches(3.4), 0, Inches(3.4), SH, fill=NAVY_2)
    for i in range(4):
        for j in range(6):
            rect(s, SW - Inches(2.95) + Inches(0.46) * j,
                 Inches(2.1) + Inches(0.46) * i, Inches(0.1), Inches(0.1),
                 fill=NAVY_3, shape=MSO_SHAPE.OVAL)
    text(s, Inches(1.1), Inches(2.35), Inches(8.0), Inches(1.0), "Thank you!",
         size=54, color=WHITE, font=FONT_B, bold=True)
    rect(s, Inches(1.1), Inches(3.58), Inches(1.3), Inches(0.06), fill=ORANGE)
    text(s, Inches(1.1), Inches(3.88), Inches(7.5), Inches(0.9),
         "Questions & discussion\nCPP Module 03 — Inheritance, Interfaces & Polymorphism",
         size=15, color=RGBColor(0x9F, 0xB3, 0xCC), line_spacing=1.4)
    text(s, Inches(1.1), Inches(5.45), Inches(7.5), Inches(0.9),
         "ClapTrap  →  ScavTrap  →  FragTrap  →  DiamondTrap",
         size=14, color=RGBColor(0x5E, 0x73, 0x8C), font=MONO)
    PAGE_NO[0] += 1
    return s


# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------
def build():
    prs = Presentation()
    prs.slide_width = SW
    prs.slide_height = SH

    s_title(prs)
    s_agenda(prs)
    s_subject(prs)
    s_roadmap(prs)

    # ---- part 2 : the knowledge ----
    s_concept(
        prs, "Concept 1 — Inheritance", "part 2 · the knowledge you need",
        [
            (0, "**Inheritance** = deriving a new class from an existing one to "
                "**reuse** and **extend** it."),
            (1, "The relation is *“is-a”*: a `ScavTrap` **is-a** `ClapTrap`."),
            (1, "Syntax: `class Derived : public Base`."),
            (0, "**What the derived class gets**"),
            (1, "All the **public** and **protected** members of the base, for free."),
            (1, "The base's **private** members are *not* accessible → we need the "
                "`protected` setters."),
            (1, "The base constructor **must** be called, in the initializer list."),
            (0, "**C++ specifics**"),
            (1, "There is **no `super`**: the base is called by name, `ClapTrap(name)`."),
            (1, "In a `class`, everything is **private by default**."),
            (1, "The base is built **before** the derived one, and destroyed **after** it."),
        ],
        """class ScavTrap : public virtual ClapTrap
{
public:
\tScavTrap(std::string const & name);

\tvoid guardGate();

private:
\tint  myOwnData_;
};

//  the base is called by name,
//  in the initializer list
ScavTrap::ScavTrap(std::string const & name)
\t: ClapTrap(name)
{
\tmyOwnData_ = 0;
}""",
        "inheritance in 8 lines",
        note=("Encapsulation is preserved",
              "The derived class gets the **behaviour**, not the **data**: it must go "
              "through the public / protected interface of the base."))

    s_concept(
        prs, "Concept 2 — Virtual functions & dynamic binding",
        "part 2 · the knowledge you need",
        [
            (0, "A **`virtual`** method can be **overridden** by a derived class."),
            (1, "The base declares `virtual void attack(std::string const &);` and the "
                "derived class redeclares the **same signature**."),
            (0, "**Static binding** (compile time)"),
            (1, "Without `virtual`, the function is chosen from the **type of the "
                "pointer**: `ClapTrap*` → `ClapTrap::attack()`, always."),
            (0, "**Dynamic binding** (run time)"),
            (1, "With `virtual`, the function is chosen from the **real type of the "
                "object**: a `ClapTrap*` pointing to a `ScavTrap` → `ScavTrap::attack()`."),
            (0, "**Under the hood**"),
            (1, "The compiler adds a hidden **vtable** (virtual function table) and a "
                "pointer to it inside every object with virtual methods."),
            (0, "**The rule I must never forget**"),
            (1, "**The destructor must be `virtual`** as soon as the class is used "
                "polymorphically, otherwise `delete` on a base pointer leaks."),
        ],
        """class ClapTrap
{
public:
\t//  virtual -> the derived classes
\t//  may replace this behaviour
\tvirtual void attack(std::string const & target);

\t//  virtual -> delete through a
\t//  ClapTrap* destroys everything
\tvirtual ~ClapTrap();
};

class ScavTrap : public virtual ClapTrap
{
public:
\t//  same signature -> an OVERRIDE
\tvirtual void attack(std::string const & target);
};""",
        "virtual in action")

    s_concept(
        prs, "Concept 3 — Abstract classes & interfaces",
        "part 2 · the knowledge you need",
        [
            (0, "A class that declares at least one **pure virtual** function is "
                "**abstract**."),
            (1, "Syntax: `virtual void f() = 0;` — the `= 0` is the marker."),
            (1, "An abstract class **cannot be instantiated**: `Base b;` is a compile "
                "error."),
            (1, "It is a pure **contract**: *“every child must implement this”*."),
            (0, "**Why the subject does not use one here**"),
            (1, "ex00 requires a `ClapTrap` object to be created "
                "(`ClapTrap robot(\"Clappy\");`) → `ClapTrap` must be **concrete**."),
            (1, "So `attack()` is declared `virtual` but **not** pure virtual."),
            (0, "**The “interface” of the module**"),
            (1, "It is the set of public methods shared by all the traps: `attack()`, "
                "`takeDamage()`, `beRepaired()`."),
            (1, "We manipulate them through a `ClapTrap*` → the **polymorphic** usage "
                "the module title refers to."),
        ],
        """//  an ABSTRACT class = an interface
class Robot
{
public:
\tvirtual void attack(std::string const &) = 0;
\tvirtual void beRepaired(unsigned int)    = 0;
\tvirtual ~Robot() {}
};

//  Robot r;   <-- ERROR: cannot
//               instantiate an abstract class

//  a CONCRETE class
class ClapTrap : public Robot
{
public:
\tvirtual void attack(std::string const & target);
\tvirtual void beRepaired(unsigned int amount);
};""",
        "pure virtual vs. virtual")

    s_concept(
        prs, "Concept 4 — Access specifiers & encapsulation",
        "part 2 · the knowledge you need",
        [
            (0, "**`public`** — accessible from **everywhere** (the interface)."),
            (0, "**`protected`** — accessible from the class **and its derived "
                "classes** only."),
            (0, "**`private`** — accessible from the class **only**."),
            (0, "**The rule of thumb**"),
            (1, "Data → `private`, always."),
            (1, "Behaviour the outside world needs → `public`."),
            (1, "Helpers meant for the children → `protected`."),
            (0, "**Inheritance and access**"),
            (1, "With `public` inheritance, the base's `public` members stay `public` "
                "in the derived class, and its `protected` ones stay `protected`."),
            (1, "The base's `private` members are **never** accessible, not even from a "
                "derived class."),
            (0, "**How I applied it here**"),
            (1, "`name_`, `hitPoints_`, … → `private` (the subject requires it)."),
            (1, "`setHitPoints()`, `hasEnergy()`, `consumeEnergy()` → `protected`."),
            (1, "`getName()`, `attack()`, … → `public`."),
        ],
        """class ClapTrap
{
private:
\t//  only ClapTrap itself can
\t//  touch these
\tstd::string  name_;
\tunsigned int hitPoints_;

public:
\t//  everybody can use these
\tvirtual void attack(std::string const & target);
\tstd::string const & getName() const;

protected:
\t//  ClapTrap AND its children
\t//  (ScavTrap, FragTrap, ...)
\tvoid setHitPoints(unsigned int hitPoints);
\tbool hasEnergy() const;
};""",
        "the three sections")

    s_concept(
        prs, "Concept 5 — The Rule of Three (Orthodox Canonical Form)",
        "part 2 · the knowledge you need",
        [
            (0, "A class that owns a resource must manage **three** things:"),
            (1, "the **destructor** — to release the resource,"),
            (1, "the **copy constructor** — to copy it deeply,"),
            (1, "the **copy assignment operator** — to assign it deeply."),
            (1, "Plus the **default constructor**, which the 42 subject asks for "
                "explicitly."),
            (0, "**Why it matters**"),
            (1, "If the compiler generates them it copies the **pointers**, not the "
                "data → two objects share the same memory → **double free** or "
                "**leak**."),
            (1, "Here the member is a `std::string`, which manages its own memory — but "
                "the subject demands the three methods, so I write them by hand."),
            (0, "**The two rules of `operator=`**"),
            (1, "Check `if (this != &other)` to avoid the self-assignment bug."),
            (1, "Return `*this` so that `a = b = c;` works (chaining)."),
            (0, "**Inheritance**"),
            (1, "A derived `operator=` must call the base's one explicitly: "
                "`ClapTrap::operator=(other);` — otherwise the base part is not copied."),
        ],
        """ClapTrap::ClapTrap(ClapTrap const & other)
\t: name_(other.name_),
\t  hitPoints_(other.hitPoints_),
\t  energyPoints_(other.energyPoints_),
\t  attackDamage_(other.attackDamage_)
{
\tstd::cout << "ClapTrap: a copy of " << name_
\t\t\t  << " has been created." << std::endl;
}

ClapTrap & ClapTrap::operator=(ClapTrap const & other)
{
\tif (this != &other)
\t{
\t\tname_ = other.name_;
\t\thitPoints_ = other.hitPoints_;
\t\t//  ...
\t}
\treturn (*this);
}""",
        "the copy semantics")

    # ---- part 3 : the implementation ----
    s_ex00_intro(prs)
    s_ex00_ctor(prs)
    s_ex00_attack(prs)
    s_ex00_setter(prs)
    s_ex00_main(prs)
    s_ex00_proof(prs)

    s_ex01_intro(prs)
    s_ex01_ctor(prs)
    s_ex01_override(prs)
    s_ex01_poly(prs)
    s_ex01_proof(prs)

    s_ex02_intro(prs)
    s_ex02_decision(prs)
    s_ex02_proof(prs)

    s_ex03_intro(prs)
    s_ex03_problem(prs)
    s_ex03_fix(prs)
    s_ex03_impl(prs)
    s_ex03_shadow(prs)
    s_ex03_order(prs)
    s_ex03_values(prs)
    s_ex03_proof(prs)

    # ---- part 4 : summary ----
    s_design_map(prs)
    s_cheatsheet(prs)
    s_pitfalls(prs)
    s_norms(prs)
    s_testing(prs)
    s_makefile(prs)
    s_conclusion(prs)
    s_thanks(prs)

    prs.save(OUT_NAME)
    print("saved:", OUT_NAME)
    print("slides:", len(prs.slides._sldIdLst))


if __name__ == "__main__":
    build()
