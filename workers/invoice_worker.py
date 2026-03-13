from apscheduler.schedulers.blocking import BlockingScheduler
from jobs.invoice_generator_job import create_invoices

scheduler = BlockingScheduler()

scheduler.add_job(create_invoices, "interval", hours=3)

print("Worker configurado")


if __name__ == "__main__":
    print("Worker iniciado...")
    scheduler.start()