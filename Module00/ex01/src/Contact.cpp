#include "../include/Contact.hpp"

void		Contact::set_contact(const std::string &fName, const std::string &lName, const std::string &ncName, const std::string &phNum, const std::string &darkSide)
{
	first_name = fName;
	last_name = lName;
	nickname = ncName;
	ph_number = phNum;
	darkside = darkSide;
}

std::string	Contact::get_firstname() const
{
	return (first_name);
}

std::string	Contact::get_lastname() const
{
	return (last_name);
}

std::string	Contact::get_nickname() const
{
	return (nickname);
}

std::string	Contact::get_phnumber() const
{
	return (ph_number);
}

std::string	Contact::get_darksecret() const
{
	return (darkside);
}
