import file_handling

flag_info = False

global mshv, hthv, mmh1, dm1, mmh2, dm2


def truy_xuat_data_hoc_vien(ma_so_hoc_vien):
    file_hoc_vien = open(file_handling.get_file_path(), "r")
    danh_sach = file_hoc_vien.readlines()

    found = False

    for entry in danh_sach:
        dong = entry.split(sep="|")
        if dong[0] == ma_so_hoc_vien:
            info_hoc_vien = entry.split(sep="|")
            found = True

            global mshv, hthv, mmh1, dm1, mmh2, dm2
            mshv = info_hoc_vien[0]
            hthv = info_hoc_vien[1]
            mmh1 = info_hoc_vien[2]
            dm1 = info_hoc_vien[3]
            mmh2 = info_hoc_vien[4]
            dm2 = info_hoc_vien[5]

            global flag_info
            flag_info = True

            import table_draw as td
            td.table_draw()

        else:
            continue

    if not found:
        print("\nLỗi: Không tìm thấy học viên!")

    flag_info = False


def hoc_vien_info():
    user_mshv_input = str(input("Nhập mã số học viên: "))
    truy_xuat_data_hoc_vien(user_mshv_input)
