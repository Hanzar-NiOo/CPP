#include "AMateria.hpp"
#include "Character.hpp"
#include "Cure.hpp"
#include "ICharacter.hpp"
#include "IMateriaSource.hpp"
#include "Ice.hpp"
#include "MateriaSource.hpp"

#include <iostream>

static void testSubjectExample()
{
	std::cout << "--- testSubjectExample ---" << std::endl;

	IMateriaSource *src = new MateriaSource();
	src->learnMateria(new Ice());
	src->learnMateria(new Cure());
	ICharacter *me = new Character("me");
	AMateria *tmp;
	tmp = src->createMateria("ice");
	me->equip(tmp);
	tmp = src->createMateria("cure");
	me->equip(tmp);
	ICharacter *bob = new Character("bob");
	me->use(0, *bob);
	me->use(1, *bob);
	delete bob;
	delete me;
	delete src;
}

static void testUnequip()
{
	std::cout << "--- testUnequip ---" << std::endl;
	std::cout << "(unequip does not delete the materia, it is left on the floor)" << std::endl;

	Character me("me");
	AMateria *ice = new Ice();
	me.equip(ice);
	me.use(0, me);
	me.unequip(0);
	me.use(0, me); // nothing happens, the slot is empty
	delete ice;    // the materia is handled here
}

static void testFullInventory()
{
	std::cout << "--- testFullInventory ---" << std::endl;
	std::cout << "(a character owns 4 slots, the 5th materia is refused)" << std::endl;

	Character me("me");
	me.equip(new Ice());
	me.equip(new Cure());
	me.equip(new Ice());
	me.equip(new Cure());
	AMateria *extra = new Ice();
	me.equip(extra);
	delete extra; // the character did not take it, it is still ours
}

static void testInvalidUse()
{
	std::cout << "--- testInvalidUse ---" << std::endl;
	std::cout << "(using an empty slot or a slot that does not exist does nothing)" << std::endl;

	Character me("me");
	Character bob("bob");
	me.use(0, bob);
	me.use(42, bob);
	me.use(-1, bob);
	me.unequip(0);
	me.unequip(42);
}

static void testUnknownMateria()
{
	std::cout << "--- testUnknownMateria ---" << std::endl;
	std::cout << "(an unknown type returns 0)" << std::endl;

	MateriaSource src;
	src.learnMateria(new Ice());
	AMateria *materia = src.createMateria("unknown");
	if (materia == 0)
		std::cout << "the unknown materia could not be created." << std::endl;
}

static void testDeepCopy()
{
	std::cout << "--- testDeepCopy ---" << std::endl;
	std::cout << "(a copy of a character must not be shallow)" << std::endl;

	Character original("original");
	original.equip(new Ice());

	Character copy(original);
	if (copy.getMateria(0) != original.getMateria(0))
		std::cout << "the copy owns its own materia: deep copy." << std::endl;

	Character assigned("assigned");
	assigned.equip(new Cure());
	assigned = original; // the cure is deleted before the new ones are added
	if (assigned.getMateria(0) != original.getMateria(0))
		std::cout << "the assigned character owns its own materia: deep copy." << std::endl;
}

static void testMateriaSourceCopy()
{
	std::cout << "--- testMateriaSourceCopy ---" << std::endl;

	MateriaSource source;
	source.learnMateria(new Ice());
	source.learnMateria(new Cure());

	MateriaSource copy(source);
	AMateria *materia = copy.createMateria("ice");
	if (materia)
	{
		std::cout << "the copied source created a " << materia->getType() << " materia." << std::endl;
		delete materia;
	}
}

int main()
{
	std::cout << "=== Module 04 - ex03: Interface & recap ===" << std::endl;

	testSubjectExample();
	testUnequip();
	testFullInventory();
	testInvalidUse();
	testUnknownMateria();
	testDeepCopy();
	testMateriaSourceCopy();

	std::cout << "=== ex03 done ===" << std::endl;
	return (0);
}
