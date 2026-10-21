#include "Dog.hpp"

#include <iostream>

Dog::Dog()
	: Animal()
{
	type = "Dog";
	std::cout << "Dog: a dog has been created." << std::endl;
}

Dog::Dog(Dog const & other)
	: Animal(other)
{
	std::cout << "Dog: a copy of a dog has been created." << std::endl;
}

Dog & Dog::operator=(Dog const & other)
{
	if (this != &other)
	{
		Animal::operator=(other);
		std::cout << "Dog: a dog has been assigned from another dog." << std::endl;
	}
	return (*this);
}

Dog::~Dog()
{
	std::cout << "Dog: the dog has been destroyed." << std::endl;
}

void Dog::makeSound() const
{
	std::cout << "Woof woof!" << std::endl;
}
