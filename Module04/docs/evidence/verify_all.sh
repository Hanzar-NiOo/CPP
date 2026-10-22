#!/bin/bash
# Strict compilation + sanitizer verification for every Module 04 exercise.
set -u
cd /mnt/d/42/CPP/Module04
FAIL=0
for d in ex00 ex01 ex02 ex03; do
  echo "================ $d ================"
  ( cd "$d"
    make clean >/dev/null 2>&1
    make >/dev/null 2>&1 || { echo "  PLAIN BUILD FAILED"; FAIL=1; continue; }
    echo "  plain build            : OK"
    g++ -Wall -Wextra -Werror -Wshadow -pedantic -std=c++98 -I include \
        src/*.cpp -o /tmp/m04/strict_$d 2>/tmp/m04/strict_$d.log
    if [ $? -eq 0 ]; then echo "  -Wshadow -pedantic     : OK"
    else echo "  -Wshadow -pedantic     : FAILED"; cat /tmp/m04/strict_$d.log; FAIL=1; fi
    g++ -Wall -Wextra -Werror -std=c++98 -fsanitize=address,undefined -I include \
        src/*.cpp -o /tmp/m04/asan_$d 2>/dev/null
    if [ $? -ne 0 ]; then echo "  sanitizer build        : FAILED"; FAIL=1; continue; fi
    /tmp/m04/asan_$d >/tmp/m04/asan_$d.out 2>&1
    rc=$?
    if [ $rc -eq 0 ] && ! grep -qE "ERROR: (AddressSanitizer|LeakSanitizer)|runtime error" /tmp/m04/asan_$d.out; then
      echo "  asan+ubsan run          : OK (exit 0, no report)"
    else
      echo "  asan+ubsan run          : FAILED (exit $rc)"; FAIL=1
      grep -E "ERROR|runtime error" /tmp/m04/asan_$d.out | head -5
    fi )
done
echo "========================================"
[ $FAIL -eq 0 ] && echo "ALL CHECKS PASSED" || echo "SOME CHECKS FAILED"
exit $FAIL
