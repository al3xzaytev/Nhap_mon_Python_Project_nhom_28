# Phụ trách việc xoá học viên

import file_handling


def xoa_hoc_vien():
    print("[ - Xoá học viên. - ]")
    file_hoc_vien = open(file_handling.get_file_path(), "r")
    danh_sach = file_hoc_vien.readlines()
    file_path = file_hoc_vien.name

    while True:
        found = False
        mshv_input = input("Nhập mã số học viên để xoá: ")

        for entry in danh_sach:
            mshv_entry = entry.split(sep="|")

            if mshv_entry[0] == mshv_input:
                print(f"Đã tìm thấy {mshv_input}.")
                danh_sach.remove(entry)
                found = True
                file_hoc_vien.close()
            else:
                continue

        if found:
            file_modded = open(file_path, "w")
            for entries in danh_sach:
                file_modded.write(entries)
            file_modded.close()
            print("Đã xoá", mshv_input, "khỏi danh sách.")
        elif not found:
            print("Không thể tìm thấy mã số học viên", mshv_input, "trong danh sách.")
