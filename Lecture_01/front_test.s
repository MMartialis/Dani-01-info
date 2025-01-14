.text
    li x1, 10

loop:
    bgtz, x1 end
    addi x1, x1, -1
    # do stuff
    j loop
end:
    li a0, 10
    ecall