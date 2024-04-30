# Phụ trách làm việc với file và đường dẫn

import os.path as op

default_file = "hocvien.dat"
file_path = op.abspath(default_file)


def set_file_path():
    global file_path
    print(f"Đường dẫn hiện tại: {file_path}\n")
    while True:
        input_path = str(input("Nhập đường dẫn tập tin dữ liệu mới: "))
        if input_path == "quit":
            break
        else:
            if input_path == "":
                file_path = op.abspath(default_file)
                print("Đường dẫn đã chọn:", file_path)
                print("\nDanh sách", file_path, "đã mở.")
                break
            else:
                if op.exists(op.abspath(input_path)):
                    file_path = op.abspath(input_path)
                    print("Đường dẫn đã chọn:", file_path)
                    print("\nDanh sách", file_path, "đã mở.")
                    break
                else:
                    print("Lỗi: Tập tin không tồn tại!\n")


def process_file(command):
    while True:
        if op.exists(op.abspath(file_path)):
            if command == "read":
                file = open(file_path, "r")
                content = file.readlines()
                return content
            elif command == "write":
                file = open(file_path, "w")
                return file
            elif command == "append":
                file = open(file_path, "a")
                return file
        else:
            print("Lỗi: Tập tin không tồn tại! Xin hãy thay đổi đường dẫn đến tập tin.")
            set_file_path()
