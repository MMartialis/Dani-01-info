#include <stdio.h>
#include <stdlib.h>

int main() {
    const int nb = 10;
    /* alloc space for nb integers */
    void* memAddress = malloc(nb*sizeof(int));  // asks the memory controller to reserve an nb bytes long space in the memory
                                                //, and saves the address to this space in a variable
    // since memAddress is an unknown var type (void), we need to CAST it into an pointer pointing to an INT
    int* p = (int*) memAddress;

    /* pointer p should now have a pointer 
       of a space for nb integers   */
    /* if p contains NULL, something went wrong, probably the computer is out of memory */
    if (p == NULL) { // the computer has no free memory to allocate
        /* exit of program here*/
        return -1;
    }
    for (int i = 0; i < nb; i++) {
        /* the integer p points to is assigned
           to i and p is incremented */
        *p++ = i;  // please note, that i++ first returns with the old value, then increases the variable value with one
    }
    for (int i = 0; i < nb; i++) {
        /* decrement p and then dereferenc */
        printf("%d\n", *(--p));   // --i first decrements the value of p, then reurns with the NEW value
    }
    /* p has now its initial value */
    free(p); // we delete the variable p and free up the memory
    return 0;
}
