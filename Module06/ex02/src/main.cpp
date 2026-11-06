#include "Base.hpp"

int main()
{
	std::srand(static_cast<unsigned int>(std::time(NULL)));
 
	std::cout << "--- fixed objects ---" << std::endl;
	A a;
	B b;
	C c;
	std::cout << "pointer: "; identify(&a);
	std::cout << "pointer: "; identify(&b);
	std::cout << "pointer: "; identify(&c);
	std::cout << "reference: "; identify(a);
	std::cout << "reference: "; identify(b);
	std::cout << "reference: "; identify(c);
 
	std::cout << "--- random objects ---" << std::endl;
	for (int i = 0; i < 8; i++)
	{
		Base *obj = generate();
		std::cout << "  identify(ptr) : "; identify(obj);
		std::cout << "  identify(ref) : "; identify(*obj);
		delete obj;
	}
	return 0;
}
