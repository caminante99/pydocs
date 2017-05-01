# Py2to3 - ST3 Plugin

Py2to3 translates python 2 to 3, which makes it easier to convert ST2 plugins to ST3. The plugin runs `2to3` on the currently open python file and opens a new diff file to show the changes. The original python file is overwritten and a backup is saved as `file.py.bak`. Errors from `2to3` are printed to the console. The idea is to make it easier to run `2to3` when adapting ST2 plugins to ST3. The command can be run from the command palette using `Python 2to3: Translate Python 2 to 3`.

Feel free to send pull request for other changes that make the ST2 to ST3 conversion easier.
