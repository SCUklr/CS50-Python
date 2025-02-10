def name():
    """获取用户收入并去空格和大小写"""
    filename = input("请输入文件名: ").strip().lower()

    # 文件名分割
    a, b, extension = filename.rpartition(".")

    # 匹配
    if extension == "gif":
        print("image/gif")
    elif extension == "jpg" or extension == "jpeg":
        print("image/jpeg")
    elif extension == "png":
        print("image/png")
    elif extension == "pdf":
        print("application/pdf")
    elif extension == "txt":
        print("text/plain")
    elif extension == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")

name()
