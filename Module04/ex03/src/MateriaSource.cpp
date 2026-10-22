#include "MateriaSource.hpp"
#include "AMateria.hpp"

#include <iostream>

MateriaSource::MateriaSource()
{
	for (int i = 0; i < 4; i++)
		learned_[i] = 0;
	std::cout << "MateriaSource: a new materia source has been created." << std::endl;
}

MateriaSource::MateriaSource(MateriaSource const & other)
{
	for (int i = 0; i < 4; i++)
	{
		if (other.learned_[i])
			learned_[i] = other.learned_[i]->clone();
		else
			learned_[i] = 0;
	}
	std::cout << "MateriaSource: a copy of a materia source has been created." << std::endl;
}

MateriaSource & MateriaSource::operator=(MateriaSource const & other)
{
	if (this != &other)
	{
		for (int i = 0; i < 4; i++)
		{
			delete learned_[i];
			learned_[i] = 0;
		}
		for (int i = 0; i < 4; i++)
		{
			if (other.learned_[i])
				learned_[i] = other.learned_[i]->clone();
		}
		std::cout << "MateriaSource: a materia source has been assigned from another one." << std::endl;
	}
	return (*this);
}

MateriaSource::~MateriaSource()
{
	for (int i = 0; i < 4; i++)
		delete learned_[i];
	std::cout << "MateriaSource: the materia source has been destroyed." << std::endl;
}

void MateriaSource::learnMateria(AMateria *m)
{
	if (!m)
		return;
	for (int i = 0; i < 4; i++)
	{
		if (!learned_[i])
		{
			learned_[i] = m->clone();
			delete m;
			std::cout << "MateriaSource: a new " << learned_[i]->getType()
					  << " materia has been learned." << std::endl;
			return;
		}
	}
	delete m;
	std::cout << "MateriaSource: the source cannot learn more than 4 materias." << std::endl;
}

AMateria *MateriaSource::createMateria(std::string const & type)
{
	for (int i = 0; i < 4; i++)
	{
		if (learned_[i] && learned_[i]->getType() == type)
		{
			AMateria *materia = learned_[i]->clone();
			std::cout << "MateriaSource: a new " << type << " materia has been created." << std::endl;
			return (materia);
		}
	}
	std::cout << "MateriaSource: the type " << type << " is unknown." << std::endl;
	return (0);
}
