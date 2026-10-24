#include "Character.hpp"

Character::Character() : name("unnamed"), floor(0)
{
    for (int i = 0; i < 4; i++)
        inventory[i] = 0;
}

Character::Character(std::string const & name) : name(name), floor(0)
{
    for (int i = 0; i < 4; i++)
        inventory[i] = 0;
}

Character::Character(const Character& other) : name(other.name), floor(0)
{
    for (int i = 0; i < 4; i++)
    {
        if (other.inventory[i])
            inventory[i] = other.inventory[i]->clone();   // deep copy
        else
            inventory[i] = 0;
    }
}

Character& Character::operator=(const Character& other)
{
    if (this != &other)
    {
        clearInventory();               // delete old Materias FIRST (subject)
        name = other.name;
        for (int i = 0; i < 4; i++)
        {
            if (other.inventory[i])
                inventory[i] = other.inventory[i]->clone();
            else
                inventory[i] = 0;
        }
    }
    return *this;
}

Character::~Character()
{
    clearInventory();
    clearFloor();
}

std::string const & Character::getName() const
{
    return name;
}

void Character::equip(AMateria* m)
{
    if (!m)
        return;
    for (int i = 0; i < 4; i++)         // already equipped? would be a double delete
        if (inventory[i] == m)
            return;
    for (int i = 0; i < 4; i++)         // first empty slot, 0 to 3
    {
        if (!inventory[i])
        {
            removeFromFloor(m);         // in case it was unequipped earlier
            inventory[i] = m;
            return;
        }
    }
    // inventory full: nothing happens (the caller still owns m)
}

void Character::unequip(int idx)
{
    if (idx < 0 || idx > 3 || !inventory[idx])
        return;
    addToFloor(inventory[idx]);         // save the address BEFORE clearing the slot
    inventory[idx] = 0;                 // NO delete
}

void Character::use(int idx, ICharacter& target)
{
    if (idx < 0 || idx > 3 || !inventory[idx])
        return;
    inventory[idx]->use(target);
}

AMateria* Character::getMateria(int idx) const
{
    if (idx < 0 || idx > 3)
        return 0;
    return inventory[idx];
}

void Character::clearInventory()
{
    for (int i = 0; i < 4; i++)
    {
        delete inventory[i];            // delete on 0 is safe
        inventory[i] = 0;
    }
}

void Character::clearFloor()
{
    while (floor)
    {
        FloorNode* node = floor;
        floor = node->next;
        delete node->materia;
        delete node;
    }
}

void Character::addToFloor(AMateria* m)
{
    FloorNode* node = new FloorNode;
    node->materia = m;
    node->next = floor;
    floor = node;
}

void Character::removeFromFloor(AMateria* m)
{
    FloorNode** cur = &floor;
    while (*cur)
    {
        if ((*cur)->materia == m)
        {
            FloorNode* tmp = *cur;
            *cur = tmp->next;
            delete tmp;                 // delete the node, NOT the Materia
            return;
        }
        cur = &(*cur)->next;
    }
}
