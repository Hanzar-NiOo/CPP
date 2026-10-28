#ifndef BUREAUCRAT_HPP
# define BUREAUCRAT_HPP

# include <iostream>
# include <string>
# include <exception>

class Form;

class Bureaucrat
{
	private:
		const std::string	_name;
		int					_grade;

	public:
		// Orthodox Canonical Form
		Bureaucrat();
		Bureaucrat(const Bureaucrat &other);
		Bureaucrat &operator=(const Bureaucrat &other);
		~Bureaucrat();

		// Parameterized Constructor
		Bureaucrat(const std::string &name, int grade);

		// Getters
		const	std::string	&getName() const;
		int					getGrade() const;

		// Grade modification (1 = highest, 150 = lowest)
		void				incrementGrade();
		void				decrementGrade();

		// New in ex01
		void	signForm(Form &form);

		// Exceptions (no need for Orthodox Canonical Form)
		class GradeTooHighException : public std::exception
		{
			public:
				virtual const char	*what() const throw();
		};

		class GradeTooLowException : public std::exception
		{
			public:
				virtual const char	*what() const throw();
		};
};

std::ostream	&operator<<(std::ostream &os, const Bureaucrat &b);

#endif
