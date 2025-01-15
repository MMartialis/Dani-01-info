#include <stdio.h>

void passByVl(int* numbaddress){
    printf("The global variable is: %d, and its address: %p \n", *numbaddress, numbaddress);
    *numbaddress = *numbaddress *2;
    printf("The variable's address is stored on %d bytes\n", sizeof(numbaddress));
    printf("The global variable is stored on %d bytes \n", sizeof(*numbaddress));
}

void passArray(int* arrayaddress, int arraysize){
    printf("The array is %d elements long \n",arraysize);
    for (int i = 0;  i < arraysize; i++ ){
       arrayaddress[i] = arrayaddress[i] *2;
    }

}

void main(){
    int var = 5;
    printf("The variable is: %d \n", var);
    passByVl(&var);
    printf("The variable after the function ran is: %d \n", var);


    int array[] = {1, 2, 3, 4, 5, 6};
    printf("The array before the function is: ");
    for (int i =0; i<sizeof(array)/sizeof(array[0]); i++){
        printf(" %i", array[i]);
    }
    printf("The array after the function ran is: ");
    passArray(array,sizeof(array)/sizeof(array[0]));
    for (int i =0; i<sizeof(array)/sizeof(array[0]); i++){
        printf(" %i", array[i]);
    }



    int array2[8];

}