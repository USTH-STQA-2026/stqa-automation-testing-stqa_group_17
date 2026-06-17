
import os
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, SCREENSHOT_DIR,wait_for_flutter,
)


def test_search_book_by_name(page, test_config):
    """TC-04: Search book by name – results found (*Tìm kiếm sách theo tên — tìm thấy kết quả*)"""

    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)

    login(page, test_config)
    wait_for_flutter(page)

    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Flutter")
    wait_for_flutter(page)

    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc04_search_by_name.png"))

    assert page.locator('flt-semantics[aria-label*="Flutter"]').count() > 0


def test_search_book_no_result(page, test_config):
    """TC-05: Search book – no results (*Tìm kiếm sách — không có kết quả*)"""
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    
    login(page, test_config)
    wait_for_flutter(page)

    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "xyz_khong_ton_tai_12345")
    wait_for_flutter(page)

    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc05_search_no_result.png"))

    assert page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]').count() == 0



def test_filter_by_category(page, test_config):
    """TC-06: Filter books by category 'Công nghệ' (*Lọc sách theo thể loại 'Công nghệ'*) """
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    
    login(page, test_config)
    wait_for_flutter(page)

    flutter_fill(page, "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)", "Công nghệ")
    wait_for_flutter(page)

    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc06_filter_by_category.png"))

    book_list = page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]')
    book_count = book_list.count()
    
    assert book_count > 0, "Không có sách nào hiển thị để kiểm tra"
    
    for i in range(book_count):
        aria_label = book_list.nth(i).get_attribute("aria-label")
        assert "Công nghệ" in aria_label


def test_search_by_author(page, test_config):
    """TC-07: Search book by author name (*Tìm kiếm sách theo tên tác giả*)"""
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    
    login(page, test_config)
    wait_for_flutter(page)

    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Nguyễn Minh Đức")
    wait_for_flutter(page)
    
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc07_search_by_author.png"))

    assert page.locator('flt-semantics[aria-label*="Nguyễn Minh Đức"]').count() > 0