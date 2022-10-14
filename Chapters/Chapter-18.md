# Packers and Unpacking

## Packer Anatomy
 - Cannot examine the original unpacked program
 - Original executable usually compressed and/or encrypted

### Unpacking Stub
 - Responsible for loading the original program
 - Often small and does not contribute to the main functionality of the program

#### General steps
 1. Unpacks the original executable into memory
 2. Resolves all of the imports of the original executable
 3. Transfers execution to the original entry point (OEP)

### Loading the Executable
 - Allocate memory for each of the executable’s sections based on that header
 - Loader then copies the sections into the allocated spaces in memory

### Resolving Imports

#### Option 1
 - Use of `LoadLibrary` and `GetProcAddress` functions

#### Option 2
 - Keep the original import table intact
 - Static analysis of the packed program will reveal all the original imports

#### Option 3
 - Keep one import function from each DLL
 - Simpler than option 1, as libraries do not need to be loaded by the unpacking stub

#### Option 4
 - Removal of all imports
 - Find all the functions needed from other libraries without using function
 - Find `LoadLibrary` and `GetProcAddress`, and use them to locate all the other libraries
 - No direct reference using import table

### Tail Jump
 - Instruction that transfers execution to the OEP
 - Obscure this function by using a ret or call instruction
 - Use OS functions such as `NtContinue` or `ZwContinue` to hide OEP action


