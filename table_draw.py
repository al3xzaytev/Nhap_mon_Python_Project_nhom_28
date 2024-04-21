# Phụ trách việc vẽ bảng

import diem_so
import xem_danh_sach


def table_draw():
    print()
    print("|", '{:^14}'.format("Mã số học viên"), "|", end="")
    print(" ", end="")
    print('{:<30}'.format("Họ tên"), "|", end="")
    print(" ", end="")

    from diem_so import flag_dm1, flag_dm2, flag_diem_so
    from xem_danh_sach import flag_danh_sach
    if flag_dm1 is True:
        print('{:^11}'.format("Điểm môn 1"), "|")  # These must be 11 to be aligned for some reason????

    elif flag_dm2 is True:
        print('{:^11}'.format("Điểm môn 2"), "|")

    elif flag_diem_so is True:
        print('{:^11}'.format("Điểm môn 1"), "|",
              '{:^12}'.format("Điểm môn 2"), "|", end="\n")  # This one is 12 ????
    elif flag_danh_sach is True:
        print('{:^14}'.format("Mã môn học 1"), "|",
              '{:^12}'.format("Điểm môn 1"), "|",
              '{:^14}'.format("Mã môn học 2"), "|",
              '{:^12}'.format("Điểm môn 2"), "|")

    print("|", end="")
    for i in range(0, 16):
        print("-", end="")
    print("|", end="")
    for i in range(0, 32):
        print("-", end="")
    print("|", end="")

    if flag_dm1 is True or flag_dm2 is True:
        for i in range(0, 13):
            print("-", end="")
        print("|")

    elif flag_diem_so is True:
        for i in range(0, 13):
            print("-", end="")
        print("|", end="")
        for i in range(0, 14):
            print("-", end="")
        print("|")

    elif flag_danh_sach is True:
        for i in range(0, 16):
            print("-", end="")
        print("|", end="")
        for i in range(0, 14):
            print("-", end="")
        print("|", end="")
        for i in range(0, 16):
            print("-", end="")
        print("|", end="")
        for i in range(0, 14):
            print("-", end="")
        print("|")

    if flag_danh_sach is True:
        from xem_danh_sach import list_mshv, list_hthv, list_mmh1, list_dm1, list_mmh2, list_dm2
        for entries in range(0, len(list_mshv)):
            print("|", '{:^14}'.format(list_mshv[entries]), "|",
                  '{:<30}'.format(list_hthv[entries]), "|",
                  '{:^14}'.format(list_mmh1[entries]), "|",
                  '{:^12}'.format(list_dm1[entries]), "|",
                  '{:^14}'.format(list_mmh2[entries]), "|",
                  '{:^12}'.format(list_dm2[entries]), "|")
        xem_danh_sach.initialize()

    else:
        from diem_so import np_mshv, np_mshv_sort, np_hthv_sort
        for num_entries in range(0, len(np_mshv)):
            print("|", '{:^14}'.format(np_mshv_sort[num_entries]), "|",
                  '{:<30}'.format(np_hthv_sort[num_entries]), "|", end="")

            if flag_dm1 is True:
                from diem_so import np_dm1
                print('{:^12}'.format(np_dm1[num_entries]), "|")

            elif flag_dm2 is True:
                from diem_so import np_dm2
                print('{:^12}'.format(np_dm2[num_entries]), "|")

            elif flag_diem_so is True:
                from diem_so import np_dm1_sort, np_dm2_after_dm1_sort
                print('{:^12}'.format(np_dm1_sort[num_entries]), "|",
                      '{:^12}'.format(np_dm2_after_dm1_sort[num_entries]), "|")

        diem_so.initialization()
