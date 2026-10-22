#include "AMateria.hpp"
#include "ICharacter.hpp"

#include <iostream>

AMateria::AMateria(std::string const & type)
	: type_(type)
{
	std::cout << "AMateria: a new " << type_ << " materia has been created." << std::endl;
}

AMateria::~AMateria()
{
	std::cout << "AMateria: the " << type_ << " materia has been destroyed." << std::endl;
}

std::string const & AMateria::getType() const
{
	return (type_);
}

void AMateria::use(ICharacter &target)
{
	std::cout << "* uses the " << type_ << " materia on " << target.getName() << " *" << std::endl;
}
