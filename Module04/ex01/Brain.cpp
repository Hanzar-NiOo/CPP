#include "Brain.hpp"

#include <iostream>

Brain::Brain()
{
	for (int i = 0; i < 100; i++)
		ideas[i] = "";
	std::cout << "Brain: a new brain has been created." << std::endl;
}

Brain::Brain(Brain const & other)
{
	for (int i = 0; i < 100; i++)
		ideas[i] = other.ideas[i];
	std::cout << "Brain: a copy of a brain has been created." << std::endl;
}

Brain & Brain::operator=(Brain const & other)
{
	if (this != &other)
	{
		for (int i = 0; i < 100; i++)
			ideas[i] = other.ideas[i];
		std::cout << "Brain: a brain has been assigned from another brain." << std::endl;
	}
	return (*this);
}

Brain::~Brain()
{
	std::cout << "Brain: a brain has been destroyed." << std::endl;
}

std::string Brain::getIdea(int index) const
{
	if (index < 0 || index >= 100)
		return (std::string(""));
	return (ideas[index]);
}

void Brain::setIdea(int index, std::string const & idea)
{
	if (index < 0 || index >= 100)
		return;
	ideas[index] = idea;
}
