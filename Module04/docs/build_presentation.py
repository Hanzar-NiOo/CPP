import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ppt_theme import *  # noqa: F401,F403
import ppt_theme

# every content slide of this deck carries the Module 04 caption
ppt_theme.FOOTER_LABEL = ("CPP Module 04  ·  Polymorphism, "
                           "Abstract Classes & Interfaces")

OUT_NAME = os.environ.get("PPTX_OUT") or os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "Module04_CPP_Presentation.pptx"))


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
         "42 SCHOOL  ·  C++ MODULE 04  ·  EVALUATION", size=12,
         color=ORANGE, font=FONT_B, bold=True)
    text(s, Inches(0.95), Inches(1.82), Inches(8.2), Inches(2.45),
         "Subtype Polymorphism,\nAbstract Classes\n& Interfaces", size=40,
         color=WHITE, font=FONT_B, bold=True, line_spacing=1.05)
    rect(s, Inches(0.95), Inches(4.32), Inches(1.3), Inches(0.06), fill=ORANGE)
    text(s, Inches(0.95), Inches(4.58), Inches(8.0), Inches(0.4),
         "Animal → Dog, Cat      AMateria → Ice, Cure", size=15,
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
        (1, "What Module 04 asks, in one slide"),
        (1, "The two class hierarchies we are going to build"),
        (0, "**Part 2 — The knowledge you need**"),
        (1, "Subtype polymorphism, virtual functions, dynamic binding"),
        (1, "Abstract classes, pure virtual functions, interfaces"),
        (1, "Ownership, the Rule of Three, deep vs. shallow copy"),
    ]
    right = [
        (0, "**Part 3 — Implementation, step by step**"),
        (1, "ex00 — Polymorphism: Animal, Dog, Cat, WrongCat"),
        (1, "ex01 — Brain: an owned resource and the deep copy"),
        (1, "ex02 — Abstract class: `makeSound() = 0`"),
        (1, "ex03 — Interface & recap: Materia, Character, MateriaSource"),
        (0, "**Part 4 — Proof and reflection**"),
        (1, "Runtime output, norms, pitfalls, conclusion"),
    ]
    bullets(s, ML, BODY_TOP, CW * 0.47, left, size=14, gap=0.13,
            max_h=Inches(3.9))
    bullets(s, ML + CW * 0.53, BODY_TOP, CW * 0.47, right, size=14, gap=0.13,
            max_h=Inches(3.9))
    callout(s, ML, Inches(5.55), CW, "The one-sentence version",
            "This module is about **behaving according to the real type of the object** "
            "even when we only know the base type (**subtype polymorphism**), and about "
            "writing **contracts** — abstract classes and interfaces — that the concrete "
            "classes must honour.",
            accent=TEAL, bg=TEAL_L, size=12.5, h=Inches(1.0))
    return s


def s_subject(prs):
    s = content_slide(prs, "The Module 04 subject in one slide", "part 1 · the subject")
    rows = [
        ["Ex.", "Subject name", "What it asks for", "New concept"],
        ["ex00", "Polymorphism",
         "An `Animal` with a virtual `makeSound()`; `Dog` and `Cat` **override** it; "
         "`WrongCat` does **not** — and shows what happens",
         "Subtype\npolymorphism"],
        ["ex01", "I don't want to set the world on fire",
         "A `Brain` (100 ideas) **owned** by `Dog` and `Cat` with `new`; the copy ctor "
         "and the assignment must be **deep**; an array of 10 `Animal *`",
         "Ownership,\ndeep copy"],
        ["ex02", "Abstract class",
         "`Animal::makeSound()` becomes **pure virtual** (`= 0`): the class cannot be "
         "instantiated anymore, everything else works the same",
         "Abstract\nclass"],
        ["ex03", "Interface & recap",
         "`AMateria` (abstract) + `Ice` / `Cure`; the interfaces `ICharacter` and "
         "`IMateriaSource`; `Character` (4 slots) and `MateriaSource` (a factory)",
         "Interfaces,\npolymorphic\ncopy"],
    ]
    table(s, ML, BODY_TOP, CW, rows, col_w=[0.7, 2.0, 6.6, 1.7], size=11.5,
          row_h=0.78, head_h=0.40)
    callout(s, ML, Inches(5.28), CW * 0.485, "What the module title means",
            "**Subtype polymorphism** = a base-class pointer that may hold a derived "
            "object, and the call resolves on the **real** type. **Abstract class** = a "
            "class that cannot be instantiated. **Interface** = a class made only of "
            "pure virtual methods.",
            accent=TEAL, bg=TEAL_L, size=11.5, h=Inches(1.42))
    callout(s, ML + CW * 0.515, Inches(5.28), CW * 0.485, "Mandatory build flags",
            "`c++ -Wall -Wextra -Werror -std=c++98` — every warning is an **error**. "
            "C++98 means: no `nullptr`, no `override`, no `auto`, no `unique_ptr`, "
            "no range-`for`.",
            accent=ORANGE, bg=ORANGE_L, size=11.5, h=Inches(1.42))
    return s


def s_roadmap(prs):
    s = content_slide(prs, "The hierarchy of ex00 – ex02", "part 1 · roadmap")
    cx = ML + Inches(3.20)
    base_y = Inches(1.75)
    class_box(s, cx - Inches(1.45), base_y, Inches(2.9), Inches(1.00), "Animal",
              ["std::string type;", "virtual void makeSound() const;"],
              head=NAVY, size=9.5)
    mid_y = Inches(3.55)
    class_box(s, cx - Inches(3.25), mid_y, Inches(2.30), Inches(0.90), "Dog",
              ["void makeSound() const;"], head=TEAL, size=9.5)
    class_box(s, cx + Inches(0.95), mid_y, Inches(2.30), Inches(0.90), "Cat",
              ["void makeSound() const;"], head=ORANGE, size=9.5)
    w_y = Inches(5.12)
    class_box(s, cx - Inches(3.25), w_y, Inches(2.30), Inches(0.85), "WrongAnimal",
              ["virtual void makeSound() const;"], head=NAVY_3, size=9.5)
    class_box(s, cx + Inches(0.95), w_y, Inches(2.30), Inches(0.85), "WrongCat",
              ["(no override!)"], head=RED, size=9.5)
    arrow_to(s, cx - Inches(2.10), mid_y, cx - Inches(0.70), base_y + Inches(1.00))
    arrow_to(s, cx + Inches(2.10), mid_y, cx + Inches(0.70), base_y + Inches(1.00))
    arrow_to(s, cx - Inches(2.10), w_y, cx - Inches(2.10), mid_y + Inches(0.90),
             color=NAVY_3)
    arrow_to(s, cx + Inches(2.10), w_y, cx + Inches(2.10), mid_y + Inches(0.90),
             color=NAVY_3)
    text(s, ML + Inches(0.05), Inches(6.12), Inches(5.6), Inches(0.5),
         "The red box is the point of ex00:\nnot overriding is a silent bug.",
         size=12, color=GREY, line_spacing=1.3)
    items = [
        (0, "**The exercise in one picture**"),
        (1, "`Animal` is the **base**: it owns the `type` and a virtual `makeSound()`."),
        (1, "`Dog` and `Cat` are **subtypes**: they override `makeSound()`."),
        (1, "`WrongCat` inherits from `WrongAnimal` and **forgets** to override → it "
            "produces the wrong sound."),
        (1, "That is why the subject asks for a *wrong* class: to make the default "
            "behaviour **visible**."),
    ]
    bullets(s, ML + CW * 0.55, BODY_TOP, CW * 0.45, items, size=13, gap=0.12,
            max_h=Inches(4.4))
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


def s_ex00_subject(prs):
    s = content_slide(prs, "ex00 — Polymorphism", "part 3 · ex00 · the base class",
                      accent=ORANGE)
    items = [
        (0, "**The subject**"),
        (1, "An `Animal` class with a `type`, a **virtual** `makeSound()` and a "
            "**virtual** destructor."),
        (1, "`Dog` and `Cat` inherit from it, set their own `type` and **override** "
            "`makeSound()`."),
        (1, "A `WrongCat` that inherits from a `WrongAnimal` **without** overriding — "
            "to show what the default behaviour looks like."),
        (1, "Calling `makeSound()` through an `Animal *` must print the sound of the "
            "**real** animal."),
        (0, "**What I add on top**"),
        (1, "The copy constructor, the assignment operator and the destructor all "
            "print a message, and `getType()` exposes the type."),
        (1, "Everything is in a **protected** `type` attribute: the subclasses set it "
            "in their constructor, the outside world only reads it."),
    ]
    bullets(s, ML, BODY_TOP, CW * 0.47, items, size=13.5, gap=0.13,
            max_h=Inches(3.6))
    code = """class Animal
{
public:
\tAnimal();
\tAnimal(Animal const & other);
\tAnimal & operator=(Animal const & other);
\tvirtual ~Animal();

\tvirtual void makeSound() const;
\tstd::string const & getType() const;

protected:
\tstd::string type;
};"""
    code_panel(s, ML + CW * 0.50, BODY_TOP, CW * 0.50, code, max_h=Inches(3.5),
               title="include/Animal.hpp", size=10.5)
    callout(s, ML, Inches(5.30), CW, "The two `virtual` keywords that matter",
            "`virtual void makeSound() const;` → the call will be resolved on the "
            "**real** type (polymorphism).   `virtual ~Animal();` → deleting through an "
            "`Animal *` destroys the **whole** object, derived part included.",
            accent=TEAL, bg=TEAL_L, size=12, h=Inches(0.9))
    return s


