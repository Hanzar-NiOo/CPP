#ifndef ANIMAL_HPP
#define ANIMAL_HPP

#include <string>

class Animal
{
public:
	Animal();
	Animal(Animal const & other);
	Animal & operator=(Animal const & other);
	virtual ~Animal();

	virtual void makeSound() const = 0;
	std::string const & getType() const;

protected:
	std::string type;
};

#endif
