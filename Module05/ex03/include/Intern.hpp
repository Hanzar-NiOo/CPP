#ifndef INTERN_HPP
# define INTERN_HPP

# include <string>

// Forward declaration: this header only uses AForm through a pointer.
class AForm;

class Intern
{
private:
	// One small factory function per form type. makeForm() picks one of them
	// from a lookup table instead of using an if / else if chain.
	static AForm	*createShrubbery(const std::string &target);
	static AForm	*createRobotomy(const std::string &target);
	static AForm	*createPardon(const std::string &target);

public:
	// Orthodox Canonical Form
	Intern();
	Intern(const Intern &other);
	Intern &operator=(const Intern &other);
	~Intern();

	// Returns a new form (the caller must delete it), or NULL if the
	// form name is unknown.
	AForm	*makeForm(const std::string &formName,
				const std::string &target) const;
};

#endif
