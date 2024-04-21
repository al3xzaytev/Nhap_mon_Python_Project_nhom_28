import os.path


def get_file_path():
    default_file = "hocvien.dat"

    while True:
        file_path = str(input("\nNhập đường dẫn file dữ liệu: "))
        if file_path == "quit":
            import main as m
            m.intro()
        elif file_path == "":
            file_path = default_file
            print("Đường dẫn đã chọn:", file_path)
            return file_path
        else:
            print("Đường dẫn đã chọn:", file_path)
            if not os.path.exists(file_path):
                print("File không tồn tại!")
            else:
                print("Danh sách", file_path, "đã mở.")
                return file_path
