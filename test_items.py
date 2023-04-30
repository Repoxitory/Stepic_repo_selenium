#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(url)
    button = browser.find_elements(by=By.CSS_SELECTOR, value="button.btn")
    assert button, "Кнопка добавления в корзину - не найдена"
