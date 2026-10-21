#include "WrongAnimal.hpp"

#include <iostream>

WrongAnimal::WrongAnimal()
	: type("WrongAnimal")
{
	std::cout << "WrongAnimal: a wrong animal has been created." << std::endl;
}

WrongAnimal::WrongAnimal(WrongAnimal const & other)
	: type(other.type)
{
	std::cout << "WrongAnimal: a copy of a wrong animal has been created." << std::endl;
}

WrongAnimal & WrongAnimal::operator=(WrongAnimal const & other)
{
	if (this != &other)
	{
		type = other.type;
		std::cout << "WrongAnimal: a wrong animal has been assigned from another wrong animal." << std::endl;
	}
	return (*this);
}

WrongAnimal::~WrongAnimal()
{
	std::cout << "WrongAnimal: the wrong animal " << type << " has been destroyed." << std::endl;
}

void WrongAnimal::makeSound() const
{
	std::cout << "Wrong animal sound: grrrooo..." << std::endl;
}

std::string const & WrongAnimal::getType() const
{
	return (type);
}
