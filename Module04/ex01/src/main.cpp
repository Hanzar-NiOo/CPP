#include "Animal.hpp"
#include "Brain.hpp"
#include "Cat.hpp"
#include "Dog.hpp"

#include <iostream>

static void testSubjectExample()
{
	std::cout << "--- testSubjectExample ---" << std::endl;

	const Animal *j = new Dog();
	const Animal *i = new Cat();
	delete j; // should not create a leak
	delete i;
}

static void testArrayOfAnimals()
{
	std::cout << "--- testArrayOfAnimals ---" << std::endl;
	std::cout << "(an array of 10 animals, half of them dogs and half of them cats)" << std::endl;

	Animal *animals[10];
	for (int i = 0; i < 10; i++)
	{
		if (i % 2 == 0)
		{
			Dog *dog = new Dog();
			dog->setIdea(i, "I want to play!");
			animals[i] = dog;
		}
		else
		{
			Cat *cat = new Cat();
			cat->setIdea(i, "I want some food!");
			animals[i] = cat;
		}
	}

	for (int i = 0; i < 10; i++)
	{
		std::cout << "animal " << i << " is a " << animals[i]->getType() << std::endl;
		animals[i]->makeSound();
	}

	std::cout << "(every animal is deleted through an Animal pointer)" << std::endl;
	for (int i = 0; i < 10; i++)
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

int main()
{
	std::cout << "=== Module 04 - ex01: I don't want to set the world on fire ===" << std::endl;

	testSubjectExample();
	testArrayOfAnimals();
	testDeepCopy();

	std::cout << "=== ex01 done ===" << std::endl;
	return (0);
}
