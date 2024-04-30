import os.path as op

default_file = "hocvien.dat"
file_path = op.abspath(default_file)


def set_file_path():
    global file_path
    while True:
        print(f"Đường dẫn hiện tại: {file_path}")
        input_path = str(input("\nNhập đường dẫn tập tin dữ liệu mới: "))
        if input_path == "quit":
            import main as m
            m.main()
        else:
            if input_path == "":
                file_path = op.abspath(default_file)
            else:
                print("Đường dẫn đã chọn:", input_path)
                if op.exists(op.abspath(input_path)):
                    file_path = op.abspath(input_path)
                    print("\nDanh sách", file_path, "đã mở.")
                    break
                else:
                    print("Lỗi: Tập tin không tồn tại!\n")


def get_file_path():
    return file_path
