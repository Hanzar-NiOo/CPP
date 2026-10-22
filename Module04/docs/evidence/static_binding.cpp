// ---------------------------------------------------------------------------
//  DELIBERATE EXPERIMENT  (evidence for the Module 04 evaluation)
//
//  Goal : show that WITHOUT "virtual" the call is bound at COMPILE TIME.
//
//  This is the ex00 class hierarchy, with one single difference: the
//  makeSound() of Animal is NOT virtual.  The object is really a Dog
//  (getType() prints "Dog"), but makeSound() still runs the base version,
//  because the compiler picked the function from the type of the pointer.
//
//  The real ex00 declares :  virtual void makeSound() const;
//  and the Dog / Cat overrides are then really overrides.
//
//  Build & run :  ./run_evidence.sh
// ---------------------------------------------------------------------------

#include <iostream>
#include <string>

class Animal
{
public:
	Animal() : type("Animal") { }
	virtual ~Animal() { }
	std::string const & getType() const { return (type); }
	void makeSound() const        //  <-- NOT virtual
	{
		std::cout << "Animal: makes a generic animal sound..." << std::endl;
	}
protected:
	std::string type;
};

class Dog : public Animal
{
public:
	Dog() { type = "Dog"; }
	void makeSound() const        //  <-- hidden, not overridden
	{
		std::cout << "Woof woof!" << std::endl;
	}
};

int main()
{
	Animal *j = new Dog();
	std::cout << "the real type is: " << j->getType() << std::endl;
	j->makeSound();
	delete j;
	return (0);
}
