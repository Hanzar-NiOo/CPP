NAME        = sed_is_for_losers

CXX         = c++
CXXFLAGS    = -Wall -Wextra -Werror -std=c++98

SRCS        = src/main.cpp src/Sed.cpp
OBJS        = $(SRCS:.cpp=.o)

all: $(NAME)

$(NAME): $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) -o $(NAME)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -I include -c $< -o $@

clean:
	rm -f $(OBJS)

fclean: clean
	rm -f $(NAME) test*.replace

re: fclean all

# Automated test suite targeting edge cases
test: $(NAME)
	@echo "--- 1. Testing normal replacement ---"
	@echo "Hello world, world!" > test1.txt
	./$(NAME) test1.txt "world" "42"
	@echo "Result:" && cat test1.txt.replace
	@rm -f test1.txt

	@echo "\n--- 2. Testing multiple consecutive occurrences ---"
	@echo "aaaaa" > test2.txt
	./$(NAME) test2.txt "aa" "b"
	@echo "Result:" && cat test2.txt.replace
	@rm -f test2.txt

	@echo "\n--- 3. Testing empty s1 error handling ---"
	@echo "test content" > test3.txt
	./$(NAME) test3.txt "" "replacement" || echo "Caught expected error!"
	@rm -f test3.txt

	@echo "\n--- 4. Testing non-existent file ---"
	./$(NAME) nonexistent_file.txt "a" "b" || echo "Caught expected error!"

	@echo "\n--- 5. Testing incorrect argument count ---"
	./$(NAME) file.txt "a" || echo "Caught expected error!"

.PHONY: all clean fclean re test
