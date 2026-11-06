#ifndef SERIALIZER_HPP
# define SERIALIZER_HPP

# include <stdint.h>
# include "Data.hpp"

class Serializer
{
	private:
		// OCF
		Serializer();
		Serializer(Serializer &other);
		Serializer &operator=(Serializer &other);
		~Serializer();

	public:
		// Member functions
		static uintptr_t	serialize(Data* ptr);
		static Data* 		deserialize(uintptr_t raw);
};

#endif
