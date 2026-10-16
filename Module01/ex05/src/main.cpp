#include "Harl.hpp"
#include <iostream>

int main(void) {
    Harl harl;

    std::cout << "=== Test 1: DEBUG ===" << std::endl;
    harl.complain("DEBUG");
    std::cout << std::endl;

    std::cout << "=== Test 2: INFO ===" << std::endl;
    harl.complain("INFO");
    std::cout << std::endl;

    std::cout << "=== Test 3: WARNING ===" << std::endl;
    harl.complain("WARNING");
    std::cout << std::endl;

    std::cout << "=== Test 4: ERROR ===" << std::endl;
    harl.complain("ERROR");
    std::cout << std::endl;

    std::cout << "=== Test 5: UNKNOWN LEVEL ===" << std::endl;
    harl.complain("RANDOM_NOISE");
    std::cout << std::endl;

    std::cout << "=== Test 6: EMPTY STRING ===" << std::endl;
    harl.complain("");
    std::cout << std::endl;

    return (0);
}
