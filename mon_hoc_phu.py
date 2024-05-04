import file_handling


def count_mon_hoc_phu(mshv):
    file_content = file_handling.process_file("read")
    danh_sach = []
    for number_of_lines in file_content:
        line = number_of_lines.split(sep="\n")
        newline = line[0].split(sep="|")
        danh_sach.append(newline)

    has_mhp = False
    hvinfo = []
    for entry in danh_sach:
        if len(entry) > 6 and entry[0] == mshv:
            has_mhp = True
            hvinfo.append(entry[0])
            hvinfo.append(entry[1])
            hvinfo.append(entry[2])
            hvinfo.append(entry[3])
            hvinfo.append(entry[4])
            hvinfo.append(entry[5])
            mhp = 6
            d = 7
            smhp = 1
            while mhp < len(entry):
                hvinfo.append(entry[mhp])
                hvinfo.append(entry[d])
                mhp += 2
                d += 2
                smhp += 1
        else:
            continue

    if has_mhp:
        print(f"\nHọc viên: {hvinfo[0]}")
        mhp = 6
        d = 7
        smhp = 1
        while mhp < len(hvinfo):
            print(f"Môn học phụ {smhp}: {hvinfo[mhp]}")
            mhp += 2
            d += 2
            smhp += 1
            return True
    else:
        print(f"\nHọc viên {mshv} không có môn học phụ.")
        return False


def add_mon_hoc_phu():
    print("++++++++++ THÊM MÔN HỌC PHỤ ++++++++++")
    file = file_handling.process_file("read")

    danh_sach = []
    for entry in file:
        line = entry.split(sep="\n")
        info_hoc_vien = line[0].split(sep="|")
        danh_sach.append(info_hoc_vien)

    while True:
        mshv_input = input("Nhập mã số học viên: ")
        flag_trung_lap = False
        for entry in danh_sach:
            if mshv_input == entry[0]:
                flag_trung_lap = True
        if mshv_input == "quit":
            return None
        elif len(mshv_input) == 8 and flag_trung_lap:
            break
        else:
            print("Lỗi: Mã số học viên không hợp lệ!\n")

    found = False

    for entry in file:
        mshv_entry = entry.split(sep="|")
        if mshv_entry[0] == mshv_input:
            found = True
        else:
            continue
    if found:
        count_mon_hoc_phu(mshv_input)

    while True:
        mmhp = str(input("Nhập mã môn học phụ mới (4 chữ cái): "))
        if mmhp == "quit":
            return None
        elif len(mmhp) == 4:
            break
        else:
            print("Lỗi: Mã môn học không hợp lệ!\n")
    while True:
        dmhp = input("Nhập điểm môn học phụ (số nguyên từ 0-10): ")
        if dmhp == "quit":
            return None
        elif dmhp.isdigit() and 0 <= int(dmhp) <= 10:
            break
        else:
            print("Lỗi: Điểm không hợp lệ!\n")

    addition = "|" + mmhp + "|" + dmhp + "\n"
    danh_sach = []
    num = 0
    for entry in file:
        info_hoc_vien = entry.split(sep="|")
        if info_hoc_vien[0] == mshv_input:
            entry = entry.replace("\n", addition)
        num += 1
        danh_sach.append(entry)
    file_modded = file_handling.process_file("write")
    for entries in danh_sach:
        file_modded.write(entries)
    file_modded.close()
    print(f"Thêm môn học phụ {mmhp} cho học viên {mshv_input} thành công.")


