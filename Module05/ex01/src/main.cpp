#include "Bureaucrat.hpp"
#include "Form.hpp"

static void	printTitle(const std::string &title)
{
	std::cout << std::endl << "=== " << title << " ===" << std::endl;
}

int	main(void)
{
	printTitle("Test 1: valid Form + operator<<");
	try
	{
		Form	f("Tax", 50, 25);
		std::cout << f << std::endl;
	}
	catch (std::exception &e)
	{
		std::cout << "Unexpected: " << e.what() << std::endl;
	}

	printTitle("Test 2: Form grade 0 -> Form::GradeTooHighException");
	try
	{
		Form	f("Bad", 0, 10);
		std::cout << f << std::endl;
	}
	catch (Form::GradeTooHighException &e)
	{
		std::cout << "Caught: " << e.what() << std::endl;
	}

	printTitle("Test 3: Form execute grade 151 -> Form::GradeTooLowException");
	try
	{
		Form	f("Bad", 10, 151);
		std::cout << f << std::endl;
	}
	catch (Form::GradeTooLowException &e)
	{
		std::cout << "Caught: " << e.what() << std::endl;
	}

	printTitle("Test 4: beSigned directly, grade high enough");
	try
	{
		Bureaucrat	boss("Boss", 10);
		Form		f("Contract", 20, 20);
		std::cout << f << std::endl;
		f.beSigned(boss);
		std::cout << f << std::endl;
	}
	catch (std::exception &e)
	{
		std::cout << "Unexpected: " << e.what() << std::endl;
	}

	printTitle("Test 5: beSigned directly, grade too low");
	try
	{
		Bureaucrat	intern("Intern", 100);
		Form		f("Contract", 20, 20);
		f.beSigned(intern);
		std::cout << "Should not be printed" << std::endl;
	}
	catch (Form::GradeTooLowException &e)
	{
		std::cout << "Caught: " << e.what() << std::endl;
	}

	printTitle("Test 6: signForm success");
	try
	{
		Bureaucrat	boss("Boss", 10);
		Form		f("Contract", 20, 20);
		boss.signForm(f);
		std::cout << f << std::endl;
	}
	catch (std::exception &e)
	{
		std::cout << "Unexpected: " << e.what() << std::endl;
	}

	printTitle("Test 7: signForm failure");
	try
	{
		Bureaucrat	intern("Intern", 100);
		Form		f("Contract", 20, 20);
		intern.signForm(f);
		std::cout << f << std::endl;
	}
	catch (std::exception &e)
	{
		std::cout << "Unexpected: " << e.what() << std::endl;
	}

	printTitle("Test 8: boundary, grade equals required grade");
	try
	{
		Bureaucrat	exact("Exact", 20);
		Form		f("Contract", 20, 20);
		exact.signForm(f);
	}
	catch (std::exception &e)
	{
		std::cout << "Unexpected: " << e.what() << std::endl;
	}

	printTitle("Test 9: copy constructor and assignment");
	try
	{
		Bureaucrat	boss("Boss", 1);
		Form		a("A", 10, 10);
		boss.signForm(a);
		Form		b(a);
		Form		c("C", 99, 99);
		c = a;
		std::cout << "a: " << a << std::endl;
		std::cout << "b: " << b << std::endl;
		std::cout << "c: " << c << std::endl;
	}
	catch (std::exception &e)
	{
		std::cout << "Unexpected: " << e.what() << std::endl;
	}

	return (0);
}
