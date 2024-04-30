import file_handling


def truy_xuat_data_hoc_vien(ma_so_hoc_vien):
    file_content = file_handling.process_file("read")
    found = False
    for entry in file_content:
        dong = entry.split(sep="|")
        if dong[0] == ma_so_hoc_vien:
            line = entry.split(sep="\n")
            info_hoc_vien = line[0].split(sep="|")
            found = True
            import table_draw as td
            td.table_draw("hvinfo", info_hoc_vien)
        else:
            continue
    if not found:
        print("\nLỗi: Không tìm thấy học viên!")


def hoc_vien_info():
    user_mshv_input = str(input("Nhập mã số học viên: "))
    truy_xuat_data_hoc_vien(user_mshv_input)
