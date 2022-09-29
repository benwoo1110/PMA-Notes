# Anti-Disassembly

## Basic Understanding
 - Sequence of code may have multiple disassembly representation
 - Malware contain invalid code that obscure real functionality
 - Takes advantage of assumptions and limitation of disassembly software

## Defeating Disassembly Algorithms

### Linear Disassembly
 - Iterates over a block of code, disassembling one instruction at a time from top down
 - Uses the size of the disassembled instruction to determine which byte to disassemble next
 - No regard for flow-control instructions
 - Pros:
   - Easier to implement and less processing required
 - Cons:
   - Potentially disassembly too much code:
     - Code is disassembly even if flow-control will only cause a portion of code to be executed
   - unable to distinguish between code and data:
     - Code section of nearly all binaries will also contain data that isn’t instructions

### Flow-Oriented Disassembly
 - Examines each instruction and builds a list of locations to disassemble
 - Problematic code aspects such as pointers, exceptions, and conditional branching

## Anti-Disassembly Techniques
 - Compiler always takes the false branch first

### Jump Instructions with the Same Target
```
jz short near ptr loc_4011C4+1
jnz short near ptr loc_4011C4+1
```
 - `jz loc_512` is followed by `jnz loc_512`
 - Effectively an unconditional `jmp`

### A Jump Instruction with a Constant Condition
 - condition that will always be true/false
 - The "false branch"/"`jmp` instruction" will lead to invalid location

### NOP-ing Out Instructions with IDA Pro
```py
import idaapi

idaapi.CompileLine('static n_key() { RunPythonStatement("nopIt()"); }')
AddHotkey("Alt-N", "n_key")

def nopIt():
    start = ScreenEA()
    end = NextHead(start)
    for ea in range(start, end):
    PatchByte(ea, 0x90)
    Jump(end)
    Refresh()
```

## Obscuring Flow Control

### The Function Pointer Problem
```
mov [ebp+var_4], offset sub_4011C0
push 2Ah
call [ebp+var_4]
```
 - `var_4` will be a reference to `sub_4011C0` but IDA cannot detect it

### Adding Missing Code Cross-References in IDA Pro
```py
AddCodeXref(0x004011DE, 0x004011C0, fl_CF)
AddCodeXref(0x004011EA, 0x004011C0, fl_CF)
```

### Return Pointer Abuse
 - 
 - Prematurely terminate the function
 - Adjust the function boundaries:
   - Place the cursor in IDA Pro inside the function you wish to adjust and press ALT-P

### Misusing Structured Exception Handlers

