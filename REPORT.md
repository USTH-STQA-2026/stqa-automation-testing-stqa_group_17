# REPORT — Kiểm thử Web UI Tự động
## Hệ thống Mượn sách Thư viện ABC | STQA Group 17

---

## 👥 Thông tin nhóm

| | Thông tin |
|---|---|
| **Tên nhóm** | Nhóm 17 |
| **Lớp** | STQA2A |
| **Học kỳ** | HK2 - 2025 - 2026 |
| **Hệ thống kiểm thử** | [https://stqa.rbc.vn](https://stqa.rbc.vn) |

| # | MSSV | Họ và tên | Vai trò |
|---|------|-----------|---------|
| 1 | 23BI14160 | Nguyễn Ngọc Minh Hiếu | Nhóm trưởng |
| 2 | 23BI141123 | Hua Thai Duong | Thành viên |
| 3 | BI11-161 | Phan Sỹ Long | Thành viên |

---

## 🛠️ Công nghệ & Công cụ sử dụng

| Công cụ | Phiên bản | Mục đích |
|---------|-----------|---------|
| **Python** | 3.12.1 | Ngôn ngữ lập trình test |
| **Playwright** | 1.49.1 | Browser automation framework |
| **pytest** | 8.3.4 | Test runner & assertion framework |
| **pytest-playwright** | 0.6.2 | Plugin tích hợp Playwright với pytest |
| **python-dotenv** | 1.1.0 | Quản lý biến môi trường |
| **Chromium** | Latest | Trình duyệt chạy test |

### Kỹ thuật đặc biệt — Flutter Web (CanvasKit)

Hệ thống [stqa.rbc.vn](https://stqa.rbc.vn) sử dụng **Flutter Web với CanvasKit renderer** — toàn bộ UI render trên `<canvas>`, không có HTML DOM thông thường. Nhóm đã áp dụng các kỹ thuật sau để tương tác:

- **Flutter Semantics Tree**: Bật `flt-semantics` elements ẩn để Playwright có thể tương tác
- **ARIA Selectors**: Dùng `aria-label`, `role` thay vì CSS class/ID thông thường
- **Smart Wait**: Dùng `wait_for_flutter()` thay vì `time.sleep()` để tránh race condition

---

## 📋 Kết quả kiểm thử

### Tổng quan

| Chỉ số | Kết quả |
|--------|---------|
| **Tổng số test case** | 12 |
| **PASSED** ✅ | 12 |
| **FAILED** ❌ | 0 |
| **SKIPPED** ⏭️ | 0 |
| **Tỉ lệ thành công** | **100%** |

---

### Chi tiết từng Test Case

#### 🔐 Đăng nhập — `test_login.py`

| TC | Tên test | Mô tả | Kết quả |
|----|----------|-------|---------|
| TC-01 | `test_login_success` | Đăng nhập với email/mật khẩu hợp lệ → kiểm tra tên user hoặc nút "Đăng xuất" xuất hiện | ✅ PASSED |
| TC-02 | `test_login_fail_wrong_password` | Đăng nhập với mật khẩu sai → kiểm tra thông báo "Mật khẩu không đúng" | ✅ PASSED |
| TC-03 | `test_login_fail_empty_fields` | Đăng nhập với trường trống → kiểm tra thông báo "Vui lòng nhập email và mật khẩu" | ✅ PASSED |

#### 🔍 Tìm kiếm & Lọc — `test_search.py`

| TC | Tên test | Mô tả | Kết quả |
|----|----------|-------|---------|
| TC-04 | `test_search_book_by_name` | Tìm kiếm từ khóa "Flutter" → kiểm tra có sách Flutter trong kết quả | ✅ PASSED |
| TC-05 | `test_search_book_no_result` | Tìm kiếm từ khóa không tồn tại → kiểm tra không hiện sách nào | ✅ PASSED |
| TC-06 | `test_filter_by_category` | Lọc theo thể loại "Công nghệ" → kiểm tra từng sách đều thuộc thể loại đó | ✅ PASSED |
| TC-07 | `test_search_by_author` | Tìm kiếm theo tên tác giả "Nguyễn Minh Đức" → kiểm tra có kết quả | ✅ PASSED |

#### 📚 Mượn & Trả sách — `test_borrow_return.py`

| TC | Tên test | Mô tả | Kết quả |
|----|----------|-------|---------|
| TC-08 | `test_borrow_book` | Mượn sách "Có sẵn" → xác nhận dialog → kiểm tra snackbar "Mượn sách thành công" | ✅ PASSED |
| TC-09 | `test_view_borrowed_books` | Chuyển sang tab "Mượn / Trả" → kiểm tra có sách đang mượn hiển thị | ✅ PASSED |
| TC-10 | `test_return_book` | Trả sách trong tab "Mượn / Trả" → kiểm tra snackbar "Trả sách thành công" | ✅ PASSED |

#### ⚙️ Chung — `test_general.py`

| TC | Tên test | Mô tả | Kết quả |
|----|----------|-------|---------|
| TC-11 | `test_logout` | Đăng xuất → kiểm tra nút "Đăng nhập" hoặc tiêu đề hệ thống xuất hiện | ✅ PASSED |
| TC-12 | `test_switch_language_to_english` | Chuyển ngôn ngữ sang EN → kiểm tra text tiếng Anh ("Library", "Books", "Logout") | ✅ PASSED |

---

## 🐛 Bugs phát hiện & cách xử lý

### Bug 1 — Race condition khi assert snackbar (TC-08, TC-10)

**Mô tả:**
Sau khi xác nhận mượn sách hoặc trả sách, test gọi `all_text_contents()` ngay lập tức trước khi snackbar kịp render → assertion thất bại dù thao tác thực tế đã thành công.

**Nguyên nhân gốc rễ:**
`wait_for_flutter` chưa được import trong `test_borrow_return.py` → không có cơ chế chờ UI cập nhật.

**Cách fix:**
```python
# Trước ❌ — đọc sem_text ngay, không chờ
sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
assert "thành công" in sem_text

# Sau ✅ — chờ snackbar xuất hiện trước
wait_for_flutter(page, text="Mượn sách thành công")
sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
assert "Mượn sách thành công" in sem_text
```

**Kết quả:** TC-08 và TC-10 chuyển từ FAILED → PASSED.

---

### Bug 2 — Assertion quá lỏng lẻo (TC-10)

**Mô tả:**
Assertion ban đầu dùng `"Có sẵn" in sem_text` để kiểm tra việc trả sách thành công. Điều kiện này luôn **TRUE** vì trang luôn có ít nhất 1 sách "Có sẵn" → test PASS dù trả sách thất bại.

**Cách fix:**
Thay bằng `wait_for_flutter(page, text="Trả sách thành công")` và assert đúng snackbar text.

---

## 🔍 Kỹ thuật & Pattern nổi bật

### 1. RIPR Model (TC-01)
Test `test_login_success` được viết theo mô hình **RIPR**:
- **R**eachability: Truy cập trang đăng nhập
- **I**nfection: Nhập dữ liệu kích hoạt logic
- **P**ropagation: Smart Wait cho state lan truyền ra UI
- **R**evealability: Assert phát hiện lỗi nếu có

### 2. Smart Wait thay vì `time.sleep()`
```python
# ❌ Hard sleep — chậm, không ổn định
time.sleep(5)

# ✅ Smart Wait — nhanh, ổn định
wait_for_flutter(page, text="Đăng xuất")
```

### 3. Flutter Semantics Selectors
```python
# Input field
input[aria-label="Email"]

# Button
flt-semantics[role="button"]:has-text("Đăng nhập")

# Tab
flt-semantics[role="tab"][aria-label="Mượn / Trả"]

# Book card
flt-semantics[role="group"][aria-label*="Mã: BOOK"]

# Book với trạng thái
flt-semantics[role="group"][aria-label*="Có sẵn"]
```

### 4. Screenshot tự động
Mỗi test case chụp màn hình tại thời điểm assert và lưu vào thư mục `screenshots/`:

| File | Test case |
|------|-----------|
| `login_success.png` | TC-01 |
| `login_fail_wrong_password.png` | TC-02 |
| `login_fail_empty_fields.png` | TC-03 |
| `tc04_search_by_name.png` | TC-04 |
| `tc05_search_no_result.png` | TC-05 |
| `tc06_filter_by_category.png` | TC-06 |
| `tc07_search_by_author.png` | TC-07 |
| `tc08_borrow_book.png` | TC-08 |
| `tc09_view_borrowed_books.png` | TC-09 |
| `tc10_return_book.png` | TC-10 |
| `logout.png` | TC-11 |
| `switch_lang_to_english.png` | TC-12 |

---

## 📊 Nhận xét & Đánh giá

### Điểm mạnh của bộ test
- **Tỉ lệ PASS 100%** — tất cả 12 test case đều chạy thành công
- **Không dùng `time.sleep()`** — toàn bộ sử dụng Smart Wait, ổn định và nhanh hơn
- **Coverage đầy đủ** — bao phủ các luồng chính: đăng nhập, tìm kiếm, mượn/trả, đăng xuất, đổi ngôn ngữ
- **Screenshot tự động** — hỗ trợ debug trực quan khi test thất bại
- **Assertion rõ ràng** — thông báo lỗi bằng cả tiếng Anh lẫn tiếng Việt

### Hạn chế & hướng cải thiện
- Chưa test **negative case** cho mượn/trả (VD: mượn sách đã hết)
- Chưa test **giới hạn mượn** (số sách tối đa được mượn cùng lúc)
- Có thể bổ sung **pytest-html** để xuất báo cáo HTML đẹp hơn
- Nên thêm **parametrize** để test nhiều tài khoản hoặc từ khóa khác nhau

---

## ▶️ Hướng dẫn chạy lại test

```bash
# 1. Cài dependencies (chỉ làm 1 lần)
pip install -r requirements.txt
playwright install chromium

# 2. Tạo file .env từ template
copy .env.example .env
# Điền TEST_EMAIL, TEST_PASSWORD, TEST_DISPLAY_NAME

# 3. Chạy toàn bộ test
pytest

# 4. Chạy từng file
pytest tests/test_login.py
pytest tests/test_search.py
pytest tests/test_borrow_return.py
pytest tests/test_general.py
```

> ⚠️ Cần có file `.env` với thông tin tài khoản hợp lệ trên [https://stqa.rbc.vn](https://stqa.rbc.vn) trước khi chạy test.

---

*Báo cáo được tạo bởi Nhóm 17 — STQA2A — HK2 2025-2026*
