#include "Character.hpp"
#include "AMateria.hpp"

#include <iostream>

Character::Character(std::string const & name)
	: name_(name)
{
	for (int i = 0; i < 4; i++)
		inventory_[i] = 0;
	std::cout << "Character: " << name_ << " has been created." << std::endl;
}

Character::Character(Character const & other)
	: name_(other.name_)
{
	for (int i = 0; i < 4; i++)
	{
		if (other.inventory_[i])
			inventory_[i] = other.inventory_[i]->clone();
		else
			inventory_[i] = 0;
	}
	std::cout << "Character: a copy of " << name_ << " has been created." << std::endl;
}

Character & Character::operator=(Character const & other)
{
	if (this != &other)
	{
		// the old materias are deleted before the new ones are added
		for (int i = 0; i < 4; i++)
		{
			delete inventory_[i];
			inventory_[i] = 0;
		}
		name_ = other.name_;
		for (int i = 0; i < 4; i++)
		{
			if (other.inventory_[i])
				inventory_[i] = other.inventory_[i]->clone();
		}
		std::cout << "Character: " << name_ << " has been assigned from another character." << std::endl;
	}
	return (*this);
}

Character::~Character()
{
	for (int i = 0; i < 4; i++)
		delete inventory_[i];
	std::cout << "Character: " << name_ << " has been destroyed." << std::endl;
}

std::string const & Character::getName() const
{
	return (name_);
}

void Character::equip(AMateria *m)
{
	if (!m)
		return;
	for (int i = 0; i < 4; i++)
	{
		if (!inventory_[i])
		{
			inventory_[i] = m;
			std::cout << "Character: " << name_ << " equips a " << m->getType()
					  << " materia in slot " << i << "." << std::endl;
			return;
		}
	}
	std::cout << "Character: " << name_ << " cannot equip that materia, the inventory is full." << std::endl;
}

void Character::unequip(int idx)
{
	if (idx < 0 || idx > 3 || !inventory_[idx])
		return;
	std::cout << "Character: " << name_ << " unequips the " << inventory_[idx]->getType()
			  << " materia from slot " << idx << "." << std::endl;
	// the materia is not deleted, it is left on the floor
	inventory_[idx] = 0;
}

void Character::use(int idx, ICharacter &target)
{
	if (idx < 0 || idx > 3 || !inventory_[idx])
		return;
	inventory_[idx]->use(target);
}

AMateria *Character::getMateria(int idx) const
{
	if (idx < 0 || idx > 3)
		return (0);
	return (inventory_[idx]);
}
