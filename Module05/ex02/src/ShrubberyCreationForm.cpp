#include "ShrubberyCreationForm.hpp"

// OCF
ShrubberyCreationForm::ShrubberyCreationForm()
	: AForm("ShrubberyCreationForm", 145, 137), _target("default")
{
}

ShrubberyCreationForm::ShrubberyCreationForm(const ShrubberyCreationForm &other)
	: AForm(other), _target(other._target)
{
}

ShrubberyCreationForm &ShrubberyCreationForm::operator=(
	const ShrubberyCreationForm &other)
{
	if (this != &other)
	{
		AForm::operator=(other);
		this->_target = other._target;
	}
	return (*this);
}

ShrubberyCreationForm::~ShrubberyCreationForm()
{
}

// Parameterized Instrucotr
ShrubberyCreationForm::ShrubberyCreationForm(const std::string &target)
	: AForm("ShrubberyCreationForm", 145, 137), _target(target)
{
}

// Member function
void ShrubberyCreationForm::executeAction() const
{
	std::ofstream	file((this->_target + "_shrubbery").c_str());

	if (!file.is_open())
		throw ShrubberyCreationForm::FileOpenException();
	for (int i = 0; i < 3; i++)
	{
		file << "    *    " << std::endl;
		file << "   ***   " << std::endl;
		file << "  *****  " << std::endl;
		file << " ******* " << std::endl;
		file << "*********" << std::endl;
		file << "    |    " << std::endl;
		file << "    |    " << std::endl;
		file << std::endl;
	}
}

// Exception
const char *ShrubberyCreationForm::FileOpenException::what() const throw()
{
	return ("could not create the shrubbery file");
}
