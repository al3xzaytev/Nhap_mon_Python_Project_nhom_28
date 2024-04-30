# Phụ trách việc xử lý dữ liệu để sắp xếp

import file_handling


def diem_mon(mon_hoc):
    file_hoc_vien = file_handling.process_file("read")

    danh_sach = []
    for number_of_lines in file_hoc_vien:
        line = number_of_lines.split(sep="\n")
        newline = line[0].split(sep="|")
        danh_sach.append(newline)

    if mon_hoc == "dm1":
        danh_sach.sort(key=lambda x: int(x[3]))
        import table_draw as td
        td.table_draw("dm1", danh_sach)

    elif mon_hoc == "dm2":
        danh_sach.sort(key=lambda x: int(x[5]))
        import table_draw as td
        td.table_draw("dm2", danh_sach)


def ma_mon_hoc(mon_hoc):
    file_hoc_vien = file_handling.process_file("read")

    danh_sach = []
    for number_of_lines in file_hoc_vien:
        line = number_of_lines.split(sep="\n")
        newline = line[0].split(sep="|")
        danh_sach.append(newline)

    entry = 0
    if mon_hoc == "mmh1":
        mmh1_input = input("Nhập mã môn học 1 cần xem điểm: ")
        while entry < len(danh_sach):
            if danh_sach[entry][2] != mmh1_input:
                danh_sach.pop(entry)
                entry = 0
            else:
                entry += 1
        if not danh_sach:
            print(f"Lỗi: Không tìm thấy môn học 1 '{mmh1_input}'!")
        else:
            print(f"Bảng điểm cho mã môn học 1 '{mmh1_input}':")
            import table_draw as td
            td.table_draw("mmh1", danh_sach)

    elif mon_hoc == "mmh2":
        mmh2_input = input("Nhập mã môn học 2 cần xem điểm: ")
        while entry < len(danh_sach):
            if danh_sach[entry][4] != mmh2_input:
                danh_sach.pop(entry)
                entry = 0
            else:
                entry += 1

        if not danh_sach:
            print(f"Lỗi: Không tìm thấy môn học 2 '{mmh2_input}'!")
        else:
            print(f"Bảng điểm cho mã môn học 2 '{mmh2_input}':")
            import table_draw as td
            td.table_draw("mmh2", danh_sach)


def diem_so():
    file_hoc_vien = file_handling.process_file("read")

    danh_sach = []
    for number_of_lines in file_hoc_vien:
        line = number_of_lines.split(sep="\n")
        newline = line[0].split(sep="|")
        danh_sach.append(newline)

    danh_sach.sort(key=lambda x: (int(x[3]), int(x[5])))

    import table_draw as td
    td.table_draw("diemso", danh_sach)
