
from mynews.apscheduler import BackgroundScheduler
from mynews.apscheduler import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from mynews.tasks import send_article_list_email

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # Запуск задачи каждую пятницу в 18:00
    scheduler.add_job(
        send_article_list_email,
        trigger=CronTrigger(day_of_week='fri', hour=18),
        id="send_article_list_email",
        name="Отправка списка статей по электронной почте",
        replace_existing=True,
    )

    scheduler.start()
