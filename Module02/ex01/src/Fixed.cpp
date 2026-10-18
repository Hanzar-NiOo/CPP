#include "Fixed.hpp"

Fixed::Fixed( void ) : _value( 0 )
{
	std::cout << "Default constructor called" << std::endl;
}

Fixed::Fixed( int const n ) : _value( n << _fractionalBits )
{
	std::cout << "Int constructor called" << std::endl;
}

Fixed::Fixed( float const f )
	: _value( static_cast<int>( roundf( f * ( 1 << _fractionalBits ) ) ) )
{
	std::cout << "Float constructor called" << std::endl;
}

Fixed::Fixed( Fixed const & src )
{
	std::cout << "Copy constructor called" << std::endl;
	*this = src;
}

Fixed & Fixed::operator=( Fixed const & rhs )
{
	std::cout << "Copy assignment operator called" << std::endl;
	if ( this != &rhs )
		this->_value = rhs.getRawBits();
	return *this;
}

Fixed::~Fixed( void )
{
	std::cout << "Destructor called" << std::endl;
}

int	Fixed::getRawBits( void ) const
{
	return this->_value;
}

void	Fixed::setRawBits( int const raw )
{
	this->_value = raw;
}

float	Fixed::toFloat( void ) const
{
	return static_cast<float>( this->_value ) / ( 1 << _fractionalBits );
}

int	Fixed::toInt( void ) const
{
	return this->_value >> _fractionalBits;
}

std::ostream &	operator<<( std::ostream & o, Fixed const & rhs )
{
	o << rhs.toFloat();
	return o;
}
