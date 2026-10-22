#ifndef MATERIASOURCE_HPP
#define MATERIASOURCE_HPP

#include "IMateriaSource.hpp"

class MateriaSource : public IMateriaSource
{
public:
	MateriaSource();
	MateriaSource(MateriaSource const & other);
	MateriaSource & operator=(MateriaSource const & other);
	virtual ~MateriaSource();

	// The MateriaSource takes ownership of the given materia: a copy of it is
	// kept as a template and the original one is released, so that no memory
	// is leaked.
	virtual void learnMateria(AMateria *m);
	virtual AMateria *createMateria(std::string const & type);

private:
	AMateria *learned_[4];
};

#endif
