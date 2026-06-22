NAME    = MyAwesomePhoneBook
CXX     = g++
CXXFLAGS = -Wall -Werror -Wextra -std=c++17

SRC     =   src/main.cpp  src/Contact.cpp src/PhoneBook.cpp

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
