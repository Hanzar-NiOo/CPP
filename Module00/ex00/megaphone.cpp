#include <iostream>
#include <cctype>

int	main(int argc, char **argv)
{
	int	arg_idx, idx;

	if (argc == 1 || argv[1][0] == '\0')
		std::cout << "* LOUD AND UNBEARABLE FEEDBACK NOISE *" << std::endl;
	else
	{
		arg_idx = 1;
		while (argv[arg_idx])
		{
			idx = 0;
			while (argv[arg_idx][idx])
			{
				char upper = toupper(argv[arg_idx][idx]);
				std::cout << upper;
				idx++;
			}
			arg_idx++;
		}
		std::cout << std::endl;
	}
	return 0;
}
