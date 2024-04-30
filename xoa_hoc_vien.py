# Phụ trách việc xoá học viên

import file_handling


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
