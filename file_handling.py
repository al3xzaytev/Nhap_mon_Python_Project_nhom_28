def file_path():
    default_file = "hocvien.dat"

    file_path = str(input("Nhập đường dẫn file: "))

    if file_path == "":
        file_path = default_file
    print("Đường dẫn đã chọn:", file_path)
    return file_path
