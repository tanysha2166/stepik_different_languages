url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_is_present(browser):
    browser.get(url)
    browser.implicitly_wait(5)
    assert browser.find_elements_by_class_name("btn-add-to-basket"), "No add to card button"
