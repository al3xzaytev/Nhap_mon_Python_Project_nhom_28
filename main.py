# Nhập môn Python lớp thứ 6 tiết 8-11
# Nhóm 28
# Project 1
import os
import file_handling


def main():
    const_nam_dep_trai = True

    while const_nam_dep_trai is True:
        user_input = input("\n>: ")
        if user_input == "help" or user_input == "1":
            abs_path = os.path.abspath("help.txt")
            help_file = open(abs_path, 'r', encoding='utf-8')
            print()
            print(help_file.read())
        elif user_input == "dir" or user_input == "2":
            import file_handling
            file_handling.set_file_path()
        elif user_input == "add" or user_input == "3":
            import hoc_vien_info as hvinfo
            hvinfo.them_hoc_vien()
        elif user_input == "delete" or user_input == "4":
            import hoc_vien_info as hvinfo
            hvinfo.xoa_hoc_vien()
        elif user_input == "mshv" or user_input == "5":
            import hoc_vien_info as hvinfo
            hvinfo.hoc_vien_info()
        elif user_input == "view" or user_input == "6":
            import diem_so as ds
            ds.xem_danh_sach()
        elif user_input == "dm1" or user_input == "7":
            import diem_so as ds
            ds.diem_mon("dm1")
        elif user_input == "dm2" or user_input == "8":
            import diem_so as ds
            ds.diem_mon("dm2")
        elif user_input == "diemso" or user_input == "9":
            import diem_so as ds
            ds.diem_so()
        elif user_input == "mmh1" or user_input == "10":
            import diem_so as ds
            ds.ma_mon_hoc("mmh1")
        elif user_input == "mmh2" or user_input == "11":
            import diem_so as ds
            ds.ma_mon_hoc("mmh2")
        elif user_input == "mhp" or user_input == "12":
            import mon_hoc_phu as mhp
            print("\nChọn việc cần làm:\n"
                  "1. Thêm môn học phụ\n"
                  "2. Xoá môn học phụ\n"
                  "3. Xem điểm môn học phụ\n"
                  "4. Xem điểm môn học phụ của học viên")
            while True:
                mhp_input = input("\n>: ")
                if mhp_input == "1":
                    mhp.add_mon_hoc_phu()
                    break
                elif mhp_input == "2":
                    mhp.del_mon_hoc_phu()
                    break
                elif mhp_input == "3":
                    mhp_so = int(input("Xem điểm môn học phụ số: "))
                    mhp_ma = input("Mã môn học phụ: ")
                    mhp.ma_mhp(mhp_so, mhp_ma)
                    break
                elif mhp_input == "4":
                    mshv = input("Nhập mã số học viên cần xem điểm: ")
                    mhp_so = int(input("Xem điểm môn học phụ số: "))
                    mhp.diem_mhp(mshv, mhp_so)
                    break
                elif mhp_input == "quit":
                    break
                else:
                    print("Lỗi: Lệnh không hợp lệ!")
        elif user_input == "quit":
            break
        elif user_input == "clear":
            intro()
        else:
            print(f"Lỗi: Lệnh '{user_input}' không hợp lệ.")


def intro():
    os.system('cls')
    print("""TRƯỜNG ĐẠI HỌC SƯ PHẠM KỸ THUẬT THÀNH PHỐ HỒ CHÍ MINH
NHẬP MÔN PYTHON THỨ 6 TIẾT 8-11
INPY131685_23_2_03
                
NHÓM 28
PROJECT 1\n""")
    print("=============================================")
    print("Phần mềm quản lý danh sách học viên")
    print("=============================================")
    print("\nĐường dẫn tập tin dữ liệu hiện tại:")
    print(file_handling.file_path)
    print("\nĐể hiển thị danh sách các lệnh, gõ 'help' hoặc nhấn số 1.")
    main()


if __name__ == "__main__":
    intro()
