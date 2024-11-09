from shopping_cart import ShoppingCart


def test_can_add_items_to_cart():
    cart = ShoppingCart()
    cart.add("apple")
    assert cart.size()==1