def s_ex00_dogcat(prs):
    s = content_slide(prs, "ex00 — Dog and Cat: the override", "ex00 · step 1",
                      accent=ORANGE)
    code = """class Dog : public Animal
{
public:
\tDog();
\tDog(Dog const & other);
\tDog & operator=(Dog const & other);
\tvirtual ~Dog();

\tvirtual void makeSound() const;
};

Dog::Dog()
\t: Animal()
{
\ttype = "Dog";
\tstd::cout << "Dog: a dog has been created." << std::endl;
}

void Dog::makeSound() const
{
\tstd::cout << "Woof woof!" << std::endl;
}"""
    code_panel(s, ML, BODY_TOP, CW * 0.50, code, max_h=Inches(3.9),
               title="include/Dog.hpp  +  src/Dog.cpp", size=10)
    items = [
        (0, "**What an override is (recap)**"),
        (1, "The derived class declares a method with the **exact same signature** as "
            "a `virtual` base method."),
        (1, "The base method must be `virtual` — otherwise the base version always "
            "runs (I show the proof on the next slide)."),
        (0, "**The 3 rules**"),
        (1, "Same name, same parameters, same return type."),
        (1, "The base method is `virtual`."),
        (1, "The access level may differ — mine stays `public`."),
        (0, "**The constructor**"),
        (1, "`: Animal()` calls the base constructor first, then the body sets "
            "`type = \"Dog\"` — the base's `type` is `protected`, so the subclass can "
            "write it."),
    ]
    bullets(s, ML + CW * 0.53, BODY_TOP, CW * 0.47, items, size=13, gap=0.12,
            max_h=Inches(3.9))
    return s


def s_ex00_wrong(prs):
    s = content_slide(prs, "ex00 — WrongCat: the point of the exercise",
                      "ex00 · step 2 · the bug made visible", accent=RED)
    code = """class WrongAnimal
{
public:
\tvirtual void makeSound() const;
};

class WrongCat : public WrongAnimal
{
public:
\t//  NO "virtual void makeSound() const;" here !
};

const WrongAnimal *wcat = new WrongCat();
wcat->makeSound();   //  ->  "Wrong animal sound: grrrooo..." !"""
    code_panel(s, ML, BODY_TOP, CW * 0.48, code, max_h=Inches(2.7),
               title="include/WrongCat.hpp", size=10.5)
    items = [
        (0, "**What the subject wants to show**"),
        (1, "If a subclass **does not override** a virtual method, the **base** "
            "implementation is used."),
        (1, "`WrongCat` is therefore a cat that **grrrooo**s."),
        (1, "It is a *silent* bug: the code compiles, it runs, it just does the "
            "**wrong thing**."),
        (0, "**Why the subject asks for it**"),
        (1, "It is the counterpart of the `Dog` / `Cat` example: together they show "
            "that the **polymorphic** behaviour comes from the *override*, not from "
            "the inheritance."),
        (1, "And it shows the **default** behaviour of a `virtual` method, which is "
            "the base's one."),
    ]
    bullets(s, ML + CW * 0.52, BODY_TOP, CW * 0.48, items, size=13, gap=0.12,
            max_h=Inches(3.2))
    code = """--- testWrongCat ---
WrongCat
Wrong animal sound: grrrooo...    <-- the WRONG sound
Wrong animal sound: grrrooo...    <-- the base one
"""
    code_panel(s, ML, Inches(4.65), CW * 0.48, code, max_h=Inches(1.5), term=True,
               title="real output", size=9.8)
    callout(s, ML + CW * 0.52, Inches(5.05), CW * 0.48, "The lesson to remember",
            "**Inheritance is not overriding.** As long as the derived class does not "
            "redeclare the method, the base's behaviour is inherited as it is — the "
            "object is a `WrongCat`, but it behaves like a `WrongAnimal`.",
            accent=ORANGE, bg=ORANGE_L, size=11.5, h=Inches(1.2))
    return s


def s_ex00_static(prs):
    s = content_slide(prs, "ex00 — What `virtual` really buys you",
                      "ex00 · proof", accent=ORANGE)
    items = [
        (0, "**The experiment**"),
        (1, "I removed `virtual` from `makeSound()` and kept everything else "
            "(`docs/evidence/`)."),
        (1, "The object is **really** a `Dog` — `getType()` prints *“Dog”*."),
        (1, "But `makeSound()` prints the **Animal** version: the call was bound at "
            "**compile time**."),
        (0, "**The two bindings**"),
        (1, "**Static binding** — the compiler picks the function from the *type of "
            "the expression*."),
        (1, "**Dynamic binding** — with `virtual`, a hidden **vtable** decides at run "
            "time."),
        (0, "**Consequence**"),
        (1, "Without `virtual`, `Dog::makeSound()` is merely **hidden**, not "
            "overridden."),
    ]
    bullets(s, ML + CW * 0.50, BODY_TOP, CW * 0.50, items, size=12.5, gap=0.12,
            max_h=Inches(3.35))
    code = """//  the same classes, but WITHOUT "virtual"
class Animal
{
public:
\tvoid makeSound() const     //  <-- NOT virtual
\t{
\t\tstd::cout << "Animal: generic sound..." << std::endl;
\t}
};

class Dog : public Animal
{
public:
\tvoid makeSound() const     //  <-- hidden, not overridden
\t{
\t\tstd::cout << "Woof woof!" << std::endl;
\t}
};

int main()
{
\tAnimal *j = new Dog();
\tstd::cout << "the real type is: " << j->getType() << std::endl;
\tj->makeSound();   //  <-- binds to Animal::makeSound
}"""
    code_panel(s, ML, BODY_TOP, CW * 0.47, code, max_h=Inches(5.18),
               title="the experiment  (the `virtual` keyword removed)", size=10)
    code = """the real type is: Dog
Animal: makes a generic animal sound...   <-- NOT the dog's sound"""
    code_panel(s, ML + CW * 0.50, Inches(4.98), CW * 0.50, code, max_h=Inches(1.1),
               term=True, title="real output", size=10)
    callout(s, ML + CW * 0.50, Inches(6.01), CW * 0.50,
            "This is the whole module in one line",
            "One interface, many behaviours — but **only** if the base method is "
            "`virtual`.",
            accent=TEAL, bg=TEAL_L, size=12, h=Inches(0.80))
    return s


def s_ex00_destroy(prs):
    s = content_slide(prs, "ex00 — Destruction through a base pointer",
                      "ex00 · step 3", accent=ORANGE)
    code = """static void testDestructionThroughBasePointer()
{
\tAnimal *animals[3];
\tanimals[0] = new Dog();
\tanimals[1] = new Cat();
\tanimals[2] = new Animal();

\tfor (int i = 0; i < 3; i++)
\t\tdelete animals[i];
}"""
    code_panel(s, ML, BODY_TOP, CW * 0.47, code, max_h=Inches(1.9),
               title="src/main.cpp", size=10.5)
    items = [
        (0, "**The rule**"),
        (1, "A `delete` on a base pointer must destroy the **derived** part too, "
            "otherwise it leaks."),
        (1, "That works **only** if the base destructor is `virtual`."),
        (0, "**The order of the calls**"),
        (1, "`Dog::~Dog()` first — the derived destructor."),
        (1, "Then `Animal::~Animal()` — the base destructor."),
        (1, "Exactly the reverse of the construction order."),
        (0, "**Without `virtual`**"),
        (1, "Only `Animal::~Animal()` would run: the `Dog` part is never destroyed → "
            "**memory leak**."),
    ]
    bullets(s, ML + CW * 0.52, BODY_TOP, CW * 0.48, items, size=13, gap=0.12,
            max_h=Inches(3.4))
    code = """Animal: an animal has been created.
Dog: a dog has been created.
Animal: an animal has been created.
Cat: a cat has been created.
Animal: an animal has been created.
Dog: the dog has been destroyed.        <-- derived first
Animal: the animal Dog has been destroyed.   <-- then the base
Cat: the cat has been destroyed.
Animal: the animal Cat has been destroyed.
Animal: the animal Animal has been destroyed."""
    code_panel(s, ML, Inches(3.80), CW * 0.47, code, max_h=Inches(2.6), term=True,
               title="real output", size=9.6)
    return s


