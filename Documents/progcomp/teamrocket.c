#include <stdio.h>
#include <stdlib.h>
int main(int argc, char **argv) {
int elements[14] = {
99, 99, 111, 97, 108, 109, 108, 112, 101, 117, 103, 115, 101
};
int count = 0;
while (count < 14) {
printf("%c", elements[count]);
count = count + 2;
}
return EXIT_SUCCESS;
}