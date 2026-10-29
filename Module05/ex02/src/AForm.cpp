#include "AForm.hpp"
#include "Bureaucrat.hpp"

// OCF
AForm::AForm()
	: _name("Default"), _signed(false), _gradeToSign(150), _gradeToExecute(150)
{
}

AForm::AForm(const AForm &other)
	: _name(other._name), _signed(other._signed),
	_gradeToSign(other._gradeToSign), _gradeToExecute(other._gradeToExecute)
{
}

AForm &AForm::operator=(const AForm &other)
{
	if (this != &other)
		this->_signed = other._signed;
	return (*this);
}

AForm::~AForm()
{
}

// Parameterized Instructor
AForm::AForm(const std::string &name, int gradeToSign, int gradeToExecute)
	: _name(name), _signed(false),
	_gradeToSign(gradeToSign), _gradeToExecute(gradeToExecute)
{
	if (gradeToSign < 1 || gradeToExecute < 1)
		throw AForm::GradeTooHighException();
	if (gradeToSign > 150 || gradeToExecute > 150)
		throw AForm::GradeTooLowException();
}

// Getters
const std::string &AForm::getName() const
{
	return (this->_name);
}

bool AForm::getIsSigned() const
{
	return (this->_signed);
}

int AForm::getGradeToSign() const
{
	return (this->_gradeToSign);
}

int AForm::getGradeToExecute() const
{
	return (this->_gradeToExecute);
}

// Member functions
void AForm::beSigned(const Bureaucrat &b)
{
	if (b.getGrade() > this->_gradeToSign)
		throw AForm::GradeTooLowException();
	this->_signed = true;
}

void AForm::execute(const Bureaucrat &executor) const
{
	if (!this->_signed)
		throw AForm::FormNotSignedException();
	if (executor.getGrade() > this->_gradeToExecute)
		throw AForm::GradeTooLowException();
	this->executeAction();
}

// Exceptions
const char *AForm::GradeTooHighException::what() const throw()
{
	return ("grade is too high (highest possible grade is 1)");
}

const char *AForm::GradeTooLowException::what() const throw()
{
	return ("grade is too low");
}

const char *AForm::FormNotSignedException::what() const throw()
{
	return ("the form is not signed");
}

// Insertion operator overload
std::ostream &operator<<(std::ostream &os, const AForm &f)
{
	os << "Form " << f.getName()
		<< " [signed: " << (f.getIsSigned() ? "yes" : "no")
		<< ", grade to sign: " << f.getGradeToSign()
		<< ", grade to execute: " << f.getGradeToExecute() << "]";
	return (os);
}
