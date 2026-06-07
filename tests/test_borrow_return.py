"""
Borrow & Return Tests (*Kiểm thử Mượn & Trả sách*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

Students must complete ALL 3 test cases in this file.
(*Sinh viên cần hoàn thành TẤT CẢ 3 test case trong file này.*)

Hints (*Gợi ý*):
    - Use login() helper to log in (*Dùng login() helper để đăng nhập*)
    - "Mượn / Trả" tab: role="tab", aria-label="Mượn / Trả"
    - Available books have "Có sẵn" in aria-label, borrowed books have "Đang mượn"
      (*Sách "Có sẵn" có aria-label chứa "Có sẵn", sách "Đang mượn" chứa "Đang mượn"*)
    - Borrow button: 'flt-semantics[role="button"]:has-text("Mượn sách này")'
      (*Nút mượn*)
    - After clicking "Mượn sách này", a confirmation dialog appears — click "Mượn" again
      (*Sau khi click "Mượn sách này" sẽ hiện dialog xác nhận — cần click nút "Mượn" lần nữa*)
    - Return button: 'flt-semantics[role="button"]:has-text("Trả sách")'
      (*Nút trả*)
"""
import os
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, SCREENSHOT_DIR, wait_for_flutter,
)


def test_borrow_book(page, test_config):
    """TC-08: Borrow an available book (*Mượn sách có trạng thái 'Có sẵn'*)

    🔴 COMPLETED (*HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → find an "Available" book → click "Mượn sách này" → confirm dialog
        → verify book status changes to "Borrowed".
        (*Đăng nhập → tìm sách "Có sẵn" → click "Mượn sách này" → xác nhận dialog
        → kiểm tra sách chuyển sang trạng thái "Đang mượn".*)

    Suggested steps (*Gợi ý các bước*):
        1. login(page, test_config)
        2. Find available book: page.locator('flt-semantics[role="group"][aria-label*="Có sẵn"]')
           (*Tìm sách Có sẵn*)
        3. Click "Mượn sách này" button inside that book card
           (*Click nút "Mượn sách này" trong sách đó*)
        4. Wait for confirmation dialog, re-enable semantics
           (*Đợi dialog xác nhận, bật lại semantics*)
        5. Click "Mượn" button (confirm button in dialog)
           (*Click nút "Mượn" — nút xác nhận trong dialog*)
        6. Assert: "Đang mượn" or "thành công" appears
           (*Assert: "Đang mượn" hoặc "thành công" xuất hiện*)
    """
    # Step 1: Log in
    login(page, test_config)

    # Step 2: Find an available book ("Có sẵn")
    available_book = page.locator('flt-semantics[role="group"][aria-label*="Có sẵn"]').first
    available_book.wait_for(state="attached", timeout=10000)

    # Step 3: Click "Mượn sách này" button inside that book card
    borrow_btn = page.locator('flt-semantics[role="button"]:has-text("Mượn sách này")').first
    borrow_btn.wait_for(state="attached", timeout=10000)
    borrow_btn.click()

    # Step 4: Wait for confirmation dialog, re-enable semantics
    enable_flutter_semantics(page)

    # Step 5: Click "Mượn" button to confirm in the dialog
    confirm_btn = page.locator('flt-semantics[role="button"]:has-text("Mượn")').first
    confirm_btn.wait_for(state="attached", timeout=10000)
    confirm_btn.click()

    # Re-enable semantics after dialog closes
    enable_flutter_semantics(page)

    # Step 6: Wait for success snackbar "Mượn sách thành công!" to appear
    # (Root cause of original failure: sem_text was read too fast before snackbar appeared
    #  — wait_for_flutter was not imported, causing a race condition)
    wait_for_flutter(page, text="Mượn sách thành công")

    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc08_borrow_book.png"))

    # Step 7: Assert snackbar text is visible on current page
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    has_borrowed = "Mượn sách thành công" in sem_text or "thành công" in sem_text

    assert has_borrowed, \
        "Borrow failed: success snackbar 'Mượn sách thành công' not found " \
        "(Mượn thất bại: không thấy thông báo 'Mượn sách thành công')"


def test_view_borrowed_books(page, test_config):
    """TC-09: View borrowed books list (*Xem danh sách sách đang mượn — tab Mượn / Trả*)

    🔴 COMPLETED (*HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → switch to "Mượn / Trả" tab → verify borrowed books are shown.
        (*Đăng nhập → chuyển sang tab "Mượn / Trả" → kiểm tra có sách đang mượn.*)

    Hints (*Gợi ý*):
        - Click tab: page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]')
        - Verify: books with "Đang mượn" in aria-label, or "Trả sách" button exists
          (*Kiểm tra: có sách với aria-label chứa "Đang mượn" hoặc có nút "Trả sách"*)
    """
    # Step 1: Log in
    login(page, test_config)

    # Step 2: Switch to "Mượn / Trả" tab
    tab = page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]').first
    tab.wait_for(state="attached", timeout=10000)
    tab.click()

    # Re-enable semantics after tab switch
    enable_flutter_semantics(page)

    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc09_view_borrowed_books.png"))

    # Step 3: Verify borrowed books are shown —
    # either books with "Đang mượn" in aria-label OR "Trả sách" button exists
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    has_borrowed_books = (
        page.locator('flt-semantics[aria-label*="Đang mượn"]').count() > 0
        or page.locator('flt-semantics[role="button"]:has-text("Trả sách")').count() > 0
        or "Đang mượn" in sem_text
        or "Trả sách" in sem_text
    )

    assert has_borrowed_books, \
        "No borrowed books found in 'Mượn / Trả' tab " \
        "(Không tìm thấy sách đang mượn trong tab 'Mượn / Trả')"


def test_return_book(page, test_config):
    """TC-10: Return a borrowed book (*Trả sách đang mượn*)

    🔴 COMPLETED (*HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → go to "Mượn / Trả" tab → click "Trả sách" → verify book is returned.
        (*Đăng nhập → tab "Mượn / Trả" → click "Trả sách" → kiểm tra sách được trả.*)

    Hints (*Gợi ý*):
        - Switch to "Mượn / Trả" tab (*Chuyển tab "Mượn / Trả"*)
        - Find return button: page.locator('flt-semantics[role="button"]:has-text("Trả sách")')
          (*Tìm nút "Trả sách"*)
        - Click and verify status change or success message
          (*Click và kiểm tra sách chuyển trạng thái hoặc có thông báo thành công*)
    """
    # Step 1: Log in
    login(page, test_config)

    # Step 2: Switch to "Mượn / Trả" tab
    tab = page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]').first
    tab.wait_for(state="attached", timeout=10000)
    tab.click()

    # Re-enable semantics after tab switch
    enable_flutter_semantics(page)

    # Step 3: Find and click "Trả sách" button
    return_btn = page.locator('flt-semantics[role="button"]:has-text("Trả sách")').first
    return_btn.wait_for(state="attached", timeout=10000)
    return_btn.click()

    # Re-enable semantics after action
    enable_flutter_semantics(page)

    # Step 4: Wait for success snackbar "Trả sách thành công!" to appear
    # (Same fix as test_borrow_book — must wait before reading sem_text to avoid race condition)
    wait_for_flutter(page, text="Trả sách thành công")

    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc10_return_book.png"))

    # Step 5: Assert snackbar is visible on current page
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    has_returned = "Trả sách thành công" in sem_text or "thành công" in sem_text

    assert has_returned, \
        "Return failed: success snackbar 'Trả sách thành công' not found " \
        "(Trả sách thất bại: không thấy thông báo 'Trả sách thành công')"
