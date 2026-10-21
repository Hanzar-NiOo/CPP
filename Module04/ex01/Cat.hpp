#ifndef CAT_HPP
#define CAT_HPP

#include "Animal.hpp"
#include "Brain.hpp"

class Cat : public Animal
{
public:
	Cat();
	Cat(Cat const & other);
	Cat & operator=(Cat const & other);
	virtual ~Cat();

	virtual void makeSound() const;

	std::string getIdea(int index) const;
	void setIdea(int index, std::string const & idea);

private:
	Brain *brain;
};

#endif
