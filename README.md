## CtoHaskell

从 C 语言到 Haskell 语言的转换器，基于大语言模型。

## 暂定框架

`assistant.py`：提供与 LLM 对话的接口。
`checker.py`：接入 GCC 与 GHC，做语法检查。
`preprocessor.py`：预处理 C 代码，提取全局变量。
`translator.py`：将 C 代码翻译到 Haskell 代码。
`optimizer.py`：对 Haskell 代码进行优化。
`verifier.py`：对 C 代码和 Haskell 代码进行对比。
`ui.py`：用户界面。

## 备注

### 测试

使用 pytest 进行单元测试。

用法为在 tests 文件夹下创建以 `test_` 开头的文件，编写以 `test_` 开头的函数，一般每个源代码模块对应一个测试文件。

测试函数不需要输入参数与返回值，以是否不抛出异常作为是否通过的标准。

如欲测试某代码是否正确抛出异常，则用 `with pytest.raises(xxxError):` 包裹，表示该部分代码应抛出错误 `xxxError`。

在项目根目录运行 `python -m pytest` 以运行测试。