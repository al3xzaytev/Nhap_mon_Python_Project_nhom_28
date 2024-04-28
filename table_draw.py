# Phụ trách việc vẽ bảng

def table_draw(command, data):
    print()
    print("|", '{:^14}'.format("Mã số học viên"), "|", end="")
    print(" ", end="")
    print('{:<30}'.format("Họ tên"), "|", end="")
    print(" ", end="")

    if command == "view" or command == "hvinfo":
        print('{:^14}'.format("Mã môn học 1"), "|",
              '{:^12}'.format("Điểm môn 1"), "|",
              '{:^14}'.format("Mã môn học 2"), "|",
              '{:^12}'.format("Điểm môn 2"), "|")
    elif command == "dm1":
        print('{:^11}'.format("Điểm môn 1"), "|")  # These must be 11 to be aligned for some reason????
    elif command == "dm2":
        print('{:^11}'.format("Điểm môn 2"), "|")  # These must be 11 to be aligned for some reason????
    elif command == "mmh1":
        print('{:^14}'.format("Mã môn học 1"), "|",
              '{:^12}'.format("Điểm môn 1"), "|")
    elif command == "mmh2":
        print('{:^14}'.format("Mã môn học 2"), "|",
              '{:^12}'.format("Điểm môn 2"), "|")
    elif command == "diemso":
        print('{:^12}'.format("Điểm môn 1"), "|",
              '{:^12}'.format("Điểm môn 2"), "|")  # This one is 12 ????

    print("|", end="")
    for i in range(0, 16):  # Mã số học viên
        print("-", end="")
    print("|", end="")
    for i in range(0, 32):  # Họ tên học viên
        print("-", end="")
    print("|", end="")

    if command == "view" or command == "hvinfo":
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
    elif command == "dm1" or command == "dm2":
        for i in range(0, 13):  # Điểm môn 1/2
            print("-", end="")
        print("|")
    elif command == "mmh1" or command == "mmh2":
        for i in range(0, 16):  # Mã môn học
            print("-", end="")
        print("|", end="")
        for i in range(0, 14):  # Điểm môn học
            print("-", end="")
        print("|")
    elif command == "diemso":
        for i in range(0, 14):  # Điểm môn 1
            print("-", end="")
        print("|", end="")
        for i in range(0, 14):  # Điểm môn 2
            print("-", end="")
        print("|")

    if command == "view":
        for entries in data:
            print("|", '{:^14}'.format(entries[0]), "|",
                  '{:<30}'.format(entries[1]), "|",
                  '{:^14}'.format(entries[2]), "|",
                  '{:^12}'.format(entries[3]), "|",
                  '{:^14}'.format(entries[4]), "|",
                  '{:^12}'.format(entries[5]), "|")
    elif command == "dm1" or command == "dm2":
        for entries in data:
            print("|", '{:^14}'.format(entries[0]), "|",
                  '{:<30}'.format(entries[1]), "|", end="")
            if command == "dm1":
                print('{:^12}'.format(entries[3]), "|")
            elif command == "dm2":
                print('{:^12}'.format(entries[5]), "|")

    elif command == "mmh1" or command == "mmh2":
        for entries in data:
            print("|", '{:^14}'.format(entries[0]), "|",
                  '{:<30}'.format(entries[1]), "|", end="")
            if command == "mmh1":
                print('{:^15}'.format(entries[2]), "|",
                      '{:^12}'.format(entries[3]), "|")
            elif command == "mmh2":
                print('{:^15}'.format(entries[4]), "|",
                      '{:^12}'.format(entries[5]), "|")
    elif command == "diemso":
        for entries in data:
            print("|", '{:^14}'.format(entries[0]), "|",
                  '{:<30}'.format(entries[1]), "|",
                  '{:^12}'.format(entries[3]), "|",
                  '{:^12}'.format(entries[5]), "|")
    elif command == "hvinfo":
        print("|", '{:^14}'.format(data[0]), "|",
              '{:<30}'.format(data[1]), "|",
              '{:^14}'.format(data[2]), "|",
              '{:^12}'.format(data[3]), "|",
              '{:^14}'.format(data[4]), "|",
              '{:^12}'.format(data[5]), "|")
