TRƯỜNG ĐẠI HỌC SƯ PHẠM KỸ THUẬT THÀNH PHỐ HỒ CHÍ MINH
NHẬP MÔN PYTHON THỨ 6 TIẾT 8-11
INPY131685_23_2_03

NHÓM 28
PROJECT 1

============================================================
1. GIỚI THIỆU
============================================================
Phần mềm này là phần mềm quản lý danh sách học sinh được phát triển bởi
nhóm 28 lớp Nhập môn lập trình Python thứ 6 tiết 8-11 - mã lớp INPY131685_23_2_03.

Nhóm 28 gồm có ba thành viên:

- Trần Hoàng Nam - 22950012
- Nguyễn Trương Thái Thuận - 22950020
- Nguyễn Phúc Tiến - 22950024

Phần mềm được viết bằng ngôn ngữ lập trình Python.
Dự án bắt đầu vào ngày 19-04-2024.

============================================================
2. HƯỚNG DẪN SỬ DỤNG
============================================================
Cách sử dụng như sau:
1. Mở chương trình bằng file main.py
2. Nhập lệnh. Gõ 'help' để hiển thị danh sách lệnh.

Sau đó, người dùng nhập các tham số theo chỉ dẫn của chương trình,
tuỳ thuộc vào lệnh đã nhập.

============================================================
3. CÁCH THỨC HOẠT ĐỘNG
============================================================

------------------------------
3.1. TẬP TIN DỮ LIỆU VÀ DANH SÁCH
------------------------------
Phần mềm này đọc các tập tin có định dạng .dat, nhưng cũng có thể sử dụng .txt.
Các tập tin này thể hiện danh sách học viên.

Mỗi dòng của danh sách thể hiện thông tin của một học viên.
Mỗi dòng sẽ theo mẫu như sau:
MSHV|HTHV|MMH1|DM1|MMH2|DM2

Tương ứng với:
Mã số học viên|Họ tên học viên|Mã môn học 1|Điểm môn học 1|Mã môn học 2|Điểm môn học 2

Nếu một học viên có 1 môn học phụ, định dạng sẽ được thay đổi bằng cách
với mỗi môn học phụ, hai giá trị mới được thêm vào: MMHP1|DMHP1

Ví dụ:
MSHV|HTHV|MMH1|DM1|MMH2|DM2|MMHP1|DMHP1

Tương ứng với:
Mã số học viên|Họ tên học viên|Mã môn học 1|Điểm môn học 1|Mã môn học 2|Điểm môn học 2|Mã môn học phụ 1|Điểm MHP 1

Tất cả các dòng đều được xếp theo thứ tự này và cách nhau bằng ký tự '|'.
Mỗi dòng trong file dữ liệu thể hiện thông tin 1 học viên.

Phần mềm chỉ chấp nhận danh sách theo mẫu này. Bất cứ danh sách theo mẫu nào khác sẽ báo lỗi.
Một ví dụ về danh sách hợp lệ là file 'hocvien.txt' có trong phần mềm.

------------------------------
3.2. NHẬP ĐƯỜNG DẪN
------------------------------
Tệp tin 'file_handling.py' phụ trách việc nhập đường dẫn cho các tính năng cần nó.
file_handling.py có hai function là set_file_path() và get_file_path().

- Đường dẫn file mặc định là file 'hocvien.txt' có trong chương trình.
  File này nằm cùng thư mục với các file python khác.

set_file_path() hoạt động như sau:
- Đường dẫn file người dùng nhập vào là dạng chuỗi (string).
  Nếu người dùng không nhập gì thì sẽ dùng đường dẫn file mặc định.
- Thông báo đường dẫn file qua terminal.
- Đặt giá trị file_path là string chứa đường dẫn file.

