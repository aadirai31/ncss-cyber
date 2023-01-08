// Simple program to print a knock knock joke
// 6 Jan 2023 Aaditya Rai
#include <stdlib.h>
#include <stdio.h>

int add(int x, int y);
int twice(int x) ;
int main (int arc, char** argv) {
   int answer, temp;
   temp = twice(1);
   temp = add(1, temp);
   answer = twice(temp);
   answer = add(answer, temp);
   answer = add(answer, 1);
   printf("%d\n", answer);
   
   return EXIT_SUCCESS;
}

int add(int x, int y) {
   int answer;
   answer = x + y;
   return answer;
}

int twice(int x) {
   int answer;
   answer = x * 2;
   return answer;
}
