# search-content-api
This is a vietnamese school project:
Xây dựng hệ thống truy vấn trên dữ liệu Wikipedia tiếng Việt.

- Viết chương trình đánh chỉ mục và truy vấn thông tin trên tập dữ liệu Wikipedia tiếng Việt.

- Sinh viên có thể sử dụng các thư viện có sẵn (chẳng hạn như lucene, minion, xapian)

- Tập dump của Wikipedia được giới hạn lại và lưu trong data.zip (thư mục chia sẻ nội dung môn

học trên Drive).

Định dạng của tập tin data.txt (giải nén của data.zip) gồm nhiều dòng, mỗi dòng là thông tin của

một bài viết, với cú pháp như sau.

<Địa chỉ>\t[<Tựa đề>]\t<Tóm lược>

\t: dấu tab

<>: định dạng trong đề bài này, không tồn tại trong dữ liệu

<Tóm lược> có được bằng 1 heuristic nên có thể tồn tại những thông tin

không mong muốn. Chúng ta cứ sử dụng toàn bộ thông tin cung cấp bởi

mỗi dòng trong data.txt.

- Ở mức độ đơn giản, chúng ta chỉ cần quan tâm các token ngăn cách bằng khoảng trắng thay vì

vấn đề từ (gồm nhiều chữ) trong tiếng Việt.

- Yêu cầu nộp bài:

o Source code (để xây dựng hệ thống chỉ mục và truy vấn)

o Các tập tin của hệ thống chỉ mục (tải lên Drive và nộp link)

o Báo cáo (cho cả phần 1 và phần 2 của bài tập này): mô tả cách thực hiện bài tập, cách sử

dụng chương trình đã viết. Một số ảnh chụp màn hình thể hiện thao tác truy vấn và kết

quả trả về.
