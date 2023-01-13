// program to print the name of a number
// <date> <name>

#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

#include "numberNames.h"


int main (int argc, char *argv[]) {
   // load number from the command line
   assert (argc > 1);
   int number = atoi (argv[1]);

   // note: this function only works for positive numbers less than 1000
   assert (number >=0); 
   assert (number < 1000);

   // some useful values you might want to use
   int unitsDigit     = number % 10;
   int tensDigit      = (number/10) % 10;
   int hundredsDigit  = number/100 ;
   int lastTwoDigits  = number % 100;

   // display info FYI
   // comment these lines out once the program is working
   printf ("\n");
   printf ("The units digit is %d\n",     unitsDigit);
   printf ("The tens digit is %d\n",      tensDigit);
   printf ("The hundreds digit is %d\n",  hundredsDigit);
   printf ("The last two digits are %d\n",lastTwoDigits);
   printf ("\n");   

   printf ("The number %d is pronounced as ", number);

   // edit the code below and insert new code as required to print out the names of 
   // numbers using ifs

   // don't make it a long sequence of hundreds of if statements!
   // make your code succint clear and with as little repitition as you can 

   // print hundreds part  (write this last - once you have it working for numbers under 100)

   // print the last two digits


   if (unitsDigit == 1) {
         printf (NAME1);
      } else if (unitsDigit == 2) {
         printf (NAME2);
      } else if (unitsDigit == 3) {
         printf (NAME3);
      } else if (unitsDigit == 4) {
         printf (NAME4);
      } else if (unitsDigit == 5) {
         printf (NAME5);
      } else if (unitsDigit == 6) {
         printf (NAME6);
      } else if (unitsDigit == 7) {
         printf (NAME7);
      } else if (unitsDigit == 8) {
         printf (NAME8);
      } else if (unitsDigit == 9) {
         printf (NAME9);
      } else {
         assert ("logic error");
      }

   printf ("\n");
   printf ("\nDone!\n");

   return EXIT_SUCCESS;
}

