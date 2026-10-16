#include "Zombie.hpp"

int main(void) {
    int hordeSize = 5;

    std::cout << "=== Creating a horde of " << hordeSize << " zombies ===" << std::endl;
    Zombie* horde = zombieHorde(hordeSize, "HordeMember");

    if (horde != NULL) {
        for (int i = 0; i < hordeSize; ++i) {
            std::cout << "[" << i << "] ";
            horde[i].announce();
        }

        std::cout << "\n=== Deallocating the horde with delete[] ===" << std::endl;
        delete[] horde;
    }
    return (0);
}