def s_ex00_proof(prs):
    s = content_slide(prs, "ex00 — Runtime proof", "ex00 · proof", accent=ORANGE)
    out = """=== Module 04 - ex00: Polymorphism ===
--- testSubjectExample ---
Dog
Cat
Meow meow!          <-- through an "Animal *" (a Cat)
Woof woof!          <-- through an "Animal *" (a Dog)
Animal: makes a generic animal sound...
--- testWrongCat ---
WrongCat
Wrong animal sound: grrrooo...   <-- the base version !
Wrong animal sound: grrrooo...
--- testDestructionThroughBasePointer ---
Dog: the dog has been destroyed.
Animal: the animal Dog has been destroyed.
Cat: the cat has been destroyed.
Animal: the animal Cat has been destroyed.
Animal: the animal Animal has been destroyed.
--- testCopy ---
Woof woof!
Meow meow!
=== ex00 done ==="""
    code_panel(s, ML, BODY_TOP, CW * 0.56, out, max_h=Inches(4.9), term=True,
               title="terminal  ·  ./ex00", size=9.6)
    items = [
        (0, "**What the output proves**"),
        (1, "Through an `Animal *`, `i->makeSound()` prints *“Meow meow!”* and "
            "`j->makeSound()` prints *“Woof woof!”* → **dynamic binding**. ✔"),
        (1, "`meta->makeSound()` prints the generic sound: the base is still "
            "concrete in ex00. ✔"),
        (1, "`WrongCat` prints the **wrong animal** sound → the default behaviour is "
            "the base's one. ✔"),
        (1, "The destructors are called **derived first, then base**, through the "
            "base pointer. ✔"),
        (1, "The copies print their own messages and still make their own sound. ✔"),
    ]
    bullets(s, ML + CW * 0.585, BODY_TOP, CW * 0.415, items, size=12.5, gap=0.11,
            max_h=Inches(4.9))
    return s


def s_ex01_subject(prs):
    s = content_slide(prs, "ex01 — I don't want to set the world on fire",
                      "part 3 · ex01 · the brain", accent=TEAL)
    items = [
        (0, "**The subject**"),
        (1, "A `Brain` class holding **100 ideas** (`std::string ideas[100]`)."),
        (1, "`Dog` and `Cat` **own** a `Brain *` created with `new` and released with "
            "`delete` in their destructor."),
        (1, "The copy constructor and the assignment operator must make a **deep** "
            "copy of the brain."),
        (1, "The `main` builds an array of `Animal *` (half dogs, half cats) and "
            "deletes every animal through the base pointer."),
        (0, "**Why this exercise exists**"),
        (1, "It is the first time a class **owns** something → the copy semantics "
            "stop being optional, they become **mandatory**."),
        (1, "A shallow copy would make the two animals share the same brain → "
            "**double free** (I show the proof on the next slides)."),
    ]
    bullets(s, ML, BODY_TOP, CW * 0.47, items, size=13.5, gap=0.13,
            max_h=Inches(3.6))
    code = """class Brain
{
public:
\tBrain();
\tBrain(Brain const & other);
\tBrain & operator=(Brain const & other);
\t~Brain();

\tstd::string getIdea(int index) const;
\tvoid setIdea(int index, std::string const & idea);

private:
\tstd::string ideas[100];
};"""
    code_panel(s, ML + CW * 0.50, BODY_TOP, CW * 0.50, code, max_h=Inches(3.4),
               title="include/Brain.hpp", size=10.5)
    callout(s, ML, Inches(5.30), CW, "The fixed-size array, not a std::vector",
            "The subject forbids the STL containers until module 08, so `ideas` is a "
            "plain C array of **100** `std::string`. The same rule applies to the "
            "inventories of ex03: **4** slots, plain arrays, no `std::vector`.",
            accent=ORANGE, bg=ORANGE_L, size=12, h=Inches(0.9))
    return s


def s_ex01_deep(prs):
    s = content_slide(prs, "ex01 — The deep copy", "ex01 · step 1", accent=TEAL)
    code = """//  the constructor: the brain is created
Dog::Dog()
\t: Animal(),
\t  brain(new Brain())
{
\ttype = "Dog";
}

//  the copy constructor: a NEW brain is created
Dog::Dog(Dog const & other)
\t: Animal(other),
\t  brain(new Brain(*other.brain))
{
}

//  the assignment: the old brain is deleted first
Dog & Dog::operator=(Dog const & other)
{
\tif (this != &other)
\t{
\t\tAnimal::operator=(other);
\t\tdelete brain;
\t\tbrain = new Brain(*other.brain);
\t}
\treturn (*this);
}

//  the destructor: the brain is released
Dog::~Dog()
{
\tdelete brain;
}"""
    code_panel(s, ML, BODY_TOP, CW * 0.49, code, max_h=Inches(4.5),
               title="src/Dog.cpp", size=9.8)
    items = [
        (0, "**The three rules of a deep copy**"),
        (1, "**Constructor** → `new Brain(*other.brain)`: a brand new brain, filled "
            "with a copy of the ideas."),
        (1, "**Assignment** → `delete brain;` **then** `new Brain(*other.brain)`: the "
            "old brain is released first, otherwise it leaks."),
        (1, "**Destructor** → `delete brain;`: the brain is released."),
        (0, "**What the shallow copy would do**"),
        (1, "`brain(other.brain)` copies the **pointer**, not the data."),
        (1, "The two dogs then share the same brain → it is deleted twice → "
            "**double free**."),
        (0, "**The Rule of Three**"),
        (1, "A class that owns a raw pointer needs a **copy constructor**, an "
            "**assignment operator** and a **destructor** — the three must be "
            "consistent with each other."),
    ]
    bullets(s, ML + CW * 0.52, BODY_TOP, CW * 0.48, items, size=12.5, gap=0.11,
            max_h=Inches(4.6))
    return s


def s_ex01_bug(prs):
    s = content_slide(prs, "ex01 — Proof: what a shallow copy really does",
                      "ex01 · the bug, made visible", accent=RED)
    items = [
        (0, "**The experiment**"),
        (1, "I wrote the copy constructor as `brain(other.brain)` — a **shallow** "
            "copy — and ran it under `-fsanitize=address`."),
        (1, "The program is in `docs/evidence/` and `run_evidence.sh` replays it."),
        (0, "**What happens**"),
        (1, "The brain is created **once** but destroyed **twice**: the two dogs "
            "share the same pointer."),
        (1, "AddressSanitizer catches it immediately: *“attempting double-free”*."),
        (1, "The process id and the addresses change at **every run** — the "
            "**message** does not."),
        (0, "**Why it matters for the evaluation**"),
        (1, "This is exactly what the subject is testing: a copy must be **deep**, "
            "otherwise the program is undefined behaviour."),
        (1, "My real code does **not** have this bug — the test below proves it."),
    ]
    bullets(s, ML, BODY_TOP, CW * 0.45, items, size=13, gap=0.12,
            max_h=Inches(3.85))
    code = """Brain: created
Brain: destroyed
Brain: destroyed          <-- deleted twice!
=================================================================
==3705==ERROR: AddressSanitizer: attempting double-free on 0x502000000010 in thread T0:
    #0 ... in operator delete(void*)
    #1 ... in Dog::~Dog()
    #2 ... in main
0x502000000010 is located 0 bytes inside of 1-byte region
freed by thread T0 here:
    #0 ... in operator delete(void*)
    #1 ... in Dog::~Dog()
    #2 ... in main
previously allocated by thread T0 here:
    #0 ... in operator new(unsigned long)
    #1 ... in Dog::Dog()
    #2 ... in main
SUMMARY: AddressSanitizer: double-free in operator delete(void*)"""
    code_panel(s, ML + CW * 0.48, BODY_TOP, CW * 0.52, code, max_h=Inches(3.56),
               term=True, title="real output  (the buggy version)", size=9.2)
    code = """Brain: a new brain has been created.
Brain: a copy of a brain has been created.
the original dog thinks: I want to play!
the copy of the dog thinks: I want to sleep!"""
    code_panel(s, ML + CW * 0.48, Inches(5.22), CW * 0.52, code, max_h=Inches(1.4),
               term=True, title="my real code (ex01)", size=9.2)
    callout(s, ML, Inches(5.22), CW * 0.45, "The proof of a deep copy",
            "The original thinks *“I want to play!”* and the copy thinks *“I want to "
            "sleep!”* → they have **two different brains**. With a shallow copy they "
            "would share one, and the last write would win.",
            accent=TEAL, bg=TEAL_L, size=11.5, h=Inches(1.4))
    return s


