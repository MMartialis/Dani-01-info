.text                   # what I write after this will be executed
    la x1, numbers      # load the address of the numbers array into the x1 register
    lb x2, 0(x1)        # load the first byte of the array into the x2 register

loop:                   # label for the loop
    addi x1, x1, 1      # increment the address in x1
    lb x3, 0(x1)        # load the next byte of the array into the x3 register
    beq x3, x0, end     # if x3 is 0, jump to the end of the program
    add x2, x2, x3      # add the value in x3 to the sum in x2
    j loop              # jump back to the loop


end:                    # label for the end of the program
    li a0, 10           # load the exit code into a0
    ecall               # exit the program

.data # what I write after this will be data
numbers:
    .byte 5, 4, 5, 15, 10, 0 # array of bytes, with a 0 terminator
