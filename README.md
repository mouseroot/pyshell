# pyshell
Pure python based shell.

## Commands

- ls - List files
- cat - Display contents of file
- cd - Change directory
- help - shows avaliable commands

## Running multiple commands

pyshell allows you to run multiple commands on a single line, all seperated by the ;
an example:
```bash
ls .. ; cat test.txt ; help
```
Output:
```bash
=== ls .. ===
pyshell
apps
config
=== cat test.txt ===
Hello world

=== help ===
ls - list files
cat - display file content
cd - change directory
help - this message
```