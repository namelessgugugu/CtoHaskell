class Preprocessor:
    def __init__(self, gcc_path, fake_libc_path):
        """
        Create preprocessor of C code.

        Parameters:
            gcc_path - path of gcc.
            fake_libc_path - path of fake_libc_include, used by pycparser.
        """
        pass

    def preprocess(self, code):
        """
        Preprocess C code to split global varibles and other function.

        Parameters:
            code - C code to be preprocessed.

        Returns:
            global_varibles - code of all global varible declarations in code.
            other - other part of the code.
        """
        pass