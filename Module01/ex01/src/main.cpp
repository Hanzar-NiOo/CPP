#include "Zombie.hpp"

int main(void) {
    int hordeSize = 5;

    std::cout << "=== Test 1: Creating a horde of " << hordeSize << " zombies ===" << std::endl;
    Zombie* horde = zombieHorde(hordeSize, "HordeMember");

    if (horde != NULL) {
        for (int i = 0; i < hordeSize; ++i) {
            std::cout << "[" << i << "] ";
            horde[i].announce();
        }

        std::cout << "\n=== Deallocating the horde with delete[] ===" << std::endl;
        delete[] horde;
    }

    std::cout << "\n=== Test 2: Edge cases (N <= 0) ===" << std::endl;
    Zombie* emptyHorde = zombieHorde(0, "Nobody");
    if (emptyHorde == NULL) {
        std::cout << "Correctly handled N = 0 (returned NULL)" << std::endl;
    }

    Zombie* negativeHorde = zombieHorde(-3, "NegativeZombie");
    if (negativeHorde == NULL) {
        std::cout << "Correctly handled N < 0 (returned NULL)" << std::endl;
    }

    return (0);
}
