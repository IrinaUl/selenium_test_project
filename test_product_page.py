from .pages.product_page import ProductPage
import pytest

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
pages_list = [f'{link}?promo=offer{i}' for i in range(10)]
pages_list[7] = pytest.param(pages_list[7], marks=pytest.mark.xfail)

@pytest.mark.parametrize('link', pages_list)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_page()