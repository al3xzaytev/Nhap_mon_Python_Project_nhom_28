print("Chào mừng bạn đến với phần mềm quản lý danh sách học sinh hàng đầu Việt Nam.")


def main():
    nam_dep_trai = True

    while nam_dep_trai is True:
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
            import sap_xep_dm1 as dm1
            dm1.sap_xep()
        elif user_input == "dm2" or user_input == "5":
            import sap_xep_dm2 as dm2
            dm2.sap_xep()


main()
