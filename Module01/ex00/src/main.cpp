#include "Zombie.hpp"

int main(void) {
    std::cout << "=== TStack Allocation via randomChump ===" << std::endl;
    randomChump("StackChump");

    std::cout << "\n=== Heap Allocation via newZombie ===" << std::endl;
    Zombie* heapZombie = newZombie("HeapWalker");
    heapZombie->announce();

    std::cout << "\n=== Cleaning up Heap Zombie ===" << std::endl;
    delete heapZombie;

    std::cout << "\nProgram terminating." << std::endl;
    return (0);
}
