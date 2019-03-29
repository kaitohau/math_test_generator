"""
    latexfile.py
"""
import os
import subprocess
import textwrap


class LatexFile:
    PROLOGUE = textwrap.dedent('''\
        \\documentclass[{}pt,dvipdfmx,a4paper]{{article}}
        \\usepackage{{amsmath}}
        \\usepackage{{tgpagella, euler}}
        \\usepackage{{amsmath,multicol,eso-pic}}
        \\evensidemargin 0.0in
        \\oddsidemargin 0.0in
        \\textwidth 6.5in
        \\begin{{document}}\
    ''')

    def __init__(self, fname, title=None, point=10):
        self.title = title
        self.text = []
        self.fname = fname
        self.point = point
        if title is None:
            self.title = ''
        else:
            self.title = '\\title{{{}}} \n\\date{{}} \n\\maketitle'.format(
                title)

    def add_text(self, text):
        self.text.append(text)

    def begin_cols(self):
        self.text.append('\\begin{multicols}{2}\n \\begin{enumerate}\n')

    def end_cols(self):
        self.text.append('\n\\end{enumerate}\n\\end{multicols}')

    def add_eq(self, e):
        self.text.append('\\item\n' + '$' + e + '$\n')

#         self.text.append('\\begin{align*}\n' + equation + '\n\\end{align*}')

    def add_eqs(self, eqs, leftalign=True):
        if leftalign is True:
            self.text.append('\\begin{multicols}{2}\n \\begin{enumerate}\n')
            for e in eqs:
                self.text.append('\\item\n' + '$' + e + '$\n')

            self.text.append('\n\\end{enumerate}\n\\end{multicols}')
        else:
            self.text.append('\\begin{align*}\n' +
                             '\\\\ \n'.join(eqs) + '\n\\end{align*}')

    def output(self):
        res = '\n'.join([
            self.PROLOGUE.format(self.point),
            self.title,
            '\n'.join(self.text),
            '\\end{document}'
        ])
        return res

    def compile(self, remove=True):
        with open(self.fname + '.tex', mode='wt') as fout:
            fout.write(self.output())
        command1 = 'platex {}.tex'.format(self.fname)
        print(command1.split(' '))
        subprocess.run(command1.split(' '))
        command2 = "dvipdfmx {}".format(self.fname)
        print(command2.split(' '))
        subprocess.run(command2.split(' '))
        if remove is True:
            rmv_list = [self.fname + x for x in ('.aux', '.log', '.dvi')]
            for rmv_fname in rmv_list:
                os.remove(rmv_fname)
