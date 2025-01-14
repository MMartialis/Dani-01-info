.text
    li x1, 10

loop:
    addi x1, x1, -1
    # do stuff
    bgtz x1, loop

    li a0, 10
    ecall