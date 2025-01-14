def factorial(a:int)->int:
    if a <= 0:
        return 0
    return(a + factorial(a-1))




print("The fact is: ", factorial(4) )