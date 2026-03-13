from fastapi import APIRouter, Request
import logging
import config.stark_setup as stark_setup

from services.transfer_service import create_transfer

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/webhook")
async def webhook(req: Request):

    payload = await req.json()

    event = payload.get("event")
    log = event.get("log") if event else None

    if not log:
        logger.error("Invalid webhook payload")
        return {"status": "invalid payload"}

    event_type = log.get("type")
    invoice = log.get("invoice")

    logger.info(f"Webhook event: {event_type}")

    if invoice:
        logger.info(
            f"Invoice update | id={invoice.get('id')} | status={invoice.get('status')}"
        )

    if event_type != "credited":
        logger.info(f"Ignoring event type: {event_type}")
        return {"status": "ignored"}

    if not invoice:
        logger.error("Invoice data missing in webhook")
        return {"status": "invalid invoice"}

    create_transfer(invoice)

    return {"status": "ok"}