# Sắp xếp theo điểm môn 2

import numpy as np

data_file = "hocvien.dat"
file_hoc_vien = open(data_file, "r")
dong = file_hoc_vien.readlines()


def sap_xep():
    print("Danh sách học sinh theo thứ tự DM2 tăng dần:")
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
    print("|", '{:^14}'.format("Ma so hoc vien"), "|",
          '{:<30}'.format("Ho ten"), "|",
          '{:^12}'.format("Diem mon 2"), "|",)

    for i in range(0, 66):
        print("-", end="")

    print()

    for num_entries in range(0, len(np_mshv)):
        print("|", '{:^14}'.format(np_mshv_sort[num_entries]), "|",
              '{:<30}'.format(np_hthv_sort[num_entries]), "|",
              '{:^12}'.format(np_dm2[num_entries]), "|",)
    print()
