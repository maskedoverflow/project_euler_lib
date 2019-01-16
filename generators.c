#include "generators.h"

int fibonacci_gen(int reset)
{
  static unsigned long first = 0;
  static unsigned long second = 1;

  if (reset) {
    first = 0;
    second = 1;
  }

  unsigned long temp = first + second;
  first = second;
  return first = temp;      
}