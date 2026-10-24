#ifndef CHARACTER_HPP
# define CHARACTER_HPP

# include <string>
# include "ICharacter.hpp"
# include "AMateria.hpp"

class Character : public ICharacter
{
	private:
		struct FloorNode
		{
			AMateria*  materia;
			FloorNode* next;
		};

		std::string name;
		AMateria*   inventory[4];
		FloorNode*  floor;

		void clearInventory();
		void clearFloor();
		void addToFloor(AMateria* m);
		void removeFromFloor(AMateria* m);

	public:
		Character();
		Character(std::string const & name);
		Character(const Character& other);
		Character& operator=(const Character& other);
		~Character();

		std::string const & getName() const;
		void equip(AMateria* m);
		void unequip(int idx);
		void use(int idx, ICharacter& target);

		AMateria* getMateria(int idx) const;   // not in the interface: only for tests
};

#endif
