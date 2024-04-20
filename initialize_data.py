# Hiện tại chưa cần dùng đến function này
# Cơ bản chỉ dùng để display danh sách học viên

def initialize_data():
    data_file = "hocvien.dat"
    file_hoc_vien = open(data_file, "r")
    dong = file_hoc_vien.readlines()

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
