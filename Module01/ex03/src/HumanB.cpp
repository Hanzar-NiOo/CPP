#include "HumanB.hpp"

HumanB::HumanB(const std::string& name) : _name(name), _weapon(NULL) {
}

HumanB::~HumanB(void) {
}

void HumanB::setWeapon(Weapon& weapon) {
    this->_weapon = &weapon;
}

void HumanB::attack(void) const {
    if (this->_weapon != NULL) {
        std::cout << this->_name << " attacks with their " << this->_weapon->getType() << std::endl;
    } else {
        std::cout << this->_name << " has no weapon to attack with" << std::endl;
    }
}
