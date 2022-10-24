# Anti-Debugging

## Windows Debugger Detection

### Using the Windows API
 - In-built functions designed for debugger detection
 - Other functions repurposed to detect a debugger

`IsDebuggerPresent` - Searches the Process Environment Block (PEB) for attached debugger

`CheckRemoteDebuggerPresent` - Check if a given process has debugger present

`NtQueryInformationProcess`

`OutputDebugString`

### Manually Checking Structures


#### BeingDebugged Flag

#### ProcessHeap Flag

#### NTGlobalFlag

### Checking for System Residue

## Identifying Debugger Behavior