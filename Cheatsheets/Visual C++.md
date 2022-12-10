# Visual C++

## Build Configs

### Program Database
Program Database (PDB) file holds debugging and project state information that allows incremental linking of a Debug configuration of your app. Visual Studios have PDB enabled by default.

The setting for generating PDB file is under ``Linker -> Debugging`.
![](20221130163650.png)

When building it will generate the exe along with the associated pdb. The exe will also have reference to the pbd's file path.
![](20221130163055.png)
![](20221130164804.png)

To disable generating PDB for release, set `Linker -> Debugging -> Generate Debug Info` to `No`.

If pdb is disabled, only the exe is generated during compilation:
![](20221130164846.png)

### Security Checks
![](20221130165820.png)
![](20221130165357.png)


### Optimisations
![](20221130173044.png)

When optimsations are disabled, the deassembled pseudocode has the same code structure as the source code. 
![](20221130173545.png)
![](20221130173602.png)

When optimsations are enabled, the subrountine is combined together as it is only used once.
![](20221130173454.png)
