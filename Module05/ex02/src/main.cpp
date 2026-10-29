#include <cstdlib>
#include <ctime>
#include <fstream>
#include "Bureaucrat.hpp"
#include "AForm.hpp"
#include "ShrubberyCreationForm.hpp"
#include "RobotomyRequestForm.hpp"
#include "PresidentialPardonForm.hpp"

static void	printTitle(const std::string &title)
{
	std::cout << std::endl << "=== " << title << " ===" << std::endl;
}

int	main(void)
{
	std::srand(std::time(NULL));

	printTitle("Test 1: ShrubberyCreationForm, sign + execute");
	{
		Bureaucrat				gardener("Gardener", 130);
		ShrubberyCreationForm	form("home");

		std::cout << form << std::endl;
		gardener.signForm(form);
		gardener.executeForm(form);

		std::ifstream	file("home_shrubbery");
		std::cout << "file home_shrubbery created: "
			<< (file.is_open() ? "yes" : "no") << std::endl;
	}

	printTitle("Test 2: RobotomyRequestForm, 6 attempts (50% each)");
	{
		Bureaucrat			doctor("Doctor", 40);
		RobotomyRequestForm	form("Bender");

		doctor.signForm(form);
		for (int i = 0; i < 6; i++)
			doctor.executeForm(form);
	}

	printTitle("Test 3: PresidentialPardonForm, success");
	{
		Bureaucrat				president("President", 1);
		PresidentialPardonForm	form("Arthur Dent");

		president.signForm(form);
		president.executeForm(form);
	}

	printTitle("Test 4: execute an UNSIGNED form");
	{
		Bureaucrat				president("President", 1);
		PresidentialPardonForm	form("Ford Prefect");

		president.executeForm(form);
		std::cout << form << std::endl;
	}

	printTitle("Test 5: signed, but executor grade too low");
	{
		Bureaucrat				boss("Boss", 1);
		Bureaucrat				clerk("Clerk", 50);
		PresidentialPardonForm	form("Trillian");

		boss.signForm(form);
		clerk.executeForm(form);
	}

	printTitle("Test 6: signer grade too low");
	{
		Bureaucrat				clerk("Clerk", 100);
		PresidentialPardonForm	form("Marvin");

		clerk.signForm(form);
		std::cout << form << std::endl;
	}

	printTitle("Test 7: boundary grades (exactly the required grade)");
	{
		Bureaucrat				exact("Exact", 5);
		PresidentialPardonForm	form("Zaphod");

		exact.signForm(form);
		exact.executeForm(form);
	}

	printTitle("Test 8: polymorphism through AForm* (virtual destructor)");
	{
		Bureaucrat	boss("Boss", 1);
		AForm		*forms[3];

		forms[0] = new ShrubberyCreationForm("garden");
		forms[1] = new RobotomyRequestForm("Wall-E");
		forms[2] = new PresidentialPardonForm("Slartibartfast");
		for (int i = 0; i < 3; i++)
		{
			boss.signForm(*forms[i]);
			boss.executeForm(*forms[i]);
		}
		for (int i = 0; i < 3; i++)
			delete forms[i];
	}

	printTitle("Test 9: copy constructor and assignment");
	{
		Bureaucrat				boss("Boss", 1);
		PresidentialPardonForm	a("Original");
		boss.signForm(a);

		PresidentialPardonForm	b(a);
		PresidentialPardonForm	c("Other");
		c = a;
		std::cout << "a: " << a << std::endl;
		std::cout << "b: " << b << std::endl;
		std::cout << "c: " << c << std::endl;
		boss.executeForm(c);
	}

	return (0);
}
