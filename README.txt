TRƯỜNG ĐẠI HỌC SƯ PHẠM KỸ THUẬT THÀNH PHỐ HỒ CHÍ MINH

NHẬP MÔN PYTHON THỨ 6 TIẾT 8-11
NHÓM 28
PROJECT 1

==============================
1. GIỚI THIỆU
==============================
Phần mềm này là phần mềm quản lý danh sách học sinh được phát triển bởi
nhóm 28 lớp Nhập môn lập trình Python thứ 6 tiết 8-11.

Nhóm gồm có ba thành viên:

- Trần Hoàng Nam 22950012
- Nguyễn Trương Thái Thuận 22950020
- Nguyễn Phúc Tiến 22950024

Phần mềm được viết bằng ngôn ngữ lập trình Python.
Dự án bắt đầu vào ngày 19-04-2024.

==============================
2. HƯỚNG DẪN SỬ DỤNG
==============================
Cách sử dụng như sau:
1. Mở chương trình bằng file main.py
2. Nhập lệnh. Nếu không biết lệnh, gõ 'help' để hiển thị danh sách lệnh.

Danh sách lệnh như sau:

add - Thêm học viên
delete - Xóa học viên bằng MSHV
view - Xem danh sách
dm1 - Xem bảng điểm mã môn học 1.
dm2 - Xem bảng điểm mã môn học 2.
diemso - Xem bảng điểm môn học 1 và 2.

Thứ tự các bảng điểm được xếp theo từ nhỏ đến lớn.
Đối với bảng điểm hai môn học, môn học 1 sẽ ưu tiên được sắp xếp trước.

Sau khi nhập lệnh, chương trình sẽ yêu cầu nhập đường dẫn vào file text.
Sau đó, người dùng nhập theo chỉ dẫn của chương trình

==============================
3. CÁCH THỨC HOẠT ĐỘNG
==============================

Các libraries được nhập vào gồm có:

NumPy - có trong 'diem_so.py', 'sap_xep_dm1', 'sap_xep_dm2'
------------------------------
3.1. DANH SÁCH
------------------------------
Danh sách được xếp theo thứ tự:
MSHV|HTHV|MMH1|DM1|MMH2|DM2|

Tương ứng với:
Mã số học viên|Họ tên học viên|Mã môn học 1|Điểm môn học 1|Mã môn học 2|Điểm môn học 2

Các giá trị được xếp theo thứ tự này và cách nhau bằng ký tự '|'.

Phần mềm chỉ chấp nhận danh sách theo format này. Bất cứ danh sách theo format khác sẽ báo lỗi.
Một ví dụ về danh sách hợp lệ là file 'hocvien.dat' có trong phần mềm.
