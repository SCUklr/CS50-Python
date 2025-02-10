user_input = input("请输入问候语")
user_input = user_input.lower()
user_input = user_input.strip(" ")

if user_input.startswith("hello"):
    print("$0")
elif user_input.startswith("h"):
    print("$20")
else:
    print("$100")
