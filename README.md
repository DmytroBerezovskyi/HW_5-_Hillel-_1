# HW_5-_Hillel-_1

# The application catalog was created in the project, migrations were made, TIME_ZONE was set, the key for the project was moved to the virtual environment (dotenv) in the .env file.

# ДЗ 6. Flake8, CI/CD (Black, tox)

# Установлен и настрооен flake8 с дополнительными модулями (flake8-django, flake8-import-order, flake8-builtins, flake8-print).

# Настроен файл конфигураций для него и проверен код на предмет ошибок и исправлены.

# Добавилен файл настроек для CI/CD и настроен так, что бы при попадании изменений в репозиторий запускается CI/CD

# В CI/CD проверен код на ошибки от flake8(+расширения) и запущены тесты



# *CI/CD - Github Actions.


# ДЗ 7. queryset methods, managment commands

#В текущем репозитории (дз 6)

#1.
#Написать кастомную менеджент комманду которая будет генерировать случайных пользователей ( https://docs.djangoproject.com/en/4.1/ref/models/querysets/#create ) c username, email и #password. Команда принимает один обязательный аргумент - количество вновь сгенерированных пользователей. Значения меньше 1 и больше 10 - должны вызывать ошибку.

#(Ожидаю использования bulk_create, но не буду запрещать другие способы)

#python manage.py create_users 3

#2.
#Написать кастомную менеджент комманду которая удалит пользователей ( https://docs.djangoproject.com/en/4.1/ref/models/querysets/#delete ) с указанными id. Команда принимает id #пользователей через пробел. Запрещено удалять суперпользователя (https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.User.is_superuser) - при наличии хотя #бы одного суперпользователя в списке id - команда не должна выполнятся.

#(Ожидаю выполнение этой части без использования циклов, но не буду запрещать другие способы)

#python manage.py delete_users 1 2 3 4 5
#https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/
#https://docs.djangoproject.com/en/4.1/ref/models/querysets/#bulk-create
#https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.UserManager.create_user
#https://docs.djangoproject.com/en/4.1/topics/auth/passwords/#django.contrib.auth.hashers.make_password
#https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.User.set_password
#https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html

#3.
#Создать файл фикстур используя менеджмент команду dumpdata (https://docs.djangoproject.com/en/4.1/ref/django-admin/#dumpdata)
#https://docs.djangoproject.com/en/4.1/ref/django-admin/#what-s-a-fixture
#https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata (секция Restore fresh database)


#ДЗ 8. OneToOneField, ForeignKey, ManyToManyField

#Реализовать в приложении (catalog созданной в одном из предшествующих заданий) модели использующие поля OneToOneField, ForeignKey, ManyToManyField.

#Использовать graph_models из django-extensions что бы отобразить структуру моделей ТОЛЬКО этого приложения. Результат - изображение сопоставимое с представленным в ридми файле #репозитория https://github.com/KhvPaul/django_example_project

#Учтите, что для работы этой команды необходимо доустановить зависимости в систему. Если у вас не получается - можете составить условную диаграмму связей между таблицами самостоятельно.

#Пример:
#Город
#Клиент (MTM на товар, FK на город)
#Товар
#Поставщик (OTO на город)

#Написать по запросу из инстанса одной модели в другую по каждой из связей (всего 3 запроса).
#...
#city = City.objects.get(id=1)
#city."<model>_set".filter(date__year=2022).order_by("-date")
#<SQL>
#retailer = Retailer.objects.get(id=1)
#retailer.city
#<SQL>
#...
#Для создания запроса используйте shell_plus --print-sql что бы ваш SQL отобразился в консоли.

#Ожидаю:

#Ссылка на репозиторий
#Прикрепленный скрин с диаграммой связей между таблицами (и/или наличие его в репозитории)
#Запрос и его SQL версия (текст или скрин в комментарии и/или в репозитории)


#ДЗ 9. Django Forms
#Выполнять в текущем проекте (можете создать еще одно приложение)
#Добавить вью по пути /triangle
#На этой вью необходимо использовать форму которая будет принимать значения двух катетов треугольника (положительные, больше нуля, для простоты используйте int значения если хотите). #После отправки формы, если значения были валидными - на этой же странице вывести значение гипотенузы.
#Это должна быть одна view
#Можете использовать 1 или 2 темплейта при необходимости для рендера формы и результата.
#Если один темплейт - значение гипотенузы по умолчанию None - проверяйте его в темплейте, и на основании того None или "значение" рендерите форму или значение гипотенузы
#template.html
#if gip
#  <p> гипотенуза равна gip
#form.as_p
#в этом случае вы не будете использовать redirect
#
#Использовать только формы. Модели не нужно.
#TLDR:
#1 form
#1 url
#1 view (get and get+submit)
#1 or 2 template
#redirect - optional
