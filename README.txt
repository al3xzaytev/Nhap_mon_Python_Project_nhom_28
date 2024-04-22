TRƯỜNG ĐẠI HỌC SƯ PHẠM KỸ THUẬT THÀNH PHỐ HỒ CHÍ MINH
NHẬP MÔN PYTHON THỨ 6 TIẾT 8-11
INPY131685_23_2_03

NHÓM 28
PROJECT 1

============================================================
1. GIỚI THIỆU
============================================================
Phần mềm này là phần mềm quản lý danh sách học sinh được phát triển bởi
nhóm 28 lớp Nhập môn lập trình Python thứ 6 tiết 8-11 mã lớp INPY131685_23_2_03.

Nhóm 28 gồm có ba thành viên:

- Trần Hoàng Nam 22950012
- Nguyễn Trương Thái Thuận 22950020
- Nguyễn Phúc Tiến 22950024

Phần mềm được viết bằng ngôn ngữ lập trình Python.
Dự án bắt đầu vào ngày 19-04-2024.

============================================================
2. HƯỚNG DẪN SỬ DỤNG
============================================================
Cách sử dụng như sau:
1. Mở chương trình bằng file main.py
2. Nhập lệnh. Nếu không biết lệnh, gõ 'help' để hiển thị danh sách lệnh.

Danh sách lệnh như sau:

help: Hiển thị danh sách lệnh
add: Thêm học viên
delete: Xoá học viên theo mã số học viên
view: Xem danh sách
dm1: Xem bảng điểm DM1 của học viên theo thứ tự tăng dần của DM1
dm2: Xem bảng điểm DM2 của học viên theo thứ tự tăng dần của DM2
diemso: Xem bảng điểm DM1 và DM2 của học viên theo thứ tự tăng dần của DM1-DM2

Thứ tự các bảng điểm được xếp theo từ nhỏ đến lớn.
Đối với bảng điểm hai môn học, môn học 1 sẽ ưu tiên được sắp xếp trước.

Sau khi nhập lệnh, chương trình sẽ yêu cầu nhập đường dẫn vào file text.
Nếu không nhập bất cứ đường dẫn gì, chương trình sẽ mặc định sử dụng
file 'hocvien.dat' chung thư mục vói chương trình.

Sau đó, người dùng nhập các tham số theo chỉ dẫn của chương trình.

============================================================
3. CÁCH THỨC HOẠT ĐỘNG
============================================================

Các library được nhập vào gồm có:

NumPy - có trong 'diem_so.py'

------------------------------
3.1. DANH SÁCH
------------------------------
Danh sách được xếp theo thứ tự:
MSHV|HTHV|MMH1|DM1|MMH2|DM2|

Tương ứng với:
Mã số học viên|Họ tên học viên|Mã môn học 1|Điểm môn học 1|Mã môn học 2|Điểm môn học 2

Tất cả các dòng đều được xếp theo thứ tự này và cách nhau bằng ký tự '|'.
Mỗi dòng trong file dữ liệu thể hiện thông tin 1 học viên.

Phần mềm chỉ chấp nhận danh sách theo format này. Bất cứ danh sách theo format khác sẽ báo lỗi.
Một ví dụ về danh sách hợp lệ là file 'hocvien.dat' có trong phần mềm.

------------------------------
3.2. NHẬP ĐƯỜNG DẪN
------------------------------
Tệp tin 'file_handling.py' phụ trách việc nhập đường dẫn cho các tính năng cần nó.
file_handling.py có một function là file_path().

Function này hoạt động như sau:

- Đường dẫn file mặc định là file 'hocvien.dat' có trong chương trình.
  File này nằm cùng thư mục với các file python khác.
- Đường dẫn file người dùng nhập vào là dạng chuỗi (string).
  Nếu người dùng không nhập gì thì sẽ dùng đường dẫn file mặc định.
- Thông báo đường dẫn file qua terminal.
- Trả về giá trị là string chứa đường dẫn file.

