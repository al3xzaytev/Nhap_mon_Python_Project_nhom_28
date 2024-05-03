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
            print(f"Môn học phụ {smhp}: {hvinfo[mhp]}, Điểm {hvinfo[d]}")
            mhp += 2
            d += 2
            smhp += 1
    else:
        print(f"\nHọc viên {mshv} không có môn học phụ.")

        # COUNT SOURCE CODE
        # has_mhp = False
        # if len(entry) > 6:
        #     has_mhp = True
        # if has_mhp:
        #     print(f"\nMSHV: {entry[0]}", end=" | ")
        #     mhp = 6
        #     d = 7
        #     smhp = 1
        #     while mhp < len(entry):
        #         print(f"MHP {smhp}: {entry[mhp]}, Điểm {entry[d]}", end=" | ")
        #         mhp += 2
        #         d += 2
        #         smhp += 1
        # else:
        #     print(f"\nMSHV: {entry[0]}", end=" | Không có môn học phụ")


def add_mon_hoc_phu():
    print("===== THÊM MÔN HỌC PHỤ =====")
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
    print(addition)

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
