// solutions in the 4x4 challenge
// <the date here> <your name here>
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <math.h>

// change this to be your and your name
#define MINE "Aadi's"

int main (int arc, char *argv[]) {
   int sum0;   // this variable is to store the solution to your sum which makes 0
   int sum1;   // this variable is to store the solution to your sum which makes 1
   int sum2;   // and so on...
   int sum3;
   int sum4;
   int sum5;
   int sum6;
   int sum7;
   int sum8;
   int sum9;

   printf("Welcome to %s version of the Four Fours problem. Here goes:\n", MINE);

 // solve the first few cases, you do the rest
   sum0 = (4-4)+(4-4);
   sum1 = 44 / 44;
   sum2 = (4/4) + (4/4);
   sum3 = (4+4+4)/4;
   sum4 = 4 + (44%4);   // you can fix this
   sum5 = ((4*4) + 4)/4;   // you can fix this
   sum6 = (4+4+4)/Math.sqrt(4);   // you can fix this
   sum7 = (44/4) - 4;   // you can fix this
   sum8 = (4*4) + (-4-4) ;   // you can fix this
   sum9 = (4+4) + 4/4;   // you can fix this


   // print the first five sums, one at a time
   printf("%d, ", sum0);
   printf("%d, ", sum1);
   printf("%d, ", sum2);
   printf("%d, ", sum3);
   printf("%d\n",  sum4);

   // or printf also lets you print like this - the second five printed all in one program line
   printf("%d, %d, %d, %d, %d\n", sum5, sum6, sum7, sum8, sum9);

   // test that the correct answers are being produced
   assert (sum0 == 0);
   assert (sum1 == 1);
   assert (sum2 == 2);
   assert (sum3 == 3);
   assert (sum4 == 4);
   assert (sum5 == 5);
   assert (sum6 == 6);
   assert (sum7 == 7);
   assert (sum8 == 8);

   // if you make it this far you have passed the first nine tests

   printf ("All tests 0-9 passed!  Well done.  You are awesome!");

   return EXIT_SUCCESS;
}
