NAME      := a.out
CXX       := c++
CXXFLAGS := -Wall -Wextra -Werror -std=c++98
SRCS      := $(wildcard *.cpp)
OBJS      := $(SRCS:.cpp=.o)

all: $(NAME)

$(NAME): $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) -o $(NAME)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(NAME)

re: clean all

.PHONY: all clean re
