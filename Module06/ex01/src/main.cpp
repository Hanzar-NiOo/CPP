#include "Serializer.hpp"
#include <iostream>

int main()
{
	Data data;
	data.id = 42;
	data.name = "serialization";
	data.value = 3.14;

	Data		*original = &data;
	uintptr_t	raw = Serializer::serialize(original);
	Data		*restored = Serializer::deserialize(raw);

	std::cout << "original ptr : " << original << std::endl;
	std::cout << "raw uintptr_t: " << raw << std::endl;
	std::cout << "restored ptr : " << restored << std::endl;

	if (restored == original)
		std::cout << "OK: pointers are equal" << std::endl;
	else
	{
		std::cout << "KO: pointers differ" << std::endl;
		return 1;
	}

	std::cout << "restored->id    = " << restored->id << std::endl;
	std::cout << "restored->name  = " << restored->name << std::endl;
	std::cout << "restored->value = " << restored->value << std::endl;
	return 0;
}
