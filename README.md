## CtoHaskell

[仓库链接](https://github.com/namelessgugugu/CtoHaskell)

从 C 语言到 Haskell 语言的转换器，基于大语言模型。

### 部署方法

  1. 下载源码（注意：Github 上的仓库没有 `external/mingw64` 与 `external/ghc-9.6.7`，需自行下载两个编译器），在项目根目录进行后续操作。

  2. 输入 `pip install -r requirement.txt` 安装所需依赖。

  3. 在 `config/general.json` 中配置各项参数，其中 `GCC` 和 `GHC` 应填写 `gcc` 和 `ghc` 的路径。例如 Windows 系统下可填写 `./external/mingw64/bin/gcc.exe` 和 `./external/ghc-9.6.7/bin/ghc.exe`。

  4. 在 `config/secret.json` 中填写硅基流动的 API 密钥。

  5. 输入 `python -m src.main` 运行程序，弹出 GUI 窗口。

  6. 在上方代码框输入 C 语言代码，点击 Convert 按钮转化为 Haskell 代码。

### 打包方法

  1. 在项目根目录输入 `pyinstaller main.spec` 打包得到 `dist` 下的可执行文件 `main`。

  2. 将 `main` 与 `config` 文件夹放置在同一级目录下，填写 `config/general.json` 与 `config/secret.json`（注意：`gcc` 和 `ghc` 需填写绝对路径）。

  3. 运行可执行文件 `main` 即可弹出 GUI 窗口。

