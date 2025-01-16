#include <stdio.h>
#include <stdbool.h>


bool isVowel(char a){
        return (a == 'a'|| a == 'e' || a == 'i' || a == 'o' || a == 'u');
}
void main(){
    char c = 'e';
   //printf("The letter %c is a vowel: %d",c, isVowel(c));
    if (isVowel(c)){
        printf("The charater %c is a vowel", c);
    }
    else {
        printf("The charater %c is not a vowel", c);
    }
    char word[] = "HelloWorld";
    int count = 0;

    for (int i=0; word[i]!='\0'; i++){
        if (isVowel(word[i])){
            count++;
        }
    }
    printf("There are %i vowels in the word", count);




//    printf("The charater %c", c);
//        if (isVowel(c)){
//            printf(" is ");
//        }
//    else {printf("is not");}
//    printf(" a vowel\n");

}

