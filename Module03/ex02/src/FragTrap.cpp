#include "FragTrap.hpp"

#include <iostream>

FragTrap::FragTrap()
	: ClapTrap()
{
	setHitPoints(100);
	setEnergyPoints(100);
	setAttackDamage(30);
	std::cout << "FragTrap: " << getName() << " has jumped into the battle!" << std::endl;
}

FragTrap::FragTrap(std::string const & name)
	: ClapTrap(name)
{
	setHitPoints(100);
	setEnergyPoints(100);
	setAttackDamage(30);
	std::cout << "FragTrap: " << getName() << " has jumped into the battle!" << std::endl;
}

FragTrap::FragTrap(FragTrap const & other)
	: ClapTrap(other)
{
	std::cout << "FragTrap: a copy of " << getName() << " has jumped into the battle!" << std::endl;
}

FragTrap & FragTrap::operator=(FragTrap const & other)
{
	if (this != &other)
	{
		ClapTrap::operator=(other);
		std::cout << "FragTrap: " << getName() << " has been assigned from another FragTrap." << std::endl;
	}
	return (*this);
}

FragTrap::~FragTrap()
{
	std::cout << "FragTrap: " << getName() << " has been destroyed." << std::endl;
}

void FragTrap::highFivesGuys()
{
	std::cout << "FragTrap " << getName() << " asks everybody for a high five! Let's go!" << std::endl;
}
