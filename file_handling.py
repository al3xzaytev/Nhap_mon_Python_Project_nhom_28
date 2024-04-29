import os.path


def get_file_path():
    default_file = "hocvien.dat"
    while True:
        file_path = str(input("\nNhập đường dẫn tập tin dữ liệu: "))
        if file_path == "quit":
            import main as m
            m.main()
        else:
            if file_path == "":
                abs_path = os.path.abspath(default_file)
                print("Đường dẫn đã chọn:", abs_path)
                return abs_path
            else:
                abs_path = os.path.abspath(file_path)
                print("Đường dẫn đã chọn:", abs_path)
                if os.path.exists(abs_path):
                    print("Danh sách", abs_path, "đã mở.")
                    return abs_path
                else:
                    print("Lỗi: Tập tin không tồn tại!\n")
