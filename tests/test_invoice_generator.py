from app.invoice_generator import create_invoices


def test_invoice_quantity_range(monkeypatch):

    created = []

    def mock_create(invoices):
        created.extend(invoices)
        return invoices

    monkeypatch.setattr("starkbank.invoice.create", mock_create)

    create_invoices()

    assert 8 <= len(created) <= 12
