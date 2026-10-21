#include "ClapTrap.hpp"

#include <iostream>

static void testCombat()
{
	std::cout << "--- testCombat: a ClapTrap fights ---" << std::endl;

	ClapTrap robot("Clappy");
	robot.attack("target-1");
	robot.attack("target-2");
	robot.takeDamage(4);
	robot.beRepaired(2);

	std::cout << "Clappy now has " << robot.getHitPoints() << " hit points, "
			  << robot.getEnergyPoints() << " energy points and "
			  << robot.getAttackDamage() << " attack damage." << std::endl;
}

static void testNoEnergy()
{
	std::cout << "--- testNoEnergy: energy points are consumed ---" << std::endl;

	ClapTrap robot("Energyless");
	for (int i = 0; i < 12; i++)
		robot.attack("a wall");

	std::cout << "Energyless has " << robot.getEnergyPoints() << " energy points left." << std::endl;
}

static void testDestruction()
{
	std::cout << "--- testDestruction: no hit points left ---" << std::endl;

	ClapTrap robot("Doomed");
	robot.takeDamage(50);
	robot.attack("target-3");
	robot.beRepaired(10);
	robot.takeDamage(5);

	std::cout << "Doomed has " << robot.getHitPoints() << " hit points left." << std::endl;
}

static void testCopy()
{
	std::cout << "--- testCopy: copy constructor and assignment ---" << std::endl;

	ClapTrap original("Original");
	original.takeDamage(3);

	ClapTrap copy(original);
	std::cout << "copy is named " << copy.getName() << " and has "
			  << copy.getHitPoints() << " hit points." << std::endl;

	ClapTrap assigned("Assigned");
	assigned = original;
	std::cout << "assigned is named " << assigned.getName() << " and has "
			  << assigned.getHitPoints() << " hit points." << std::endl;
}

int main()
{
	std::cout << "=== Module 03 - ex00: Aaaaand... OPEN! ===" << std::endl;

	testCombat();
	testNoEnergy();
	testDestruction();
	testCopy();

	std::cout << "=== ex00 done ===" << std::endl;
	return (0);
}