def s_ex01_array(prs):
    s = content_slide(prs, "ex01 — An array of ten animals",
                      "ex01 · step 2", accent=TEAL)
    code = """Animal *animals[10];
for (int i = 0; i < 10; i++)
{
\tif (i % 2 == 0)
\t{
\t\tDog *dog = new Dog();
\t\tdog->setIdea(i, "I want to play!");
\t\tanimals[i] = dog;
\t}
\telse
\t{
\t\tCat *cat = new Cat();
\t\tcat->setIdea(i, "I want some food!");
\t\tanimals[i] = cat;
\t}
}

for (int i = 0; i < 10; i++)
{
\tstd::cout << "animal " << i << " is a "
\t\t\t  << animals[i]->getType() << std::endl;
\tanimals[i]->makeSound();
}

for (int i = 0; i < 10; i++)
\tdelete animals[i];"""
    code_panel(s, ML, BODY_TOP, CW * 0.50, code, max_h=Inches(4.6),
               title="src/main.cpp", size=9.6)
    items = [
        (0, "**What this exercises**"),
        (1, "The array is declared as `Animal *animals[10]` — **one** type, ten "
            "different objects."),
        (1, "Each element points to a `Dog` or a `Cat`; the array itself knows "
            "nothing about it."),
        (1, "`getType()` and `makeSound()` are called through the base pointer → the "
            "**real** behaviour of each animal."),
        (0, "**The ownership**"),
        (1, "The `main` creates the animals with `new` → the `main` owns them."),
        (1, "It deletes them through the `Animal *` → the **virtual** destructor "
            "makes sure the brain is released too."),
        (0, "**The result in the output**"),
        (1, "10 animals, 10 different sounds, and 10 brains destroyed — no leak."),
    ]
    bullets(s, ML + CW * 0.53, BODY_TOP, CW * 0.47, items, size=12.5, gap=0.11,
            max_h=Inches(4.6))
    return s


def s_ex01_proof(prs):
    s = content_slide(prs, "ex01 — Runtime proof", "ex01 · proof", accent=TEAL)
    out = """--- testArrayOfAnimals ---
animal 0 is a Dog
Woof woof!
animal 1 is a Cat
Meow meow!
animal 2 is a Dog
Woof woof!
...
animal 9 is a Cat
Meow meow!
(every animal is deleted through an Animal pointer)
Dog: the dog has been destroyed.
Brain: a brain has been destroyed.
Animal: the animal Dog has been destroyed.
Cat: the cat has been destroyed.
Brain: a brain has been destroyed.
Animal: the animal Cat has been destroyed.
...
--- testDeepCopy ---
the original dog thinks: I want to play!
the copy of the dog thinks: I want to sleep!
the original cat thinks: I want some food!
the copy of the cat thinks: I want to nap!"""
    code_panel(s, ML, BODY_TOP, CW * 0.56, out, max_h=Inches(4.9), term=True,
               title="terminal  ·  ./ex01", size=9.4)
    items = [
        (0, "**What the output proves**"),
        (1, "The array of 10 base pointers produces the **right** sound for each "
            "animal. ✔"),
        (1, "Each destruction prints **3** lines: the derived destructor, then "
            "*“Brain: a brain has been destroyed.”*, then the base destructor → the "
            "brain is released **exactly once**. ✔"),
        (1, "The original and the copy think **different things** → the brain was "
            "copied deeply. ✔"),
        (1, "The assignment (`catCopy = catOriginal`) also prints *“Brain: a brain has "
            "been destroyed.”* **before** *“Brain: a copy of a brain has been "
            "created.”* → the old brain is released first. ✔"),
    ]
    bullets(s, ML + CW * 0.585, BODY_TOP, CW * 0.415, items, size=12.5, gap=0.11,
            max_h=Inches(4.9))
    return s


def s_ex02_subject(prs):
    s = content_slide(prs, "ex02 — Abstract class", "part 3 · ex02 · the pure virtual",
                      accent=ORANGE)
    items = [
        (0, "**The subject**"),
        (1, "`Animal::makeSound()` becomes **pure virtual**."),
        (1, "The class becomes **abstract**: it cannot be instantiated anymore."),
        (1, "Everything else works exactly as in ex01."),
        (0, "**What changes in the code**"),
        (1, "**One line** in `Animal.hpp`."),
        (1, "And the **definition** of `makeSound()` disappears from `Animal.cpp` — a "
            "pure virtual function has **no body**."),
        (1, "The `WrongAnimal` / `WrongCat` pair stays concrete: `WrongAnimal` still "
            "implements `makeSound()`."),
        (0, "**Why it is better**"),
        (1, "The compiler now **guarantees** that every animal has a sound — you "
            "cannot forget to implement it."),
        (1, "It is the same guarantee the interfaces of ex03 give, but with a shared "
            "implementation for the common parts."),
    ]
    bullets(s, ML, BODY_TOP, CW * 0.47, items, size=13.5, gap=0.13,
            max_h=Inches(3.9))
    code = """//  include/Animal.hpp  (ex01 -> ex02)
 class Animal
 {
 public:
 \tAnimal();
 \tAnimal(Animal const & other);
 \tAnimal & operator=(Animal const & other);
 \tvirtual ~Animal();

-\tvirtual void makeSound() const;
+\tvirtual void makeSound() const = 0;
 \tstd::string const & getType() const;

 protected:
 \tstd::string type;
 };

//  src/Animal.cpp  -- the definition is removed
-void Animal::makeSound() const
-{
-\tstd::cout << "Animal: makes a generic animal sound..."
-\t\t\t  << std::endl;
-}"""
    code_panel(s, ML + CW * 0.50, BODY_TOP, CW * 0.50, code, max_h=Inches(3.9),
               title="the whole difference", size=9.6)
    callout(s, ML, Inches(5.60), CW, "A note on the name",
            "The subject suggests renaming the class to `AAnimal` (the `A` prefix of "
            "the 42 conventions for an abstract class). I kept the name `Animal` "
            "because the subject of ex00 already introduces it that way and the "
            "exercises stay consistent — but the rename is trivial and I would do it "
            "if the evaluator expects it.",
            accent=TEAL, bg=TEAL_L, size=11.5, h=Inches(0.95))
    return s


def s_ex02_error(prs):
    s = content_slide(prs, "ex02 — What the compiler now refuses",
                      "ex02 · proof", accent=RED)
    items = [
        (0, "**The experiment**"),
        (1, "In the `main` of ex02 I write `Animal animal;` — the instantiation the "
            "subject forbids (`docs/evidence/`)."),
        (1, "The compiler refuses, and it tells us **exactly why**."),
        (0, "**What the error proves**"),
        (1, "The class is **abstract** — it cannot be instantiated."),
        (1, "The compiler names the pure virtual function: *“`virtual void "
            "Animal::makeSound() const`”*."),
        (1, "This is a **compile-time** guarantee: it is impossible to write an "
            "animal without a sound."),
        (0, "**What still works**"),
        (1, "`Animal *animals[4]; animals[0] = new Dog();` → perfectly legal: "
            "pointing to a concrete subclass is allowed."),
        (1, "Only **instantiating** the abstract class is forbidden."),
    ]
    bullets(s, ML, BODY_TOP, CW * 0.45, items, size=13, gap=0.12,
            max_h=Inches(4.2))
    code = """abstract_error.cpp: In function 'int main()':
abstract_error.cpp:7:16: error: cannot declare variable
    'animal' to be of abstract type 'Animal'
    7 |         Animal animal;
      |                ^~~~~~
In file included from abstract_error.cpp:3:
../../ex02/include/Animal.hpp:6:7: note:   because the following
    virtual functions are pure within 'Animal':
    6 | class Animal
      |       ^~~~~~
../../ex02/include/Animal.hpp:14:22: note:
    'virtual void Animal::makeSound() const'
   14 |         virtual void makeSound() const = 0;
      |                      ^~~~~~~~~"""
    code_panel(s, ML + CW * 0.48, BODY_TOP, CW * 0.52, code, max_h=Inches(4.3),
               term=True, title="real compiler output", size=9.0)
    callout(s, ML + CW * 0.48, Inches(5.05), CW * 0.52, "The rule in one line",
            "A class with at least one pure virtual function is **abstract**: it "
            "cannot be instantiated, but it can be **inherited** and **used through "
            "pointers**.",
            accent=TEAL, bg=TEAL_L, size=11.5, h=Inches(1.2))
    return s


def s_ex02_proof(prs):
    s = content_slide(prs, "ex02 — Runtime proof", "ex02 · proof", accent=ORANGE)
    out = """=== Module 04 - ex02: Abstract class ===
--- testAbstractAnimal ---
(the Animal class is abstract, it cannot be instantiated anymore)
(writing 'Animal animal;' in the main would not compile)
Animal: an animal has been created.
Brain: a new brain has been created.
Dog: a dog has been created.
...
animal 0 is a Dog
Woof woof!
animal 1 is a Cat
Meow meow!
...
Dog: the dog has been destroyed.
Brain: a brain has been destroyed.
Animal: the animal Dog has been destroyed.
...
--- testWrongCat ---
Wrong animal sound: grrrooo...
--- testDeepCopy ---
the original dog thinks: I want to play!
the copy of the dog thinks: I want to sleep!
=== ex02 done ==="""
    code_panel(s, ML, BODY_TOP, CW * 0.56, out, max_h=Inches(4.9), term=True,
               title="terminal  ·  ./ex02", size=9.4)
    items = [
        (0, "**What the output proves**"),
        (1, "The behaviour of ex01 is **unchanged**: same sounds, same destruction "
            "order, same deep copies. ✔"),
        (1, "Only one thing disappeared: the *“Animal: makes a generic animal "
            "sound…”* line — because there is no longer any concrete `Animal`. ✔"),
        (1, "`WrongCat` still prints the wrong sound: `WrongAnimal` is **concrete** "
            "and implements `makeSound()`. ✔"),
        (1, "The deep copy still works. ✔"),
    ]
    bullets(s, ML + CW * 0.585, BODY_TOP, CW * 0.415, items, size=12.5, gap=0.11,
            max_h=Inches(4.9))
    return s


