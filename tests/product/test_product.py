from inventory_report.product import Product


def test_create_product() -> None:
    initi = Product(
        "123",
        "geladeira",
        "vale",
        "19/11/1999",
        "19/11/2024",
        "123456",
        "vai dar certo",
    )

    assert initi.id == "123"
    assert initi.product_name == "geladeira"
    assert initi.company_name == "vale"
    assert initi.manufacturing_date == "19/11/1999"
    assert initi.expiration_date == "19/11/2024"
    assert initi.serial_number == "123456"
    assert initi.storage_instructions == "vai dar certo"
