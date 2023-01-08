
// Simple program to print a knock knock joke
// 6 Jan 2023 Aaditya Rai
#include <stdlib.h>
#include <stdio.h>

#define NUM_VERSES 3


int main (int arc, char** argv) {
   int i;
   int triangleNumber;
   i = 1; 
   while (i <= 10) {
      triangleNumber = triangleNumber + i;
      printf("%d\n", triangleNumber);
      i++;
   }

   

   return EXIT_SUCCESS;
}


