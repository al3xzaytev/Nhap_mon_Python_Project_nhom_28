# Phụ trách việc xử lý dữ liệu để sắp xếp

import numpy as np
import file_handling

"""Global values below are placed so PyCharm does not go apeshit"""
global np_dm1, np_dm2, np_mshv, np_mshv_sort, np_hthv_sort
global np_dm1_sort, np_dm2_after_dm1_sort

flag_dm1 = False
flag_dm2 = False
flag_diem_so = False


def initialization():
    global flag_dm1, flag_dm2, flag_diem_so
    flag_dm1 = False
    flag_dm2 = False
    flag_diem_so = False


def dm1():
    global flag_dm1
    flag_dm1 = True
    file_hoc_vien = open(file_handling.get_file_path(), "r")
    dong = file_hoc_vien.readlines()

    list_mshv = []
    list_hthv = []
    list_dm1 = []

    for number_of_lines in dong:
        danh_sach = number_of_lines.split(sep="|")
        list_mshv.append(danh_sach[0])
        list_hthv.append(danh_sach[1])
        list_dm1.append(int(danh_sach[3]))

    global np_dm1
    global np_mshv
    global np_mshv_sort
    global np_hthv_sort

    np_mshv = np.array(list_mshv)
    np_hthv = np.array(list_hthv)
    np_dm1 = np.array(list_dm1)

    sort_args = np_dm1.argsort()

    np_dm1 = np_dm1[sort_args]
    np_mshv_sort = np_mshv[sort_args]
    np_hthv_sort = np_hthv[sort_args]

    import table_draw as tr
    tr.table_draw()


def dm2():
    global flag_dm2
    flag_dm2 = True

    file_hoc_vien = open(file_handling.get_file_path(), "r")
    dong = file_hoc_vien.readlines()

    list_mshv = []
    list_hthv = []
    list_dm2 = []

    for number_of_lines in dong:
        danh_sach = number_of_lines.split(sep="|")
        list_mshv.append(danh_sach[0])
        list_hthv.append(danh_sach[1])
        list_dm2.append(int(danh_sach[5]))

    global np_dm2
    global np_mshv
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


def diem_so():
    global flag_diem_so
    flag_diem_so = True
    file_hoc_vien = open(file_handling.get_file_path(), "r")
    dong = file_hoc_vien.readlines()

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

    global np_dm1
    global np_dm2
    global np_mshv
    global np_mshv_sort
    global np_hthv_sort
    global np_dm1_sort
    global np_dm2_after_dm1_sort

    np_mshv = np.array(list_mshv)
    np_hthv = np.array(list_hthv)
    np_dm1 = np.array(list_dm1)
    np_dm2 = np.array(list_dm2)

    sort_args_dm1 = np.lexsort((np_dm2, np_dm1))
    np_dm1_sort = np_dm1[sort_args_dm1]

    np_mshv_sort = np_mshv[sort_args_dm1]
    np_hthv_sort = np_hthv[sort_args_dm1]
    np_dm2_after_dm1_sort = np_dm2[sort_args_dm1]

    import table_draw as tr
    tr.table_draw()
