# C++ — Module 03: Inheritance

Implementation of the exercises of the 42 C++ Module 03 (Inheritance).

## Structure

```
Module03/
├── ex00/   Aaaaand... OPEN!      ClapTrap
├── ex01/   Serena, my love!      ClapTrap + ScavTrap
├── ex02/   Repetitive work        ClapTrap + ScavTrap + FragTrap
└── ex03/   Now it's weird!        ClapTrap + ScavTrap + FragTrap + DiamondTrap
```

Each directory is self contained (ex01 contains the files of ex00, ex02 the files
of ex01, ...) and holds its own `Makefile` and `main.cpp` with its own tests.

## Build and run

```bash
cd ex00        # or ex01, ex02, ex03
make            # compiles with -Wall -Wextra -Werror -std=c++98
./a.out
make clean      # removes the objects and the binary
make re         # clean + build
```

## Exercises

### ex00 — ClapTrap
`ClapTrap` holds a name, 10 hit points, 10 energy points and 0 attack damage.
`attack()`, `takeDamage()` and `beRepaired()` are implemented: attacking and
repairing each cost one energy point, and nothing can be done without hit
points or energy points. Constructors and destructor print a message.

### ex01 — ScavTrap
`ScavTrap` inherits from `ClapTrap`, calls the base constructor/destructor and
prints its own messages. It is initialised with 100 hit points, 50 energy
points and 20 attack damage, overrides `attack()` and adds `guardGate()`.

### ex02 — FragTrap
`FragTrap` also inherits from `ClapTrap` (100 hit points, 100 energy points,
30 attack damage) and adds `highFivesGuys()`. Its construction and destruction
messages differ from the ones of `ScavTrap`.

### ex03 — DiamondTrap
`DiamondTrap` inherits from **both** `FragTrap` and `ScavTrap`:

* `ClapTrap` is inherited **virtually**, so the single `ClapTrap` instance of a
  `DiamondTrap` is created once and only once, by the most derived class.
* `ClapTrap::name_` holds the constructor parameter followed by `_clap_name`,
  while `DiamondTrap` owns a private `name_` attribute with the very same name
  (it shadows the private attribute of the base class, which is why the code
  compiles without any `-Wshadow` warning).
* Hit points and attack damage come from `FragTrap` (100 / 30), energy points
  come from `ScavTrap` (50) and `attack()` is the one of `ScavTrap`.
* `whoAmI()` displays both names.

Construction order: `ClapTrap` → `FragTrap` → `ScavTrap` → `DiamondTrap`.
Destruction order: the exact reverse.

## Design notes

* The `ClapTrap` attributes stay private, as required by the subject. The
  derived classes initialise them through the protected setters
  (`setHitPoints()`, `setEnergyPoints()`, `setAttackDamage()`), which is the
  "update ClapTrap accordingly" asked by the subject.
* `attack()` is virtual from the very beginning so that the derived classes can
  override it. `FragTrap` deliberately does **not** override it, otherwise
  `DiamondTrap::attack()` would be ambiguous.
* `ScavTrap` and `FragTrap` inherit `ClapTrap` virtually from ex01 on: the
  behaviour is unchanged in ex01 and ex02 and it makes the diamond of ex03
  possible.
* Every class follows the Orthodox Canonical Form (default constructor, copy
  constructor, copy assignment operator and destructor) and all the
  implementations live in the `.cpp` files.

## Rules followed

* Compiled with `c++ -Wall -Wextra -Werror -std=c++98` (also verified with
  `-Wshadow -pedantic`).
* No `using namespace`, no `friend`, no `printf`/`malloc`/`free`.
* No STL container and no algorithm (modules 08 and 09 only).
* Include guards on every header, each header is self contained and includes
  its own dependencies.
* No memory leak: all the exercises were checked with
  `-fsanitize=address,undefined`.
