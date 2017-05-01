import sublime, sublime_plugin
import subprocess

class Py2to3Command(sublime_plugin.TextCommand):
    def run(self, edit):
        # check syntax
        lang = self.view.settings().get('syntax')
        if not "python" in lang.lower():
            return()
        # save current file
        self.view.run_command('save')
        # get path of current file
        path = self.view.file_name()
        # run 2to3
        PIPE = subprocess.PIPE
        p = subprocess.Popen(['2to3', '-w', path], stdout=PIPE, stderr=PIPE)
        p.wait()
        out, err = p.communicate()
        # print errors to console
        if err != b'':
            print('Python 2to3 Errors')
            print(err.decode("utf-8"))
        # show diff file
        if out != b'':
            window = sublime.active_window()
            window.new_file()
            # add diff to file
            window.active_view().insert(edit, 0, out.decode("utf-8"))
            # change syntax to diff
            window.active_view().set_syntax_file('Packages/Diff/Diff.tmLanguage')
        else:
            sublime.status_message("Py2to3: No changes conducted")