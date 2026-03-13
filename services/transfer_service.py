import starkbank
import logging

logger = logging.getLogger(__name__)

processed_invoices = set()


def create_transfer(invoice):

    invoice_id = invoice.get("id")

    if invoice_id in processed_invoices:
        logger.warning(f"Invoice {invoice_id} already processed. Ignoring duplicate webhook.")
        return

    amount = invoice.get("amount", 0) - invoice.get("fee", 0)

    if amount <= 0:
        logger.error(f"Invalid transfer amount: {amount}")
        return

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

        logger.info(f"Transfer created | invoice_id={invoice_id} | amount={amount}")

        processed_invoices.add(invoice_id)

        return transfer

    except Exception as e:

        logger.error(f"Error creating transfer: {str(e)}")
        raise