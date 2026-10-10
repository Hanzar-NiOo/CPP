#include "Zombie.hpp"

Zombie* zombieHorde(int N, std::string name) {
    if (N <= 0) {
        return (NULL);
    }

    // Allocate N zombies in a single allocation
    Zombie* horde = new Zombie[N];

    // Initialize each zombie with the provided name
    for (int i = 0; i < N; ++i) {
        horde[i].setName(name);
    }

    return (horde);
}
