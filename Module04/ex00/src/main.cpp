#include "Animal.hpp"
#include "Dog.hpp"
#include "Cat.hpp"
#include "WrongAnimal.hpp"
#include "WrongCat.hpp"

static void title(const std::string& s)
{
    std::cout << "\n===== " << s << " =====" << std::endl;
}

int main()
{
    title("1. Subject test");
    {
        const Animal* meta = new Animal();
        const Animal* j = new Dog();
        const Animal* i = new Cat();

        std::cout << j->getType() << " " << std::endl;
        std::cout << i->getType() << " " << std::endl;
        i->makeSound();
        j->makeSound();
        meta->makeSound();

        delete meta;
        delete j;
        delete i;
    }

    title("2. Wrong classes (no virtual)");
    {
        const WrongAnimal* w = new WrongCat();
        std::cout << w->getType() << std::endl;
        w->makeSound();                    // WrongAnimal sound!

        const WrongCat* wc = new WrongCat();
        wc->makeSound();                   // WrongCat sound (static type is WrongCat)

        delete w;
        delete wc;
    }

    title("3. Objects on the stack");
    {
        Dog d;
        Cat c;
        d.makeSound();
        c.makeSound();
    }

    title("4. Copy constructor and assignment");
    {
        Dog a;
        Dog b(a);          // copy constructor
        Dog c;
        c = a;             // copy assignment
        std::cout << b.getType() << " / " << c.getType() << std::endl;
        b.makeSound();
    }

    title("5. Array of Animal*");
    {
        const Animal* zoo[4];
        zoo[0] = new Dog();
        zoo[1] = new Cat();
        zoo[2] = new Dog();
        zoo[3] = new Cat();
        for (int k = 0; k < 4; k++)
            zoo[k]->makeSound();
        for (int k = 0; k < 4; k++)
            delete zoo[k];
    }

    title("6. Reference (polymorphism works with references too)");
    {
        Dog d;
        const Animal& ref = d;
        ref.makeSound();
    }

    return 0;
}
