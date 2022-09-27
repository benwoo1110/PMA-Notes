# x86 Registers
![](../Images/Basic-Assembly-x86-registers.png)

### EAX
 - Multiplication
 - Return value for function call

### EDX
 - Division

### ESP
 - Current stack pointer

### EBP
 - Base pointer for the current stack frame

### ECX
 - Repeat instructions
 - E.g. counter for loops

### ESI, EDI
 - Index register to store memory address

### EIP
 - Instruction Pointer
 - Holds memory address of next instruction to run

### Status Register (EFLAGS)
| Flag | Description |
| ---- | ----------- |
| ZF | Zero Flag set when operation result is 0 |
| CF | Carry Flag set when operation result cannot be stored |
| SF | Sign Flag set when operation result is negative |
| TF | Trap Flag – set to debug, CPU will single step |

# Data Types
| Id | Name | Size |
| -- | ---- | ---- |
| DB | Byte | 1b |
| DW | Word | 2b |
| DD | Doubleword | 4b |
| DQ | Quadword | 8b |
| DT | Ten bytes | 10b |

# Common Instructions