def s_ex03_subject(prs):
    s = content_slide(prs, "ex03 — Interface & recap", "part 3 · ex03 · the big one",
                      accent=TEAL)
    rows = [
        ["Class", "Kind", "Role"],
        ["`AMateria`", "abstract class", "The base of the Materias: `getType()`, a pure "
         "virtual `clone()` and a virtual `use(ICharacter &)`"],
        ["`Ice` / `Cure`", "concrete classes", "The two Materias: they override "
         "`clone()` and `use()`"],
        ["`ICharacter`", "interface", "The contract of a character: `getName()`, "
         "`equip()`, `unequip()`, `use()` — all pure virtual"],
        ["`Character`", "implementation", "A character with a **name** and an "
         "inventory of **4** slots"],
        ["`IMateriaSource`", "interface", "The contract of a source: `learnMateria()`, "
         "`createMateria()` — pure virtual"],
        ["`MateriaSource`", "implementation", "A factory that learns at most **4** "
         "Materias and creates new ones"],
    ]
    table(s, ML, BODY_TOP, CW, rows, col_w=[1.7, 1.9, 8.0], size=11.5,
          row_h=0.52, head_h=0.42)
    callout(s, ML, Inches(5.75), CW, "What this exercise really teaches",
            "It puts **everything** together: an abstract class (`AMateria`), two "
            "**interfaces** (`ICharacter`, `IMateriaSource`), **polymorphic copying** "
            "(`clone()`), and **ownership** — who deletes the Materias, and when. "
            "It is the recap of the whole module.",
            accent=TEAL, bg=TEAL_L, size=12, h=Inches(0.95))
    return s


def s_ex03_materia(prs):
    s = content_slide(prs, "ex03 — AMateria: the abstract class",
                      "ex03 · step 1", accent=TEAL)
    code = """class ICharacter;

class AMateria
{
public:
\tAMateria(std::string const & type);
\tvirtual ~AMateria();

\tstd::string const & getType() const;
\tvirtual AMateria *clone() const = 0;
\tvirtual void use(ICharacter &target);

protected:
\tstd::string type_;
};

void AMateria::use(ICharacter &target)
{
\tstd::cout << "* uses the " << type_ << " materia on "
\t\t\t  << target.getName() << " *" << std::endl;
}"""
    code_panel(s, ML, BODY_TOP, CW * 0.49, code, max_h=Inches(4.3),
               title="include/AMateria.hpp  +  src/AMateria.cpp", size=9.8)
    items = [
        (0, "**The abstract class**"),
        (1, "`clone()` is **pure virtual**: every concrete Materia must know how to "
            "copy itself."),
        (1, "`use(ICharacter &)` is **virtual with a generic body**: the default "
            "implementation prints *“uses the … materia on …”*."),
        (0, "**Why the generic body exists**"),
        (1, "It gives a **fallback** to the concrete Materias that do not override it "
            "— here `Ice` and `Cure` both do."),
        (1, "It is also the subject's own wording: a generic `use()` plus two "
            "specialised ones."),
        (0, "**The forward declaration**"),
        (1, "`class ICharacter;` at the top — we only need a **reference** to it in "
            "the prototype, so a forward declaration is enough and it avoids the "
            "circular include."),
    ]
    bullets(s, ML + CW * 0.52, BODY_TOP, CW * 0.48, items, size=12.5, gap=0.11,
            max_h=Inches(4.4))
    return s


def s_ex03_icecure(prs):
    s = content_slide(prs, "ex03 — Ice and Cure: the concrete Materias",
                      "ex03 · step 2", accent=TEAL)
    code = """class Ice : public AMateria
{
public:
\tIce();
\tvirtual ~Ice();

\tvirtual AMateria *clone() const;
\tvirtual void use(ICharacter &target);
};

Ice::Ice()
\t: AMateria("ice")
{
}

AMateria *Ice::clone() const
{
\treturn (new Ice());
}

void Ice::use(ICharacter &target)
{
\tstd::cout << "* shoots an ice bolt at " << target.getName()
\t\t\t  << " *" << std::endl;
}"""
    code_panel(s, ML, BODY_TOP, CW * 0.49, code, max_h=Inches(4.3),
               title="include/Ice.hpp  +  src/Ice.cpp", size=9.8)
    items = [
        (0, "**Two concrete Materias**"),
        (1, "`Ice` → the type *“ice”*, `Cure` → the type *“cure”*."),
        (1, "Both override `clone()` and `use()`; the rest is inherited from "
            "`AMateria`."),
        (0, "**`clone()` — the polymorphic copy constructor**"),
        (1, "`AMateria *clone() const` returns a **new object of the dynamic type**."),
        (1, "Through an `AMateria *` pointing to an `Ice`, `clone()` gives back an "
            "`Ice` — the class knows how to copy *itself*."),
        (1, "This is the C++98 way of doing it: the return type is the **base** "
            "pointer, because covariant return types only arrived in C++17."),
        (0, "**`use()` — the specialisation**"),
        (1, "`Ice` shoots an ice bolt, `Cure` heals the target's wounds."),
    ]
    bullets(s, ML + CW * 0.52, BODY_TOP, CW * 0.48, items, size=12.5, gap=0.11,
            max_h=Inches(4.5))
    return s


def s_ex03_interfaces(prs):
    s = content_slide(prs, "ex03 — ICharacter and IMateriaSource: the interfaces",
                      "ex03 · step 3", accent=TEAL)
    code = """class AMateria;

class ICharacter
{
public:
\tvirtual ~ICharacter();
\tvirtual std::string const & getName() const = 0;
\tvirtual void equip(AMateria *m) = 0;
\tvirtual void unequip(int idx) = 0;
\tvirtual void use(int idx, ICharacter &target) = 0;
};

class AMateria;

class IMateriaSource
{
public:
\tvirtual ~IMateriaSource();
\tvirtual void learnMateria(AMateria *m) = 0;
\tvirtual AMateria *createMateria(std::string const & type) = 0;
};"""
    code_panel(s, ML, BODY_TOP, CW * 0.49, code, max_h=Inches(4.0),
               title="include/ICharacter.hpp  +  include/IMateriaSource.hpp", size=9.4)
    items = [
        (0, "**What is an interface in C++?**"),
        (1, "A class whose methods are **all pure virtual** — nothing but a "
            "contract."),
        (1, "The `I` prefix is the 42 convention to make it obvious at the call "
            "site: `ICharacter *me = new Character(\"me\");`."),
        (0, "**Why the destructor is not pure virtual**"),
        (1, "A **virtual** destructor is still **defined** (in the `.cpp`), so that "
            "deleting through the interface is safe."),
        (1, "The 42 Norms forbid any implementation inside a header → the body goes "
            "into a separate `.cpp` file."),
        (0, "**The forward declaration**"),
        (1, "`class AMateria;` — the interfaces only manipulate Materias through "
            "**pointers**, so they never need the full definition."),
    ]
    bullets(s, ML + CW * 0.52, BODY_TOP, CW * 0.48, items, size=12.5, gap=0.11,
            max_h=Inches(4.3))
    return s


def s_ex03_character(prs):
    s = content_slide(prs, "ex03 — Character: the inventory",
                      "ex03 · step 4", accent=TEAL)
    code = """class Character : public ICharacter
{
public:
\tCharacter(std::string const & name);
\tvirtual std::string const & getName() const;
\tvirtual void equip(AMateria *m);
\tvirtual void unequip(int idx);
\tvirtual void use(int idx, ICharacter &target);

\tAMateria *getMateria(int idx) const;

private:
\tstd::string name_;
\tAMateria *inventory_[4];
};"""
    code_panel(s, ML, BODY_TOP, CW * 0.50, code, max_h=Inches(4.2),
               title="include/Character.hpp", size=11)
    items = [
        (0, "**The inventory**"),
        (1, "A plain array of **4** pointers — no STL yet (module 08)."),
        (1, "`0` is the “empty slot” marker, because C++98 has no `nullptr`."),
        (1, "The array is **not** initialised in the header: the constructor does it."),
        (0, "**Every method is `virtual`**"),
        (1, "The class implements the `ICharacter` contract — the compiler checks "
            "that all four pure virtual methods are there."),
        (1, "Because the destructor of the interface is virtual, `delete` through an "
            "`ICharacter *` is safe."),
        (0, "**The name**"),
        (1, "`name_` is a `std::string` stored **by value** — copying a character "
            "copies the string, no pointer involved."),
    ]
    bullets(s, ML + CW * 0.53, BODY_TOP, CW * 0.47, items, size=12.5, gap=0.11,
            max_h=Inches(4.2))
    callout(s, ML, Inches(5.98), CW, "Why the slots are raw pointers, and not a "
            "std::vector<AMateria *>",
            "Module 04 is C++98 and the 42 Norms forbid the containers of the "
            "standard library here (they come back in module 08). A fixed array of "
            "**4** pointers also matches the subject exactly: *“the character has "
            "4 materia slots”*.",
            accent=ORANGE, bg=ORANGE_L, size=11.5, h=Inches(0.80))
    return s


