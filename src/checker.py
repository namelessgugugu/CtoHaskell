class CChecker:
    def __init__(self, gcc_path):
        """
        Create a C syntax checker.

        Parameters:
            gcc_path - path of gcc.
        """
        pass

    def check(self, code):
        """
        Check whether code is grammatically correct.

        Parameters:
            code - C code.
        
        Returns:
            If code passes the check, None is returned,
            otherwise a string of error message is returned.
        """

class HaskellChecker:
    def __init__(self, ghc_path):
        """
        Create a Haskell syntax checker.

        Parameters:
            ghc_path - path of ghc.
        """
        pass

    def check(self, code):
        """
        Check whether code is grammatically correct.

        Parameters:
            code - Haskell code.
        
        Returns:
            If code passes the check, None is returned,
            otherwise a string of error message is returned.
        """
        pass