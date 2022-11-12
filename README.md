# Курс 4. Домашняя работа SkyPRO PD 12

______________________________________

### **Урок 18. Архитектура**

______________________________________
Для запуска программы используйте `main.py`

Что сделано:

:white_check_mark: созданы модели Movie, Director и Genre

:white_check_mark: созданы схемы Marshmallow для всех моделей

:white_check_mark: созданы **DAO** модели Movie, Director и Genre

:white_check_mark: созданы **Service** модели Movie, Director и Genre

:white_check_mark: созданы неймспейсы **RESTX** для всех маршрутов

:white_check_mark: созданы индивидуальные **CBV** для Movie, Director и Genre

:white_check_mark: корректно работает выдача всех фильмов по маршруту /movies/ с возможностью фильтрации результата 
через аргументы **director_id**, **genre_id** и **year** или конкретного фильма по маршруту /movies/id

:white_check_mark: корректно работает выдача всех режиссеров по маршруту /directors/
или конкретного режиссера по маршруту /directors/id

:white_check_mark: корректно работает выдача всех жанров по маршруту /genres/
или списка фильмов по жанру по маршруту /genres/id

:white_check_mark: корректно работает **POST** добавление фильма по маршруту /movies/ с заголовком **Locations**

:white_check_mark: корректно работает **PUT** обновление фильма по маршруту /movies/id

:white_check_mark: корректно работает **DELETE** удаление фильма по маршруту /movies/id

:white_check_mark: Обработчики ошибок **404** и **500** и обработчики внутри кода
_____________________________________
**Дополнительно реализовано:**

:white_check_mark: Написана проверка работоспособности через **HTTP Request** в папке `app\api`
