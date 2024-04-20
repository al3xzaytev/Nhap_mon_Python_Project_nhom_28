def xoa_hoc_vien():
    print("Xoá học viên.")
    data_file = "hocvien.dat"
    file_hoc_vien = open(data_file, "r")
    dong = file_hoc_vien.readlines()

    while True:
        found = False
        mshv_input = input("Nhập mã số học viên để xoá: ")

        for entry in dong:
            mshv_entry = entry.split(sep="|")

            if mshv_entry[0] == mshv_input:
                print(f"Đã tìm thấy {mshv_input}.")
                dong.remove(entry)
                found = True
            else:
                continue

        if found:
            file_hoc_vien = open(data_file, "w")
            for entries in dong:
                file_hoc_vien.write(entries)
            file_hoc_vien.close()
            print("Đã xoá", mshv_input, "khỏi danh sách.")
        elif not found:
            print("Không thể tìm thấy mã số học viên", mshv_input, "trong danh sách.")
