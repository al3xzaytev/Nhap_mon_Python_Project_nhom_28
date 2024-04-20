def xoa_hoc_vien():
    print("Xoá học viên.")
    default_file = "hocvien.dat"

    file_path = str(input("Nhập đường dẫn file:\n>: "))

    if file_path == "":
        file_path = default_file

    print(file_path)
    file_hoc_vien = open(file_path, "r")
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
            file_hoc_vien = open(file_path, "w")
            for entries in dong:
                file_hoc_vien.write(entries)
            file_hoc_vien.close()
            print("Đã xoá", mshv_input, "khỏi danh sách.")
            import main as m
            m.main()
        elif not found:
            print("Không thể tìm thấy mã số học viên", mshv_input, "trong danh sách.")
            import main as m
            m.main()
