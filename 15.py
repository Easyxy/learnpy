# 调用参数模块
from sys import argv

# 定义位置参数变量
script,filename = argv

# 使用open打开文件，返回文件对象
txt = open(filename)
#print(txt)

# 读取txt文件并输出到屏幕
print(f"Here's your file {filename}")
#print(txt.read())
print(open(filename).read())
# 手动输入文件名，打开文件并输出
print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())