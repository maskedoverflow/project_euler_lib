#include "factorization.h"

long brutal_teardown(unsigned long long number, unsigned long long factor)
{
  if (number < factor) 
    return factor;
  if (number % factor)
    return brutal_teardown(number, factor + 1);
  else
    return brutal_teardown(number / factor, factor);
}

long biggest_factor(unsigned long long number)
{
  return brutal_teardown(number, 2ULL);
}