def s_ex03_equip(prs):
    s = content_slide(prs, "ex03 — `equip()` and `unequip()`",
                      "ex03 · step 4", accent=TEAL)
    code = """void Character::equip(AMateria *m)
{
\tif (!m)
\t\treturn;
\tfor (int i = 0; i < 4; i++)
\t{
\t\tif (!inventory_[i])
\t\t{
\t\t\tinventory_[i] = m;
\t\t\treturn;
\t\t}
\t}
\t//  the inventory is full: the caller keeps the materia
}

void Character::unequip(int idx)
{
\tif (idx < 0 || idx > 3 || !inventory_[idx])
\t\treturn;
\tinventory_[idx] = 0;   //  NOT deleted: left on the floor
}"""
    code_panel(s, ML, BODY_TOP, CW * 0.50, code, max_h=Inches(5.0),
               title="src/Character.cpp", size=11)
    items = [
        (0, "**`equip()` takes ownership**"),
        (1, "The character stores the pointer → the character **deletes** it in its "
            "destructor."),
        (1, "If the inventory is **full**, the materia is **not** taken: it stays the "
            "property of the caller."),
        (0, "**`unequip()` does not delete**"),
        (1, "The slot is emptied but the Materia is left alive — the caller becomes "
            "the owner."),
        (1, "This asymmetry is the trickiest part of the exercise, and the subject "
            "asks for it explicitly."),
        (0, "**Both are defensive**"),
        (1, "`equip(0)` is ignored, and `unequip()` rejects an index outside "
            "`0..3` or an empty slot → no crash, no out-of-bounds write."),
    ]
    bullets(s, ML + CW * 0.53, BODY_TOP, CW * 0.47, items, size=12.5, gap=0.11,
            max_h=Inches(3.55))
    callout(s, ML + CW * 0.53, Inches(5.30), CW * 0.47, "The contract in one line",
            "`equip()` **consumes** the pointer, `unequip()` **returns** it: "
            "ownership moves, and it is always explicit.",
            accent=TEAL, bg=TEAL_L, size=11.5, h=Inches(1.15))
    return s


def s_ex03_source(prs):
    s = content_slide(prs, "ex03 — MateriaSource: the factory",
                      "ex03 · step 5", accent=TEAL)
    code = """class MateriaSource : public IMateriaSource
{
public:
\tMateriaSource();
\tvirtual void learnMateria(AMateria *m);
\tvirtual AMateria *createMateria(std::string const & type);

private:
\tAMateria *learned_[4];
};

void MateriaSource::learnMateria(AMateria *m)
{
\tif (!m)
\t\treturn;
\tfor (int i = 0; i < 4; i++)
\t{
\t\tif (!learned_[i])
\t\t{
\t\t\tlearned_[i] = m->clone();   //  keep a template
\t\t\tdelete m;                   //  release the original
\t\t\treturn;
\t\t}
\t}
\tdelete m;   //  the source is full: the materia is released
}

AMateria *MateriaSource::createMateria(std::string const & type)
{
\tfor (int i = 0; i < 4; i++)
\t{
\t\tif (learned_[i] && learned_[i]->getType() == type)
\t\t\treturn (learned_[i]->clone());
\t}
\treturn (0);   //  unknown type
}"""
    code_panel(s, ML, BODY_TOP, CW * 0.49, code, max_h=Inches(4.6),
               title="include/MateriaSource.hpp  +  src/MateriaSource.cpp", size=9.2)
    items = [
        (0, "**`learnMateria()` takes ownership**"),
        (1, "The subject's `main` writes `src->learnMateria(new Ice());` — the "
            "temporary is **never** deleted by the caller."),
        (1, "So the source must take ownership: it keeps a **clone** as a template "
            "and **deletes the original**."),
        (1, "Without that, the subject's own example would leak."),
        (0, "**`createMateria()` is a factory**"),
        (1, "It looks for a learned template of that type and returns a **clone** of "
            "it — a brand new Materia the caller owns."),
        (1, "An unknown type returns **`0`**, exactly as the subject asks."),
        (0, "**Why clone and not share?**"),
        (1, "Two characters must never share the same Materia, otherwise unequipping "
            "it in one would break the other."),
    ]
    bullets(s, ML + CW * 0.52, BODY_TOP, CW * 0.48, items, size=12, gap=0.10,
            max_h=Inches(4.7))
    return s


def s_ex03_ownership(prs):
    s = content_slide(prs, "ex03 — Ownership: who deletes what?",
                      "ex03 · the key design table", accent=ORANGE)
    rows = [
        ["Call", "Who owns the Materia afterwards?", "Who deletes it?"],
        ["`me.equip(m)` — the slot is free", "**the character**",
         "the character, in `~Character()`"],
        ["`me.equip(m)` — the inventory is full", "**the caller** (unchanged)",
         "the caller"],
        ["`me.unequip(0)`", "**the caller** (it is left on the floor)",
         "the caller, if it wants to"],
        ["`src->learnMateria(new Ice())`", "**the source** (it keeps a clone)",
         "the source releases the original at once"],
        ["`src->createMateria(\"ice\")`", "**the caller**",
         "the caller"],
        ["`AMateria *c = m->clone();`", "**the caller**", "the caller"],
    ]
    table(s, ML, BODY_TOP, CW, rows, col_w=[3.2, 4.6, 3.8], size=11.5,
          row_h=0.5, head_h=0.44)
    callout(s, ML, Inches(5.25), CW * 0.485, "The rule I follow everywhere",
            "**Every function says who owns the pointer.** `equip()` takes it, "
            "`unequip()` gives it back, `learnMateria()` takes it, `createMateria()` "
            "gives one. There is never a moment where nobody knows.",
            accent=TEAL, bg=TEAL_L, size=11.5, h=Inches(1.2))
    callout(s, ML + CW * 0.515, Inches(5.25), CW * 0.485, "Why the deep copy matters here",
            "The copy constructor of `Character` **clones** every Materia of the "
            "other character, and the assignment operator **deletes** its own Materias "
            "first. Two characters never share a Materia — that is what `clone()` is "
            "for.",
            accent=ORANGE, bg=ORANGE_L, size=11.5, h=Inches(1.2))
    return s


def s_ex03_proof(prs):
    s = content_slide(prs, "ex03 — Runtime proof", "ex03 · proof", accent=TEAL)
    out = """=== Module 04 - ex03: Interface & recap ===
--- testSubjectExample ---
MateriaSource: a new ice materia has been learned.
MateriaSource: a new cure materia has been learned.
Character: me has been created.
Character: me equips a ice materia in slot 0.
Character: me equips a cure materia in slot 1.
Character: bob has been created.
* shoots an ice bolt at bob *
* heals bob's wounds *
--- testFullInventory ---
Character: me equips a ice materia in slot 0.
...
Character: me cannot equip that materia, the inventory is full.
--- testUnknownMateria ---
MateriaSource: the type unknown is unknown.
the unknown materia could not be created.
--- testDeepCopy ---
the copy owns its own materia: deep copy.
the assigned character owns its own materia: deep copy.
=== ex03 done ==="""
    code_panel(s, ML, BODY_TOP, CW * 0.56, out, max_h=Inches(4.9), term=True,
               title="terminal  ·  ./ex03", size=9.2)
    items = [
        (0, "**What the output proves**"),
        (1, "The subject's scenario works **through the interfaces**: `IMateriaSource "
            "*` and `ICharacter *` are enough to run the whole thing. ✔"),
        (1, "The two Materias behave **differently** through the same `use()` call → "
            "polymorphism. ✔"),
        (1, "The 5th Materia is **refused** when the inventory is full, and the "
            "caller keeps it. ✔"),
        (1, "An unknown type returns `0` → the caller checks the pointer. ✔"),
        (1, "The copy owns **its own** Materias → deep copy, thanks to `clone()`. ✔"),
    ]
    bullets(s, ML + CW * 0.585, BODY_TOP, CW * 0.415, items, size=12.5, gap=0.11,
            max_h=Inches(4.9))
    return s


