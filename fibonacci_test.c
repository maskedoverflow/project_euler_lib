#include "generators.h"
#include <stdio.h>

int main(void) {
  for (int i = 1; i < 5; i++){
    printf("Fibnoacci no.%i: %li\n", i, fibonacci_gen(0));
  }

  return 0;
}