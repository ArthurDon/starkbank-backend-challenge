from unittest.mock import patch
from app.main import webhook
import pytest


class FakeRequest:
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


@pytest.mark.asyncio
@patch("starkbank.transfer.create")
async def test_transfer_amount_minus_fee(mock_transfer):

    request = FakeRequest()

    await webhook(request)

    transfer_list = mock_transfer.call_args.args[0]
    transfer = transfer_list[0]

    assert transfer.amount == 1900
