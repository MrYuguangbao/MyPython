import time
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

def func():
    s = 0
    for i in range(1, 5):
        s += i
    print('sum:' + str(s))
    print('current time:' + str(datetime.datetime.now()))

def dojob():
    scheduler = BlockingScheduler()
    scheduler.add_job(func,CronTrigger.from_crontab('15 16 * * *'))
    scheduler.start()

dojob()

