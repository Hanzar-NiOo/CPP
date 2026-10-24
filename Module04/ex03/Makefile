NAME      := ex03
CXX       := c++
CXXFLAGS := -Wall -Wextra -Werror -std=c++98
SRCS      := src/AMateria.cpp src/Character.cpp src/Cure.cpp src/Ice.cpp src/main.cpp src/MateriaSource.cpp
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
