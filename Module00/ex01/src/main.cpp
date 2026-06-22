#include "../include/Contact.hpp"
#include "../include/PhoneBook.hpp"

int	main(void)
{
	std::string	action;
	std::string	xline(45, 'x');
	int			search_idx;
	PhoneBook	phonebook;

	do
	{
		std::cout << "Action : ";
		std::cin >> action;
		if (action == "ADD")
		{
			phonebook.add_contact();
			std::cout << xline << std::endl;
		}
		else if (action == "SEARCH")
		{
			std::cout << "Index of the contact : ";
			std::cin >> search_idx;
			phonebook.search_contact(search_idx);
			std::cout << xline << std::endl;
		}
		else if (action == "EXIT")
			std::cout << "Program exists." << std::endl;
		else
			std::cout << "Invalid input!" << std::endl;
	} while (action != "EXIT");
	return 0;
}
