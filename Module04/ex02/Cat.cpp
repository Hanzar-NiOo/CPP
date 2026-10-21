#include "Cat.hpp"

#include <iostream>

Cat::Cat()
	: Animal(),
	  brain(new Brain())
{
	type = "Cat";
	std::cout << "Cat: a cat has been created." << std::endl;
}

Cat::Cat(Cat const & other)
	: Animal(other),
	  brain(new Brain(*other.brain))
{
	std::cout << "Cat: a copy of a cat has been created." << std::endl;
}

Cat & Cat::operator=(Cat const & other)
{
	if (this != &other)
	{
		Animal::operator=(other);
		delete brain;
		brain = new Brain(*other.brain);
		std::cout << "Cat: a cat has been assigned from another cat." << std::endl;
	}
	return (*this);
}

Cat::~Cat()
{
	std::cout << "Cat: the cat has been destroyed." << std::endl;
	delete brain;
}

void Cat::makeSound() const
{
	std::cout << "Meow meow!" << std::endl;
}

std::string Cat::getIdea(int index) const
{
	return (brain->getIdea(index));
}

void Cat::setIdea(int index, std::string const & idea)
{
	brain->setIdea(index, idea);
}
