#include "Animal.hpp"
#include "Brain.hpp"
#include "Cat.hpp"
#include "Dog.hpp"
#include "WrongAnimal.hpp"
#include "WrongCat.hpp"

#include <iostream>

static void testAbstractAnimal()
{
	std::cout << "--- testAbstractAnimal ---" << std::endl;
	std::cout << "(the Animal class is abstract, it cannot be instantiated anymore)" << std::endl;
	std::cout << "(writing 'Animal animal;' in the main would not compile)" << std::endl;

	Animal *animals[4];
	animals[0] = new Dog();
	animals[1] = new Cat();
	animals[2] = new Dog();
	animals[3] = new Cat();

	for (int i = 0; i < 4; i++)
	{
		std::cout << "animal " << i << " is a " << animals[i]->getType() << std::endl;
		animals[i]->makeSound();
	}

	for (int i = 0; i < 4; i++)
		delete animals[i];
}

static void testDeepCopy()
{
	std::cout << "--- testDeepCopy ---" << std::endl;
	std::cout << "(a copy of a dog or a cat must not be shallow)" << std::endl;

	Dog original;
	original.setIdea(0, "I want to play!");

	Dog copy(original);
	copy.setIdea(0, "I want to sleep!");

	std::cout << "the original dog thinks: " << original.getIdea(0) << std::endl;
	std::cout << "the copy of the dog thinks: " << copy.getIdea(0) << std::endl;

	Cat catOriginal;
	catOriginal.setIdea(0, "I want some food!");

	Cat catCopy;
	catCopy = catOriginal;
	catCopy.setIdea(0, "I want to nap!");

	std::cout << "the original cat thinks: " << catOriginal.getIdea(0) << std::endl;
	std::cout << "the copy of the cat thinks: " << catCopy.getIdea(0) << std::endl;
}

static void testWrongCat()
{
	std::cout << "--- testWrongCat ---" << std::endl;
	std::cout << "(the WrongCat does not override makeSound, so it uses the WrongAnimal one)" << std::endl;

	const WrongAnimal *wcat = new WrongCat();
	wcat->makeSound(); // will output the wrong animal sound!
	delete wcat;
}

int main()
{
	std::cout << "=== Module 04 - ex02: Abstract class ===" << std::endl;

	testAbstractAnimal();
	testDeepCopy();
	testWrongCat();

	std::cout << "=== ex02 done ===" << std::endl;
	return (0);
}
