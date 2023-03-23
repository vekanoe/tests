#### Разворот приложения:

перейти в папку проекта
 
    cd tests


создать файл со значениями переменных окружения. Отредактировать значения по необходимости

    cp deploy/.env.dist deploy/.env


создать/запустить контейнеры

    docker-compose up -d  --build


создать суперпользователя

    docker-compose exec web python manage.py createsuperuser


#### Предустановленные данные

С помощью django-команды load_company_data в базу загружены несколько сотрудников и отделов. 


#### Админка для администратора системы:

Доступна стандартная админка Django, в которую выведено разработанное приложение 

/admin/company/


#### Эндпойнты API:

1. /api/login/ - залогиниться
    
2. /api/logout/ - разлогиниться

3. /api/employees/ - сотрудники

4. /api/departments/ - отделы


***

#### Документация:

1. /swagger/
    
2. /redoc/