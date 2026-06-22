#include "../include/Contact.hpp"
#include "../include/PhoneBook.hpp"

PhoneBook::PhoneBook()
{
    count = 0;
    oldestIndex = 0;
}

static std::string truncate(const std::string &str)
{
    if (str.length() > 10)
        return (str.substr(0, 9) + ".");
    return (str);
}

void    PhoneBook::print_contacts(int search_idx) const
{
    std::cout << std::right
			<< std::setw(10) << "Index" << "|"
			<< std::setw(10) << "First name" << "|"
			<< std::setw(10) << "Last name" << "|"
			<< std::setw(10) << "Nickname" << "|"
			<< std::endl;

	std::cout << std::right
			<< std::setw(10) << search_idx << "|"
			<< std::setw(10) << truncate(contacts[search_idx - 1].get_firstname()) << "|"
			<< std::setw(10) << truncate(contacts[search_idx - 1].get_lastname()) << "|"
			<< std::setw(10) << truncate(contacts[search_idx - 1].get_nickname()) << "|"
			<< std::endl;
}

void    PhoneBook::search_contact(int	search_idx)
{
    if (count == 0)
    {
        std::cout << "Phonebook is empty." << std::endl;
        return ;
    }
	else if (search_idx > 8 || search_idx > count || search_idx <= 0)
	{
		std::cout << "The requested index is unavilable." << std::endl;
		return ;
	}
    print_contacts(search_idx);
}

static void	get_input(std::string content, std::string &input)
{
	while (true)
	{
		std::cout << content;
		std::getline(std::cin, input);
		if (input.empty())
			std::cout << "The input value must not be empty." << std::endl;
		else
		{
			bool is_all_whitespace = true;
			for (unsigned char ch : input) 
            {
                if (!std::isspace(ch)) 
                {
                    is_all_whitespace = false;
                    break;
                }
            }
			if (is_all_whitespace) 
            {
                std::cout << "Invalid input. Please try again." << std::endl;
            }
            else 
                break;
		}
	}
}

void    PhoneBook::save_contact(const std::string &fName, const std::string &lName,
            const std::string &ncName, const std::string &phNum,
            const std::string &darkSide)
{
    if (count < 8)
    {
        contacts[count].set_contact(fName, lName, ncName, phNum, darkSide);
        count++;
    }
    else
    {
        contacts[oldestIndex].set_contact(fName, lName, ncName, phNum, darkSide);
        oldestIndex++;
        if (oldestIndex == 8)
            oldestIndex = 0;
    }
	std::cout << "New contact is saved successfully." << std::endl;
}

void	PhoneBook::add_contact()
{
	Contact		contact;
	std::string	fName;
	std::string	lName;
	std::string	ncName;
	std::string	phNum;
	std::string	darkSide;

	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	get_input("First Name : ", fName);
	get_input("Last Name : ", lName);
	get_input("Nickname : ", ncName);
	get_input("Phone-number : ", phNum);
	get_input("Darkside : ", darkSide);
	save_contact(fName, lName, ncName, phNum, darkSide);
}
