def xem_danh_sach():
    # Danh sách sẽ theo form dưới đây:
    # MSHV|HTHV|MMH1|DM1|MMH2|DM2|

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

    print()
    print("Danh sách", data_file, "đã mở.")
    print()
    print("|", '{:^14}'.format("Mã số học viên"), "|",
          '{:<30}'.format("Họ tên"), "|",
          '{:^14}'.format("Mã môn học 1"), "|",
          '{:^12}'.format("Điểm môn 1"), "|",
          '{:^14}'.format("Mã môn học 2"), "|",
          '{:^12}'.format("Điểm môn 2"), "|")

    ''' Cách format cũ
    print('%-14s' % 'Ma so hoc vien', "|",
          '%-30s' % "Ho ten hoc vien", "|",
          '%-14s' % "Ma mon hoc 1", "|",
          '%-12s' % "Diem mon 1", "|",
          '%-14s' % "Ma mon hoc 2", "|",
          '%-12s' % "Diem mon 2")
    '''
    for i in range(0, 115):
        print("-", end="")
    print()
    for num_entries in range(0, len(list_mshv)):
        print("|", '{:^14}'.format(list_mshv[num_entries]), "|",
              '{:<30}'.format(list_hthv[num_entries]), "|",
              '{:^14}'.format(list_mmh1[num_entries]), "|",
              '{:^12}'.format(list_dm1[num_entries]), "|",
              '{:^14}'.format(list_mmh2[num_entries]), "|",
              '{:^12}'.format(list_dm2[num_entries]), "|")
        ''' Cách format cũ
        print('%-14s' % (list_mshv[num_entries]), "|",
              '%-30s' % list_hthv[num_entries], "|",
              '%-14s' % list_mmh1[num_entries], "|",
              '%-12s' % list_dm1[num_entries], "|",
              '%-14s' % list_mmh2[num_entries], "|",
              '%-12s' % list_dm2[num_entries], " ")
        '''
    print()
    import main as m
    m.main()
