from unittest.mock import patch
from jobs.invoice_generator_job import create_invoices


def test_invoice_generator_creates_batch():

    with patch("starkbank.invoice.create") as mock_create:

        create_invoices()

        assert mock_create.called