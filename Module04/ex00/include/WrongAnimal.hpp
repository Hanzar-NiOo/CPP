#ifndef WRONGANIMAL_HPP
#define WRONGANIMAL_HPP

#include <string>

class WrongAnimal
{
public:
	WrongAnimal();
	WrongAnimal(WrongAnimal const & other);
	WrongAnimal & operator=(WrongAnimal const & other);
	virtual ~WrongAnimal();

	virtual void makeSound() const;
	std::string const & getType() const;

protected:
	std::string type;
};

#endif
