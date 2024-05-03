# Phụ trách việc đọc thông tin học viên cũng như thêm và xóa học viên

import file_handling


def hoc_vien_info():
    file_content = file_handling.process_file("read")
    user_mshv_input = str(input("Nhập mã số học viên: "))
    if user_mshv_input == "quit":
        return
    else:
        found = False
        for entry in file_content:
            dong = entry.split(sep="|")
            if dong[0] == user_mshv_input:
                line = entry.split(sep="\n")
                info_hoc_vien = line[0].split(sep="|")
                found = True
                import table_draw as td
                td.table_draw("hvinfo", info_hoc_vien)
            else:
                continue
        if not found:
            print("\nLỗi: Không tìm thấy học viên!")


def them_hoc_vien():
    print("[ + Thêm học viên + ]")
    file = file_handling.process_file("read")
    danh_sach = []
    for entry in file:
        line = entry.split(sep="\n")
        info_hoc_vien = line[0].split(sep="|")
        danh_sach.append(info_hoc_vien)

    print("\nNhập thông tin học viên.")

    while True:
        mshv = input("Nhập mã số học viên: ")
        flag_trung_lap = False  # Kiểm tra xem mã số học viên có bị trùng không
        for entry in danh_sach:
            if mshv == entry[0]:
                flag_trung_lap = True
        if mshv == "quit":
            return None
        elif len(mshv) == 8 and not flag_trung_lap:
            break
        else:
            print("Lỗi: Mã số học viên không hợp lệ!\n")

    while True:
        hthv = str(input("Nhập họ tên học viên (không dấu): "))
        if hthv == "quit":
            return None
        elif len(hthv) > 30:
            print("Lỗi: Họ tên học viên không thể quá 30 ký tự!\n")
        else:
            break

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
            break
        else:
            print("Lỗi: Điểm không hợp lệ!\n")

    file = file_handling.process_file("append")
    file.write(f"{mshv}|")
    file.write(f"{hthv}|")
    file.write(f"{mmh1}|")
    file.write(f"{dm1}|")
    file.write(f"{mmh2}|")
    file.write(f"{dm2}\n")
    file.close()

    print("Thêm học viên thành công.")


def xoa_hoc_vien():
    print("[ - Xoá học viên - ]")
    file_hoc_vien = file_handling.process_file("read")

    found = False
    mshv_input = input("Nhập mã số học viên để xoá: ")

    if mshv_input == "quit":
        return None
    else:
        for entry in file_hoc_vien:
            mshv_entry = entry.split(sep="|")

            if mshv_entry[0] == mshv_input:
                print(f"\nĐã tìm thấy học viên.")
                print(f"Mã số học viên: {mshv_entry[0]}")
                print(f"Họ tên học viên: {mshv_entry[1]}")
                file_hoc_vien.remove(entry)
                found = True
            else:
                continue
        if found:
            print(f"\nBạn có chắc chắn muốn xoá học viên {mshv_input} không?")
            while True:
                delete_confirmation = input("Gõ Y để xoá, N để huỷ: ")
                if delete_confirmation == "Y" or delete_confirmation == "y":
                    file_modded = file_handling.process_file("write")
                    for entries in file_hoc_vien:
                        file_modded.write(entries)
                    file_modded.close()
                    print("\nĐã xoá", mshv_input, "khỏi danh sách.")
                    break
                elif delete_confirmation == "N" or delete_confirmation == "n":
                    print("\nĐã huỷ xoá.")
                    break
                else:
                    print("Lỗi: Không hợp lệ.\n")
        elif not found:
            print("\nLỗi: Không thể tìm thấy mã số học viên", mshv_input, "trong danh sách.")
