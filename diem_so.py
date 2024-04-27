# Phụ trách việc xử lý dữ liệu để sắp xếp

import numpy as np
import file_handling

global np_dm1, np_dm2, np_mshv_sort, np_hthv_sort
global np_dm1_sort, np_dm2_after_dm1_sort
global list_mshv, list_hthv, list_mmh1, list_dm1, list_mmh2, list_dm2

flag_dm1 = False
flag_dm2 = False
flag_diem_so = False
flag_mmh1 = False
flag_mmh2 = False


def dm1():
    global flag_dm1
    flag_dm1 = True
    file_hoc_vien = open(file_handling.get_file_path(), "r")
    dong = file_hoc_vien.readlines()

    global list_mshv, list_hthv, list_dm1
    list_mshv = []
    list_hthv = []
    list_dm1 = []

    for number_of_lines in dong:
        danh_sach = number_of_lines.split(sep="|")
        list_mshv.append(danh_sach[0])
        list_hthv.append(danh_sach[1])
        list_dm1.append(int(danh_sach[3]))

    global np_dm1, np_mshv_sort, np_hthv_sort

    np_mshv = np.array(list_mshv)
    np_hthv = np.array(list_hthv)
    np_dm1 = np.array(list_dm1)

    sort_args = np_dm1.argsort()

    np_dm1 = np_dm1[sort_args]
    np_mshv_sort = np_mshv[sort_args]
    np_hthv_sort = np_hthv[sort_args]

    import table_draw as tr
    tr.table_draw()

    flag_dm1 = False


def dm2():
    global flag_dm2
    flag_dm2 = True

    file_hoc_vien = open(file_handling.get_file_path(), "r")
    dong = file_hoc_vien.readlines()

    global list_mshv, list_hthv, list_dm2

    list_mshv = []
    list_hthv = []
    list_dm2 = []

    for number_of_lines in dong:
        danh_sach = number_of_lines.split(sep="|")
        list_mshv.append(danh_sach[0])
        list_hthv.append(danh_sach[1])
        list_dm2.append(int(danh_sach[5]))

    global np_dm2
    global np_mshv_sort
    global np_hthv_sort

    np_mshv = np.array(list_mshv)
    np_hthv = np.array(list_hthv)
    np_dm2 = np.array(list_dm2)

    sort_args = np_dm2.argsort()

    np_dm2 = np_dm2[sort_args]
    np_mshv_sort = np_mshv[sort_args]
    np_hthv_sort = np_hthv[sort_args]

    import table_draw as tr
    tr.table_draw()

    flag_dm2 = False


def diem_so():
    global flag_diem_so
    flag_diem_so = True
    file_hoc_vien = open(file_handling.get_file_path(), "r")
    dong = file_hoc_vien.readlines()

    global list_mshv, list_hthv, list_dm1, list_dm2
    list_mshv = []
    list_hthv = []
    list_dm1 = []
    list_dm2 = []

    for number_of_lines in dong:
        danh_sach = number_of_lines.split(sep="|")
        list_mshv.append(danh_sach[0])
        list_hthv.append(danh_sach[1])
        list_dm1.append(int(danh_sach[3]))
        list_dm2.append(int(danh_sach[5]))

    global np_mshv_sort, np_hthv_sort, np_dm1_sort, np_dm2_after_dm1_sort
    np_mshv = np.array(list_mshv)
    np_hthv = np.array(list_hthv)
    ds_np_dm1 = np.array(list_dm1)
    ds_np_dm2 = np.array(list_dm2)

    sort_args_dm1 = np.lexsort((ds_np_dm1, ds_np_dm2))
    np_dm1_sort = ds_np_dm1[sort_args_dm1]
    np_mshv_sort = np_mshv[sort_args_dm1]
    np_hthv_sort = np_hthv[sort_args_dm1]
    np_dm2_after_dm1_sort = ds_np_dm2[sort_args_dm1]

    import table_draw as td
    td.table_draw()

    flag_diem_so = False


def mmh1():
    global flag_mmh1
    flag_mmh1 = True
    file_hoc_vien = open(file_handling.get_file_path(), "r")
    dong = file_hoc_vien.readlines()

    mmh1_input = input("Nhập mã môn học 1 cần xem điểm: ")

    global list_mshv, list_hthv, list_mmh1, list_dm1
    list_mshv = []
    list_hthv = []
    list_mmh1 = []
    list_dm1 = []

    for number_of_lines in dong:
        danh_sach = number_of_lines.split(sep="|")
        list_mshv.append(danh_sach[0])
        list_hthv.append(danh_sach[1])
        list_mmh1.append(danh_sach[2])
        list_dm1.append(int(danh_sach[3]))

    entry = 0
    while entry < len(list_mmh1):
        if list_mmh1[entry] != mmh1_input:
            list_mshv.pop(entry)
            list_hthv.pop(entry)
            list_mmh1.pop(entry)
            list_dm1.pop(entry)
            entry = 0
        else:
            entry += 1
    if not list_mmh1:
        print("Lỗi: Không tìm thấy môn học!")
    else:
        print(f"Bảng điểm cho mã môn học '{mmh1_input}':")
        import table_draw as td
        td.table_draw()
        flag_mmh1 = False


def mmh2():
    global flag_mmh2
    flag_mmh2 = True
    file_hoc_vien = open(file_handling.get_file_path(), "r")
    dong = file_hoc_vien.readlines()

    mmh2_input = input("Nhập mã môn học 2 cần xem điểm: ")

    global list_mshv, list_hthv, list_mmh2, list_dm2
    list_mshv = []
    list_hthv = []
    list_mmh2 = []
    list_dm2 = []

    for number_of_lines in dong:
        danh_sach = number_of_lines.split(sep="|")
        list_mshv.append(danh_sach[0])
        list_hthv.append(danh_sach[1])
        list_mmh2.append(danh_sach[4])
        list_dm2.append(int(danh_sach[5]))

    entry = 0
    while entry < len(list_mmh2):
        if list_mmh2[entry] != mmh2_input:
            list_mshv.pop(entry)
            list_hthv.pop(entry)
            list_mmh2.pop(entry)
            list_dm2.pop(entry)
            entry = 0
        else:
            entry += 1
    if not list_mmh2:
        print("Lỗi: Không tìm thấy môn học!")
    else:
        print(f"Bảng điểm cho mã môn học '{mmh2_input}':")
        import table_draw as td
        td.table_draw()
        flag_mmh2 = False
