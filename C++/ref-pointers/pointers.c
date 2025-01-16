#include <stdio.h>

void passByRef(int* numberaddress){
    printf("Global variable is stored at: %p \n", numberaddress); 
    printf("Global variable is: %d \n", *numberaddress); 
    *numberaddress = *numberaddress *2;   //amire mutat a pointer az szor 2

}

int passByValueI(int x){
    x = x*2;
    return x; 
}


void main(){
    int n = 5;
    printf("The number is : %d \n", n);

    int* address = &n;
     printf("The numbers address is : %p", address); 

    printf("The number stored at address %p is : %d \n", address, *address); 


    int cicus;
    printf("How many cicus are there?: ");
    scanf("%d", &cicus);    //cicusra mutato pointert hasznalva rakja bele a global variable be
    printf("There are %d kittens.", cicus);


    int numb = 10;
    printf("The number is: %d \n", numb);
    passByRef(&numb);        // called he function and give it the pointer to the numb
    printf("The number after the function ran is: %d \n", numb);

    printf("Now the number is %d ", passByValueI(numb)); 
    numb = passByValueI(numb);
    printf("Now the number is %d ", numb); 

}