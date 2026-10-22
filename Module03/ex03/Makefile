NAME      := ex02
CXX       := c++
CXXFLAGS := -Wall -Wextra -Werror -std=c++98
SRCS      := src/ClapTrap.cpp src/main.cpp src/ScavTrap.cpp src/FragTrap.cpp
OBJS      := $(SRCS:.cpp=.o)

all: $(NAME)

$(NAME): $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) -o $(NAME)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -I include -c $< -o $@

clean:
	rm -f $(OBJS) $(NAME)

re: clean all

.PHONY: all clean re
