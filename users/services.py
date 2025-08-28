import stripe

from config.settings import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY



def create_stripe_price(amount, product):
    """Создание цены в страйпе"""

    return stripe.Price.create(
        currency="rub",
        unit_amount=int(amount * 100),
        product_data={"name": product.name},

    )

def create_stripe_session(price):
    """Создание сессии на оплату в страйпе"""

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/success",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")


def create_stripe_product(product):
    """Создание продукта в страйпе"""

    return stripe.Product.create(
        name=product.name
    )
