#ifndef BRAIN_HPP
#define BRAIN_HPP

#include <string>

class Brain
{
public:
	Brain();
	Brain(Brain const & other);
	Brain & operator=(Brain const & other);
	~Brain();

	std::string getIdea(int index) const;
	void setIdea(int index, std::string const & idea);

private:
	std::string ideas[100];
};

#endif
