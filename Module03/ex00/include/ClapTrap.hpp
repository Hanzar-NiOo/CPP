#ifndef CLAPTRAP_HPP
#define CLAPTRAP_HPP

#include <string>

class ClapTrap
{
	private:
		// According to the subject
		std::string name_;
		unsigned int hitPoints_;
		unsigned int energyPoints_;
		unsigned int attackDamage_;

	public:
		ClapTrap();
		ClapTrap(std::string const & name);
		ClapTrap(ClapTrap const & other);
		ClapTrap & operator=(ClapTrap const & other);
		virtual ~ClapTrap();

		// According to the subject
		virtual void attack(std::string const & target);
		void takeDamage(unsigned int amount);
		void beRepaired(unsigned int amount);

		std::string const & getName() const;
		unsigned int getHitPoints() const;
		unsigned int getEnergyPoints() const;
		unsigned int getAttackDamage() const;

	protected:
		void setName(std::string const & name);
		void setHitPoints(unsigned int hitPoints);
		void setEnergyPoints(unsigned int energyPoints);
		void setAttackDamage(unsigned int attackDamage);
		bool hasHitPoints() const;
		bool hasEnergy() const;
		void consumeEnergy();
};

#endif
