# Phụ trách việc xoá học viên

import file_handling


def xoa_hoc_vien():
    print("[ - Xoá học viên - ]")
    file_hoc_vien = open(file_handling.get_file_path(), "r")
    danh_sach = file_hoc_vien.readlines()
    file_path = file_hoc_vien.name

    found = False
    mshv_input = input("Nhập mã số học viên để xoá: ")

    if mshv_input == "quit":
        return None
    else:
        for entry in danh_sach:
            mshv_entry = entry.split(sep="|")

            if mshv_entry[0] == mshv_input:
                print(f"\nĐã tìm thấy {mshv_input}.")
                danh_sach.remove(entry)
                found = True
                file_hoc_vien.close()
            else:
                continue
        if found:
            print(f"\nBạn có chắc chắn muốn xoá học viên {mshv_input} không?")
            delete_confirmation = input("Gõ Y để xoá, N để huỷ: ")
            if delete_confirmation == "Y":
                file_modded = open(file_path, "w")
                for entries in danh_sach:
                    file_modded.write(entries)
                file_modded.close()
                print("\nĐã xoá", mshv_input, "khỏi danh sách.")
            elif delete_confirmation == "N":
                print("\nĐã huỷ xoá.")
        elif not found:
            print("\nKhông thể tìm thấy mã số học viên", mshv_input, "trong danh sách.")