get_file_path() trả về file_path. Giá trị được trả về sẽ được các file khác sử dụng trong hàm open() để mở file,
từ đó thực thi các tính năng.
------------------------------
3.3. THÊM HỌC VIÊN
------------------------------
Tệp tin 'them_hoc_vien.py' phụ trách tính năng thêm học viên.
Tính năng thêm học viên hoạt động như sau:
- Import file_handling
- Mở file ra.
- Yêu cầu người dùng nhập các thông tin của học viên.
- Quay trở lại giao diện chính khi hoàn tất.
------------------------------
3.3. XOÁ HỌC VIÊN
------------------------------
Tệp tin 'xoa_hoc_vien.py' phụ trách tính năng thêm học viên.
Tính năng xóa học viên hoạt động như sau:
- Import file_handling
- Mở file ra.
- Đọc file rồi lưu trữ nội dung file vào một list có tên 'danh_sach'.
  Mỗi giá trị trong list tương ứng với một dòng trong file dữ liệu.
- Yêu cầu người dùng nhập mã số học viên cần xoá.
- Tạo giá trị flag "Found" = False.
- Dùng vòng lặp kiểm tra từng giá trị trong list danh_sach.
  Trước tiên, mã số học viên trong list danh_sach được tách ra bằng cách
  mỗi giá trị trong list danh_sach (tương ứng với một dòng trong file dữ liệu) đều được split(sep="|")
  rồi kiểm tra giá trị đầu tiên của string đó sau khi split, vì giá trị đầu tiên sẽ là mã số học viên,
  tương ứng với MSHV vốn nằm ở vị trí đầu dòng trong file dữ liệu.

  Nếu tìm được mã số học viên trùng với MSHV cần xoá, sẽ xoá giá trị có mã số học viên đó trong danh_sach
  bằng remove(). Sau đó flag "Found" sẽ được chuyển giá trị thành True, thể hiện việc tìm thấy MSHV cần xoá.
- Sau khi vòng lặp kết thúc, kiểm tra flag "Found" xem đã tìm được chưa (sẽ chuyển thành True).

  Nếu flag "Found" là True (nghĩa là đã tìm và xoá được học viên khỏi list danh_sach),
  phần mềm sẽ hỏi lại một lần nữa xem người dùng có muốn xoá không.
  Nếu người dùng xác nhận muốn xoá, phần mềm sẽ
  tiến hành nhập lại danh sách dữ liệu mới từ list danh_sach vào file dữ liệu
  bằng cách mở file ra, xoá hết dữ liệu trong file và nhập dữ liệu mới không có học viên.

  Nếu flag "Found" vẫn là False như ban đầu (không thể tìm được học viên),
  thông báo lại cho người dùng.

- Quay trở lại giao diện chính.

------------------------------
3.4. SẮP XẾP DANH SÁCH THEO ĐIỂM
------------------------------
Tệp tin diem_so.py phụ trách tính năng sắp xếp danh sách theo điểm.

------------------------------
3.4.1. SẮP XẾP DANH SÁCH THEO ĐIỂM
------------------------------
Cách thức hoạt động của các tính năng sắp xếp theo điểm như sau:
- Import file_handling
- Mở file ra, đọc rồi lưu trữ nội dung file vào một list có tên.
  Mỗi giá trị trong list tương ứng với một dòng trong file dữ liệu.
- Dùng vòng lặp nhập từng giá trị trong từng dòng của file dữ liệu vào 3 list trên.
  Mỗi dòng trong file dữ liệu thể hiện thông tin 1 học viên.
  Mỗi thông tin của mỗi học viên được cách nhau bằng ký tự '|'.
  (chi tiết xin xem phần 3.1.)
  Khi vòng lặp hoàn tất, danh_sach sẽ lưu trữ thông tin từng dòng theo kiểu list trong list.
- Dùng hàm sort() lên list danh_sach để sắp xếp theo điểm.
- Vẽ bảng.
------------------------------
3.4.2. CƠ CHẾ VẼ BẢNG
------------------------------
Cơ chế vẽ bảng sử dụng các toán tử string formatting của Python.
Chi tiết về các toán tử này xin tham khảo tài liệu của Python:
https://docs.python.org/2/library/stdtypes.html#string-formatting