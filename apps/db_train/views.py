from django.shortcuts import render
from django.views import View
from .models import Author, AuthorProfile, Entry, Tag
from django.db.models import Q, Max, Min, Avg, Count


class TrainView(View):
    def get(self, request):
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem']) # TODO Какие авторы имеют самую высокую уровень самооценки(self_esteem)?
        count_article = Author.objects.annotate(number_of_article=Count('entries')).order_by('-number_of_article').first()
        # self.answer2 = count_article  # TODO Какой автор имеет наибольшее количество опубликованных статей?
        self.answer2 = Entry.objects.values('author').annotate(count_article=Count('id'))\
            .order_by('-count_article').first()
        self.answer3 = Entry.objects.filter(Q(tags__name='Кино')|Q(tags__name='Музыка')).distinct()
        # TODO Какие статьи содержат тег 'Кино' или 'Музыка' ?
        self.answer4 = Author.objects.aggregate(count=Count('username', filter=Q(gender='ж')))  # TODO Сколько авторов женского пола зарегистрировано в системе?
        self.answer5 = Author.objects.aggregate(count=Count('username', filter=Q(status_rule=True)))   # TODO Какой процент авторов согласился с правилами при регистрации?
        self.answer6 = AuthorProfile.objects.filter(Q(stage__gte=1)&Q(stage__lte=5))  # TODO Какие авторы имеют стаж от 1 до 5 лет?
        max_age_author = Author.objects.aggregate(max_age=Max('age'))
        self.answer7 = Author.objects.filter(age=max_age_author['max_age'])  # TODO Какой автор имеет наибольший возраст?
        self.answer8 = None  # TODO Сколько авторов указали свой номер телефона?
        self.answer9 = None  # TODO Какие авторы имеют возраст младше 25 лет?
        self.answer10 = None  # TODO Сколько статей написано каждым автором?

        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}

        return render(request, 'train_db/training_db.html', context=context)
