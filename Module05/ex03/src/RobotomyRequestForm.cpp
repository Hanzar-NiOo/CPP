#include "RobotomyRequestForm.hpp"

// OCF
RobotomyRequestForm::RobotomyRequestForm()
	: AForm("RobotomyRequestForm", 72, 45), _target("default")
{
}

RobotomyRequestForm::RobotomyRequestForm(const RobotomyRequestForm &other)
	: AForm(other), _target(other._target)
{
}

RobotomyRequestForm &RobotomyRequestForm::operator=(
	const RobotomyRequestForm &other)
{
	if (this != &other)
	{
		AForm::operator=(other);
		this->_target = other._target;
	}
	return (*this);
}

RobotomyRequestForm::~RobotomyRequestForm()
{
}

// Parameterized Instructor
RobotomyRequestForm::RobotomyRequestForm(const std::string &target)
	: AForm("RobotomyRequestForm", 72, 45), _target(target)
{
}

// Member function
void RobotomyRequestForm::executeAction() const
{
	std::cout << "* BZZZZT... DRRRRRR... VRRRRRRR... *" << std::endl;
	if (std::rand() % 2)
		std::cout << this->_target << " has been robotomized successfully"
			<< std::endl;
	else
		std::cout << "the robotomy of " << this->_target << " failed"
			<< std::endl;
}
