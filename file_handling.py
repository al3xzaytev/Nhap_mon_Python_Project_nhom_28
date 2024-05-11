# Phụ trách làm việc với file và đường dẫn

import os.path as op

# Đọc đường dẫn file trong path.txt
path_file_path = str(open("path.txt", "r").read())
file_path = op.abspath(path_file_path)
default_file = "DATAPYTHON\hocvien.txt"


def write_file_path(path):  # Lưu đường dẫn file vào path.txt
    path_file_config = open("path.txt", "w")
    path_file_config.write(path)


def set_file_path():  # Gọi hàm này khi người dùng cần gõ đường dẫn mới
    global file_path
    global default_file
    print(f"Đường dẫn hiện tại: {file_path}")
    while True:
        input_path = str(input("\nNhập đường dẫn tập tin dữ liệu mới: "))
        if input_path == "quit":
            return
        else:
            if input_path == "":
                file_path = op.abspath(file_path)
                print("Đường dẫn đã chọn:", file_path)
                print("\nDanh sách", file_path, "đã mở.")
                return
            elif input_path == "default":
                print("Đã thiết lập đường dẫn mặc định:", op.abspath(default_file))
                write_file_path(default_file)
                return
            else:
                if op.exists(op.abspath(input_path)):
                    print("Đường dẫn đã chọn:", input_path)
                    if catch_invalid_file(input_path) == "allclear":
                        file_path = op.abspath(input_path)
                        write_file_path(file_path)
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
                            return
                        elif create_new_file_prompt == "quit":
                            return
                        else:
                            print("Lỗi: Sai cú pháp lệnh.")


def catch_invalid_file(path):  # Kiểm tra xem file dữ liệu có theo định dạng đúng hay không
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
        print("\n========================================")
        print("Lỗi: Tập tin không đúng định dạng! Hãy chọn tập tin khác.")
        print("========================================\n")
        return
    else:
        return "allclear"


def process_file(command):  # Xử lý file - gồm đọc và viết file
    if op.exists(op.abspath(file_path)):
        if catch_invalid_file(file_path) == "allclear":
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
            return
    else:
        print("Lỗi: Tập tin không tồn tại! Xin hãy thay đổi đường dẫn đến tập tin.")
        set_file_path()
        return


def create_new_file(path):  # Dùng cho tính năng tạo file mới khi nhập vào đường dẫn chưa có file sẵn
    new_file = open(path, "w")
    new_file.write("22000000|Nguyen Van A|AAAA|10|BBBB|10")
    new_file.close()

    global file_path
    file_path = path
    write_file_path(file_path)
    print(f"\nĐã tạo tập tin mẫu tại {path}.\n\nDùng lệnh 'view' để đọc tập tin, "
          f"'add' để thêm học viên và 'delete' để xoá học viên.\n"
          f"Đừng quên xoá học viên mẫu!")
    return
