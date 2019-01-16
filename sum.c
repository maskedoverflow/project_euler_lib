#include "sum.h"
//get the sum of all numbers in an array
//the elements being numbers for which addition is defined is a given
long sum(long_array *set_of_numbers)
{
  long sum = 0;
  for (int i = 0; i < set_of_numbers->count_length; i++)
  {
    sum += set_of_numbers->extension[i];            
  }
  return sum;
}