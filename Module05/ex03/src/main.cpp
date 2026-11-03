#include <cstdlib>
#include <ctime>
#include "Bureaucrat.hpp"
#include "AForm.hpp"
#include "Intern.hpp"

static void	printTitle(const std::string &title)
{
	std::cout << std::endl << "=== " << title << " ===" << std::endl;
}

int	main(void)
{
	std::srand(std::time(NULL));

	printTitle("Test 1: example from the subject (robotomy request, Bender)");
	{
		Intern	someRandomIntern;
		AForm	*rrf;

		rrf = someRandomIntern.makeForm("robotomy request", "Bender");
		if (rrf)
			std::cout << *rrf << std::endl;
		delete rrf;
	}

	printTitle("Test 2: the three valid form names");
	{
		Intern		intern;
		const char	*names[3] = {"shrubbery creation", "robotomy request",
			"presidential pardon"};
		AForm		*forms[3];

		for (int i = 0; i < 3; i++)
		{
			forms[i] = intern.makeForm(names[i], "target");
			if (forms[i])
				std::cout << *forms[i] << std::endl;
		}
		for (int i = 0; i < 3; i++)
			delete forms[i];
	}

	printTitle("Test 3: unknown form name returns NULL");
	{
		Intern	intern;
		AForm	*f = intern.makeForm("coffee order", "Bob");

		std::cout << "returned pointer is "
			<< (f == NULL ? "NULL" : "NOT NULL") << std::endl;
		delete f;
	}

	printTitle("Test 4: edge cases (empty, wrong case, extra space)");
	{
		Intern	intern;
		AForm	*a = intern.makeForm("", "Bob");
		AForm	*b = intern.makeForm("Robotomy Request", "Bob");
		AForm	*c = intern.makeForm("robotomy request ", "Bob");

		delete a;
		delete b;
		delete c;
	}

	printTitle("Test 5: full workflow, intern builds, bureaucrat signs + executes");
	{
		Intern		intern;
		Bureaucrat	boss("Boss", 1);
		AForm		*form = intern.makeForm("presidential pardon", "Arthur Dent");

		if (form)
		{
			boss.signForm(*form);
			boss.executeForm(*form);
		}
		delete form;
	}

	printTitle("Test 6: intern's form is checked like any other (low grade)");
	{
		Intern		intern;
		Bureaucrat	clerk("Clerk", 100);
		AForm		*form = intern.makeForm("presidential pardon", "Marvin");

		if (form)
		{
			clerk.signForm(*form);
			clerk.executeForm(*form);
		}
		delete form;
	}

	printTitle("Test 7: shrubbery created by the intern writes the file");
	{
		Intern		intern;
		Bureaucrat	gardener("Gardener", 100);
		AForm		*form = intern.makeForm("shrubbery creation", "intern_test");

		if (form)
		{
			gardener.signForm(*form);
			gardener.executeForm(*form);
		}
		delete form;
	}

	printTitle("Test 8: copy constructor and assignment of Intern");
	{
		Intern	a;
		Intern	b(a);
		Intern	c;
		AForm	*f;

		c = a;
		f = b.makeForm("robotomy request", "Copy");
		delete f;
		f = c.makeForm("robotomy request", "Assigned");
		delete f;
	}

	return (0);
}
