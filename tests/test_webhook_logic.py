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
                        "amount": 1000,
                        "fee": 0
                    }
                }
            }
        }


def test_transfer_created_on_credited_event():

    with patch("starkbank.transfer.create") as mock_transfer:

        request = DummyRequest()

        asyncio.run(webhook(request))

        assert mock_transfer.called
