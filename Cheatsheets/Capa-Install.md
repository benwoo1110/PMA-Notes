# Capa Install

## 1. Python Requirement
capa explorer supports Python versions >= 3.7.x and the following IDA Pro versions:

| | IDA 7.4 | IDA 7.5 | IDA 7.6 |
| --- | --- | --- | --- |
| Python 3.7.x | Yes | Yes | Yes |
| Python 3.8.x | Partial (see below) | Yes | Yes |
| Python 3.9.x | No | Partial (see below) | Yes |

Install the correct version of python from https://www.python.org/downloads/ before proceeding.

To check and select python version used by IDA Pro, use `idapyswitch.exe` found in IDA install folder.

## 2. Pip Package
```
pip install flare-capa
```

### Pip Installation Offline
Follow these steps if your install location does not have internet access.

1. Using another host with internet access, download the same python version. https://www.python.org/downloads/
2. Create a new folder and open terminal/commandprompt.
3. `pip download flare-capa`
4. Transfer the entire folder to your install location. 
5. `pip install --no-index --find-links flare_capa-4.0.1-py2.py3-none-any.whl`

## 3. Capa-Explorer Plugin
Download [capa_explorer.py](https://raw.githubusercontent.com/mandiant/capa/master/capa/ida/plugin/capa_explorer.py) and copy it to IDA plugins directory.

## 4. Capa Rules
- Direct download: https://github.com/mandiant/capa-rules/archive/refs/heads/v4.zip
- Git clone: `git clone https://github.com/mandiant/capa-rules.git -b v4 /local/path/to/rules`
