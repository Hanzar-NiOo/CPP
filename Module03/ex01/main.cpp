#include "ClapTrap.hpp"
#include "ScavTrap.hpp"

#include <iostream>

static void testConstructionChaining()
{
	std::cout << "--- testConstructionChaining ---" << std::endl;
	std::cout << "(a ClapTrap is built first, then the ScavTrap)" << std::endl;

	{
		ScavTrap scav("Scavvy");
		std::cout << "Scavvy has " << scav.getHitPoints() << " hit points, "
				  << scav.getEnergyPoints() << " energy points and "
				  << scav.getAttackDamage() << " attack damage." << std::endl;
	}
	std::cout << "(the ScavTrap is destroyed first, then the ClapTrap)" << std::endl;
}

static void testSpecialAbility()
{
	std::cout << "--- testSpecialAbility ---" << std::endl;

	ScavTrap scav("Gatekeeper");
	scav.guardGate();
	scav.attack("a target");
	scav.takeDamage(30);
	scav.beRepaired(20);
}

static void testPolymorphism()
{
	std::cout << "--- testPolymorphism ---" << std::endl;

	ClapTrap *robot = new ScavTrap("Polymorph");
	robot->attack("a target");
	robot->takeDamage(10);
	delete robot;
}

static void testCopy()
{
	std::cout << "--- testCopy ---" << std::endl;

	ScavTrap original("Original");
	original.takeDamage(10);

	ScavTrap copy(original);
	std::cout << "the copy has " << copy.getHitPoints() << " hit points." << std::endl;

	ScavTrap assigned("Assigned");
	assigned = original;
	std::cout << "the assigned one has " << assigned.getHitPoints() << " hit points." << std::endl;
}

int main()
{
	std::cout << "=== Module 03 - ex01: Serena, my love! ===" << std::endl;

	testConstructionChaining();
	testSpecialAbility();
	testPolymorphism();
	testCopy();

	std::cout << "=== ex01 done ===" << std::endl;
	return (0);
}
