// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

// @i will be counting from R1, when it reaches 0, we jump to the end
@1
D=M //copy R1 into D
@i
M=D // and now M[i] = R1
@2
M=0 //initialize sum to 0
(LOOP)
// if i=0 we break 
@i
D=M //d = i
@END
D; JEQ // if i = 0, break 

// we decrement i and do sum
@1
D=D-A //d=i-1
@i
M=D //i=i-1

@2
D=M
@0
D=D+M //d=R0+SUM
@2
M=D //sum=sum+R0

@LOOP
0;JMP

(END)   
@END
0; JMP