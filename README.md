[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ZpUiBug-)
# STQA Library Automation — Starter Template

Bài tập thực hành **Kiểm thử Web UI tự động** cho môn **Kiểm thử và Đảm bảo chất lượng phần mềm (STQA)**.
(*A hands-on **Automated Web UI Testing** assignment for the **Software Testing & Quality Assurance (STQA)** course.*)

Sử dụng **Playwright + Python** để kiểm thử hệ thống Mượn sách Thư viện ABC tại [https://stqa.rbc.vn](https://stqa.rbc.vn).
(*Uses **Playwright + Python** to test the Library Book Borrowing System.*)

> **📚 Hệ thống hư cấu / Fictional System**: Thư viện ABC là hệ thống **hư cấu** được thiết kế cho mục đích học tập. Tên nhân vật, tổ chức và dữ liệu đều là giả lập. / *ABC Library is a **fictional** system designed for educational purposes. All names, organizations, and data are simulated.*

---

## 👥 Thông tin nhóm / Team Information

> **⚠️ Sinh viên: Điền thông tin nhóm vào bảng dưới đây trước khi nộp bài.**

|              | Thông tin                    |
| ------------ | ---------------------------- |
| **Tên nhóm** | `<!-- VD: Nhóm 1 -->`        |
| **Lớp**      | `<!-- VD: SE001.P11 -->`     |
| **Học kỳ**   | `<!-- VD: HK2 2025-2026 -->` |

| #   | MSSV | Họ và tên | Vai trò     |
| --- | ---- | --------- | ----------- |
| 1   |      |           | Nhóm trưởng |
| 2   |      |           | Thành viên  |
| 3   |      |           | Thành viên  |
| 4   |      |           | Thành viên  |

---

## 📖 Trước khi bắt đầu — Bối cảnh / Before You Start — Context

### Bài tập này nằm ở đâu trong quy trình?

```
SRS (Yêu cầu phần mềm) → Dev xây hệ thống → A1: Kiểm thử thủ công → A2: Kiểm thử tự động (BẠN Ở ĐÂY)
```

Ở bài **A1** (nếu đã làm), bạn đã kiểm thử thủ công: mở trình duyệt, nhấn nút, ghi kết quả. Bây giờ ở **A2**, bạn sẽ **tự động hóa** các thao tác đó bằng code.

### Những ai liên quan? (*Stakeholders*)

| Vai trò         | Ai?            | Liên quan thế nào?                                                                                          |
| --------------- | -------------- | ----------------------------------------------------------------------------------------------------------- |
| **Khách hàng**  | Thư viện ABC   | Đưa ra yêu cầu nghiệp vụ ([BRD](docs/BRD-yeu-cau-nghiep-vu.md)) → BA viết [SRS](docs/SRS-library-system.md) |
| **Dev Team**    | Nhóm lập trình | Xây hệ thống                                                                                                |
| **Tester / QC** | **Bạn**        | Viết automated test, phát hiện lỗi                                                                          |
| **QA Lead**     | Giảng viên     | Review kết quả test                                                                                         |

### Tester dựa vào đâu để kiểm thử?

| Nguồn                      | Trong bài này                                                    |
| -------------------------- | ---------------------------------------------------------------- |
| **SRS** (đặc tả yêu cầu)   | [docs/SRS-library-system.md](docs/SRS-library-system.md) — 8 REQ |
| **Test accounts**          | [docs/test-accounts.md](docs/test-accounts.md) — 6 tài khoản     |
| **A1 test cases** (nếu có) | Tham khảo TC thủ công để viết code tự động                       |

### Software Testing vs Quality Assurance

|                  | **Testing** (Bài này)                             | **QA**                                       |
| ---------------- | ------------------------------------------------- | -------------------------------------------- |
| **Bạn đang làm** | ✅ Viết automated test, chạy test, chụp screenshot | Bonus B4: Viết REPORT.md đánh giá chất lượng |
| **Mục đích**     | Tìm lỗi tự động, nhanh, lặp lại được              | Đánh giá quy trình, đề xuất cải tiến         |

---

> ⚠️ Website sử dụng **Flutter Web (CanvasKit renderer)** — toàn bộ giao diện render trên `<canvas>`, không có HTML DOM thông thường. Dự án đã cung cấp sẵn các helper function để tương tác qua **Accessibility Semantics Tree**.
>
> (*The website uses **Flutter Web (CanvasKit renderer)** — the entire UI is rendered on `<canvas>`, with no standard HTML DOM. This project provides helper functions to interact via the Accessibility Semantics Tree.*)

---

## 📁 Cấu trúc dự án / Project Structure

```
stqa-library-automation-starter/
├── conftest.py          # Fixtures & helper functions (COMPLETE / ĐÃ HOÀN CHỈNH)
├── web_detector.py      # Web technology detector module (COMPLETE / ĐÃ HOÀN CHỈNH)
├── pytest.ini           # pytest configuration (Cấu hình pytest)
├── requirements.txt     # Dependencies
├── .env.example         # Environment variable template (Template biến môi trường)
├── .gitignore
├── LICENSE
├── README.md
└── tests/
    ├── test_login.py           # TC-01 (example / mẫu) + TC-02, TC-03 (TODO)
    ├── test_search.py          # TC-04 ~ TC-07 (TODO)
    ├── test_borrow_return.py   # TC-08 ~ TC-10 (TODO)
    └── test_general.py         # TC-11 ~ TC-12 (TODO)
```

---

## 🚀 Cài đặt / Installation

### 1. Clone repo & tạo môi trường ảo

```bash
git clone <repo-url>
cd stqa-library-automation-starter
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
# venv\Scripts\activate    # Windows
```

### 2. Cài đặt dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. Cấu hình biến môi trường

Tạo file `.env` từ template:

```bash
cp .env.example .env
```

Sửa `.env` với thông tin đăng nhập của bạn:

```
BASE_URL=https://stqa.rbc.vn
TEST_EMAIL=your_email@example.com
TEST_PASSWORD=your_password
TEST_DISPLAY_NAME=Your Display Name
```

> ⚠️ **KHÔNG commit file `.env`** — file này đã được thêm vào `.gitignore`.

---

## ▶️ Chạy test / Running Tests

```bash
# Run all tests (Chạy tất cả test)
pytest

# Run a specific file (Chạy 1 file cụ thể)
pytest tests/test_login.py

# Run a specific test case (Chạy 1 test case cụ thể)
pytest tests/test_login.py::test_login_success

# Verbose output (Hiện output chi tiết)
pytest -v -s
```

Screenshot được lưu tự động vào thư mục `screenshots/`.

---

## 🤖 CI với GitHub Actions (cho sinh viên)

Repo đã có workflow CI tại `.github/workflows/pytest-ci.yml` và sẽ tự chạy khi:

- Có `push` lên repo
- Có `pull_request`

CI sẽ thực hiện:

1. Cài Python + dependencies
2. Cài Playwright Chromium
3. Chạy `pytest --junitxml=report.xml`
4. Upload artifacts gồm:
  - `report.xml`
  - `screenshots/**`

### Cách xem kết quả CI

1. Vào tab **Actions** trên GitHub
2. Mở run mới nhất của workflow **Pytest CI**
3. Kéo xuống phần **Artifacts** để tải `pytest-artifacts`
4. Mở `report.xml` để xem kết quả theo chuẩn JUnit XML

### Chính sách public repo

- Workflow này chỉ chạy các test đang có trong thư mục `tests/` của repo public.
- Không thêm hidden tests vào repo public.

---

## 📋 Danh sách Test Case / Test Case List

| TC    | Mô tả                                                | File                    | Trạng thái |
| ----- | ---------------------------------------------------- | ----------------------- | ---------- |
| TC-01 | Đăng nhập thành công (*Login success*)               | `test_login.py`         | ✅ Mẫu      |
| TC-02 | Đăng nhập thất bại — sai mật khẩu (*Wrong password*) | `test_login.py`         | 🔴 TODO     |
| TC-03 | Đăng nhập thất bại — để trống (*Empty fields*)       | `test_login.py`         | 🔴 TODO     |
| TC-04 | Tìm sách theo tên (*Search by name*)                 | `test_search.py`        | 🔴 TODO     |
| TC-05 | Tìm sách — không có kết quả (*No result*)            | `test_search.py`        | 🔴 TODO     |
| TC-06 | Lọc theo thể loại (*Filter by category*)             | `test_search.py`        | 🔴 TODO     |
| TC-07 | Tìm theo tác giả (*Search by author*)                | `test_search.py`        | 🔴 TODO     |
| TC-08 | Mượn sách (*Borrow a book*)                          | `test_borrow_return.py` | 🔴 TODO     |
| TC-09 | Xem sách đang mượn (*View borrowed books*)           | `test_borrow_return.py` | 🔴 TODO     |
| TC-10 | Trả sách (*Return a book*)                           | `test_borrow_return.py` | 🔴 TODO     |
| TC-11 | Đăng xuất (*Logout*)                                 | `test_general.py`       | 🔴 TODO     |
| TC-12 | Chuyển ngôn ngữ sang EN (*Switch language*)          | `test_general.py`       | 🔴 TODO     |

**Yêu cầu:** Hoàn thành tất cả 11 test case còn lại (TC-02 → TC-12).

---

## 🔧 Các hàm hỗ trợ có sẵn / Available Helper Functions

Các hàm đã được cung cấp trong `conftest.py` — **KHÔNG cần tự viết lại**.
(*These functions are provided in `conftest.py` — you do NOT need to rewrite them.*)

### Flutter Web helpers

| Hàm                                 | Mô tả                                                                                     |
| ----------------------------------- | ----------------------------------------------------------------------------------------- |
| `enable_flutter_semantics(page)`    | Bật Semantics Tree — bắt buộc trước khi tương tác (*Enable Accessibility Semantics Tree*) |
| `flutter_fill(page, label, value)`  | Nhập text vào input field (*Fill text into an input field using `aria-label`*)            |
| `flutter_click_button(page, text)`  | Click button theo text hiển thị (*Click a button by its displayed text*)                  |
| `wait_for_flutter(page, text, ...)` | Smart Wait — chờ Semantics Tree cập nhật (*Wait for Flutter Semantics Tree update*)       |

### Universal helpers

| Hàm                                    | Mô tả                                                                       |
| -------------------------------------- | --------------------------------------------------------------------------- |
| `smart_fill(page, label, value, tech)` | Tự chọn cách nhập phù hợp (*Auto-select fill strategy*)                     |
| `smart_click(page, text, tech)`        | Tự chọn cách click phù hợp (*Auto-select click strategy*)                   |
| `login(page, test_config)`             | Đăng nhập với credentials từ `.env` (*Log in with credentials from `.env`*) |

### Fixtures

| Fixture       | Mô tả                                                                                |
| ------------- | ------------------------------------------------------------------------------------ |
| `page`        | Context mới cho mỗi test (*Playwright Page object — fresh browser context per test*) |
| `test_config` | Dict chứa `base_url`, `email`, `password`, `display_name`, `screenshot_dir`          |
| `web_tech`    | Thông tin công nghệ web (*WebTech object — detected web technology info*)            |

---

## 💡 Cách tương tác với Flutter Web / How to Interact with Flutter Web

Flutter Web (CanvasKit) render mọi thứ lên `<canvas>` — **không có HTML DOM thông thường**. Để test, ta cần:
(*Flutter Web (CanvasKit) renders everything onto `<canvas>` — there is no standard HTML DOM. To test, we need to:*)

1. **Bật Semantics Tree**: Gọi `enable_flutter_semantics(page)` → Flutter tạo các elements ẩn `<flt-semantics>` phủ lên canvas
2. **Tương tác qua ARIA attributes**:
   - Input fields: `input[aria-label="Email"]`
   - Buttons: `flt-semantics[role="button"]:has-text("Đăng nhập")`
   - Tabs: `flt-semantics[role="tab"][aria-label="Mượn / Trả"]`
   - Groups (book cards / card sách): `flt-semantics[role="group"][aria-label*="Mã: BOOK"]`

### Ví dụ pattern cơ bản / Basic Pattern Example

```python
from conftest import login, flutter_fill, wait_for_flutter

def test_example(page, test_config):
    # 1. Đăng nhập
    login(page, test_config)

    # 2. Tìm element và tương tác
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Flutter")

    # 3. Smart Wait: chờ kết quả xuất hiện (thay vì time.sleep)
    wait_for_flutter(page, text="Flutter")

    # 4. Kiểm tra kết quả qua semantics
    result = page.locator('flt-semantics[aria-label*="Flutter"]')
    assert result.count() > 0, "Không tìm thấy kết quả"

    # 5. Hoặc lấy toàn bộ text từ semantics
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Flutter" in sem_text
```

### Lưu ý quan trọng / Important Notes

- Luôn gọi `enable_flutter_semantics(page)` sau khi navigate hoặc sau thao tác thay đổi DOM
- Dùng **Smart Wait** thay vì `time.sleep()`:
  - `wait_for_flutter(page, text="...")` — chờ text xuất hiện trong Semantics Tree
  - `page.locator("...").wait_for()` — chờ element cụ thể
  - Xem comment trong `conftest.py` để biết chi tiết các cách chờ
- Sau khi fill input, Flutter có thể tạo input ẩn trong `<flt-text-editing-host>` — helper `flutter_fill()` đã xử lý điều này

---

## 📚 Tài liệu tham khảo / References

### Tài liệu dự án

| Bạn muốn...                  | Đi đến                                                         |
| ---------------------------- | -------------------------------------------------------------- |
| Xem đề bài + rubric          | [docs/ASSIGNMENT.md](docs/ASSIGNMENT.md)                       |
| Đọc yêu cầu hệ thống (SRS)   | [docs/SRS-library-system.md](docs/SRS-library-system.md)       |
| Xem yêu cầu nghiệp vụ (BRD)  | [docs/BRD-yeu-cau-nghiep-vu.md](docs/BRD-yeu-cau-nghiep-vu.md) |
| Xem tài khoản test           | [docs/test-accounts.md](docs/test-accounts.md)                 |
| **Liên kết textbook ↔ repo** | [docs/textbook-concepts.md](docs/textbook-concepts.md)         |
| **Bài tập nhóm thảo luận**   | [docs/group-exercises.md](docs/group-exercises.md)             |

### Liên kết bên ngoài

- [Playwright Python Docs](https://playwright.dev/python/)
- [Playwright Locators](https://playwright.dev/python/docs/locators)
- [Flutter Web Accessibility](https://docs.flutter.dev/ui/accessibility)
- [pytest Documentation](https://docs.pytest.org/)
