.intel_syntax noprefix

push 0x150234
call rsp
call [rsp]
mov [rsp+0x4],rsp
add rsp,0x8
jmp rax

push 0x150234
ret

mov rax,0x150234
call rax

