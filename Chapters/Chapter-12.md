# 12 Convert Malware Launching

## Launchers
 - Setup a piece of malware for convert execution:
   - Executable within loader’s own resource section
   - Extracts an embedded executable or DLL
   - Launch the extracted malware file
   - Possibility encrypted or compressed
   - May perform privilege escalation
 - Resource-manipulation API functions:
   - FindResource
   - LoadResource
   - SizeofResource

## Process Injection
 - Injects code into another running process
 - Win32 calls:
   - VirtualAllocEx - allocate space in anexternal process’s memory
   - WriteProcessMemory - write data to that allocated space

### DLL Injection
 - Remote process forced to load malicious dll
 - Inject code into a remote process that calls LoadLibrary
 - Injection process:
   - CreateToolhelp32Snapshot, Process32First, and Process32Next to search the process list
   - CreateRemoteThread
   - Find starting point to LoadLibrary and the malicious DLL name passed as the argument
   - Use VirtualAllocEx and WriteProcessMemory to write malicious library name string into the memory space

### Direct Injection
 - Injects the malicious code directly into the remote process
 - No new dll is loaded
 - Usually injects compiled code or shellcode
 - Dump all memory buffers that occur before calls to WriteProcessMemory

## Process Replacement
 - Overwrite the memory space of a running process with a malicious executable
 - Same privileges as the process it is replacing
 - Replacement steps:
   - CreateProcess – With CREATE_SUSPENDED flag – Loads process into memory but stops it at the entry point
   -  ZwUnmapViewOfSection – Release all memory of the original process
   - VirtualAllocEx – Allocate new memory for malware
   - WriteProcessMemory – Write malware sections to victim process space
   - SetThreadContext – Set entry point to malicious code
   - ResumeThread – Initiates the malware

## Hook Injection
 - Intercept messages destined for applications

### Local and Remote Hooks
 - Local hooks: Messages destined for internal process
 - Remote hooks: Messages destined for another process on the system
   - High level: Exported function contained in the DLL
   - Low level: Contained in the process that installed the hook

### Keyloggers Using Hooks
 - WH_KEYBOARD:
   - Running in the context of a remote process
   - High level
 - WH_KEYBOARD_LL:
   - Events are sent directly to the process that installed the hook
   - Lower level

### Using SetWindowsHookEx
 - Contain code to process messages
 - Must call CallNextHookEx for next hook procedure in call chain to get the message
 - Parameters:
   - idHook – Type of hook to install
   - lpfn – Pointer to hook procedure
   - hMod – Handle to DLL with hook procedure for high level, local module for low level
   - dwThreadId – Thread with which the hook procedure is to be associated. Set zero for low-level hooks.

### Thread Targeting
 - Only a single thread will be injected in order to remain stealthy
 - Hook with a message that is not often used (e.g. WH_CBT)

## Detours
 - Library to allow for easy instrument and extend existing OS and application functionality
 - Malicious usage:
   - Perform import table modification
   - Attach DLLs to existing program files
   - Add function hooks to running processes
 - .detour section:
   - Contains the original PE header with a new import address table

## APC Injection
 - Asynchronous procedure call (APC)
 - Invoke a function on an existing thread

### User Space
 - Another thread can queue a function to be invoked in a remote thread
 - WaitForSingleObjectEx – Get threads that are in alertable state
 - QueueUserAPC- Request the thread to run function defined by attacker

### Kernel Space
 - Requires rootkit:
   - KeInitializeApc - Initializes a KAPC structure
   - KeInsertQueueApc - Place the APC object in the target thread’s corresponding APC queue
