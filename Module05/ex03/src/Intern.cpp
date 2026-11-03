#include "Intern.hpp"
#include "AForm.hpp"
#include "ShrubberyCreationForm.hpp"
#include "RobotomyRequestForm.hpp"
#include "PresidentialPardonForm.hpp"
#include <cstddef>
#include <iostream>

Intern::Intern()
{
}

// The intern has no attributes, so there is nothing to copy.
Intern::Intern(const Intern &other)
{
	(void)other;
}

Intern &Intern::operator=(const Intern &other)
{
	(void)other;
	return (*this);
}

Intern::~Intern()
{
}

AForm *Intern::createShrubbery(const std::string &target)
{
	return (new ShrubberyCreationForm(target));
}

AForm *Intern::createRobotomy(const std::string &target)
{
	return (new RobotomyRequestForm(target));
}

AForm *Intern::createPardon(const std::string &target)
{
	return (new PresidentialPardonForm(target));
}

AForm *Intern::makeForm(const std::string &formName,
	const std::string &target) const
{
	// Lookup table: a form name paired with the function that builds it.
	// Supporting a new form means adding one line here.
	struct FormEntry
	{
		const char	*name;
		AForm		*(*create)(const std::string &);
	};
	static const FormEntry	table[] = {
		{"shrubbery creation", &Intern::createShrubbery},
		{"robotomy request", &Intern::createRobotomy},
		{"presidential pardon", &Intern::createPardon}
	};
	const std::size_t	count = sizeof(table) / sizeof(table[0]);

	for (std::size_t i = 0; i < count; i++)
	{
		if (formName == table[i].name)
		{
			std::cout << "Intern creates " << formName << std::endl;
			return (table[i].create(target));
		}
	}
	std::cout << "Intern cannot create \"" << formName
		<< "\": this form name does not exist" << std::endl;
	return (NULL);
}
