#ifndef	PHONEBOOK_HPP
# define PHONEBOOK_HPP

#include "Contact.hpp"

class	PhoneBook
{
	private :
		Contact	contacts[8];
		int		count;
		int		oldestIndex;

	public	:
		PhoneBook();
		void	add_contact();
		void    save_contact(const std::string &fName, const std::string &lName,
            const std::string &ncName, const std::string &phNum,
            const std::string &darkSide);
		void    print_contacts(int search_idx) const;
		void    search_contact(int search_idx);
};

#endif
