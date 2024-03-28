from django.core.mail import send_mail
from django.core.mail.backends.console import EmailBackend
from .models import Article
from datetime import datetime, timedelta

def send_article_list_email():
    last_friday = datetime.now() - timedelta(days=datetime.now().weekday()+3, weeks=1)
    articles = Article.objects.filter(pub_date__gte=last_friday)

    message = 'Списки новых статей:\n\n'
    for article in articles:
        message += f"- {article.title}:{article.url}\n"

        send_mail(
            'Новые статьи на сайте',
            message,
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
            connection =EmailBackend(),
        )