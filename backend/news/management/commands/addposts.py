from django.core.management.base import BaseCommand
from backend.news.models import Post


class Command(BaseCommand):
    help = 'Add post'

    def handle(self, *args, **options):
        i = 1
        mini_text = """Как сообщила ТАСС адвокат Улюкаева Дареджан Квеидзе, ранее бывший министр проиграл налоговый 
        спор в 100 тыс. руб., с него взыскали эту сумму. А теперь взыскивают пошлину. «Просто мой подзащитный сейчас 
        находится в колонии, а оттуда трудно оперативно оплачивать текущие платежи», - сказала адвокат."""
        text = """Как сообщила ТАСС адвокат Улюкаева Дареджан Квеидзе, ранее бывший министр проиграл налоговый спор в 
        100 тыс. руб., с него взыскали эту сумму. А теперь взыскивают пошлину. «Просто мой подзащитный сейчас находится 
        в колонии, а оттуда трудно оперативно оплачивать текущие платежи», - сказала адвокат.
        В декабре 2017 года суд приговорил Улюкаева к восьми годам лишения свободы и штрафу в 130 млн рублей. Он был
        признан виновным в получении взятки от главы «Роснефти» Игоря Сечина в размере 2 млн долларов. При исполнении
        приговора возникла правовая коллизия, вследствие которой приставы не могли взыскать штраф, так как деньги на 
        счете Улюкаева были заблокированы до исполнения приговора суда, который в свою очередь не мог быть исполнен 
        до оплаты штрафа. В октябре 2018 года Замоскворецкий суд Москвы удовлетворил заявление службы судебных 
        приставов о снятии ареста с имущества экс-министра, что позволило взыскать необходимую сумму для оплаты 
        штрафа. Под арестом по-прежнему находится недвижимое имущество Улюкаева."""
        while i <= 2:
            Post.objects.create(title="title",
                                mini_text=mini_text,
                                text=text,)
            i += 1
        self.stdout.write('Success add posts')