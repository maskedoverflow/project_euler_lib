#if !defined(GENERATORS_H)
#define GENERATORS_H

#include <stdlib.h>
#include <limits.h>
#include "types.h"
/* declarations of the fibonacci functions
  fibonacci_gen resets the fibonacci sequence if reset == 1 and returns the next sequence member

  fibonacci calls fibonacci_gen and generates the sequence

  fibonacci_sum gives an option to sum up all odd/even numbers

  fibonacci_slice returns every n-th member of the sequence
*/
long fibonacci_gen(int reset, unsigned long threshold);
long fibonacci(int n);
long fibonacci_sum(int n, int omit_every);
long_array *fibonacci_slice(int slicee, int n);


#endif // GENERATORS_H