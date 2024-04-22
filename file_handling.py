import os.path


def get_file_path():
    default_file = "hocvien.dat"

    while True:
        file_path = str(input("\nNhập đường dẫn file dữ liệu: "))
        abs_path = os.path.abspath(file_path)
        if file_path == "quit":
            import main as m
            m.intro()
        elif file_path == "":
            file_path = default_file
            abs_path = os.path.abspath(file_path)
            print("Đường dẫn đã chọn:", abs_path)
            return abs_path
        else:
            print("Đường dẫn đã chọn:", abs_path)
            if not os.path.exists(abs_path):
                print("File không tồn tại!")
            else:
                print("Danh sách", abs_path, "đã mở.")
                return abs_path
