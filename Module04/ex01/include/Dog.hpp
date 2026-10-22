#ifndef DOG_HPP
#define DOG_HPP

#include "Animal.hpp"
#include "Brain.hpp"

class Dog : public Animal
{
public:
	Dog();
	Dog(Dog const & other);
	Dog & operator=(Dog const & other);
	virtual ~Dog();

	virtual void makeSound() const;

	std::string getIdea(int index) const;
	void setIdea(int index, std::string const & idea);

private:
	Brain *brain;
};

#endif
