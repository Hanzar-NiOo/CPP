#include "AAnimal.hpp"
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
        const AAnimal* j = new Dog();
        const AAnimal* i = new Cat();
        std::cout << j->getType() << " / " << i->getType() << std::endl;
        j->makeSound();
        i->makeSound();
        delete j;   // should not create a leak
        delete i;
    }

    title("2. Array of AAnimal: half Dogs, half Cats");
    {
        const int N = 10;
        AAnimal* zoo[N];

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
            delete zoo[k];          // deleted directly as AAnimal*
    }

    title("3. Reference to the abstract type");
    {
        Dog d;
        Cat c;
        const AAnimal& r1 = d;
        const AAnimal& r2 = c;
        r1.makeSound();
        r2.makeSound();
    }

    title("4. Deep copy: copy constructor (Dog)");
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

    title("5. Deep copy: copy constructor (Cat)");
    {
        Cat original;
        original.getBrain()->setIdea(3, "climb the curtains");

        Cat copy(original);

        std::cout << "original brain: " << original.getBrain() << std::endl;
        std::cout << "copy brain:     " << copy.getBrain() << std::endl;

        original.getBrain()->setIdea(3, "stare at the wall");
        std::cout << "original idea 3: " << original.getBrain()->getIdea(3) << std::endl;
        std::cout << "copy idea 3:     " << copy.getBrain()->getIdea(3) << std::endl;
        // copy must still say "climb the curtains".
    }

    title("6. Deep copy: assignment operator (Cat)");
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

    title("7. Deep copy: assignment operator (Dog)");
    {
        Dog a;
        Dog b;
        a.getBrain()->setIdea(10, "fetch");
        b = a;
        std::cout << "a brain: " << a.getBrain() << std::endl;
        std::cout << "b brain: " << b.getBrain() << std::endl;
        b.getBrain()->setIdea(10, "bark at the mailman");
        std::cout << "a idea 10: " << a.getBrain()->getIdea(10) << std::endl;
        std::cout << "b idea 10: " << b.getBrain()->getIdea(10) << std::endl;
    }

    title("8. Copy outlives the original");
    {
        Dog* original = new Dog();
        original->getBrain()->setIdea(5, "bone");
        Dog* copy = new Dog(*original);
        delete original;            // would break a shallow copy
        std::cout << "copy idea 5: " << copy->getBrain()->getIdea(5) << std::endl;
        delete copy;
    }

    title("9. Self-assignment");
    {
        Dog d;
        d.getBrain()->setIdea(0, "still here");
        Dog& ref = d;
        d = ref;
        std::cout << d.getBrain()->getIdea(0) << std::endl;

        Cat c;
        c.getBrain()->setIdea(0, "still here too");
        Cat& cref = c;
        c = cref;
        std::cout << c.getBrain()->getIdea(0) << std::endl;
    }

    title("10. Copy through a base pointer");
    {
        Dog d;
        d.getBrain()->setIdea(0, "original idea");
        const AAnimal* a = new Dog(d);   // copy of a real Dog
        a->makeSound();
        delete a;
        std::cout << d.getBrain()->getIdea(0) << std::endl;   // d is untouched
    }

    title("11. Brain on its own");
    {
        Brain b1;
        b1.setIdea(0, "idea A");
        b1.setIdea(99, "last idea");
        Brain b2(b1);
        b2.setIdea(0, "idea B");
        std::cout << b1.getIdea(0) << " / " << b2.getIdea(0) << " / "
                  << b2.getIdea(99) << std::endl;
        std::cout << "out of range: [" << b1.getIdea(100) << "]" << std::endl;
        std::cout << "negative index: [" << b1.getIdea(-1) << "]" << std::endl;

        Brain b3;
        b3 = b1;
        std::cout << "assigned: " << b3.getIdea(0) << " / " << b3.getIdea(99) << std::endl;
    }

    title("12. Wrong classes (no virtual): still the negative example");
    {
        const WrongAnimal* w = new WrongCat();
        std::cout << w->getType() << std::endl;
        w->makeSound();                 // WrongAnimal sound!

        const WrongCat* wc = new WrongCat();
        wc->makeSound();                // WrongCat sound

        delete w;
        delete wc;
    }

    return 0;
}
