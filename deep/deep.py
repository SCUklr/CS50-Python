user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
user_input = user_input.lower() # 忽略大小写
user_input = user_input.strip(" ") # 去空格
if user_input == "42" or user_input == "forty-two" or user_input == "forty two":
    print("Yes")
else:
    print("No")
