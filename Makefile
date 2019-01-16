CC = gcc
LINKER = gcc
CFLAGS = -Wall # -Werror -Wpointer-arith -Wfatal-errors
DEBUG = -g

fibonacci_test.o: fibonacci_test.c generators.o
	$(CC) -c $(CFLAGS) $(DEBUG) -o $@ $<

generators.o: generators.c generators.h
	$(CC) -c $(CFLAGS) $(DEBUG) -o $@ $< 

fibonacci_test: fibonacci_test.o generators.o 
	$(LINKER) $(CFLAGS) $(DEBUG) -o $@ fibonacci_test.o generators.o 

clean:
	rm -f *.o *.dSYM 
	ls | grep -v "\." | xargs rm !("Makefile")