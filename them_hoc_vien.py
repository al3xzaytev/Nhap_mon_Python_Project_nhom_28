# Phụ trách việc thêm học viên

import file_handling


def them_hoc_vien():
    print("[ + Thêm học viên + ]")
    file = open(file_handling.get_file_path(), 'a')

    print("\nNhập thông tin học viên.")

    while True:
        mshv = input("Nhập mã số học viên: ")
        if mshv == "quit":
            return None
        elif len(mshv) == 8:
            break
        else:
            print("Lỗi: Mã số học viên không hợp lệ!\n")

    hthv = str(input("Nhập họ tên học viên (không dấu): "))
    if hthv == "quit":
        return None

    while True:
        mmh1 = str(input("Nhập mã môn học 1 (4 chữ cái): "))
        if mmh1 == "quit":
            return None
        elif len(mmh1) == 4:
            break
        else:
            print("Lỗi: Mã môn học không hợp lệ!\n")

    while True:
        dm1 = input("Nhập điểm môn học 1 (số nguyên từ 0-10): ")
        if dm1 == "quit":
            return None
        elif dm1.isdigit() and 0 <= int(dm1) <= 10:
            break
        else:
            print("Lỗi: Điểm không hợp lệ!\n")

    while True:
        mmh2 = str(input("Nhập mã môn học 2 (4 chữ cái): "))
        if mmh2 == "quit":
            return None
        elif len(mmh2) == 4:
            break
        else:
            print("Lỗi: Mã môn học không hợp lệ!\n")

    while True:
        dm2 = input("Nhập điểm môn học 2 (số nguyên từ 0-10): ")
        if dm2 == "quit":
            return None
        elif dm2.isdigit() and 0 <= int(dm2) <= 10:
            file.close()
            break
        else:
            print("Lỗi: Điểm không hợp lệ!\n")

    file.write(f"{mshv}|")
    file.write(f"{hthv}|")
    file.write(f"{mmh1}|")
    file.write(f"{dm1}|")
    file.write(f"{mmh2}|")
    file.write(f"{dm2}\n")

    print("Thêm học viên thành công.")
