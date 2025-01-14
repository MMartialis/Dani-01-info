#def factorial(a:int)->int:
#    if a <= 0:
#        return 0
#    return(a + factorial(a-1))

#print("The fact is: ", factorial(4) )


#def fib(a:int)->int:
#    if a == 1 or a == 2: 
#        return 1
#    return(fib(a-1) + fib(a-2))

#print("The 10th element is:", fib(10))


#def pir(a:int)->int:
#    if a <= 0:
#        return 0
#    return(a + pir(a-1))

#h=5
#for i in range(h):
#    for _ in range(i):
#        print(" ", end="")
#    for _ in range(((h-i)*2)-1):
#        print("⬤", end="")
#    print()



def recpir(h:int, s:int=1):
    if s <= h:
        for _ in range(s-1):
            print(" ", end="")

        for _ in range((h-(s-1))*2-1):
            print("⬤", end="")
        print() 
        recpir(h, s+1)
    else:
       return False 



recpir (5)