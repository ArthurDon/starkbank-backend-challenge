from fastapi import FastAPI, Request
import starkbank
import config.stark_setup as stark_setup
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/webhook")
async def webhook(req: Request):

    payload = await req.json()
    logger.info(f"Webhook received: {payload}")

    event = payload.get("event")
    log = event.get("log") if event else None

    if not log:
        logger.error("Invalid webhook payload")
        return {"status": "invalid payload"}

    event_type = log.get("type")

    if event_type != "credited":
        logger.info(f"Ignoring webhook event type: {event_type}")
        return {"status": "ignored"}

    invoice = log.get("invoice")

    if not invoice:
        logger.error("Invoice data missing in webhook")
        return {"status": "invalid invoice"}

    amount = invoice.get("amount", 0) - invoice.get("fee", 0)

    try:
        transfer = starkbank.transfer.create([
            starkbank.Transfer(
                amount=amount,
                bank_code="20018183",
                branch_code="0001",
                account_number="6341320293482496",
                name="Stark Bank S.A.",
                tax_id="20.018.183/0001-80",
                account_type="payment"
            )
        ])

        logger.info(f"Transfer created successfully: {transfer}")

    except Exception as e:
        logger.error(f"Error creating transfer: {str(e)}")

    return {"status": "ok"}
