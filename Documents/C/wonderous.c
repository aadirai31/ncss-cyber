

    // program to print wonderous number using functions
    // 7 Jan 23 Richard Buckland (based on an idea by AdP)
     
    #include <stdlib.h>
    #include <stdio.h>
    #include <assert.h>
    #include <string.h>
     
    // return three times the input
    int triple (int x);
    int isEven (int x);
    int half   (int x);
	 int wonderous (int start);
     
    int main (int argc, char *argv[]) {
       assert (argc > 1);
       int start;
       start = atoi (argv[1]);
       printf ("you entered %d\n", start);

		 int length;
		 length = 1;
		 while (length <= 500) {
			 length = wonderous(start);
			 start++;
		 }
     
       return EXIT_SUCCESS;
    }
     
     
     
    // return three times the input
    int triple (int x) {
       int answer;
       answer = 3 * x;
       return answer;
    }
     
    // return true (non zero) if x is even, false (0) if odd
    int isEven (int x) {
       int even;
       even = ((x%2) == 0);
       return even;
    }
     
    // returns half of the input, rounded down if the input is odd
    int half (int x) {
       int answer;
       answer = (x/2);
       return answer;
    }

	 int wonderous (int start) {
		int current;
		int length;
	
		// start the sequence with the number given
		current = start;
		//printf ("%d", current);
		length = 1;
	
		while (current > 1) {
			if (isEven(current)) {
				current = half(current);
			} else {
				current = triple(current) + 1;
			}
			length++;
		}
		printf ("%d: %d \n", start, length);
		return length;
	 }

