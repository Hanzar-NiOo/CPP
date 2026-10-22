#include "Animal.hpp"
#include "Cat.hpp"
#include "Dog.hpp"
#include "WrongAnimal.hpp"
#include "WrongCat.hpp"

#include <iostream>

static void testSubjectExample()
{
	std::cout << "--- testSubjectExample ---" << std::endl;

	const Animal *meta = new Animal();
	const Animal *j = new Dog();
	const Animal *i = new Cat();
	std::cout << j->getType() << " " << std::endl;
	std::cout << i->getType() << " " << std::endl;
	i->makeSound(); // will output the cat sound!
	j->makeSound();
	meta->makeSound();

	delete meta;
	delete j;
	delete i;
}

static void testWrongCat()
{
	std::cout << "--- testWrongCat ---" << std::endl;
	std::cout << "(the WrongCat does not override makeSound, so it uses the WrongAnimal one)" << std::endl;

	const WrongAnimal *wmeta = new WrongAnimal();
	const WrongAnimal *wcat = new WrongCat();
	std::cout << wcat->getType() << " " << std::endl;
	wcat->makeSound(); // will output the wrong animal sound!
	wmeta->makeSound();

	delete wmeta;
	delete wcat;
}

static void testDestructionThroughBasePointer()
{
	std::cout << "--- testDestructionThroughBasePointer ---" << std::endl;
	std::cout << "(the virtual destructor is called, then the base class destructor)" << std::endl;

	Animal *animals[3];
	animals[0] = new Dog();
	animals[1] = new Cat();
	animals[2] = new Animal();

	for (int i = 0; i < 3; i++)
		delete animals[i];
}

static void testCopy()
{
	std::cout << "--- testCopy ---" << std::endl;

	Dog original;
	Dog copy(original);
	copy.makeSound();

	Cat assigned;
	Cat other = assigned;
	other.makeSound();
}

int main()
{
	std::cout << "=== Module 04 - ex00: Polymorphism ===" << std::endl;

	testSubjectExample();
	testWrongCat();
	testDestructionThroughBasePointer();
	testCopy();

	std::cout << "=== ex00 done ===" << std::endl;
	return (0);
}
