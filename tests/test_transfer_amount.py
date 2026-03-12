from unittest.mock import patch
from app.main import webhook
import asyncio


class DummyRequest:
    async def json(self):
        return {
            "event": {
                "log": {
                    "type": "credited",
                    "invoice": {
                        "amount": 2000,
                        "fee": 100
                    }
                }
            }
        }


def test_transfer_amount_minus_fee():

    with patch("starkbank.transfer.create") as mock_transfer:

        request = DummyRequest()

        asyncio.run(webhook(request))

        args = mock_transfer.call_args[0][0][0]

        assert args.amount == 1900
