#include "Dog.hpp"

#include <iostream>

Dog::Dog()
	: Animal(),
	  brain(new Brain())
{
	type = "Dog";
	std::cout << "Dog: a dog has been created." << std::endl;
}

Dog::Dog(Dog const & other)
	: Animal(other),
	  brain(new Brain(*other.brain))
{
	std::cout << "Dog: a copy of a dog has been created." << std::endl;
}

Dog & Dog::operator=(Dog const & other)
{
	if (this != &other)
	{
		Animal::operator=(other);
		delete brain;
		brain = new Brain(*other.brain);
		std::cout << "Dog: a dog has been assigned from another dog." << std::endl;
	}
	return (*this);
}

Dog::~Dog()
{
	std::cout << "Dog: the dog has been destroyed." << std::endl;
	delete brain;
}

void Dog::makeSound() const
{
	std::cout << "Woof woof!" << std::endl;
}

std::string Dog::getIdea(int index) const
{
	return (brain->getIdea(index));
}

void Dog::setIdea(int index, std::string const & idea)
{
	brain->setIdea(index, idea);
}
