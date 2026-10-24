#include "MateriaSource.hpp"

MateriaSource::MateriaSource()
{
    for (int i = 0; i < 4; i++)
        templates[i] = 0;
}

MateriaSource::MateriaSource(const MateriaSource& other)
{
    for (int i = 0; i < 4; i++)
    {
        if (other.templates[i])
            templates[i] = other.templates[i]->clone();
        else
            templates[i] = 0;
    }
}

MateriaSource& MateriaSource::operator=(const MateriaSource& other)
{
    if (this != &other)
    {
        for (int i = 0; i < 4; i++)
        {
            delete templates[i];
            templates[i] = 0;
        }
        for (int i = 0; i < 4; i++)
            if (other.templates[i])
                templates[i] = other.templates[i]->clone();
    }
    return *this;
}

MateriaSource::~MateriaSource()
{
    for (int i = 0; i < 4; i++)
        delete templates[i];
}

void MateriaSource::learnMateria(AMateria* m)
{
    if (!m)
        return;
    for (int i = 0; i < 4; i++)
    {
        if (!templates[i])
        {
            templates[i] = m->clone();   // store a COPY (subject)
            delete m;                    // the source consumes its argument
            return;
        }
    }
    delete m;                            // memory full: still consumed
}

AMateria* MateriaSource::createMateria(std::string const & type)
{
    for (int i = 0; i < 4; i++)
        if (templates[i] && templates[i]->getType() == type)
            return templates[i]->clone();
    return 0;
}
