#include "ClapTrap.hpp"
#include "FragTrap.hpp"
#include "ScavTrap.hpp"

#include <iostream>

static void testConstructionChaining()
{
	std::cout << "--- testConstructionChaining ---" << std::endl;
	std::cout << "(a ClapTrap is built first, then the FragTrap)" << std::endl;

	{
		FragTrap frag("Fraggy");
		std::cout << "Fraggy has " << frag.getHitPoints() << " hit points, "
				  << frag.getEnergyPoints() << " energy points and "
				  << frag.getAttackDamage() << " attack damage." << std::endl;
	}
	std::cout << "(the FragTrap is destroyed first, then the ClapTrap)" << std::endl;
}

static void testSpecialAbility()
{
	std::cout << "--- testSpecialAbility ---" << std::endl;

	FragTrap frag("Cheerful");
	frag.highFivesGuys();
	frag.attack("a target");
	frag.takeDamage(30);
	frag.beRepaired(20);
}

static void testPolymorphism()
{
	std::cout << "--- testPolymorphism ---" << std::endl;

	ClapTrap *robot = new FragTrap("Polymorph");
	robot->attack("a target");
	robot->takeDamage(10);
	delete robot;
}

static void testCopy()
{
	std::cout << "--- testCopy ---" << std::endl;

	FragTrap original("Original");
	original.takeDamage(10);

	FragTrap copy(original);
	std::cout << "the copy has " << copy.getHitPoints() << " hit points." << std::endl;

	FragTrap assigned("Assigned");
	assigned = original;
	std::cout << "the assigned one has " << assigned.getHitPoints() << " hit points." << std::endl;
}

int main()
{
	std::cout << "=== Module 03 - ex02: Repetitive work ===" << std::endl;

	testConstructionChaining();
	testSpecialAbility();
	testPolymorphism();
	testCopy();

	std::cout << "=== ex02 done ===" << std::endl;
	return (0);
}
