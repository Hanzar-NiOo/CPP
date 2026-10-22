// ---------------------------------------------------------------------------
//  DELIBERATE MISTAKE  (evidence for the Module 04 evaluation)
//
//  Goal : show what a SHALLOW copy of an owned Brain really does.
//
//  The copy constructor below copies the POINTER instead of the DATA:
//      brain(other.brain)
//  so the original dog and the copy share the same Brain object.
//
//  Compiled with -fsanitize=address, this program reports a double free.
//  The real ex01 does NOT do this: its copy constructor is
//      brain(new Brain(*other.brain))
//  which is a deep copy.
//
//  Note : the 100 ideas of the real Brain are not reproduced here.  The
//  payload is irrelevant to the double free, and a 3 KB allocation lands in
//  ASan's secondary allocator, where the report degrades into a SEGV instead
//  of the clean "attempting double-free" message.
//
//  Build & run :  ./run_evidence.sh
// ---------------------------------------------------------------------------

#include <iostream>
#include <string>

class Brain
{
public:
	Brain() { std::cout << "Brain: created" << std::endl; }
	~Brain() { std::cout << "Brain: destroyed" << std::endl; }
};

class Animal
{
public:
	Animal() { }
	virtual ~Animal() { }
protected:
	std::string type;
};

class Dog : public Animal
{
public:
	Dog() : brain(new Brain()) { }
	Dog(Dog const & other) : brain(other.brain) { }   //  <-- SHALLOW on purpose
	~Dog() { delete brain; }

private:
	Brain *brain;
};

int main()
{
	Dog original;
	Dog copy(original);
	return (0);
}
