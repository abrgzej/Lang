import pytest

def test_add_to_basket(request, browser):
    language = request.config.getoption("language")
    browser.get(f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/')
    elements = browser.find_elements_by_css_selector('.btn-add-to-basket')
    assert len(elements) == 1, 'Количество элементов на странице не равно одному'