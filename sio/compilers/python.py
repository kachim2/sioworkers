from __future__ import absolute_import
import os.path

from sio.compilers.common import Compiler
from sio.workers.util import tempcwd


class PYCompiler(Compiler):
    lang = 'python'
    output_file = 'a'

    def _make_cmdline(self, executor):
        # Additional sources are automatically included
        return ['pyinstaller', 'a.py'] + self.options + list(self.extra_compilation_args)

    @classmethod
    def pycmp(cls):
        obj = cls('python3.11.2-numpy_amd64')
        obj.options = ['--onefile', '-o', 'a']
        return obj


def run_py_default(environ):
    return FPCCompiler.pycmp().compile(environ)




run_py_default = run_py_default
