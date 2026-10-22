#include "ClapTrap.hpp"
#include "DiamondTrap.hpp"
#include "FragTrap.hpp"
#include "ScavTrap.hpp"

#include <iostream>

static void testConstructionChaining()
{
	std::cout << "--- testConstructionChaining ---" << std::endl;
	std::cout << "(one single ClapTrap is built first, then FragTrap, ScavTrap and DiamondTrap)" << std::endl;
	std::cout << "(FragTrap and ScavTrap share that very same ClapTrap base, that is why they display its name)" << std::endl;

	{
		DiamondTrap diamond("Diamo");
		std::cout << "Diamo has " << diamond.getHitPoints() << " hit points, "
				  << diamond.getEnergyPoints() << " energy points and "
				  << diamond.getAttackDamage() << " attack damage." << std::endl;
	}
	std::cout << "(the destruction happens in the reverse order)" << std::endl;
}

static void testWhoAmI()
{
	std::cout << "--- testWhoAmI ---" << std::endl;

	DiamondTrap diamond("Diamo");
	diamond.whoAmI();
}

static void testInheritedAbilities()
{
	std::cout << "--- testInheritedAbilities ---" << std::endl;

	DiamondTrap diamond("Diamo");
	diamond.guardGate();
	diamond.highFivesGuys();
	diamond.attack("a target");
	diamond.takeDamage(20);
	diamond.beRepaired(10);
}

static void testPolymorphism()
{
	std::cout << "--- testPolymorphism ---" << std::endl;

	ClapTrap *robot = new DiamondTrap("Polymorph");
	robot->attack("a target");
	robot->takeDamage(10);
	delete robot;
}

static void testCopy()
{
	std::cout << "--- testCopy ---" << std::endl;

	DiamondTrap original("Original");
	original.takeDamage(10);

	DiamondTrap copy(original);
	copy.whoAmI();

	DiamondTrap assigned("Assigned");
	assigned = original;
	assigned.whoAmI();
}

int main()
{
	std::cout << "=== Module 03 - ex03: Now it's weird! ===" << std::endl;

	testConstructionChaining();
	testWhoAmI();
	testInheritedAbilities();
	testPolymorphism();
	testCopy();

	std::cout << "=== ex03 done ===" << std::endl;
	return (0);
}
