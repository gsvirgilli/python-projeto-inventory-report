from inventory_report.product import Product


def test_product_report() -> None:
    initi = Product(
        "123",
        "geladeira",
        "vale",
        "19/11/1999",
        "19/11/2024",
        "123456",
        "vai dar certo",
    )

    expected_output = (
        "The product 123 - geladeira "
        "with serial number 123456 "
        "manufactured on 19/11/1999 "
        "by the company vale "
        "valid until 19/11/2024 "
        "must be stored according to the following instructions: "
        "vai dar certo."
    )

    assert str(initi) == expected_output
