lychrel: lychrel.o
	gcc -g -O0 -o lychrel lychrel.o

lychrel.o: lychrel.c
	gcc -g -O0 -c -Wall lychrel.c

clean:
	rm lychrel *.o

indent:
	indent -kr -nut -ts4 lychrel.c
