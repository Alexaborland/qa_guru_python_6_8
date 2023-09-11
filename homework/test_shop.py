"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.model import Product
from homework.model import Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        equal_quantity = product.quantity
        assert product.check_quantity(equal_quantity)

        less_quantity = product.quantity - 1
        assert product.check_quantity(less_quantity)

        more_quantity = product.quantity + 1
        assert not product.check_quantity(more_quantity)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        equal_quantity = product.quantity
        product.buy(equal_quantity)
        assert product.quantity == 0

        less_quantity = product.quantity - 1
        product.buy(less_quantity)
        assert product.quantity == 1

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            product.buy(10000)
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        pass


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_cart_add_product(self, cart, product):
        cart.add_product(product, 1)
        assert cart.products[product] == 1
        cart.add_product(product, 100)
        assert cart.products[product] == 101

    def test_cart_remove_product(self, cart, product):
        cart.add_product(product, 2)
        assert cart.products[product] == 2
        cart.remove_product(product, 1)
        assert cart.products[product] == 1

        cart.add_product(product, 100)
        cart.remove_product(product)
        assert cart.products == {}

        cart.add_product(product, 50)
        cart.remove_product(product, remove_count=25)
        assert cart.products[product] == 25

    def test_cart_remove_all_products(self, cart, product):
        cart.add_product(product, 100)
        cart.remove_product(product, 100)
        assert cart.products == {}

    def test_cart_remove_more_than_have(self, cart, product):
        cart.add_product(product, 50)
        cart.remove_product(product, 60)
        assert cart.products == {}

    def test_cart_clear(self, cart, product):
        cart.add_product(product, 100)
        cart.clear()
        assert cart.products == {}

    def test_card_get_total_price(self, cart, product):
        cart.add_product(product, 10)
        cart.get_total_price()
        assert cart.get_total_price() == 1000

    def test_card_buy_products(self, cart, product):
        cart = Cart()
        cart.add_product(product, 10)
        cart.buy()
        assert product.quantity == 990

    def test_card_buy_more_that_available(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()





