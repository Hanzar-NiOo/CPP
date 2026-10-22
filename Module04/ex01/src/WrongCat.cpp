#include "WrongCat.hpp"

#include <iostream>

WrongCat::WrongCat()
	: WrongAnimal()
{
	type = "WrongCat";
	std::cout << "WrongCat: a wrong cat has been created." << std::endl;
}

WrongCat::WrongCat(WrongCat const & other)
	: WrongAnimal(other)
{
	std::cout << "WrongCat: a copy of a wrong cat has been created." << std::endl;
}

WrongCat & WrongCat::operator=(WrongCat const & other)
{
	if (this != &other)
	{
		WrongAnimal::operator=(other);
		std::cout << "WrongCat: a wrong cat has been assigned from another wrong cat." << std::endl;
	}
	return (*this);
}

WrongCat::~WrongCat()
{
	std::cout << "WrongCat: the wrong cat has been destroyed." << std::endl;
}
