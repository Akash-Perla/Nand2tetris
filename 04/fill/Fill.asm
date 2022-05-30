// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(BEGIN)      // Loop program forever

@KBD
D=M
@b
D;JNE
@w
D;JEQ

(b)
@counter     // Paint the screen black
M=-1
(LOOP)
@counter
M=M+1
D=M
@SCREEN
A=A+D
M=-1
@8191
D=D-A
@LOOP
D;JNE       // Finish painting the screen black
@BEGIN
0;JMP

(w)
@counterw    // Paint the screen white
M=-1
(LOOPWHITE)
@counterw
M=M+1
D=M
@SCREEN
A=A+D
M=0
@8191
D=D-A
@LOOPWHITE
D;JNE       // Finish painting the screen white

@BEGIN      // Jump back to BEGIN
0;JMP