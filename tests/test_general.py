
import os
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, SCREENSHOT_DIR, wait_for_flutter,
)


def test_logout(page, test_config):
   
    #Access page, enable semantics, login, then click logout
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    login(page, test_config)
    flutter_click_button(page, "Đăng xuất")

    #Wait for login button to appear and take screenshot
    wait_for_flutter(page, text="Đăng nhập")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "logout.png"))

    #Check if login button is visible in semantics to confirm logout success 
    sem_text= " ".join(page.locator("flt-semantics").all_text_contents())
    has_title= "Hệ thống Mượn sách thư viện" in sem_text
    has_login_btn= "Đăng nhập" in sem_text

    assert has_title or has_login_btn, \
        f"Logout failed"

def test_switch_language_to_english(page, test_config):
    
    #Access page, enable semantics, login, then click "EN" to switch to English
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    login(page, test_config)
    flutter_click_button(page, "EN")

    #Wait for English text to appear and take screenshot
    wait_for_flutter(page, text="Library")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "switch_lang_to_english.png"))

    #Check if English text is visible in semantics to confirm language switch success
    sem_text= " ".join(page.locator("flt-semantics").all_text_contents())
    en_lib= "Library" in sem_text
    en_books= "Books" in sem_text
    en_logout= "Logout" in sem_text

    assert en_lib or en_lib or en_logout, \
        f"Language switch failed"

