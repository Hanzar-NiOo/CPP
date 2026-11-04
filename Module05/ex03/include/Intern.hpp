#ifndef INTERN_HPP
# define INTERN_HPP

# include <string>

class AForm;

class Intern
{
private:
	static AForm	*createShrubbery(const std::string &target);
	static AForm	*createRobotomy(const std::string &target);
	static AForm	*createPardon(const std::string &target);

public:
	// Orthodox Canonical Form
	Intern();
	Intern(const Intern &other);
	Intern &operator=(const Intern &other);
	~Intern();

	AForm	*makeForm(const std::string &formName,
				const std::string &target) const;
};

#endif
