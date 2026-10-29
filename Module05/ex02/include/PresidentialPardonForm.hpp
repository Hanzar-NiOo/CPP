#ifndef PRESIDENTIALPARDONFORM_HPP
# define PRESIDENTIALPARDONFORM_HPP

# include <string>
# include <cstdlib>
# include <iostream>
# include "AForm.hpp"

class PresidentialPardonForm : public AForm
{
private:
	std::string	_target;

protected:
	virtual void	executeAction() const;

public:
	// Orthodox Canonical Form
	PresidentialPardonForm();
	PresidentialPardonForm(const PresidentialPardonForm &other);
	PresidentialPardonForm &operator=(const PresidentialPardonForm &other);
	virtual ~PresidentialPardonForm();

	// Parameterized function
	PresidentialPardonForm(const std::string &target);
};

#endif
