def them_hoc_vien():
    print("\nNhập thông tin học viên.")
    hoc_vien = open("hocvien.dat", "a")

    mshv = int(input("Nhập mã số học viên: "))
    hoc_vien.write(f"{mshv}|")

    hthv = str(input("Nhập họ tên học viên (không dấu): "))
    hoc_vien.write(f"{hthv}|")

    mmh1 = str(input("Nhập mã môn học 1 (4 chữ cái): "))
    hoc_vien.write(f"{mmh1}|")

    dm1 = int(input("Nhập điểm môn học 1 (số nguyên từ 0-10):"))
    hoc_vien.write(f"{dm1}")

    mmh2 = str(input("Nhập mã môn học 2 (4 chữ cái): "))
    hoc_vien.write(f"{mmh2}|")

    dm2 = int(input("Nhập điểm môn học 2 (số nguyên từ 0-10):"))
    hoc_vien.write(f"{dm2}")

    import main as m
    m.main()
