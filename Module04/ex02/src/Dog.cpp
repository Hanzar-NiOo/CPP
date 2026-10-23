#include "Dog.hpp"

Dog::Dog() : AAnimal(), brain(new Brain())
{
    type = "Dog";
    std::cout << "[Dog] default constructor called" << std::endl;
}

Dog::Dog(const Dog& other) : AAnimal(other), brain(new Brain(*other.brain))
{
    std::cout << "[Dog] copy constructor called" << std::endl;
}

Dog& Dog::operator=(const Dog& other)
{
    std::cout << "[Dog] copy assignment called" << std::endl;
    if (this != &other)
    {
        AAnimal::operator=(other);
        Brain* newBrain = new Brain(*other.brain);  // allocate first
        delete brain;                               // then free the old one
        brain = newBrain;
    }
    return *this;
}

Dog::~Dog()
{
    delete brain;
    std::cout << "[Dog] destructor called" << std::endl;
}

void Dog::makeSound() const
{
    std::cout << "Woof! Woof!" << std::endl;
}

Brain* Dog::getBrain() const
{
    return brain;
}
