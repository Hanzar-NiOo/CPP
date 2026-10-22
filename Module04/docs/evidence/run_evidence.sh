#!/bin/bash
# ---------------------------------------------------------------------------
#  Reproduces the three pieces of evidence shown in the Module 04 deck.
#
#    1. static_binding.cpp   -> the call is bound at compile time
#    2. shallow_copy.cpp     -> a shallow copy double-frees the Brain
#    3. abstract_error.cpp   -> the compiler refuses an abstract instance
#
#  Usage :  ./run_evidence.sh
# ---------------------------------------------------------------------------
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
MOD="$(cd "$HERE/../.." && pwd)"
BIN="$HERE/_bin"
mkdir -p "$BIN"

echo "############ 1. static binding (makeSound() is not virtual) ############"
g++ -Wall -Wextra -Werror -std=c++98 "$HERE/static_binding.cpp" -o "$BIN/static_binding" || exit 1
"$BIN/static_binding"
echo

echo "############ 2. shallow copy under AddressSanitizer ####################"
g++ -Wall -Wextra -Werror -std=c++98 -fsanitize=address,undefined \
    "$HERE/shallow_copy.cpp" -o "$BIN/shallow_copy" || exit 1
"$BIN/shallow_copy"
echo "(exit code $?)"
echo

echo "############ 3. instantiating the abstract Animal #####################"
cd "$HERE"
g++ -Wall -Wextra -Werror -std=c++98 -I ../../ex02/include abstract_error.cpp
echo "(the compilation above is expected to FAIL)"
