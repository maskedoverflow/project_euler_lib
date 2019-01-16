CC = gcc
LINKER = gcc
CFLAGS = -Wall # -Werror -Wpointer-arith -Wfatal-errors
DEBUG = -g

sum.o: sum.c sum.h
	$(CC) -c $(CFLAGS) $(DEBUG) -o $@ $<

fibonacci_test.o: fibonacci_test.c 
	$(CC) -c $(CFLAGS) $(DEBUG) -o $@ $<

generators.o: generators.c generators.h
	$(CC) -c $(CFLAGS) $(DEBUG) -o $@ $< 

fibonacci_test: fibonacci_test.o generators.o sum.o
	$(LINKER) $(CFLAGS) $(DEBUG) -o $@ fibonacci_test.o generators.o sum.o

clean:
	rm -f *.o *.dSYM 
	ls | grep -v "\." | grep -v Makefile | xargs rm