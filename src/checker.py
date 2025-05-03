# Check grammar for C and Haskell code.

from tempfile import NamedTemporaryFile
from pathlib import Path
import os, subprocess

class CGrammarError(ValueError):
    def __init__(self, error_message):
        self.error_message = error_message

class CChecker:
    def __init__(self, gcc_path):
        """
        Create a C syntax checker.

        Parameters:
            gcc_path - path of gcc.
        """
        self._gcc_path = gcc_path

    def check(self, code):
        """
        Check whether code is grammatically correct.

        Parameters:
            code - C code.
        
        Returns:
            If code passes the check, None is returned,
            otherwise CGrammarError(error_message) is **returned**, not raised.
        """
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
            result = subprocess.run(
                [
                    self._gcc_path,
                    "-fsyntax-only",
                    cache_name
                ],
                capture_output = True
            )
            if result.returncode != 0:
                return CGrammarError(
                        result.stderr \
                        .strip() \
                        .decode("utf-8", errors = "replace")
                    )
        finally:
            os.remove(cache_name)
        
        return None

class HaskellGrammarError(ValueError):
    def __init__(self, error_message):
        self.error_message = error_message

class HaskellChecker:
    def __init__(self, ghc_path):
        """
        Create a Haskell syntax checker.

        Parameters:
            ghc_path - path of ghc.
        """
        self._ghc_path = ghc_path

    def check(self, code):
        """
        Check whether code is grammatically correct.

        Parameters:
            code - Haskell code.
        
        Returns:
            If code passes the check, None is returned,
            otherwise HaskellGrammarError(error_message) is **returned**, not raised.
        """
        with NamedTemporaryFile(
                mode = "w+",
                suffix = ".hs",
                encoding = "utf-8",
                delete = False
            ) as cache:
            cache.write(code)
            cache.flush()
            cache_name = Path(cache.name)
        
        try:
            result = subprocess.run(
                [
                    self._ghc_path,
                    "-fno-code",
                    cache_name
                ],
                capture_output = True
            )
            if result.returncode != 0:
                return HaskellGrammarError(
                    result.stderr \
                        .strip() \
                        .decode("utf-8", errors = "replace")
                    )
        finally:
            os.remove(cache_name)
        
        return None