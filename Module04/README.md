# C++ — Module 04: Subtype Polymorphism, Abstract Classes and Interfaces

Implementation of the exercises of the 42 C++ Module 04.

## Structure

```
Module04/
├── ex00/   Polymorphism            Animal, Dog, Cat, WrongAnimal, WrongCat
├── ex01/   I don't want to set the world on fire
│                                  ex00 + Brain
├── ex02/   Abstract class         ex01 with an abstract Animal
└── ex03/   Interface & recap      AMateria, Ice, Cure, ICharacter, Character,
│                                  IMateriaSource, MateriaSource
```

Each directory is self contained (ex01 contains the files of ex00, ex02 the
files of ex01) and holds its own `Makefile` and `main.cpp` with its own tests.

## Build and run

```bash
cd ex00        # or ex01, ex02, ex03
make            # compiles with -Wall -Wextra -Werror -std=c++98
./a.out
make clean      # removes the objects and the binary
make re         # clean + build
```

## Exercises

### ex00 — Polymorphism
`Animal` has one protected attribute (`type`), a virtual destructor and a
virtual `makeSound()`. `Dog` and `Cat` inherit from it, set their own type and
override `makeSound()`, so calling it through an `Animal *` prints the sound of
the real animal. `WrongCat` inherits from `WrongAnimal` **without** overriding
`makeSound()`: it therefore prints the sound of `WrongAnimal`.

### ex01 — Brain
`Brain` contains an array of 100 `std::string`. `Dog` and `Cat` own a private
`Brain *` created with `new` in their constructor and released in their
destructor. Their copy constructor and copy assignment operator build a
**deep** copy of the brain. The `main` creates an array of `Animal *` (half
`Dog`, half `Cat`), fills it and deletes every animal through its `Animal *`
pointer, so the right destructors are called in the right order.

### ex02 — Abstract class
`Animal::makeSound()` is now pure virtual: the class cannot be instantiated
anymore, everything else works as before. (`Animal` could be renamed `AAnimal`,
as suggested by the subject, but the name was kept.)

### ex03 — Interface & recap
* `AMateria` is the abstract class of the Materias, with `getType()`,
  `clone()` (pure virtual) and `use(ICharacter &)`.
* `Ice` (`"ice"`) and `Cure` (`"cure"`) are the concrete Materias, they
  override `clone()` and `use()`:
  `* shoots an ice bolt at <name> *` and `* heals <name>'s wounds *`.
* `ICharacter` and `IMateriaSource` are the two interfaces (pure abstract
  classes); their destructors are defined in a `.cpp` file, as no implementation
  is allowed inside a header.
* `Character` owns an inventory of 4 slots. `equip()` fills the first empty
  slot, `unequip()` empties a slot **without** deleting the Materia and
  `use()` calls `AMateria::use()` with the target. A copy of a `Character` is
  deep: the old Materias are deleted before the new ones (clones) are added.
* `MateriaSource` learns at most 4 Materias and creates new ones from the
  learned templates; an unknown type returns `0`.

## Design notes

* `AMateria::use()` has a generic implementation (as in the subject) that the
  concrete Materias override.
* `learnMateria()` **takes ownership** of the given Materia: a copy of it is
  kept as a template and the original one is released. This is what allows the
  `main` of the subject (`src->learnMateria(new Ice());`) to run without
  leaking anything.
* `Character::equip()` gives the ownership of the Materia to the character
  (the character deletes it in its destructor). When the inventory is full the
  Materia is left untouched and stays the property of the caller.
* `getMateria(int)` is an additional accessor used by the tests to check that
  the copies are deep.

## Rules followed

* Compiled with `c++ -Wall -Wextra -Werror -std=c++98` (also verified with
  `-Wshadow -pedantic`).
* No `using namespace`, no `friend`, no `printf`/`malloc`/`free`.
* No STL container and no algorithm (modules 08 and 09 only): the inventories
  are plain fixed size arrays.
* Include guards on every header, each header is self contained and includes
  its own dependencies.
* No memory leak: all the exercises were checked with
  `-fsanitize=address,undefined`.
