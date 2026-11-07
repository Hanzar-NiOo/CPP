#ifndef ITER_HPP
# define ITER_HPP

# include <cstddef>

template	<typename T, typename F>
void	iter(T *arr, size_t const len, F func)
{
	for (size_t idx = 0; idx < len; idx++)
		func(arr[idx]);
}

#endif
