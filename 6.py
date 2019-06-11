# 定义变量 types_of_people
types_of_people = 10
# 定义变量x x中引用 types_of_people
x = f"There are {types_of_people} types of people."

# 定义变量 binary
binary = "binary"
# 定义变量 do_not
do_not = "don't"
# 定义变量y，引用了binary和do_not
y = f"Those who know {binary} and those who {do_not}"

# 输出变量x
print(x)
# 输出变量y
print(y)

# 变量x插入到输出中
print(f"I said:{x}")
# 变量y插入到输出中
print(f"I also said:'{y}'")

# format引用变量方法
hilarious = "False"
joke_evaluation = "Isn't that joke so funny?!{}"
print(joke_evaluation.format(hilarious))

#字符串拼接 
w = "This is the left side of..."
e = "a string with a right side"

print(w + e)