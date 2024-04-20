# Nhập môn Python lớp thứ 6 tiết 8-11
# Nhóm 28
# Project 1
print("=============================================")
print("Chào mừng bạn đến với phần mềm quản lý danh sách học sinh hàng đầu Việt Nam.")
print("=============================================")


def main():
    const_nam_dep_trai = True

    while const_nam_dep_trai is True:
        user_input = input("Nhập yêu cầu của bạn: ")
        if user_input == "add" or user_input == "2":
            import them_hoc_vien as thv
            thv.them_hoc_vien()
        elif user_input == "delete" or user_input == "3":
            import xoa_hoc_vien as xhv
            xhv.xoa_hoc_vien()
        elif user_input == "view":
            import xem_danh_sach as xds
            xds.xem_danh_sach()
        elif user_input == "dm1" or user_input == "4":
            import diem_so as ds
            ds.dm1()
        elif user_input == "dm2" or user_input == "5":
            import diem_so as ds
            ds.dm2()
        elif user_input == "diemso" or user_input == "6":
            import diem_so as ds
            ds.diem_so()


main()
