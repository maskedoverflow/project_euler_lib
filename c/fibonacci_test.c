#include "generators.h"
#include <stdio.h>

//prints out the first 10 fibonacci values
//expected result: 1 2 3 5 8 13 21 34 55

int main(int argc, char **argv)
{
  for (int i = 1; i < 10; i++)
  {
    printf("Fibnoacci no.%i: %li\n", i, fibonacci_gen(0, 100));
  }

  fibonacci_gen(1, 100);
  printf("Resetting.\n\n");

  for (int i = 1; i < 10; i++)
  {
    printf("Fibnoacci no.%i: %li\n", i, fibonacci_gen(0, 100));
  }

  printf("Testing fibonacci_slicee.\n\n");

  long_array *array = fibonacci_slice(2, 10);
  for (int i = 0; i < array->count_length; i++) {
    printf("%li;", array->extension[i]);
  }
  free(array);

    printf("Testing fibonacci_sum.\n\n");

    printf("%li\n\n", fibonacci_sum(10, 2));


    printf("Testing on real example: \n\n");
    fibonacci_gen(1, 4000000);
    long temp = 0;   
    long sum = 0;
    while ((temp = fibonacci_gen(0, 4000000)) != -1) {
    //   printf("temp: %li\n", temp);
      sum += temp % 2 ? 0 : temp;
    }

    printf("%li\n", sum);

  return 0;
}