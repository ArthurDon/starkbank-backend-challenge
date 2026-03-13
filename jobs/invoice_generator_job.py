import starkbank
import config.stark_setup as stark_setup
import random


def create_invoices():
    quantity = random.randint(8, 12)

    invoices = []

    for i in range(quantity):
        invoices.append(
            starkbank.Invoice(
                amount=random.randint(1000, 10000),
                name=f"Customer {i}",
                tax_id="012.345.678-90"
            )
        )

    created = starkbank.invoice.create(invoices)

    print(f"{len(created)} invoices created")


if __name__ == "__main__":
    create_invoices()
