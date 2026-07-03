NAME    = "BraiiiiiiinnnzzzZ"
CXX     = c++
CXXFLAGS = -Wall -Werror -Wextra -std=c++98

SRC     =   src/main.cpp  src/Zombie.cpp src/newZombie.cpp src/randomChump.cpp

OBJ     = $(SRC:.cpp=.o)

all: $(NAME)

$(NAME): $(OBJ)
	$(CXX) $(CXXFLAGS) -o $(NAME) $(OBJ)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -I include -c $< -o $@

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
