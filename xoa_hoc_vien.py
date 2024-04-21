# Phụ trách việc xoá học viên

import file_handling


def xoa_hoc_vien():
    print("[ - Xoá học viên. - ]")
    file_hoc_vien = open(file_handling.get_file_path(), "r")
    danh_sach = file_hoc_vien.readlines()
    print(danh_sach)
    while True:
        found = False
        mshv_input = input("Nhập mã số học viên để xoá: ")

        for entry in danh_sach:
            mshv_entry = entry.split(sep="|")

            if mshv_entry[0] == mshv_input:
                print(f"Đã tìm thấy {mshv_input}.")
                danh_sach.remove(entry)
                found = True
            else:
                continue

        if found:
            file_hoc_vien = open(file_handling.get_file_path(), "w")
            for entries in danh_sach:
                file_hoc_vien.write(entries)
            file_hoc_vien.close()
            print("Đã xoá", mshv_input, "khỏi danh sách.")
            import main as m
            m.main()
        elif not found:
            print("Không thể tìm thấy mã số học viên", mshv_input, "trong danh sách.")
            import main as m
            m.main()
