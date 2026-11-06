#include "Base.hpp"

Base::~Base()
{
}

// Randomly creates an A, B or C and returns it as a Base pointer.
Base *generate(void)
{
	switch (std::rand() % 3)
	{
		case 0:
			std::cout << "generated: A" << std::endl;
			return new A();
		case 1:
			std::cout << "generated: B" << std::endl;
			return new B();
		default:
			std::cout << "generated: C" << std::endl;
			return new C();
	}
}

// Pointer version: dynamic_cast on a pointer returns NULL on failure.
void identify(Base *p)
{
	if (dynamic_cast<A *>(p))
		std::cout << "A" << std::endl;
	else if (dynamic_cast<B *>(p))
		std::cout << "B" << std::endl;
	else if (dynamic_cast<C *>(p))
		std::cout << "C" << std::endl;
	else
		std::cout << "unknown" << std::endl;
}

// Reference version: no pointers allowed, and <typeinfo> is forbidden,
// so we cannot name std::bad_cast. A failed dynamic_cast on a reference
// throws, so we catch everything with catch (...).
void identify(Base &p)
{
	try
	{
		(void)dynamic_cast<A &>(p);
		std::cout << "A" << std::endl;
		return;
	}
	catch (...) {}
	try
	{
		(void)dynamic_cast<B &>(p);
		std::cout << "B" << std::endl;
		return;
	}
	catch (...) {}
	try
	{
		(void)dynamic_cast<C &>(p);
		std::cout << "C" << std::endl;
		return;
	}
	catch (...) {}
	std::cout << "unknown" << std::endl;
}