Giá trị được trả về sẽ được các file khác sử dụng trong hàm open() để mở file,
từ đó thực thi các tính năng.
------------------------------
3.3. THÊM HỌC VIÊN
------------------------------
Tệp tin 'them_hoc_vien.py' phụ trách tính năng thêm học viên.
Tính năng thêm học viên hoạt động như sau:
- Import file_handling
- Mở file ra dùng open(file_handling.file_path(), "a"). Function file.path() trả về đường dẫn file.
- Yêu cầu người dùng nhập các thông tin của học viên.
- Quay trở lại giao diện chính khi hoàn tất.
------------------------------
3.3. XOÁ HỌC VIÊN
------------------------------
Tệp tin 'xoa_hoc_vien.py' phụ trách tính năng thêm học viên.
Tính năng xóa học viên hoạt động như sau:
- Import file_handling
- Mở file ra dùng open(file_handling.file_path(), "r"). Function file.path() trả về đường dẫn file.
- Dùng readlines() rồi lưu trữ nội dung file vào một list có tên 'danh_sach'.
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
  tiến hành nhập lại danh sách dữ liệu mới từ list danh_sach vào file dữ liệu
  bằng cách mở file ra dùng open(file_handling.file_path(), "w")
  và nhập dữ liệu.

  Nếu flag "Found" vẫn là False như ban đầu (không thể tìm được học viên),
  thông báo lại cho người dùng.

- Quay trở lại giao diện chính.

# Có một vấn đề hiện tại là cách làm này (copy toàn bộ file ra một list, xoá giá trị,
  rồi lại ghi đè list đó lên file) rất không tối ưu. Hiện tại chưa tìm được cách
  giải quyết cho vấn đề này.

------------------------------
3.4. SẮP XẾP DANH SÁCH THEO ĐIỂM
------------------------------
Tệp tin diem_so.py phụ trách tính năng sắp xếp danh sách theo điểm.
Các tính năng liên quan đến sắp xếp có sử dụng thư viện NumPy.

------------------------------
3.4.1. SẮP XẾP DANH SÁCH THEO ĐIỂM MỘT MÔN DM1/2
------------------------------
Cách thức hoạt động của tính năng sắp xếp theo điểm một môn như sau:
- Import file_handling
- Mở file ra dùng open(file_handling.file_path(), "r"). Function file.path() trả về đường dẫn file.
- Dùng readlines() rồi lưu trữ nội dung file vào một list có tên 'danh_sach'.
  Mỗi giá trị trong list tương ứng với một dòng trong file dữ liệu.
- Tạo 3 list list_mshv, list_hthv, list_dm1/list_dm2 (tuỳ theo môn nào được chọn; trong hướng dẫn này sẽ chọn dm1).
  3 list này lúc đầu sẽ rỗng; dùng để lưu trữ các giá trị MSHV, HTHV, và điểm.
- Dùng vòng lặp nhập từng giá trị trong từng dòng của file dữ liệu vào 3 list trên.
  Mỗi dòng trong file dữ liệu thể hiện thông tin 1 học viên.
  Mỗi giá trị của học viên được cách nhau bằng ký tự '|'.
  (chi tiết xin xem phần 3.1.)
  Khi vòng lặp hoàn tất, 3 list trên sẽ lưu trữ thông tin của danh sách.
- Tạo 3 mảng (array) NumPy np_mshv, np_hthv, np_dm1.
  3 mảng này sẽ nhận giá trị của list_mshv, list_hthv, list_dm1.
- Hiện tại 3 mảng này đều được sắp xếp với các giá trị tương ứng trong file dữ liệu.
  Ví dụ mảng list_mshv có [0] là "22950012", thì list_hthv có [0] là "Tran Hoang Nam",
  đúng như trong file dữ liệu.
- Sử dụng argsort() của numpy để tìm ra cách sắp xếp điểm từ bé đến lớn.

  argsort() của numpy sẽ trả về cách sắp xếp lại các mảng.
  Ví dụ có mảng a = np.array([1, 2, 5, 4, 0])
  Khi chạy a.argsort() sẽ trả về giá trị ([4, 0, 1, 3, 2]) với các số là vị trí các giá trị trong a
  sắp xếp theo thứ tự từ bé đến lớn.

  np_dm1.argsort() sẽ trả về cách sắp xếp theo thứ tự giá trị nhỏ nhất đến lớn nhất.
  Giá trị ở đây là điểm. Chúng ta gán sort_args = np_dm1.argsort()
  Từ đó chúng ta áp dụng cách sắp xếp sort_args cho cả ba mảng.

  Cơ bản là cả ba mảng đều đã được sắp xếp theo đúng thứ tự rồi nên khi áp dụng
  cùng một cách sắp xếp sẽ không bị loạn thứ tự.
- Vẽ bảng.
------------------------------
3.4.2. SẮP XẾP DANH SÁCH THEO ĐIỂM HAI MÔN DM1 VÀ DM2
------------------------------

------------------------------
3.4.3. CƠ CHẾ VẼ BẢNG
------------------------------
Cơ chế vẽ bảng sử dụng các toán tử string formatting của Python.
Chi tiết về các toán tử này xin tham khảo tài liệu của Python:
https://docs.python.org/2/library/stdtypes.html#string-formatting

