#include "Animal.hpp"
#include "Dog.hpp"
#include "Cat.hpp"
#include "Brain.hpp"
#include "WrongAnimal.hpp"
#include "WrongCat.hpp"

static void title(const std::string& s)
{
    std::cout << "\n===== " << s << " =====" << std::endl;
}

int main()
{
    title("1. Subject test (no leak)");
    {
        const Animal* j = new Dog();
        const Animal* i = new Cat();
        delete j;
        delete i;
    }

    title("2. Array of Animals: half Dogs, half Cats");
    {
        const int N = 10;
        Animal* zoo[N];

        for (int k = 0; k < N; k++)
        {
            if (k < N / 2)
                zoo[k] = new Dog();
            else
                zoo[k] = new Cat();
        }
        for (int k = 0; k < N; k++)
            zoo[k]->makeSound();
        for (int k = 0; k < N; k++)
            delete zoo[k];          // deleted as Animal*
    }

    title("3. Deep copy: copy constructor (Dog)");
    {
        Dog original;
        original.getBrain()->setIdea(0, "chase the ball");

        Dog copy(original);

        std::cout << "original brain: " << original.getBrain() << std::endl;
        std::cout << "copy brain:     " << copy.getBrain() << std::endl;
        // The two addresses must be DIFFERENT.

        copy.getBrain()->setIdea(0, "sleep");
        std::cout << "original idea 0: " << original.getBrain()->getIdea(0) << std::endl;
        std::cout << "copy idea 0:     " << copy.getBrain()->getIdea(0) << std::endl;
        // original must still say "chase the ball".
    }

    title("4. Deep copy: assignment operator (Cat)");
    {
        Cat a;
        Cat b;
        a.getBrain()->setIdea(0, "knock the glass off the table");
        b.getBrain()->setIdea(0, "nap");

        b = a;

        a.getBrain()->setIdea(0, "ignore everyone");
        std::cout << "a idea 0: " << a.getBrain()->getIdea(0) << std::endl;
        std::cout << "b idea 0: " << b.getBrain()->getIdea(0) << std::endl;
        // b must still say "knock the glass off the table".
    }

    title("5. Copy outlives the original");
    {
        Dog* original = new Dog();
        original->getBrain()->setIdea(5, "bone");
        Dog* copy = new Dog(*original);
        delete original;            // would break a shallow copy
        std::cout << "copy idea 5: " << copy->getBrain()->getIdea(5) << std::endl;
        delete copy;
    }

    title("6. Self-assignment");
    {
        Dog d;
        d.getBrain()->setIdea(0, "still here");
        Dog& ref = d;
        d = ref;
        std::cout << d.getBrain()->getIdea(0) << std::endl;
    }

    title("7. Copy through a base pointer");
    {
        Dog d;
        const Animal* a = new Dog(d);   // copy made from a real Dog
        a->makeSound();
        delete a;
    }

    title("8. Brain on its own");
    {
        Brain b1;
        b1.setIdea(0, "idea A");
        b1.setIdea(99, "last idea");
        Brain b2(b1);
        b2.setIdea(0, "idea B");
        std::cout << b1.getIdea(0) << " / " << b2.getIdea(0) << " / "
                  << b2.getIdea(99) << std::endl;
        std::cout << "out of range: [" << b1.getIdea(100) << "]" << std::endl;
    }

    return 0;
}
