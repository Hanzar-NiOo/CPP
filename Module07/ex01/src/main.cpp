#include "iter.hpp"
#include "iostream"

template	<typename T>
void	print(T value)
{
	std::cout << value << std::endl;
}

template	<typename T>
void	increment(T &value)
{
	value++;
}

void	shout(std::string &str)
{
	str += "!";
}

int	main()
{
	// 1. Print an int array
	int arr[] = {0, 1, 2, 4};
	iter(arr, sizeof(arr) / sizeof(arr[0]), print<int>);
	std::cout << std::endl;

	// 2. Modify elements through a non-const reference
	iter(arr, 4, increment<int>);
	iter(arr, 4, print<int>);
	std::cout << std::endl;

	// 3. Different types
	double d[] = {1.5, 2.5, 3.5};
	iter(d, 3, increment<double>);
	iter(d, 3, print<double>);
	std::cout << std::endl;

	std::string s[] = {"a", "b", "c"};
	iter(s, 3, shout);
	iter(s, 3, print<std::string>);
	std::cout << std::endl;

	// 4. Const array with a const-taking function
	int const ca[] = {7, 8, 9};
	iter(ca, 3, print<int>);
	std::cout << std::endl;

	// 5. Edge cases
	iter(arr, 0, print<int>);
	std::cout << "[empty ok]" << std::endl;
	iter(arr + 2, 2, print<int>);
	std::cout << std::endl;

	return 0;
}
