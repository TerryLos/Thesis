.intel_syntax noprefix
push 0x100000
ret


cmp rax,rbx
jz .label
nop
nop

.label:
mov rax,1
