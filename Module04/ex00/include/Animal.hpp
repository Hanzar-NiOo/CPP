#ifndef ANIMAL_HPP
# define ANIMAL_HPP

# include <string>
# include <iostream>

class Animal
{
protected:
    std::string type;

public:
    Animal();
    Animal(const Animal& other);
    Animal& operator=(const Animal& other);
    virtual ~Animal();                 // virtual destructor: see Step 6

    virtual void makeSound() const;    // virtual + const
    std::string getType() const;
};

#endif
