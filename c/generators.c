#include "generators.h"
#include "sum.h"
// A state preserving function that returns the next number in the fibonacci sequence when called
long fibonacci_gen(int reset, unsigned long threshold)
{
  static unsigned long first = 0;
  static unsigned long second = 1;
  static unsigned long max = 0;

  if (threshold) {
    max = threshold;
  }

  if (reset)
  {
    first = 0;
    second = 1;
    return -1;
  }

  unsigned long temp = first + second;
  first = second;
  second = temp;
  return temp < threshold ? temp : fibonacci_gen(1, threshold);
}

//returns the n-th element
long fibonacci(int n)
{
  for (int i = 0; i < n - 1; i++)
  {
    fibonacci_gen(0, INT_MAX);
  }
  long temp = fibonacci_gen(0, INT_MAX);
  fibonacci_gen(1, INT_MAX);
  return temp;
}

long fibonacci_sum(int n, int omit_every) {
    return sum(fibonacci_slice(omit_every, n));
}

//generate the first n elements of fibonacci and then returning an array containing every x-th member of the sequence
long_array *fibonacci_slice(int slicee, int n)
{
  fibonacci_gen(1, INT_MAX);
  long_array *fibs = malloc(sizeof(fibs) + sizeof(long) * (n / slicee));
  fibs->count_length = n / slicee;

  for (int i = 0, k = 0; i < n; i++)
  {
    if (!(i % slicee))
      fibs->extension[k++] = fibonacci_gen(0, INT_MAX);
    else
      fibonacci_gen(0, INT_MAX);
  } 
  fibonacci_gen(1, INT_MAX);
  return fibs;
}