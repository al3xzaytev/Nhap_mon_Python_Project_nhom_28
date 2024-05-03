# Phụ trách việc vẽ bảng

def table_draw(command, data):

    # ==============================================================================================================
    # DRAWING HEADERS
    # ==============================================================================================================

    print()
    print("|", '{:^14}'.format("Mã số học viên"), "|", end="")
    print(" ", end="")
    print('{:<30}'.format("Họ tên"), "|", end="")
    print(" ", end="")

    has_mhp = False
    smhp_max = 0
    smhp = 0
    if command == "view" or command == "hvinfo":
        print('{:^14}'.format("Mã môn học 1"), "|",
              '{:^12}'.format("Điểm môn 1"), "|",
              '{:^14}'.format("Mã môn học 2"), "|",
              '{:^12}'.format("Điểm môn 2"), "|", end="")
        for entry in data:
            if len(entry) > 6:
                has_mhp = True
        if has_mhp:
            mhp = 6
            d = 7
            smhp = 1
            if command == "view":
                for entry in data:
                    while mhp < len(entry):
                        print('{:^17}'.format(f"Môn học phụ {smhp}"), "|",
                              '{:^17}'.format(f"Điểm MH phụ {smhp}"), "|", end="")
                        mhp += 2
                        d += 2
                        smhp += 1
                        smhp_max += 1
            elif command == "hvinfo":
                while mhp < len(data):
                    print('{:^17}'.format(f"Môn học phụ {smhp}"), "|",
                          '{:^17}'.format(f"Điểm MH phụ {smhp}"), "|", end="")
                    mhp += 2
                    d += 2
                    smhp += 1
                    smhp_max += 1

    elif command == "dm1" or command == "dm2":
        if command == "dm1":
            print('{:^11}'.format("Điểm môn 1"), "|", end="")
        elif command == "dm2":
            print('{:^11}'.format("Điểm môn 2"), "|", end="")

    elif command == "mmh1" or command == "mmh2":
        if command == "mmh1":
            print('{:^14}'.format("Mã môn học 1"), "|",
                  '{:^12}'.format("Điểm môn 1"), "|", end="")
        elif command == "mmh2":
            print('{:^14}'.format("Mã môn học 2"), "|",
                  '{:^12}'.format("Điểm môn 2"), "|", end="")

    elif command == "diemso":
        print('{:^12}'.format("Điểm môn 1"), "|",
              '{:^12}'.format("Điểm môn 2"), "|", end="")

    elif command == "mhp":
        print('{:^15}'.format(f"Môn học phụ"), "|",
              '{:^15}'.format(f"Điểm MH phụ"), "|", end="")

    # ==============================================================================================================
    # DRAWING HEADER/DATA SEPARATOR
    # ==============================================================================================================

    print("")
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
        print("|", end="")
        if has_mhp:
            count = 1
            while count < smhp:
                for i in range(0, 18):  # Mã MHP
                    print("-", end="")
                print("|", end="")
                for i in range(0, 19):  # Điểm MHP
                    print("-", end="")
                print("|", end="")
                count += 1
        print()
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

    elif command == "mhp":
        for i in range(0, 17):  # Mã MHP
            print("-", end="")
        print("|", end="")
        for i in range(0, 17):  # Điểm MHP
            print("-", end="")
        print("|")

    # ==============================================================================================================
    # DRAWING DATA
    # ==============================================================================================================

    if command == "view":
        for entries in data:
            print("|", '{:^14}'.format(entries[0]), "|",
                  '{:<30}'.format(entries[1]), "|",
                  '{:^14}'.format(entries[2]), "|",
                  '{:^12}'.format(entries[3]), "|",
                  '{:^14}'.format(entries[4]), "|",
                  '{:^12}'.format(entries[5]), "|", end="")
            if len(entries) > 6:
                mhp = 6
                d = 7
                smhp = 1
                while mhp < len(entries):
                    print('{:^17}'.format(entries[mhp]), "|",
                          '{:^17}'.format(entries[d]), "|", end="")
                    mhp += 2
                    d += 2
                    smhp += 1
                if smhp <= smhp_max:
                    while smhp <= smhp_max:
                        for i in range(0, 18):
                            print(" ", end="")
                        print("|", end="")
                        for z in range(0, 19):
                            print(" ", end="")
                        print("|", end="")
                        smhp += 1
            else:
                count = 1
                while count <= smhp_max:
                    for i in range(0, 18):
                        print(" ", end="")
                    print("|", end="")
                    for z in range(0, 19):
                        print(" ", end="")
                    print("|", end="")
                    count += 1
            print()

    elif command == "hvinfo":
        print("|", '{:^14}'.format(data[0]), "|",
              '{:<30}'.format(data[1]), "|",
              '{:^14}'.format(data[2]), "|",
              '{:^12}'.format(data[3]), "|",
              '{:^14}'.format(data[4]), "|",
              '{:^12}'.format(data[5]), "|", end="")
        if has_mhp:
            mhp = 6
            d = 7
            smhp = 1
            while mhp < len(data):
                print('{:^17}'.format(data[mhp]), "|",
                      '{:^17}'.format(data[d]), "|", end="")
                mhp += 2
                d += 2
                smhp += 1

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

    elif command == "mhp":
        for entries in data:
            print("|", '{:^14}'.format(entries[0]), "|",
                  '{:<30}'.format(entries[1]), "|",
                  '{:^15}'.format(entries[2]), "|",
                  '{:^15}'.format(entries[3]), "|")
