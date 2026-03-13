from datetime import timedelta, datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from jobs.invoice_generator_job import create_invoices

scheduler = BlockingScheduler()

end_time = datetime.now() + timedelta(hours=24)

scheduler.add_job(
    create_invoices,
    "interval",
    hours=3,
    end_date=end_time
)

print("Worker configurado")

if __name__ == "__main__":
    print("Worker iniciado...")
    scheduler.start()