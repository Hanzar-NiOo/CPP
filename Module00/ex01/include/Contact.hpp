#ifndef CONTACT_HPP
# define CONTACT_HPP

#include <iostream>
#include <string>
#include <limits>
#include <iomanip>
#include <cctype>

class	Contact
{
	private :
		std::string	first_name;
		std::string	last_name;
		std::string	nickname;
		std::string	ph_number;
		std::string	darkside;

	public :
		std::string	get_firstname() const;
		std::string	get_lastname() const;
		std::string	get_nickname() const;
		std::string	get_phnumber() const;
		std::string	get_darksecret() const;
		void		set_contact(const std::string &fName, const std::string &lName, const std::string &ncName, const std::string &phNum, const std::string &darkSide);
};

#endif
