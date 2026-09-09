"""
sys模块
    python中的sys模块是标准库中用于与python解释器交互的核心模块
    主要是提供访问和操作python运行时环境的功能。
"""
import sys
# 1 获取命令行参数列表
# python sys模块.py 1 2 3 4
print(f"参数列表: {sys.argv}")
print(f"类型: {type(sys.argv)}")
print(f"长度: {len(sys.argv)}")

print()

# 2 退出当前程序
# sys.exit(status)  # 终止当前程序
"""这组状态码并非 Python 语言强制规定，而是沿用类 Unix 系统的通用规范
- 0: 成功
- 1: 通用错误
- 2: 用法错误
- 126: 权限不足
- 127: 命令未找到
"""
# sys.exit退出会抛出一个异常，SystemExit
# sys.exit()
# print("测试sys.exit退出是否还执行这行代码")
# try:
#     sys.exit(1)
# except SystemExit as e:
#     # 资源释放
#     print(e.code)
#     sys.exit()

# 3 标准的输入输出
# sys.stdin - 标准输入流
# sys.stdout - 标准输出流
# sys.stderr - 标准错误流
print(f"标准输入对象: {sys.stdin}")
print(f"标准输出对象: {sys.stdout}")
print(f"标准错误对象: {sys.stderr}")

# 默认指向控制台（终端），print() 本质就是向 sys.stdout 写入内容
print("标准输出print")
sys.stdout.write("标准输出stdout\n")

# 简单说,sys.stdout的默认值就是程序启动时，自动关联的"控制台输出通道", 是print的默认输出目标
sys.stdout = open("output.txt", "w")  # 把标准输出指向打开的文件
print("Hello, Print!")  # 文件写入
sys.stdout.close()  # 记得关闭

# ValueError: I/O operation on closed file.
# 标准输出(文件)关了
# print(123)

# 恢复标准输出到控制台
# sys.__stdout__ 是 python 中标准输出(stdout)的原始文件对象
# 解释器启动的时候保存的stdout初始值，用于在标准输出被重定向之后恢复原始输出
sys.stdout = sys.__stdout__
print("hello, print!")

# 标准输入
# str1 = input("请输入:")
# print(str1)
# 相当于
print("请输入:", end="")
str1 = sys.stdin.readline()
print(str1)

# 错误输出
sys.stderr.write("错误输出stderr")

# sys.path 返回模块搜索路径列表
print(f"搜索路径数量: {len(sys.path)}")
print("搜索路径:")
# enumerate(iterable, start=0)
# enumerate() 是 Python 内置函数，核心作用是遍历可迭代对象（如列表、字符串、元组）时，同时获取「索引」和「元素值」
# iterable：必须是可迭代对象（列表、字符串、元组、字典等）；
# start：可选参数，指定索引的起始值，默认从 0 开始；
# 返回值：一个枚举对象（可迭代），每次迭代返回 (索引, 元素) 形式的元组。
for i, path in enumerate(sys.path, 1):
    print(f"\t{i}.{path}")

print()

# sys.version 返回完整的版本字符串
print(f"python版本: {sys.version}")
# sys.platform返回操作系统平台标识
print(f"当前平台: {sys.platform}")
"""
# 常见平台值：
    'win32'           - Windows 32/64 位
    'linux'           - Linux
    'darwin'          - macOS
    'cygwin'          - Cygwin (Windows 上的 Unix 兼容环境)
"""

# sys.version_info 返回版本信息的元组 (主版本号，次版本号，微版本号，发行级别，版本号)
print(sys.version_info)
print(sys.version_info.major)
print(sys.version_info.minor)
print(sys.version_info.micro)
