# Sắp xếp theo điểm môn 2

import numpy as np

data_file = "hocvien.dat"
file_hoc_vien = open(data_file, "r")
dong = file_hoc_vien.readlines()


def diem_so():
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

    np_mshv = np.array(list_mshv)
    np_hthv = np.array(list_hthv)
    np_dm1 = np.array(list_dm1)
    np_dm2 = np.array(list_dm2)

    sort_args_dm1 = np.lexsort((np_dm2, np_dm1))
    np_dm1_sort = np_dm1[sort_args_dm1]

    np_mshv_sort = np_mshv[sort_args_dm1]
    np_hthv_sort = np_hthv[sort_args_dm1]
    np_dm2_after_dm1_sort = np_dm2[sort_args_dm1]

    print()
    print("Bảng điểm học sinh theo thứ tự DM1-DM2 tăng dần:\n")
    print("|", '{:^14}'.format("Mã số học viên"), "|",
          '{:<30}'.format("Họ tên"), "|",
          '{:^12}'.format("Điểm môn 1"), "|",
          '{:^12}'.format("Điểm môn 2"), "|")
    for i in range(0, 81):
        print("-", end="")

    print()

    for num_entries in range(0, len(np_mshv)):
        print("|", '{:^14}'.format(np_mshv_sort[num_entries]), "|",
              '{:<30}'.format(np_hthv_sort[num_entries]), "|",
              '{:^12}'.format(np_dm1_sort[num_entries]), "|",
              '{:^12}'.format(np_dm2_after_dm1_sort[num_entries]), "|",)
    print()


def dm1():
    list_mshv = []
    list_hthv = []
    list_dm1 = []

    for number_of_lines in dong:
        danh_sach = number_of_lines.split(sep="|")
        list_mshv.append(danh_sach[0])
        list_hthv.append(danh_sach[1])
        list_dm1.append(int(danh_sach[3]))

    np_mshv = np.array(list_mshv)
    np_hthv = np.array(list_hthv)
    np_dm1 = np.array(list_dm1)

    sort_args = np_dm1.argsort()

    np_dm1 = np.sort(np_dm1)
    np_mshv_sort = np_mshv[sort_args]
    np_hthv_sort = np_hthv[sort_args]

    print()
    print("Bảng điểm học sinh theo thứ tự DM1 tăng dần:\n")
    print("|", '{:^14}'.format("Mã số học viên"), "|",
          '{:<30}'.format("Họ tên"), "|",
          '{:^12}'.format("Điểm môn 1"), "|")
    for i in range(0, 66):
        print("-", end="")

    print()

    for num_entries in range(0, len(np_mshv)):
        print("|", '{:^14}'.format(np_mshv_sort[num_entries]), "|",
              '{:<30}'.format(np_hthv_sort[num_entries]), "|",
              '{:^12}'.format(np_dm1[num_entries]), "|",)
    print()


def dm2():
    list_mshv = []
    list_hthv = []
    list_dm2 = []

    for number_of_lines in dong:
        danh_sach = number_of_lines.split(sep="|")
        list_mshv.append(danh_sach[0])
        list_hthv.append(danh_sach[1])
        list_dm2.append(int(danh_sach[5]))

    np_mshv = np.array(list_mshv)
    np_hthv = np.array(list_hthv)
    np_dm2 = np.array(list_dm2)

    sort_args = np_dm2.argsort()

    np_dm2 = np.sort(np_dm2)
    np_mshv_sort = np_mshv[sort_args]
    np_hthv_sort = np_hthv[sort_args]

    print()
    print("Bảng điểm học sinh theo thứ tự DM2 tăng dần:\n")
    print("|", '{:^14}'.format("Mã số học viên"), "|",
          '{:<30}'.format("Họ tên"), "|",
          '{:^12}'.format("Điểm môn 2"), "|")

    for i in range(0, 66):
        print("-", end="")

    print()

    for num_entries in range(0, len(np_mshv)):
        print("|", '{:^14}'.format(np_mshv_sort[num_entries]), "|",
              '{:<30}'.format(np_hthv_sort[num_entries]), "|",
              '{:^12}'.format(np_dm2[num_entries]), "|",)
    print()
