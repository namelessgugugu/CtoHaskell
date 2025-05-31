# Proprocess C code, seperate it into 3 parts

from .checker import CChecker

from pycparser import parse_file, c_generator
from pycparser.c_ast import *
from pycparser.plyparser import Coord, ParseError

from tempfile import NamedTemporaryFile
from pathlib import Path
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
        self._fake_libc_path = self._resolve_fake_libc_path(fake_libc_path)
        print("origin fake_libc_path : "+ str(fake_libc_path))
        print("fake_libc_path : "+ str(self._fake_libc_path))
        self._c_checker = CChecker(gcc_path)
        self._c_generator = c_generator.CGenerator()

    def _resolve_fake_libc_path(self, manual_path):
        if manual_path and Path(manual_path).exists():
            return str(Path(manual_path).resolve())
        
        possible_paths = [
            Path(getattr(sys, '_MEIPASS', '')) / "fake_libc_include",
            Path(__file__).parent.parent / "external" / "fake_libc_include",
            Path(__file__).parent.parent.parent / "external" / "fake_libc_include"
        ]
        
        for path in possible_paths:
            if path.exists():
                return str(path.resolve())
        
        raise FileNotFoundError(
            f"Cannot locate fake_libc_include. Tried:\n" +
            "\n".join(f"- {p}" for p in possible_paths)
        )

    def preprocess(self, code):
        """
        Preprocess C code to split global varibles and other function.

        Parameters:
            code - C code to be preprocessed.

        Returns:
            head_files - a list of head file included by code.
            global_varibles - a list of global varible declarations in code.
            other - other part of the code.
        
        Raises:
            CGrammarError - code is not a valid C code.
            ParseError - code cannot be parsed by pycparser.
        """
        check_result = self._c_checker.check(code)
        if check_result is not None:
            raise check_result
        
        with NamedTemporaryFile(
            mode = "w+",
            suffix = ".c",
            encoding = "utf-8",
            delete = False
        ) as cache:
            cache.write(code)
            cache.flush()
            cache_name = Path(cache.name)
        
        try:    
            ast = parse_file(
                filename = cache_name,
                use_cpp = True,
                cpp_path = self._gcc_path,
                cpp_args= ["-E", "-I" + self._fake_libc_path]
            )
            head_files = []
            global_varibles = []
            other = ""
            for node in ast.ext:
                source_file = Path(node.coord.file)
                if cache_name.samefile(source_file):
                    node_type = type(node)
                    segment = self._c_generator.visit(node)
                    if node_type is Decl:
                        global_varibles.append(segment)
                    elif node_type is DeclList:
                        global_varibles.append(segment)
                    else:
                        other += segment + "\n"
                else:
                    head_file = str(source_file.relative_to(self._fake_libc_path))
                    if not head_file.startswith("_fake"):
                        head_files.append(head_file)
        finally:
            os.remove(cache_name)
        other = other.strip()
        return (head_files, global_varibles, other)