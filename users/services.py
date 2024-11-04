import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(prod):
    """Создает продукт в страйпе."""
    product_name = prod.course.name if prod.course else "Неизвестный продукт"
    stripe_product = stripe.Product.create(name=product_name)
    return stripe_product.get('id')


def create_stipe_price(amount, product_id):
    """Создает цену курса."""
    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": product_id},
    )


def create_stipe_session(price):
    """Создает сессию на оплату страйпе."""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
