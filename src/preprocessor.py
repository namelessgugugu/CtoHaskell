# Proprocess C code, seperate it into 3 parts
from .checker import CChecker

from pycparser import parse_file
from tempfile import NamedTemporaryFile

import os

class Preprocessor:
    def __init__(self, gcc_path, fake_libc_path):
        """
        Create preprocessor of C code.

        Parameters:
            gcc_path - path of gcc.
            fake_libc_path - path of fake_libc_include, used by pycparser.
        """
        self._gcc_path = gcc_path
        self._fake_libc_path = fake_libc_path
        self._c_checker = CChecker(gcc_path)

    def preprocess(self, code):
        """
        Preprocess C code to split global varibles and other function.

        Parameters:
            code - C code to be preprocessed.

        Returns:
            head_file - code of all head 
            global_varibles - code of all global varible declarations in code.
            other - other part of the code.
        """
        with NamedTemporaryFile(
            mode = "w+",
            suffix = ".c",
            encoding = "utf-8",
            delete = False
        ) as cache:
            cache.write(code)
            cache.flush()
            cache_name = cache.name
        
        try:
            pass
        finally:
            os.remove(cache_name)