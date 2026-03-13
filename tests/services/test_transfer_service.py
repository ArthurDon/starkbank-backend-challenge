from unittest.mock import patch
from services.transfer_service import create_transfer


def test_transfer_amount_minus_fee():

    invoice = {
        "id": "123",
        "amount": 2000,
        "fee": 100
    }

    with patch("starkbank.transfer.create") as mock_transfer:

        create_transfer(invoice)

        transfer_obj = mock_transfer.call_args[0][0][0]

        assert transfer_obj.amount == 1900