#include <iostream>
#include <string>
#include "AMateria.hpp"
#include "Ice.hpp"
#include "Cure.hpp"
#include "Character.hpp"
#include "MateriaSource.hpp"

static void title(const std::string& s)
{
    std::cout << "\n===== " << s << " =====" << std::endl;
}

static void check(bool cond, const std::string& what)
{
    std::cout << (cond ? "[ OK ] " : "[FAIL] ") << what << std::endl;
}

int main()
{
    title("1. Subject test");
    {
        IMateriaSource* src = new MateriaSource();
        src->learnMateria(new Ice());
        src->learnMateria(new Cure());

        ICharacter* me = new Character("me");

        AMateria* tmp;
        tmp = src->createMateria("ice");
        me->equip(tmp);
        tmp = src->createMateria("cure");
        me->equip(tmp);

        ICharacter* bob = new Character("bob");

        me->use(0, *bob);
        me->use(1, *bob);

        delete bob;
        delete me;
        delete src;
    }

    title("2. Materia basics: types, clone, assignment");
    {
        Ice ice;
        Cure cure;
        Character bob("bob");

        check(ice.getType() == "ice", "Ice type is \"ice\"");
        check(cure.getType() == "cure", "Cure type is \"cure\"");

        AMateria* c1 = ice.clone();
        AMateria* c2 = cure.clone();
        check(c1 != &ice && c1->getType() == "ice", "Ice::clone gives a NEW Ice");
        check(c2 != &cure && c2->getType() == "cure", "Cure::clone gives a NEW Cure");
        c1->use(bob);
        c2->use(bob);
        delete c1;
        delete c2;

        AMateria& ref = ice;
        ref = cure;                                  // AMateria::operator=
        check(ice.getType() == "ice", "assignment does NOT copy the type");
    }

    title("3. Inventory: full (5th equip ignored)");
    {
        Character* me = new Character("me");
        Character bob("bob");
        for (int i = 0; i < 4; i++)
            me->equip(new Ice());
        AMateria* extra = new Cure();
        me->equip(extra);                            // ignored
        bool found = false;
        for (int i = 0; i < 4; i++)
            if (me->getMateria(i) == extra)
                found = true;
        check(!found, "5th Materia was not stored");
        for (int i = 0; i < 5; i++)
            me->use(i, bob);                         // 4 lines, slot 4 does nothing
        delete extra;                                // caller still owns it
        delete me;
    }

    title("4. Invalid indexes and empty slots (nothing happens)");
    {
        Character me("me");
        Character bob("bob");
        me.use(0, bob);                              // empty slot
        me.use(-1, bob);
        me.use(4, bob);
        me.use(1000, bob);
        me.unequip(0);                               // empty slot
        me.unequip(-1);
        me.unequip(4);
        me.unequip(1000);
        me.equip(0);                                 // NULL Materia
        check(me.getMateria(0) == 0, "inventory still empty, no crash");
    }

    title("5. Equip fills the first empty slot");
    {
        Character me("me");
        me.equip(new Ice());
        me.equip(new Cure());
        me.equip(new Ice());
        AMateria* second = me.getMateria(1);
        me.unequip(1);                               // slot 1 becomes free
        AMateria* fresh = new Cure();
        me.equip(fresh);
        check(me.getMateria(1) == fresh, "new Materia went to slot 1 (first empty)");
        check(fresh != second, "and it is a different object");
    }

    title("6. unequip must NOT delete");
    {
        Character me("me");
        Character bob("bob");
        me.equip(new Ice());
        AMateria* saved = me.getMateria(0);
        me.unequip(0);
        check(me.getMateria(0) == 0, "slot 0 is empty after unequip");
        me.use(0, bob);                              // nothing printed
        saved->use(bob);                             // still alive: prints the Ice line
        me.equip(saved);                             // take it back
        check(me.getMateria(0) == saved, "re-equipped from the floor");
        me.use(0, bob);
        me.unequip(0);                               // left on the floor
        me.equip(new Cure());
        me.unequip(0);
        me.unequip(0);                               // nothing left: ignored
    }

    title("7. Equip the same Materia twice / on two slots");
    {
        Character me("me");
        AMateria* m = new Ice();
        me.equip(m);
        me.equip(m);                                 // ignored (would double delete)
        check(me.getMateria(1) == 0, "same pointer was not stored twice");
    }

    title("8. Deep copy: copy constructor");
    {
        Character* orig = new Character("orig");
        Character bob("bob");
        orig->equip(new Ice());
        orig->equip(new Cure());

        Character copy(*orig);
        check(copy.getName() == "orig", "name copied");
        check(copy.getMateria(0) != orig->getMateria(0), "slot 0: different address");
        check(copy.getMateria(1) != orig->getMateria(1), "slot 1: different address");
        check(copy.getMateria(0)->getType() == "ice", "slot 0: same type");
        check(copy.getMateria(1)->getType() == "cure", "slot 1: same type");
        check(copy.getMateria(2) == 0, "empty slots stay empty");

        delete orig;                                 // would break a shallow copy
        copy.use(0, bob);
        copy.use(1, bob);
    }

    title("9. Deep copy: assignment operator");
    {
        Character a("a");
        Character b("b");
        a.equip(new Ice());
        b.equip(new Cure());
        b.equip(new Cure());
        b.equip(new Cure());

        b = a;                                       // b's 3 Cures must be deleted
        check(b.getName() == "a", "name copied");
        check(b.getMateria(0) != a.getMateria(0), "different address");
        check(b.getMateria(0)->getType() == "ice", "same type");
        check(b.getMateria(1) == 0 && b.getMateria(2) == 0, "old Materias are gone");

        Character& ref = b;
        b = ref;                                     // self-assignment
        check(b.getMateria(0) != 0, "self-assignment keeps the inventory");
    }

    title("10. MateriaSource: learn and create");
    {
        MateriaSource src;
        check(src.createMateria("ice") == 0, "unknown before learning");
        src.learnMateria(new Ice());
        src.learnMateria(new Cure());
        src.learnMateria(new Ice());                 // duplicates are allowed
        src.learnMateria(new Cure());
        src.learnMateria(new Ice());                 // 5th: ignored, must not leak
        src.learnMateria(0);                         // NULL: ignored

        AMateria* a = src.createMateria("ice");
        AMateria* b = src.createMateria("ice");
        AMateria* c = src.createMateria("cure");
        check(a && b && c, "known types are created");
        check(a != b, "two creates give two distinct objects");
        check(a->getType() == "ice" && c->getType() == "cure", "correct types");
        check(src.createMateria("fire") == 0, "unknown type returns 0");
        check(src.createMateria("") == 0, "empty type returns 0");
        check(src.createMateria("Ice") == 0, "type is case sensitive");
        delete a;
        delete b;
        delete c;
    }

    title("11. MateriaSource deep copy");
    {
        MateriaSource s1;
        s1.learnMateria(new Ice());

        MateriaSource s2(s1);                        // copy constructor
        AMateria* m = s2.createMateria("ice");
        check(m != 0, "copy knows \"ice\"");
        delete m;

        MateriaSource s3;
        s3.learnMateria(new Cure());
        s3 = s1;                                     // assignment replaces templates
        m = s3.createMateria("cure");
        check(m == 0, "old template \"cure\" was forgotten");
        m = s3.createMateria("ice");
        check(m != 0, "new template \"ice\" was learned");
        delete m;
    }

    title("12. Full scenario: use on self, and through interfaces");
    {
        IMateriaSource* src = new MateriaSource();
        src->learnMateria(new Ice());
        src->learnMateria(new Cure());

        ICharacter* me = new Character("me");
        me->equip(src->createMateria("ice"));
        me->equip(src->createMateria("cure"));
        me->equip(src->createMateria("unknown"));    // equip(0): ignored

        me->use(0, *me);                             // target is the user itself
        me->use(1, *me);
        me->use(2, *me);                             // empty: nothing

        delete me;                                   // via ICharacter*: virtual dtor
        delete src;                                  // via IMateriaSource*: virtual dtor
    }

    return 0;
}
