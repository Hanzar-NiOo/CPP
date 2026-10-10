#include "Zombie.hpp"

int main(void) {
    std::cout << "=== Test 1: Stack Allocation via randomChump ===" << std::endl;
    // Creates a zombie on the stack inside randomChump.
    // It announces itself and is destroyed as soon as randomChump finishes.
    randomChump("StackChump");

    std::cout << "\n=== Test 2: Heap Allocation via newZombie ===" << std::endl;
    // Creates a zombie on the heap and returns a pointer.
    // It remains in memory until delete is explicitly called.
    Zombie* heapZombie = newZombie("HeapWalker");
    heapZombie->announce();

    std::cout << "\n=== Test 3: Manual Stack Zombie in Scope ===" << std::endl;
    {
        Zombie scopedZombie("ScopedStackZombie");
        scopedZombie.announce();
        std::cout << "Exiting inner scope..." << std::endl;
    }

    std::cout << "\n=== Cleaning up Heap Zombie ===" << std::endl;
    delete heapZombie;

    std::cout << "\nProgram terminating." << std::endl;
    return (0);
}
