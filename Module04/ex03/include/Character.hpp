#ifndef CHARACTER_HPP
#define CHARACTER_HPP

#include "ICharacter.hpp"

class Character : public ICharacter
{
public:
	Character(std::string const & name);
	Character(Character const & other);
	Character & operator=(Character const & other);
	virtual ~Character();

	virtual std::string const & getName() const;
	virtual void equip(AMateria *m);
	virtual void unequip(int idx);
	virtual void use(int idx, ICharacter &target);

	AMateria *getMateria(int idx) const;

private:
	std::string name_;
	AMateria *inventory_[4];
};

#endif
