#ifndef SCALARCONVERTER_HPP
# define SCALARCONVERTER_HPP

# include <string>
# include <iostream>
# include <cfloat>
# include <iomanip>
# include <cstdlib>

class ScalarConverter
{
	// must not be instantiable by users
	private: 
		// OCF
		ScalarConverter();
		ScalarConverter(const ScalarConverter &other);
		ScalarConverter &operator=(const ScalarConverter &other);
		~ScalarConverter();

	public:
		static void	convert(const std::string &literal);
};

#endif
