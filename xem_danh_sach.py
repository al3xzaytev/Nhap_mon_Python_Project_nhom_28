# Phụ trách việc nhập và xử lý đường dẫn

import file_handling

global list_mshv, list_hthv, list_mmh1, list_dm1, list_mmh2, list_dm2

flag_danh_sach = False


def xem_danh_sach():
    global flag_danh_sach
    flag_danh_sach = True

    # Danh sách sẽ theo form dưới đây:
    # MSHV|HTHV|MMH1|DM1|MMH2|DM2|
    file_hoc_vien = open(file_handling.get_file_path(), "r")
    dong = file_hoc_vien.readlines()

    global list_mshv, list_hthv, list_mmh1, list_dm1, list_mmh2, list_dm2

    list_mshv = []
    list_hthv = []
    list_mmh1 = []
    list_dm1 = []
    list_mmh2 = []
    list_dm2 = []

    for number_of_lines in dong:
        danh_sach = number_of_lines.split(sep="|")
        list_mshv.append(danh_sach[0])
        list_hthv.append(danh_sach[1])
        list_mmh1.append(danh_sach[2])
        list_dm1.append(danh_sach[3])
        list_mmh2.append(danh_sach[4])
        list_dm2.append(danh_sach[5])

    import table_draw as tr
    tr.table_draw()
    flag_danh_sach = False