def del_mon_hoc_phu():
    print("---------- XOÁ MÔN HỌC PHỤ ----------")
    file = file_handling.process_file("read")

    danh_sach = []
    for entry in file:
        line = entry.split(sep="\n")
        info_hoc_vien = line[0].split(sep="|")
        danh_sach.append(info_hoc_vien)

    while True:
        mshv_input = input("Nhập mã số học viên: ")
        flag_trung_lap = False
        for entry in danh_sach:
            if mshv_input == entry[0]:
                flag_trung_lap = True
        if mshv_input == "quit":
            return None
        elif len(mshv_input) == 8 and flag_trung_lap:
            break
        else:
            print("Lỗi: Mã số học viên không hợp lệ!\n")

    found = False
    for entry in file:
        mshv_entry = entry.split(sep="|")
        if mshv_entry[0] == mshv_input:
            found = True
        else:
            continue
    if found:
        count_mon_hoc_phu(mshv_input)

    while True:
        mmhp = str(input("Nhập mã môn học phụ cần XOÁ (4 chữ cái): "))
        if mmhp == "quit":
            return None
        elif len(mmhp) == 4:
            break
        else:
            print("Lỗi: Mã môn học không hợp lệ!\n")

    hoc_vien = ""
    danh_sach = []

    for entry in file:
        if mmhp in entry:
            hoc_vien = entry.split(sep="|")
            hoc_vien[-1].replace("\n", "")
            count = 0
            while count < len(hoc_vien):
                if hoc_vien[count] == mmhp:
                    hoc_vien.pop(count)
                    hoc_vien.pop(count)
                    break
                else:
                    count += 1
            if "\n" not in hoc_vien[-1]:
                hoc_vien[-1] = hoc_vien[-1] + "\n"
            new = "|".join(hoc_vien)
            danh_sach.append(new)
        else:
            danh_sach.append(entry)

    if hoc_vien == "":
        print(f"Lỗi: Không tìm thấy môn học phụ {mmhp} của học viên!")
    else:
        file_modded = file_handling.process_file("write")
        for entry in danh_sach:
            file_modded.write(entry)
        file_modded.close()
        print(f"Xoá môn học phụ {mmhp} cho học viên {mshv_input} thành công.")


def ma_mhp():
    mhp_so = int(input("Xem điểm môn học phụ số: "))
    mhp_ma = input("Mã môn học phụ: ")

    file = file_handling.process_file("read")

    danh_sach = []
    for entry in file:
        line = entry.split(sep="\n")
        info_hoc_vien = line[0].split(sep="|")
        danh_sach.append(info_hoc_vien)

    index_mmhp = 6
    index_dmhp = 7
    count = 1
    while count < int(mhp_so):
        index_mmhp += 2
        index_dmhp += 2
        count += 1

    data = []
    for entry in danh_sach:
        if len(entry) >= index_dmhp and entry[index_mmhp] == mhp_ma:
            add = entry[0] + "|" + entry[1] + "|" + entry[index_mmhp] + "|" + entry[index_dmhp]
            add = add.split(sep="|")
            data.append(add)
    if not data:
        print(f"Thông báo: Học viên không có môn học phụ số {mhp_so} theo mã {mhp_ma}.")
    else:
        import table_draw as td
        td.table_draw("mhp", data)


def diem_mhp():
    file = file_handling.process_file("read")

    danh_sach = []
    for entry in file:
        line = entry.split(sep="\n")
        info_hoc_vien = line[0].split(sep="|")
        danh_sach.append(info_hoc_vien)

    while True:
        mshv = input("\nNhập mã số học viên cần xem điểm: ")
        found = False
        for hocvien in danh_sach:
            if mshv in hocvien[0]:
                found = True
                if count_mon_hoc_phu(mshv):
                    mhp_so = int(input("\nXem điểm môn học phụ số: "))

                    index_mmhp = 6
                    index_dmhp = 7
                    count = 1
                    while count < int(mhp_so):
                        index_mmhp += 2
                        index_dmhp += 2
                        count += 1
                    data = []
                    for entry in danh_sach:
                        if len(entry) >= index_dmhp and entry[0] == mshv:
                            add = entry[0] + "|" + entry[1] + "|" + entry[index_mmhp] + "|" + entry[index_dmhp]
                            add = add.split(sep="|")
                            data.append(add)
                    if not data:
                        print(f"Thông báo: Học viên không có môn học phụ số {mhp_so}.")
                    else:
                        import table_draw as td
                        td.table_draw("mhp", data)
                        return
                else:
                    return
        if mshv == "quit":
            return
        elif not found:
            print(f"Lỗi: Không tìm thấy học viên {mshv}!")
