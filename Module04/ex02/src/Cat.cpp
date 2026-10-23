#include "Cat.hpp"

Cat::Cat() : AAnimal(), brain(new Brain())
{
    type = "Cat";
    std::cout << "[Cat] default constructor called" << std::endl;
}

Cat::Cat(const Cat& other) : AAnimal(other), brain(new Brain(*other.brain))
{
    std::cout << "[Cat] copy constructor called" << std::endl;
}

Cat& Cat::operator=(const Cat& other)
{
    std::cout << "[Cat] copy assignment called" << std::endl;
    if (this != &other)
    {
        AAnimal::operator=(other);
        Brain* newBrain = new Brain(*other.brain);  // allocate first
        delete brain;                               // then free the old one
        brain = newBrain;
    }
    return *this;
}

Cat::~Cat()
{
    delete brain;
    std::cout << "[Cat] destructor called" << std::endl;
}

void Cat::makeSound() const
{
    std::cout << "Meow~" << std::endl;
}

Brain* Cat::getBrain() const
{
    return brain;
}
