#include "ScavTrap.hpp"

#include <iostream>

ScavTrap::ScavTrap()
	: ClapTrap()
{
	setHitPoints(100);
	setEnergyPoints(50);
	setAttackDamage(20);
	std::cout << "ScavTrap: " << getName() << " is ready to fight!" << std::endl;
}

ScavTrap::ScavTrap(std::string const & name)
	: ClapTrap(name)
{
	setHitPoints(100);
	setEnergyPoints(50);
	setAttackDamage(20);
	std::cout << "ScavTrap: " << getName() << " is ready to fight!" << std::endl;
}

ScavTrap::ScavTrap(ScavTrap const & other)
	: ClapTrap(other)
{
	std::cout << "ScavTrap: a copy of " << getName() << " is ready to fight!" << std::endl;
}

ScavTrap & ScavTrap::operator=(ScavTrap const & other)
{
	if (this != &other)
	{
		ClapTrap::operator=(other);
		std::cout << "ScavTrap: " << getName() << " has been assigned from another ScavTrap." << std::endl;
	}
	return (*this);
}

ScavTrap::~ScavTrap()
{
	std::cout << "ScavTrap: " << getName() << " has been destroyed." << std::endl;
}

void ScavTrap::attack(std::string const & target)
{
	if (!hasHitPoints())
	{
		std::cout << "ScavTrap " << getName() << " is out of hit points and cannot attack." << std::endl;
		return;
	}
	if (!hasEnergy())
	{
		std::cout << "ScavTrap " << getName() << " is out of energy and cannot attack." << std::endl;
		return;
	}
	consumeEnergy();
	std::cout << "ScavTrap " << getName() << " attacks " << target
			  << ", causing " << getAttackDamage() << " points of damage!" << std::endl;
}

void ScavTrap::guardGate()
{
	std::cout << "ScavTrap " << getName() << " is now in Gate keeper mode!" << std::endl;
}
