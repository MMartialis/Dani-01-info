.text
    li x1, 10          # 10 is "put" into x1 register

loop:                  # Label
    addi x1, x1, -1     # We "put" x1-1 into x1 register which is now 9
                     # do stuff  (this is what we would want to do 10 times)        
    bgtz x1, loop       # return to loop as long as x1 is bigger then 0

    li a0, 10         # when x1 is no longer bigger then 0 the program ends here
    ecall