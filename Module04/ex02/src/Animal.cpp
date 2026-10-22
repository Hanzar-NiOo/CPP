#include "Animal.hpp"

#include <iostream>

Animal::Animal()
	: type("Animal")
{
	std::cout << "Animal: an animal has been created." << std::endl;
}

Animal::Animal(Animal const & other)
	: type(other.type)
{
	std::cout << "Animal: a copy of an animal has been created." << std::endl;
}

Animal & Animal::operator=(Animal const & other)
{
	if (this != &other)
	{
		type = other.type;
		std::cout << "Animal: an animal has been assigned from another animal." << std::endl;
	}
	return (*this);
}

Animal::~Animal()
{
	std::cout << "Animal: the animal " << type << " has been destroyed." << std::endl;
}

std::string const & Animal::getType() const
{
	return (type);
}
