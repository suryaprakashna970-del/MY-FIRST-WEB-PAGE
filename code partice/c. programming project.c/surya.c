#include<stdio.h>
int main() 
{ int x = 10; // Variable outside the inner block 
	{ int y = 20; // Variable local to this block 	
	printf("Inside block: x = %d, y = %d\n", x, y); 
	}
	

printf("Outside block: x = %d\n", x); 
return 0; 
}
