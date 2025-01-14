.text 
    mv x1 x0
    mv x2 x0
    mv x3 x0
    mv x4 x0

    la x1, numbers 
    lb x3, 0(x1)
    mv x2, x3  
loop:
    addi x1, x1, 1 
    lb x3, 0(x1)
    add x2, x2, x3
    beq x3, x0, end
    j loop


end: 
    li a0, 10
    ecall 


.data
numbers:
    .byte 22, 34, 59, 78, 0