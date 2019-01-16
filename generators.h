
/* declarations of the fibonacci functions
  fibonacci_gen resets the fibonacci sequence if reset == 1 and returns the next sequence member

  fibonacci calls fibonacci_gen and generates the sequence

  fibonacci_sum gives an option to sum up all odd/even numbers

  fibonacci_slice returns every n-th member of the sequence
*/
int fibonacci_gen(int reset);
int fibonacci(int n);
int fibonacci_sum(int n, int omit);