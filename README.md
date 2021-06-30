# Название проекта

api_yamdb

![example workflow name](https://github.com/Denisscore/yamdb_final/workflows/yamdb_workflow/badge.svg)

## Как запустить контейнер

Откройте командную строку, для этого нажмите клавиши Win+r и введите команду

```
cmd
```
В открывшемся окне перейдите в каталог проекта, далее введите

```
docker-compose up
```

## Как зайти внутрь контейнера

Откройте командную строку как описано выше, и введите 

```
docker ps
```
найтите ID контейнера с назваием infra_sp2_web и далее введите

```
winpty docker exec -it <id контейнера> bash
```
## Запуск миграций

Находясь внутри контейнера web введите
```
python manage.py makemigrations api
```
далее введите
```
python manage.py migrate
```

## Создание суперпользователя

Для создания суперпользователя находясь внутри контейнера web введите
```
python manage.py createsuperuser
``` 
Далее заполните данные login, E-mail, password и подтвердите ввод

## Как загрузить дамп базы данных

Зайти в контейнер и ввести

```
python3 manage.py shell
```
выполнить в открывшемся терминале
```
from django.contrib.contenttypes.models import ContentType
```
```
ContentType.objects.all().delete()
```
```
quit()
```
Далее ввести 
```
python manage.py loaddata dump.json
```
Где dump.json название дампа БД


## Authors

* **Денис Шархов** - *Initial work* - [Denisscore](https://github.com/Denisscore)

![example workflow name](https://github.com/Denisscore/yamdb_final/workflows/yamdb_workflow/badge.svg)



