#include "ScalarConverter.hpp"

// OCF
ScalarConverter::ScalarConverter()
{
}

ScalarConverter::ScalarConverter(const ScalarConverter &)
{
}

ScalarConverter &ScalarConverter::operator=(const ScalarConverter &)
{
	return (*this);
}

ScalarConverter::~ScalarConverter()
{
}

namespace
{
	enum Type
	{
		CHAR,
		INT,
		FLOAT,
		DOUBLE,
		INVALID
	};

	// Helper functions
	bool 	isReal(const std::string &literal, size_t end)
    {
        size_t i = 0, dots = 0, digits = 0;
        if (end > 0 && (literal[0] == '+' || literal[0] == '-'))
            i++;
        for (; i < end; i++)
        {
            if (literal[i] == '.')
                dots++;
            else if (std::isdigit(static_cast<unsigned char>(literal[i])))
                digits++;
            else
                return false;
        }
        return dots == 1 && digits > 0;
    }

	bool	isFloatPseudo(const std::string &literal)
	{
		return (literal == "nanf" || literal == "+inff" || literal == "-inff");
	}

	bool	isDoublePseudo(const std::string &literal)
	{
		return (literal == "nan" || literal == "+inf" || literal == "-inf");
	}

	int decimals(const std::string &literal)
    {
        size_t dot = literal.find('.');
        size_t end = literal.size();
        if (dot == std::string::npos)
            return 1;
        if (literal[end - 1] == 'f')
            end--;
        return (end - dot - 1 < 1) ? 1 : static_cast<int>(end - dot - 1);
    }

    bool isNan(double d) { return d != d; }
    bool isInf(double d) { return !isNan(d) && (d > DBL_MAX || d < -DBL_MAX); }

    // int is representable only in [-2^31, 2^31)
    bool fitsInt(double d)
    {
        return !isNan(d) && d >= -2147483648.0 && d < 2147483648.0;
    }

	// Type detection functions
	bool	isChar(const std::string &literal)
	{
		if (literal.length() == 3 && literal[0] == '\'' && literal[2] == '\'')
			return (true);
		return (literal.length() == 1 && !std::isdigit(literal[0]));
	}

	bool	isInt(const std::string &literal)
	{
		size_t i = 0;
		if (literal[i] == '-' || literal[i] == '+')
			i++;
		for (; i < literal.length(); i++)
		{
			if (!std::isdigit(literal[i]))
				return (false);
		}
		return (true);
	}

	bool 	isDouble(const std::string &literal)
	{
		return isDoublePseudo(literal) || isReal(literal, literal.size());
	}

	bool 	isFloat(const std::string &literal)
	{
		if (isFloatPseudo(literal))
            return true;
        return !literal.empty() && literal[literal.size() - 1] == 'f' && isReal(literal, literal.size() - 1);
	}

	Type detectType(const std::string &literal)
	{
		if (literal.empty())	return INVALID;
		if (isChar(literal))	return CHAR;
		if (isInt(literal))		return INT;
		if (isFloat(literal))	return FLOAT;
		if (isDouble(literal))	return DOUBLE;
		return INVALID;
	}

	// Print functions
    void 	printCharValue(int c)   // c already known to be in 0..127
    {
        if (!std::isprint(c))
            std::cout << "Non displayable";
        else
            std::cout << "'" << static_cast<char>(c) << "'";
    }

    void 	printFloat(float f, int prec)
    {
        if (isNan(f))
            std::cout << "nanf";
        else if (isInf(f))
            std::cout << (f > 0 ? "+inff" : "-inff");
        else
            std::cout << std::fixed << std::setprecision(prec) << f << "f";
    }

    void 	printDouble(double d, int prec)
    {
        if (isNan(d))
            std::cout << "nan";
        else if (isInf(d))
            std::cout << (d > 0 ? "+inf" : "-inf");
        else
            std::cout << std::fixed << std::setprecision(prec) << d;
    }

    /* ---------- one function per real type ---------- */

    void fromChar(char c)
    {
        std::cout << "char: ";   printCharValue(c);                          std::cout << "\n";
        std::cout << "int: "     << static_cast<int>(c)                      << "\n";
        std::cout << "float: ";  printFloat(static_cast<float>(c), 1);       std::cout << "\n";
        std::cout << "double: "; printDouble(static_cast<double>(c), 1);     std::cout << std::endl;
    }

    void fromInt(int i)
    {
        std::cout << "char: ";
        if (i < 0 || i > 127) std::cout << "impossible";
        else                  printCharValue(i);
        std::cout << "\n";
        std::cout << "int: "     << i                                        << "\n";
        std::cout << "float: ";  printFloat(static_cast<float>(i), 1);       std::cout << "\n";
        std::cout << "double: "; printDouble(static_cast<double>(i), 1);     std::cout << std::endl;
    }

    void fromFloat(float f, int prec)
    {
        std::cout << "char: ";
        if (isNan(f) || isInf(f) || f < 0 || f > 127) std::cout << "impossible";
        else printCharValue(static_cast<int>(f));
        std::cout << "\n";

        std::cout << "int: ";
        if (!fitsInt(f) || isInf(f)) std::cout << "impossible";
        else                         std::cout << static_cast<int>(f);
        std::cout << "\n";

        std::cout << "float: ";  printFloat(f, prec);                        std::cout << "\n";
        std::cout << "double: "; printDouble(static_cast<double>(f), prec);  std::cout << std::endl;
    }

    void fromDouble(double d, int prec)
    {
        std::cout << "char: ";
        if (isNan(d) || isInf(d) || d < 0 || d > 127) std::cout << "impossible";
        else printCharValue(static_cast<int>(d));
        std::cout << "\n";

        std::cout << "int: ";
        if (!fitsInt(d) || isInf(d)) std::cout << "impossible";
        else                         std::cout << static_cast<int>(d);
        std::cout << "\n";

        std::cout << "float: ";
        if (!isNan(d) && !isInf(d) && (d > FLT_MAX || d < -FLT_MAX))
            std::cout << "impossible";
        else
            printFloat(static_cast<float>(d), prec);
        std::cout << "\n";

        std::cout << "double: "; printDouble(d, prec);                       std::cout << std::endl;
    }

    void printImpossible()
    {
        std::cout << "char: impossible\n"
                  << "int: impossible\n"
                  << "float: impossible\n"
                  << "double: impossible" << std::endl;
    }
}

void ScalarConverter::convert(const std::string &literal)
{
    switch (detectType(literal))
    {
        case CHAR:
        {
            char c = (literal.size() == 1) ? literal[0] : literal[1];
            fromChar(c);
            break;
        }
        case INT:
        {
            double d = std::strtod(literal.c_str(), NULL);
            if (d >= -2147483648.0 && d < 2147483648.0)
                fromInt(static_cast<int>(std::strtol(literal.c_str(), NULL, 10)));
            else
                fromDouble(d, 1);   // valid number, but too big for an int
            break;
        }
		// 7 significant decimal digits
        case FLOAT:
        {
            std::string body = literal.substr(0, literal.size() - 1); // drop 'f'
            double d = std::strtod(body.c_str(), NULL);               // handles nan / +inf / -inf
            if (!isNan(d) && !isInf(d) && (d > FLT_MAX || d < -FLT_MAX))
                printImpossible();
            else
                fromFloat(static_cast<float>(d), decimals(literal));
            break;
        }
		// 15 to 17 significant decimal digits of precision
        case DOUBLE:
            fromDouble(std::strtod(literal.c_str(), NULL), decimals(literal));
            break;
        default:
            printImpossible();
            break;
    }
}
