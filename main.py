print("Chào mừng bạn đến với phần mềm quản lý danh sách học sinh hàng đầu Việt Nam.")


def main():
    nam_dep_trai = True

    while nam_dep_trai is True:
        user_input = input("Nhập yêu cầu của bạn: ")
        if user_input == "add":
            import them_hoc_vien as thv
            thv.them_hoc_vien()
        elif user_input == "view":
            import xem_danh_sach as xds
            xds.xem_danh_sach()


main()
