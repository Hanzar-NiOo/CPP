#include "ClapTrap.hpp"

#include <iostream>

ClapTrap::ClapTrap()
	: name_(""),
	  hitPoints_(10),
	  energyPoints_(10),
	  attackDamage_(0)
{
	std::cout << "ClapTrap: " << name_ << " has been created." << std::endl;
}

ClapTrap::ClapTrap(std::string const & name)
	: name_(name),
	  hitPoints_(10),
	  energyPoints_(10),
	  attackDamage_(0)
{
	std::cout << "ClapTrap: " << name_ << " has been created." << std::endl;
}

ClapTrap::ClapTrap(ClapTrap const & other)
	: name_(other.name_),
	  hitPoints_(other.hitPoints_),
	  energyPoints_(other.energyPoints_),
	  attackDamage_(other.attackDamage_)
{
	std::cout << "ClapTrap: a copy of " << name_ << " has been created." << std::endl;
}

ClapTrap & ClapTrap::operator=(ClapTrap const & other)
{
	if (this != &other)
	{
		name_ = other.name_;
		hitPoints_ = other.hitPoints_;
		energyPoints_ = other.energyPoints_;
		attackDamage_ = other.attackDamage_;
		std::cout << "ClapTrap: " << name_ << " has been assigned from another ClapTrap." << std::endl;
	}
	return (*this);
}

ClapTrap::~ClapTrap()
{
	std::cout << "ClapTrap: " << name_ << " has been destroyed." << std::endl;
}

void ClapTrap::attack(std::string const & target)
{
	if (!hasHitPoints())
	{
		std::cout << "ClapTrap " << name_ << " is out of hit points and cannot attack." << std::endl;
		return;
	}
	if (!hasEnergy())
	{
		std::cout << "ClapTrap " << name_ << " is out of energy and cannot attack." << std::endl;
		return;
	}
	consumeEnergy();
	std::cout << "ClapTrap " << name_ << " attacks " << target
			  << ", causing " << attackDamage_ << " points of damage!" << std::endl;
}

void ClapTrap::takeDamage(unsigned int amount)
{
	if (!hasHitPoints())
	{
		std::cout << "ClapTrap " << name_ << " is already out of hit points and cannot take damage." << std::endl;
		return;
	}
	if (amount > hitPoints_)
		hitPoints_ = 0;
	else
		hitPoints_ -= amount;
	std::cout << "ClapTrap " << name_ << " takes " << amount
			  << " points of damage, it has " << hitPoints_ << " hit points left!" << std::endl;
}

void ClapTrap::beRepaired(unsigned int amount)
{
	if (!hasEnergy())
	{
		std::cout << "ClapTrap " << name_ << " is out of energy and cannot be repaired." << std::endl;
		return;
	}
	consumeEnergy();
	hitPoints_ += amount;
	std::cout << "ClapTrap " << name_ << " is repaired by " << amount
			  << " points, it has " << hitPoints_ << " hit points!" << std::endl;
}

std::string const & ClapTrap::getName() const
{
	return (name_);
}

unsigned int ClapTrap::getHitPoints() const
{
	return (hitPoints_);
}

unsigned int ClapTrap::getEnergyPoints() const
{
	return (energyPoints_);
}

unsigned int ClapTrap::getAttackDamage() const
{
	return (attackDamage_);
}

void ClapTrap::setName(std::string const & name)
{
	name_ = name;
}

void ClapTrap::setHitPoints(unsigned int hitPoints)
{
	hitPoints_ = hitPoints;
}

void ClapTrap::setEnergyPoints(unsigned int energyPoints)
{
	energyPoints_ = energyPoints;
}

void ClapTrap::setAttackDamage(unsigned int attackDamage)
{
	attackDamage_ = attackDamage;
}

bool ClapTrap::hasHitPoints() const
{
	return (hitPoints_ > 0);
}

bool ClapTrap::hasEnergy() const
{
	return (energyPoints_ > 0);
}

void ClapTrap::consumeEnergy()
{
	if (energyPoints_ > 0)
		--energyPoints_;
}
