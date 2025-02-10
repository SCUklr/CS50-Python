# 用户输入inout，去空格strip()
user_input = input("请输入四则运算表达式： ").strip()

# x, y, z = user_input.rpartition("") 不能用，只能用split
x, y, z = user_input.split()

# 记得转换str->int
x = int(x)
z = int(z)

# 判断运算符号
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z
else:
    print("ERROR!")

print(fr"{result:.1f}")