def s_design_map(prs):
    s = content_slide(prs, "The complete design map", "summary", accent=NAVY_3)
    code = """  ex00 - ex02                     ex03
  -----------                    -----
        Animal                 AMateria (abstract)
        /    \\                 /            \\
   Dog        Cat            Ice            Cure
                                   (clone, use)

  WrongAnimal                ICharacter        IMateriaSource
       |                     (interface)        (interface)
  WrongCat                    |                    |
  (no override)          Character            MateriaSource
                        (4 slots)             (4 templates)"""
    code_panel(s, ML, BODY_TOP, CW * 0.44, code, max_h=Inches(4.3),
               title="the two hierarchies", size=10)
    items = [
        (0, "**Who owns what**"),
        (1, "`Animal` owns the `type`; `Dog` and `Cat` own a `Brain`."),
        (1, "`AMateria` owns the `type_`; `Character` owns **4** Materias; "
            "`MateriaSource` owns **4** templates."),
        (0, "**The four techniques used**"),
        (1, "**`virtual`** → the behaviour depends on the real type "
            "(`makeSound()`, `use()`)."),
        (1, "**`= 0`** → the abstract classes (`AMateria`, `Animal` in ex02)."),
        (1, "**Pure virtual interfaces** → the contracts (`ICharacter`, "
            "`IMateriaSource`)."),
        (1, "**`clone()`** → the polymorphic copy constructor."),
        (1, "**The Rule of Three** → the deep copy of every owned pointer."),
    ]
    bullets(s, ML + CW * 0.47, BODY_TOP, CW * 0.53, items, size=12.5, gap=0.11,
            max_h=Inches(4.6))
    return s


def s_cheatsheet(prs):
    s = content_slide(prs, "Cheat sheet — the C++ knowledge this module needs",
                      "summary · knowledge", accent=TEAL)
    rows = [
        ["Concept", "The syntax", "What it really does", "Where I used it"],
        ["Inheritance", "`class D : public B`",
         "`D` reuses and extends `B`; it gets `B`'s public and protected members",
         "Dog, Cat, AMateria"],
        ["Virtual function", "`virtual void f();`",
         "The call is resolved on the **real** type of the object (dynamic binding)",
         "`makeSound()`, `use()`"],
        ["Pure virtual", "`virtual void f() = 0;`",
         "Makes the class **abstract** — it cannot be instantiated", "`Animal` (ex02), "
         "`AMateria`"],
        ["Interface", "a class with only pure virtuals",
         "A pure **contract** that the implementations must honour",
         "`ICharacter`, `IMateriaSource`"],
        ["Virtual destructor", "`virtual ~B();`",
         "Makes `delete` through a base pointer destroy the **whole** object",
         "`~Animal()`, `~AMateria()`"],
        ["Polymorphic copy", "`virtual B *clone() const;`",
         "Returns a new object of the **dynamic** type — the C++98 copy constructor",
         "`Ice::clone()`, `Cure::clone()`"],
        ["Rule of Three", "copy ctor + `operator=` + dtor",
         "Makes the copy **deep** and the ownership consistent", "Brain, Character, "
         "MateriaSource"],
        ["Empty marker", "`0` (C++98 has no `nullptr`)", "Means *“no pointer / empty "
         "slot”*", "the inventories"],
    ]
    table(s, ML, BODY_TOP, CW, rows, col_w=[1.7, 2.6, 5.4, 2.3], size=11,
          row_h=0.45, head_h=0.40)
    callout(s, ML, Inches(6.00), CW, "If you remember only three things",
            "**1.** `virtual` = the *real* type decides.   **2.** `= 0` = the class "
            "becomes abstract and the compiler checks the contract.   **3.** A class "
            "that owns a pointer needs a **deep** copy — copy ctor, assignment and "
            "destructor, all three.",
            accent=TEAL, bg=TEAL_L, size=11.5, h=Inches(0.8))
    return s


