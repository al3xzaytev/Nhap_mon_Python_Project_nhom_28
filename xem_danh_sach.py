# Xem danh sách cơ bản

import file_handling


def xem_danh_sach():
    file_content = file_handling.process_file("read")

    danh_sach = []
    for number_of_lines in file_content:
        line = number_of_lines.split(sep="\n")
        newline = line[0].split(sep="|")
        danh_sach.append(newline)

    import table_draw as td
    td.table_draw("view", danh_sach)
