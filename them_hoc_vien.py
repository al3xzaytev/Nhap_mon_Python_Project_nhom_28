import file_handling


def them_hoc_vien():
    print("[ + Thêm học viên + ]")
    file = open(file_handling.file_path(), 'a')

    print("\nNhập thông tin học viên.")

    mshv = int(input("Nhập mã số học viên: "))
    file.write(f"{mshv}|")

    hthv = str(input("Nhập họ tên học viên (không dấu): "))
    file.write(f"{hthv}|")

    mmh1 = str(input("Nhập mã môn học 1 (4 chữ cái): "))
    file.write(f"{mmh1}|")

    dm1 = int(input("Nhập điểm môn học 1 (số nguyên từ 0-10):"))
    file.write(f"{dm1}|")

    mmh2 = str(input("Nhập mã môn học 2 (4 chữ cái): "))
    file.write(f"{mmh2}|")

    dm2 = int(input("Nhập điểm môn học 2 (số nguyên từ 0-10):"))
    file.write(f"{dm2}|\n")
    file.close()

    import main as m
    m.main()
