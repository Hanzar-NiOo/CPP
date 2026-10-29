#ifndef SHRUBBERYCREATIONFORM_HPP
# define SHRUBBERYCREATIONFORM_HPP

# include <string>
# include <exception>
# include <fstream>
# include "AForm.hpp"

class ShrubberyCreationForm : public AForm
{
	private:
		std::string	_target;

	protected:
		virtual void	executeAction() const;

	public:
		// Orthodox Canonical Form
		ShrubberyCreationForm();
		ShrubberyCreationForm(const ShrubberyCreationForm &other);
		ShrubberyCreationForm &operator=(const ShrubberyCreationForm &other);
		virtual ~ShrubberyCreationForm();

		// Parameterized Instructor
		ShrubberyCreationForm(const std::string &target);

		// Exceptions
		class FileOpenException : public std::exception
		{
			public:
				virtual const char *what() const throw();
		};
};

#endif
