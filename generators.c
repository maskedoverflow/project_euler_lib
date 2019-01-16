#include "generators.h"

int fibonacci_gen(int reset)
{
  static unsigned long first = 1;
  static unsigned long second = 1;

  if (reset) {
    first = 1;
    second = 1;
  }

  unsigned long temp = first + second;
  second = first;
  return first = temp;      
}