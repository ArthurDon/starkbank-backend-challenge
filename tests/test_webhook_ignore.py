from unittest.mock import patch
from app.main import webhook
import asyncio


class DummyRequest:
    async def json(self):
        return {
            "event": {
                "log": {
                    "type": "created",
                    "invoice": {
                        "amount": 1000,
                        "fee": 0
                    }
                }
            }
        }


def test_no_transfer_when_not_credited():

    with patch("starkbank.transfer.create") as mock_transfer:

        request = DummyRequest()

        asyncio.run(webhook(request))

        assert not mock_transfer.called