def s_pitfalls(prs):
    s = content_slide(prs, "Common pitfalls — and how I avoided them",
                      "summary · reflection", accent=RED)
    rows = [
        ["Pitfall", "What goes wrong", "How my code avoids it"],
        ["A non-virtual destructor", "`delete` through a base pointer → the derived "
         "part leaks", "`virtual ~Animal();` and `virtual ~AMateria();`"],
        ["Forgetting to override", "The base's behaviour is silently used (the "
         "`WrongCat` case)", "Every concrete class overrides `makeSound()` / `use()`"],
        ["A shallow copy of an owned pointer", "Double free — caught by ASan",
         "`new Brain(*other.brain)`, `inventory_[i]->clone()`"],
        ["Forgetting to delete before re-assigning", "The old resource leaks",
         "`delete brain;` **then** `new Brain(...)` in `operator=`"],
        ["An abstract class instantiated", "Compile error", "`Animal` is only used "
         "through a pointer in ex02"],
        ["Defining a function in a header", "Forbidden by the 42 Norms",
         "The interface destructors are defined in a `.cpp`"],
        ["A raw pointer with no owner", "Leak or double free",
         "Every function documents **who owns** the Materia"],
        ["Using C++11 features", "Does not compile with `-std=c++98`",
         "No `nullptr`, no `override`, no `auto`, no `unique_ptr`"],
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
        (1, "No STL container and no algorithm (modules 08 / 09 only): the "
            "inventories are plain fixed size arrays."),
        (1, "Include guards on every header, and each header is **self-contained**."),
        (1, "All the implementation lives in the `.cpp` files, not in the headers."),
    ]
    right = [
        (0, "**Object oriented design**"),
        (1, "Encapsulation: `type` is `protected`, the ideas and the inventories are "
            "`private`."),
        (1, "The **Orthodox Canonical Form** on every class: default ctor, copy ctor, "
            "`operator=`, destructor."),
        (1, "No memory leak: verified with `-fsanitize=address,undefined` "
            "(**0 errors** on all four exercises)."),
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
    callout(s, ML, Inches(5.85), CW, "One design decision I want to defend",
            "The subject's `main` writes `src->learnMateria(new Ice());` — the "
            "temporary is never deleted by the caller. My `learnMateria()` therefore "
            "**takes ownership**: it keeps a `clone()` as a template and releases the "
            "original. Without that, the subject's own example would leak — and my "
            "code is leak-free under AddressSanitizer.",
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
        (1, "Each exercise has several `static` test functions covering the nominal "
            "case and the edge cases (wrong cat, full inventory, invalid slot, "
            "unknown type, copy)."),
        (0, "**2 — Strict compilation**"),
        (1, "`-Wall -Wextra -Werror` catches almost everything; `-Wshadow -pedantic` "
            "confirms the code is clean beyond the required flags."),
        (0, "**3 — Sanitizers**"),
        (1, "`-fsanitize=address,undefined` → **no leak, no UB** on any exercise."),
        (0, "**4 — Deliberate bug experiments**"),
        (1, "I compiled the *wrong* versions on purpose (no `virtual`, shallow copy, "
            "abstract instantiation) to capture the **real** compiler and sanitizer "
            "messages shown in this deck."),
    ]
    bullets(s, ML + CW * 0.52, BODY_TOP, CW * 0.48, items, size=12.5, gap=0.11,
            max_h=Inches(4.4))
    callout(s, ML, Inches(5.35), CW * 0.47, "Result",
            "ex00 ✔   ex01 ✔   ex02 ✔   ex03 ✔  — all four build without a single "
            "warning, run clean, and are leak-free under AddressSanitizer.",
            accent=TEAL, bg=TEAL_L, size=12, h=Inches(0.9))
    return s


def s_conclusion(prs):
    s = content_slide(prs, "Conclusion", "wrap-up", accent=ORANGE)
    items = [
        (0, "**What the module taught me**"),
        (1, "**Subtype polymorphism** is the heart of it: through a base pointer, "
            "the *real* type of the object decides the behaviour — one interface, "
            "many behaviours."),
        (1, "**`virtual`** is the keyword that buys it, and **`virtual ~Base()`** is "
            "the one that makes the memory safe."),
        (1, "**`= 0`** turns a class into a **contract**: the compiler then guarantees "
            "that every concrete child implements the missing behaviour."),
        (1, "**Interfaces** (`ICharacter`, `IMateriaSource`) are the purest form of "
            "that: a class made only of promises, with no state at all."),
        (1, "**Ownership** is the other half of the module: as soon as a class owns "
            "a pointer, the copy must be **deep** and every function must say who "
            "deletes what."),
        (0, "**What I am proud of**"),
        (1, "Four exercises that compile with **zero warnings** under "
            "`-Wall -Wextra -Werror -std=c++98` and are **leak-free** under "
            "`-fsanitize=address,undefined`."),
        (1, "Every subtle decision is **explained and justified** — especially the "
            "three that the subject leaves open: the ownership of `learnMateria()`, "
            "the asymmetry of `equip()` / `unequip()`, and the name of the abstract "
            "class."),
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
         "One contract,\nmany implementations —\nand every owner knows\nwhat it owns.",
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
         "Questions & discussion\nCPP Module 04 — Polymorphism, Abstract Classes & "
         "Interfaces", size=15, color=RGBColor(0x9F, 0xB3, 0xCC), line_spacing=1.4)
    text(s, Inches(1.1), Inches(5.45), Inches(7.5), Inches(0.9),
         "Animal  →  Dog, Cat      AMateria  →  Ice, Cure",
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
        prs, "Concept 1 — Subtype polymorphism", "part 2 · the knowledge you need",
        [
            (0, "**Subtype polymorphism** = a pointer or reference to a **base** "
                "class that may actually hold a **derived** object."),
            (1, "The call is resolved on the **real** type of the object, at run "
                "time."),
            (1, "The relation is *“is-a”*: a `Dog` **is-an** `Animal`."),
            (0, "**What it buys us**"),
            (1, "One piece of code can handle a family of objects: an array of "
                "`Animal *` works with dogs and cats alike."),
            (1, "New subclasses can be added later **without touching** the code that "
                "uses the base — that is the *open/closed* principle."),
            (0, "**The price**"),
            (1, "The call becomes an **indirection** through the vtable → slightly "
                "slower."),
            (1, "The base class must expose a **virtual** destructor, or the "
                "polymorphic `delete` leaks."),
        ],
        """//  one piece of code, any animal
Animal *animals[10];
for (int i = 0; i < 10; i++)
\tanimals[i] = (i % 2 == 0) ? (Animal *)new Dog()
\t                         : (Animal *)new Cat();

for (int i = 0; i < 10; i++)
{
\t//  the REAL type decides: "Woof woof!"
\t//  or "Meow meow!"
\tanimals[i]->makeSound();
\tstd::cout << animals[i]->getType() << std::endl;
}""",
        "one interface, many behaviours",
        note=("The key sentence",
              "The **static** type of the pointer says *what* can be called; the "
              "**dynamic** type says *which* implementation runs."))

    s_concept(
        prs, "Concept 2 — Virtual functions & dynamic binding",
        "part 2 · the knowledge you need",
        [
            (0, "A **`virtual`** method can be **overridden** by a derived class."),
            (1, "The base declares `virtual void makeSound() const;` and the derived "
                "class redeclares the **same signature**."),
            (0, "**Static binding** (compile time)"),
            (1, "Without `virtual`, the function is chosen from the **type of the "
                "pointer** → the base version always runs."),
            (0, "**Dynamic binding** (run time)"),
            (1, "With `virtual`, the function is chosen from the **real type of the "
                "object** → the derived version runs."),
            (0, "**Under the hood**"),
            (1, "The compiler adds a hidden **vtable** (virtual function table) and a "
                "pointer to it inside every object with virtual methods."),
            (0, "**The rule I must never forget**"),
            (1, "**The destructor must be `virtual`** as soon as the class is used "
                "polymorphically, otherwise `delete` on a base pointer leaks."),
        ],
        """class Animal
{
public:
\t//  virtual -> the derived classes
\t//  may replace this behaviour
\tvirtual void makeSound() const;

\t//  virtual -> delete through an
\t//  Animal* destroys everything
\tvirtual ~Animal();
};

class Dog : public Animal
{
public:
\t//  same signature -> an OVERRIDE
\tvirtual void makeSound() const;
};""",
        "virtual in action")

    s_concept(
        prs, "Concept 3 — Abstract classes & pure virtual functions",
        "part 2 · the knowledge you need",
        [
            (0, "A class that declares at least one **pure virtual** function is "
                "**abstract**."),
            (1, "Syntax: `virtual void f() = 0;` — the `= 0` is the marker, *not* "
                "an initialisation."),
            (1, "An abstract class **cannot be instantiated**: `Animal a;` is a "
                "compile error."),
            (1, "It **can** be inherited, and used through a pointer or a reference."),
            (0, "**A pure virtual function has no body**"),
            (1, "The definition disappears from the `.cpp` — the class only "
                "**promises** the behaviour."),
            (1, "The compiler then **checks** that every concrete child implements "
                "it."),
            (0, "**Abstract class vs. interface**"),
            (1, "An abstract class can have **data** and a **shared implementation** "
                "(`AMateria` has `type_` and a generic `use()`)."),
            (1, "An interface has **only** pure virtual methods — it is a pure "
                "contract (`ICharacter`)."),
        ],
        """//  an ABSTRACT class
class AMateria
{
public:
\tvirtual ~AMateria();

\tstd::string const & getType() const;

\t//  pure virtual: no body, the
\t//  children MUST implement it
\tvirtual AMateria *clone() const = 0;

\t//  a shared implementation
\tvirtual void use(ICharacter &target);

protected:
\tstd::string type_;
};

//  AMateria a;   <-- ERROR: cannot declare
//                   variable to be of abstract type

//  a CONCRETE class
class Ice : public AMateria
{
public:
\tvirtual AMateria *clone() const;   // implemented
\tvirtual void use(ICharacter &target);
};""",
        "pure virtual vs. virtual")

    s_concept(
        prs, "Concept 4 — Interfaces: a class of pure promises",
        "part 2 · the knowledge you need",
        [
            (0, "An **interface** is a class whose methods are **all pure virtual**."),
            (1, "It has no data and no implementation — only a contract."),
            (1, "The `I` prefix is the 42 convention: `ICharacter`, `IMateriaSource`."),
            (0, "**Why it is useful**"),
            (1, "The client code depends on the **interface**, not on the "
                "implementation: `ICharacter *me = new Character(\"me\");`."),
            (1, "A new implementation can be written without touching the client."),
            (0, "**The destructor of an interface**"),
            (1, "It is declared `virtual` but **defined** in a `.cpp` file, because "
                "the 42 Norms forbid any implementation inside a header."),
            (1, "It must be virtual, otherwise `delete` through the interface leaks."),
            (0, "**The forward declaration**"),
            (1, "`class AMateria;` — the interface only handles Materias through "
                "**pointers**, so the full definition is never needed."),
        ],
        """class AMateria;   //  forward declaration

class ICharacter
{
public:
\t//  defined in ICharacter.cpp
\tvirtual ~ICharacter();

\t//  the contract
\tvirtual std::string const & getName() const = 0;
\tvirtual void equip(AMateria *m) = 0;
\tvirtual void unequip(int idx) = 0;
\tvirtual void use(int idx, ICharacter &target) = 0;
};

//  the implementation
class Character : public ICharacter
{
public:
\tvirtual std::string const & getName() const;
\tvirtual void equip(AMateria *m);
\t//  ...
};""",
        "the contract and its implementation")

    s_concept(
        prs, "Concept 5 — Ownership, deep copy & the Rule of Three",
        "part 2 · the knowledge you need",
        [
            (0, "A class that **owns** a raw pointer must manage it in **three** "
                "places:"),
            (1, "the **destructor** — `delete brain;`"),
            (1, "the **copy constructor** — `brain(new Brain(*other.brain));`"),
            (1, "the **copy assignment operator** — `delete brain;` **then** "
                "`brain = new Brain(*other.brain);`"),
            (0, "**Why a *deep* copy?**"),
            (1, "A **shallow** copy copies the *pointer*: the two objects share the "
                "same data → it is deleted twice → **double free**."),
            (1, "A **deep** copy copies the *data*: the two objects are independent."),
            (0, "**The polymorphic version**"),
            (1, "When the owned object is polymorphic, the base class cannot know how "
                "to copy it → the child provides `clone()`."),
            (1, "That is the C++98 answer to *“give me a copy of myself”*."),
        ],
        """//  deep copy: a NEW brain is created
Dog::Dog(Dog const & other)
\t: Animal(other),
\t  brain(new Brain(*other.brain))
{
}

//  assignment: the old brain is deleted first
Dog & Dog::operator=(Dog const & other)
{
\tif (this != &other)
\t{
\t\tAnimal::operator=(other);
\t\tdelete brain;
\t\tbrain = new Brain(*other.brain);
\t}
\treturn (*this);
}

//  the polymorphic copy constructor
AMateria *Ice::clone() const
{
\treturn (new Ice());
}""",
        "the copy semantics")

    # ---- part 3 : the implementation ----
    s_ex00_subject(prs)
    s_ex00_dogcat(prs)
    s_ex00_wrong(prs)
    s_ex00_static(prs)
    s_ex00_destroy(prs)
    s_ex00_proof(prs)

    s_ex01_subject(prs)
    s_ex01_deep(prs)
    s_ex01_bug(prs)
    s_ex01_array(prs)
    s_ex01_proof(prs)

    s_ex02_subject(prs)
    s_ex02_error(prs)
    s_ex02_proof(prs)

    s_ex03_subject(prs)
    s_ex03_materia(prs)
    s_ex03_icecure(prs)
    s_ex03_interfaces(prs)
    s_ex03_character(prs)
    s_ex03_equip(prs)
    s_ex03_source(prs)
    s_ex03_ownership(prs)
    s_ex03_proof(prs)

    # ---- part 4 : summary ----
    s_design_map(prs)
    s_cheatsheet(prs)
    s_pitfalls(prs)
    s_norms(prs)
    s_testing(prs)
    s_conclusion(prs)
    s_thanks(prs)

    prs.save(OUT_NAME)
    print("saved:", OUT_NAME)
    print("slides:", len(prs.slides._sldIdLst))


if __name__ == "__main__":
    build()
