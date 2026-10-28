#include "Bureaucrat.hpp"

static void	printTitle(const std::string &title)
{
	std::cout << std::endl << "=== " << title << " ===" << std::endl;
}

int	main(void)
{
	printTitle("Test 1: valid construction + operator<<");
	try
	{
		Bureaucrat	a("Alice", 42);
		std::cout << a << std::endl;
		std::cout << "Name : " << a.getName() << std::endl;
		std::cout << "Grade: " << a.getGrade() << std::endl;
	}
	catch (std::exception &e)
	{
		std::cout << "Unexpected exception: " << e.what() << std::endl;
	}

	printTitle("Test 2: grade 0 -> GradeTooHighException");
	try
	{
		Bureaucrat	b("Bob", 0);
		std::cout << b << std::endl;
	}
	catch (Bureaucrat::GradeTooHighException &e)
	{
		std::cout << "Caught GradeTooHighException: " << e.what() << std::endl;
	}

	printTitle("Test 3: grade 151 -> GradeTooLowException");
	try
	{
		Bureaucrat	c("Carl", 151);
		std::cout << c << std::endl;
	}
	catch (Bureaucrat::GradeTooLowException &e)
	{
		std::cout << "Caught GradeTooLowException: " << e.what() << std::endl;
	}

	printTitle("Test 4: negative grade, caught as std::exception");
	try
	{
		Bureaucrat	d("Dave", -5);
		std::cout << d << std::endl;
	}
	catch (std::exception &e)
	{
		std::cout << "Caught std::exception: " << e.what() << std::endl;
	}

	printTitle("Test 5: incrementGrade (3 -> 2 -> 1 -> exception)");
	try
	{
		Bureaucrat	e("Eve", 3);
		std::cout << e << std::endl;
		e.incrementGrade();
		std::cout << e << std::endl;
		e.incrementGrade();
		std::cout << e << std::endl;
		e.incrementGrade();
		std::cout << "Should not be printed: " << e << std::endl;
	}
	catch (std::exception &e)
	{
		std::cout << "Caught: " << e.what() << std::endl;
	}

	printTitle("Test 6: decrementGrade (148 -> 149 -> 150 -> exception)");
	try
	{
		Bureaucrat	f("Frank", 148);
		std::cout << f << std::endl;
		f.decrementGrade();
		std::cout << f << std::endl;
		f.decrementGrade();
		std::cout << f << std::endl;
		f.decrementGrade();
		std::cout << "Should not be printed: " << f << std::endl;
	}
	catch (std::exception &e)
	{
		std::cout << "Caught: " << e.what() << std::endl;
	}

	printTitle("Test 7: boundary values 1 and 150 are valid");
	try
	{
		Bureaucrat	top("Top", 1);
		Bureaucrat	bottom("Bottom", 150);
		std::cout << top << std::endl;
		std::cout << bottom << std::endl;
	}
	catch (std::exception &e)
	{
		std::cout << "Unexpected exception: " << e.what() << std::endl;
	}

	printTitle("Test 8: copy constructor and assignment");
	try
	{
		Bureaucrat	g("Grace", 10);
		Bureaucrat	h(g);
		Bureaucrat	i("Ivan", 100);

		std::cout << "g: " << g << std::endl;
		std::cout << "h (copy of g): " << h << std::endl;
		std::cout << "i before: " << i << std::endl;
		i = g;
		std::cout << "i after i = g: " << i << std::endl;
	}
	catch (std::exception &e)
	{
		std::cout << "Unexpected exception: " << e.what() << std::endl;
	}

	return (0);
}
