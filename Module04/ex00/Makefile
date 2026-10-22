NAME      := ex00
CXX       := c++
CXXFLAGS := -Wall -Wextra -Werror -std=c++98
SRCS      := src/Animal.cpp src/Cat.cpp src/Dog.cpp src/WrongAnimal.cpp src/WrongCat.cpp src/main.cpp
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
