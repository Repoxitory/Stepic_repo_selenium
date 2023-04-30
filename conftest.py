#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="es", help="Set the language")


@pytest.fixture(scope="function")
def browser(request):
    print("\nЗапуск браузера для теста...")

    # Setup browser options
    language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser

    # Check the language...
    time.sleep(10)

    print("\nЗавершение работы браузера после теста...")
    browser.quit()  # Finish it!
