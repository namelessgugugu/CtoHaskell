# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# 关键路径配置（根据实际项目结构调整）
PROJECT_ROOT = '.'  # 项目根目录
CONFIG_DIR = 'config'  # 配置文件目录
PROMPT_DIR = 'prompt'  # 提示文件目录

# 主分析配置
a = Analysis(
    ['src/main.py'],  # 主入口文件路径
    pathex=[PROJECT_ROOT],
    binaries=[
        # 显式打包所有外部工具（关键修复）
        ('external/fake_libc_include', 'fake_libc_include')
    ],
    
    # 必须包含的数据文件（解决FileNotFoundError核心配置）
    datas=[
        (f'{CONFIG_DIR}/*.json', CONFIG_DIR),  # 打包所有配置文件
        (f'{PROMPT_DIR}/*', PROMPT_DIR),       # 打包所有提示文件
        
        # 如果存在其他资源文件也要显式添加，例如：
        # ('assets/*.png', 'assets'),
    ],
    
    hiddenimports=[],  # 需要手动指定的隐藏导入
    hookspath=[],
    runtime_hooks=[],
    excludes=[],  # 可排除不必要的包减小体积
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# 可执行文件配置
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# 打包成单个EXE（推荐调试用）
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='main',  # 输出EXE名称
    debug=True,   # 调试模式（正式发布可设为False）
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,     # 使用UPX压缩（需安装）
    console=True,  # 显示控制台（GUI程序改为False）
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# # 可选：打包成文件夹形式（发布时更推荐）
# coll = COLLECT(
#     exe,
#     a.binaries,
#     a.zipfiles,
#     a.datas,
#     name='main',  # 输出文件夹名称
#     strip=False,
#     upx=True,
#     upx_exclude=[],
#     append_pkg=False,
# )
