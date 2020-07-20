def test_add_to_basket(request, browser):
    elements = browser.find_elements_by_css_selector('.btn-add-to-basket')
    assert len(elements) == 1, 'The number of elements per page is not equal to one'
