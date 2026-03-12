from apscheduler.schedulers.blocking import BlockingScheduler
from app.invoice_generator import create_invoices

scheduler = BlockingScheduler()

scheduler.add_job(create_invoices, "interval", hours=3)

print("Scheduler iniciado...")

scheduler.start()
