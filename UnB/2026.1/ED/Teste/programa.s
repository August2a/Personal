	.file	"programa.c"
# GNU C17 (Ubuntu 13.3.0-6ubuntu2~24.04) version 13.3.0 (x86_64-linux-gnu)
#	compiled by GNU C version 13.3.0, GMP version 6.3.0, MPFR version 4.2.1, MPC version 1.3.1, isl version isl-0.26-GMP

# GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
# options passed: -mtune=generic -march=x86-64 -O0 -fasynchronous-unwind-tables -fstack-protector-strong -fstack-clash-protection -fcf-protection
	.text
	.globl	soma
	.type	soma, @function
soma:
.LFB0:
	.cfi_startproc
	endbr64	
	pushq	%rbp	#
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp	#,
	.cfi_def_cfa_register 6
	movl	%edi, -4(%rbp)	# a, a
	movl	%esi, -8(%rbp)	# b, b
# programa.c:4:     return a + b;
	movl	-4(%rbp), %edx	# a, tmp84
	movl	-8(%rbp), %eax	# b, tmp85
	addl	%edx, %eax	# tmp84, _3
# programa.c:5: }
	popq	%rbp	#
	.cfi_def_cfa 7, 8
	ret	
	.cfi_endproc
.LFE0:
	.size	soma, .-soma
	.section	.rodata
.LC0:
	.string	"Resultado: %d\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB1:
	.cfi_startproc
	endbr64	
	pushq	%rbp	#
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp	#,
	.cfi_def_cfa_register 6
	subq	$16, %rsp	#,
# programa.c:8:     int x = 10;
	movl	$10, -12(%rbp)	#, x
# programa.c:9:     int y = 20;
	movl	$20, -8(%rbp)	#, y
# programa.c:10:     int resultado = soma(x, y);
	movl	-8(%rbp), %edx	# y, tmp84
	movl	-12(%rbp), %eax	# x, tmp85
	movl	%edx, %esi	# tmp84,
	movl	%eax, %edi	# tmp85,
	call	soma	#
	movl	%eax, -4(%rbp)	# tmp86, resultado
# programa.c:11:     printf("Resultado: %d\n", resultado);
	movl	-4(%rbp), %eax	# resultado, tmp87
	movl	%eax, %esi	# tmp87,
	leaq	.LC0(%rip), %rax	#, tmp88
	movq	%rax, %rdi	# tmp88,
	movl	$0, %eax	#,
	call	printf@PLT	#
# programa.c:12:     return 0;
	movl	$0, %eax	#, _7
# programa.c:13: }
	leave	
	.cfi_def_cfa 7, 8
	ret	
	.cfi_endproc
.LFE1:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	1f - 0f
	.long	4f - 1f
	.long	5
0:
	.string	"GNU"
1:
	.align 8
	.long	0xc0000002
	.long	3f - 2f
2:
	.long	0x3
3:
	.align 8
4:
