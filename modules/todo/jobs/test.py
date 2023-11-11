from apscheduler.schedulers.background import BackgroundScheduler

def job():
    print("I'm working...")

schedular = BackgroundScheduler()
schedular.add_job(job,'interval',seconds=5)