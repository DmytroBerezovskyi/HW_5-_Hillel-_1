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
