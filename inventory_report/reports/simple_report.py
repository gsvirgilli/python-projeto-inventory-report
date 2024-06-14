from inventory_report.inventory import Inventory
from typing import List
from datetime import datetime
from collections import Counter


class SimpleReport:
    def __init__(self) -> None:
        self.inventories: List[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def generate(self) -> str:
        closest_expiration_date = self.get_closest_expiration_date()
        oldest_manufacturing_date = self.get_oldest_manufacturing_date()
        largest_inventory_co = self.get_largest_inventory_company()
        return (
            f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
            f"Closest expiration date: {closest_expiration_date}\n"
            f"Company with the largest inventory: {largest_inventory_co}"
        )

    def get_closest_expiration_date(self) -> str:
        current_date = datetime.now()
        return min(
            datetime.strptime(product.expiration_date, "%Y-%m-%d")
            for inventory in self.inventories
            for product in inventory.data
            if datetime.strptime(product.expiration_date, "%Y-%m-%d")
            > current_date
        ).strftime("%Y-%m-%d")

    def get_oldest_manufacturing_date(self) -> str:
        return min(
            product.manufacturing_date
            for inventory in self.inventories
            for product in inventory.data
        )

    def get_largest_inventory_company(self) -> str:
        company_counts = Counter(
            product.company_name
            for inventory in self.inventories
            for product in inventory.data
        )
        return max(company_counts, key=company_counts.get)
