# Phụ trách làm việc với file và đường dẫn

import os.path as op

default_file = "hocvien.txt"
file_path = op.abspath(default_file)


def set_file_path():
    global file_path
    print(f"Đường dẫn hiện tại: {file_path}")
    while True:
        input_path = str(input("\nNhập đường dẫn tập tin dữ liệu mới: "))
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
                    if catch_invalid_file(file_path) == "allclear":
                        return
                else:
                    print("\nLỗi: Tập tin không tồn tại!")
                    print("Bạn có muốn tạo một tập tin mới không?")
                    while True:
                        create_new_file_prompt = input("Gõ Y/N: ")
                        if create_new_file_prompt == "Y":
                            create_new_file(input_path)
                            file_path = op.abspath(input_path)
                            return
                        elif create_new_file_prompt == "N":
                            set_file_path()
                            break
                        else:
                            print("Lỗi: Sai cú pháp lệnh.")


def catch_invalid_file(path):
    try:
        file = open(path, "r")
        content = file.readlines()
        danh_sach = []
        catching_invalid_file = []
        for number_of_lines in content:
            line = number_of_lines.split(sep="\n")
            newline = line[0].split(sep="|")
            danh_sach.append(newline)
        for entry in danh_sach:
            catching_invalid_file.append(entry[0])
            catching_invalid_file.append(entry[1])
            catching_invalid_file.append(entry[2])
            catching_invalid_file.append(entry[3])
            catching_invalid_file.append(entry[4])
            catching_invalid_file.append(entry[5])
    except IndexError:
        print("========================================")
        print("Lỗi: Tập tin không đúng định dạng! Hãy chọn tập tin khác.")
        print("Chi tiết về tập tin có định dạng hợp lệ xin đọc 'README.txt'")
        print("========================================")
        set_file_path()
    else:
        return "allclear"


def process_file(command):
    if catch_invalid_file(file_path) == "allclear":
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


def create_new_file(path):
    new_file = open(path, "w")
    new_file.write("22000000|Nguyen Van A|AAAA|10|BBBB|10")
    new_file.close()

    global file_path
    file_path = path
    print(f"\nĐã tạo tập tin mẫu tại {path}.\n\nDùng lệnh 'view' để đọc tập tin, "
          f"'add' để thêm học viên và 'delete' để xoá học viên.\n"
          f"Đừng quên xoá học viên mẫu!")
