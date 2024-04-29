# Nhập môn Python lớp thứ 6 tiết 8-11
# Nhóm 28
# Project 1
import os


def main():
    const_nam_dep_trai = True

    while const_nam_dep_trai is True:
        user_input = input("\n>: ")
        if user_input == "help":
            abs_path = os.path.abspath("help.txt")
            help_file = open(abs_path, 'r', encoding='utf-8')
            print()
            print(help_file.read())
        elif user_input == "add" or user_input == "2":
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
            ds.diem_mon("dm1")
        elif user_input == "dm2" or user_input == "5":
            import diem_so as ds
            ds.diem_mon("dm2")
        elif user_input == "diemso" or user_input == "6":
            import diem_so as ds
            ds.diem_so()
        elif user_input == "mmh1":
            import diem_so as ds
            ds.ma_mon_hoc("mmh1")
        elif user_input == "mmh2":
            import diem_so as ds
            ds.ma_mon_hoc("mmh2")
        elif user_input == "mshv":
            import hoc_vien_info as hvinfo
            hvinfo.hoc_vien_info()
        elif user_input == "quit":
            break
        # elif user_input == "protovision":
        #     import protovision
        #     protovision.play()
        else:
            print(f"Lỗi: Lệnh '{user_input}' không hợp lệ.")


def intro():
    os.system('cls')
    print("=============================================")
    print("Phần mềm quản lý danh sách học viên")
    print("=============================================")
    print("Để hiển thị danh sách các lệnh, gõ 'help'.")
    main()


if __name__ == "__main__":
    intro()
