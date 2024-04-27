# Phụ trách việc vẽ bảng

def table_draw():
    print()
    print("|", '{:^14}'.format("Mã số học viên"), "|", end="")
    print(" ", end="")
    print('{:<30}'.format("Họ tên"), "|", end="")
    print(" ", end="")

    from diem_so import flag_dm1, flag_dm2, flag_diem_so, flag_mmh1, flag_mmh2
    from xem_danh_sach import flag_danh_sach
    from hoc_vien_info import flag_info
    if flag_dm1:
        print('{:^11}'.format("Điểm môn 1"), "|")  # These must be 11 to be aligned for some reason????
    elif flag_dm2:
        print('{:^11}'.format("Điểm môn 2"), "|")

    elif flag_mmh1:
        print('{:^14}'.format("Mã môn học 1"), "|",
              '{:^12}'.format("Điểm môn 1"), "|")
    elif flag_mmh2:
        print('{:^14}'.format("Mã môn học 2"), "|",
              '{:^12}'.format("Điểm môn 2"), "|")

    elif flag_diem_so:
        print('{:^11}'.format("Điểm môn 1"), "|",
              '{:^12}'.format("Điểm môn 2"), "|")  # This one is 12 ????
    elif flag_danh_sach or flag_info:
        print('{:^14}'.format("Mã môn học 1"), "|",
              '{:^12}'.format("Điểm môn 1"), "|",
              '{:^14}'.format("Mã môn học 2"), "|",
              '{:^12}'.format("Điểm môn 2"), "|")

    print("|", end="")
    for i in range(0, 16):  # Mã số học viên
        print("-", end="")
    print("|", end="")
    for i in range(0, 32):  # Họ tên học viên
        print("-", end="")
    print("|", end="")

    if flag_dm1 or flag_dm2:
        for i in range(0, 13):  # Điểm môn 1/2
            print("-", end="")
        print("|")

    elif flag_mmh1 or flag_mmh2:
        for i in range(0, 16):  # Mã môn học
            print("-", end="")
        print("|", end="")
        for i in range(0, 14):  # Điểm môn học 1
            print("-", end="")
        print("|")

    elif flag_diem_so:
        for i in range(0, 13):  # Điểm môn 1
            print("-", end="")
        print("|", end="")
        for i in range(0, 14):  # Điểm môn 2
            print("-", end="")
        print("|")

    elif flag_danh_sach or flag_info:
        for i in range(0, 16):  # Mã môn 1
            print("-", end="")
        print("|", end="")
        for i in range(0, 14):  # Điểm môn 1
            print("-", end="")
        print("|", end="")
        for i in range(0, 16):  # Mã môn 2
            print("-", end="")
        print("|", end="")
        for i in range(0, 14):  # Điểm môn 2
            print("-", end="")
        print("|")

    if flag_danh_sach or flag_info:
        if flag_danh_sach:
            from xem_danh_sach import list_mshv, list_hthv, list_mmh1, list_dm1, list_mmh2, list_dm2
            for entries in range(0, len(list_mshv)):
                print("|", '{:^14}'.format(list_mshv[entries]), "|",
                      '{:<30}'.format(list_hthv[entries]), "|",
                      '{:^14}'.format(list_mmh1[entries]), "|",
                      '{:^12}'.format(list_dm1[entries]), "|",
                      '{:^14}'.format(list_mmh2[entries]), "|",
                      '{:^12}'.format(list_dm2[entries]), "|")
        elif flag_info:
            from hoc_vien_info import mshv, hthv, mmh1, dm1, mmh2, dm2
            print("|", '{:^14}'.format(mshv), "|",
                  '{:<30}'.format(hthv), "|",
                  '{:^14}'.format(mmh1), "|",
                  '{:^12}'.format(dm1), "|",
                  '{:^14}'.format(mmh2), "|",
                  '{:^12}'.format(dm2), "|")

    else:
        if flag_mmh1 or flag_mmh2:
            from diem_so import list_mshv, list_hthv
            for entries in range(0, len(list_mshv)):
                print("|", '{:^14}'.format(list_mshv[entries]), "|",
                      '{:<30}'.format(list_hthv[entries]), "|", end="")
                if flag_mmh1:
                    from diem_so import list_mmh1, list_dm1
                    print('{:^15}'.format(list_mmh1[entries]), "|",
                          '{:^12}'.format(list_dm1[entries]), "|")
                elif flag_mmh2:
                    from diem_so import list_mmh2, list_dm2
                    print('{:^15}'.format(list_mmh2[entries]), "|",
                          '{:^12}'.format(list_dm2[entries]), "|")

        else:
            from diem_so import np_mshv_sort, np_hthv_sort
            for num_entries in range(0, len(np_mshv_sort)):
                print("|", '{:^14}'.format(np_mshv_sort[num_entries]), "|",
                      '{:<30}'.format(np_hthv_sort[num_entries]), "|", end="")
                if flag_dm1:
                    from diem_so import np_dm1
                    print('{:^12}'.format(np_dm1[num_entries]), "|")
                elif flag_dm2:
                    from diem_so import np_dm2
                    print('{:^12}'.format(np_dm2[num_entries]), "|")
                elif flag_diem_so:
                    from diem_so import np_dm1_sort, np_dm2_after_dm1_sort
                    print('{:^12}'.format(np_dm1_sort[num_entries]), "|",
                          '{:^12}'.format(np_dm2_after_dm1_sort[num_entries]), "|")
