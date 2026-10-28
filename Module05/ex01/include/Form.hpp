#ifndef FORM_HPP
# define FORM_HPP

# include <iostream>
# include <string>
# include <exception>

class Bureaucrat;

class Form
{
	private:
		const std::string	_name;
		bool				_signed;
		const int			_gradeToSign;
		const int			_gradeToExecute;

	public:
		// Orthodox Canonical Form
		Form();
		Form(const Form &other);
		Form &operator=(const Form &other);
		~Form();
	
		// Parameterized instructor
		Form(const std::string &name, int gradeToSign, int gradeToExecute);
	
		// Getters
		const std::string	&getName() const;
		bool				getIsSigned() const;
		int					getGradeToSign() const;
		int					getGradeToExecute() const;
	
		void	beSigned(const Bureaucrat &b);
	
		class GradeTooHighException : public std::exception
		{
			public:
				virtual const char *what() const throw();
		};
	
		class GradeTooLowException : public std::exception
		{
			public:
				virtual const char *what() const throw();
		};
};
 
std::ostream &operator<<(std::ostream &os, const Form &f);
 
#endif