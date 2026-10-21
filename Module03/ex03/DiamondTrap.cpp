#include "DiamondTrap.hpp"

#include <iostream>

DiamondTrap::DiamondTrap()
	: ClapTrap(""),
	  FragTrap(),
	  ScavTrap(),
	  name_("")
{
	setHitPoints(100);
	setEnergyPoints(50);
	setAttackDamage(30);
	std::cout << "DiamondTrap: " << name_ << " has been created!" << std::endl;
}

DiamondTrap::DiamondTrap(std::string const & name)
	: ClapTrap(name + "_clap_name"),
	  FragTrap(name),
	  ScavTrap(name),
	  name_(name)
{
	setHitPoints(100);
	setEnergyPoints(50);
	setAttackDamage(30);
	std::cout << "DiamondTrap: " << name_ << " has been created!" << std::endl;
}

DiamondTrap::DiamondTrap(DiamondTrap const & other)
	: ClapTrap(other),
	  FragTrap(other),
	  ScavTrap(other),
	  name_(other.name_)
{
	std::cout << "DiamondTrap: a copy of " << name_ << " has been created!" << std::endl;
}

DiamondTrap & DiamondTrap::operator=(DiamondTrap const & other)
{
	if (this != &other)
	{
		ClapTrap::operator=(other);
		name_ = other.name_;
		std::cout << "DiamondTrap: " << name_ << " has been assigned from another DiamondTrap." << std::endl;
	}
	return (*this);
}

DiamondTrap::~DiamondTrap()
{
	std::cout << "DiamondTrap: " << name_ << " has been destroyed!" << std::endl;
}

void DiamondTrap::whoAmI()
{
	std::cout << "My name is " << name_ << " and my ClapTrap name is " << getName() << std::endl;
}
