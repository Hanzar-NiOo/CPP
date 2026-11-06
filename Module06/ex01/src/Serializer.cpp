#include "Serializer.hpp"

// OCF
Serializer::Serializer()
{
}

Serializer::Serializer(Serializer &)
{
}

Serializer	&Serializer::operator=(Serializer &)
{
	return (*this);
}

Serializer::~Serializer()
{
}

// Member functions
uintptr_t Serializer::serialize(Data *ptr)
{
	return reinterpret_cast<uintptr_t>(ptr);
}
 
Data *Serializer::deserialize(uintptr_t raw)
{
	return reinterpret_cast<Data *>(raw);
}
 