#include "Cat.hpp"

#include <iostream>

Cat::Cat()
	: Animal()
{
	type = "Cat";
	std::cout << "Cat: a cat has been created." << std::endl;
}

Cat::Cat(Cat const & other)
	: Animal(other)
{
	std::cout << "Cat: a copy of a cat has been created." << std::endl;
}

Cat & Cat::operator=(Cat const & other)
{
	if (this != &other)
	{
		Animal::operator=(other);
		std::cout << "Cat: a cat has been assigned from another cat." << std::endl;
	}
	return (*this);
}

Cat::~Cat()
{
	std::cout << "Cat: the cat has been destroyed." << std::endl;
}

void Cat::makeSound() const
{
	std::cout << "Meow meow!" << std::endl;
}
