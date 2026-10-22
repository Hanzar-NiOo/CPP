#ifndef SCAVTRAP_HPP
#define SCAVTRAP_HPP

#include "ClapTrap.hpp"

class ScavTrap : public virtual ClapTrap
{
public:
	ScavTrap();
	ScavTrap(std::string const & name);
	ScavTrap(ScavTrap const & other);
	ScavTrap & operator=(ScavTrap const & other);
	virtual ~ScavTrap();

	virtual void attack(std::string const & target);
	void guardGate();
};

#endif
