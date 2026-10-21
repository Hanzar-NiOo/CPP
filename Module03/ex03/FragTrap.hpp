#ifndef FRAGTRAP_HPP
#define FRAGTRAP_HPP

#include "ClapTrap.hpp"

class FragTrap : public virtual ClapTrap
{
public:
	FragTrap();
	FragTrap(std::string const & name);
	FragTrap(FragTrap const & other);
	FragTrap & operator=(FragTrap const & other);
	virtual ~FragTrap();

	void highFivesGuys();
};

#endif
