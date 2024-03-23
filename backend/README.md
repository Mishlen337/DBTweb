##  Overview

API реализован на основе фреймворка FLaskAPI, использует базу данных MongoDB и поднимается в Docker контенере, как один из микросервисов.

---

##  Features

Содержит следующие ресурсы для обеспечивания контентом фронтенд:
1. Информация о cпециалистах: /employees
2. Информация об основных заболеваниях: /deseases
3. Информация о статьях: /articles
4. Подбор специалиста: /recommendation
5. Написания отзыва: /report

---

##  Repository Structure

```sh
└── ./
    ├── Dockerfile
    ├── app.py
    ├── config.py
    ├── requirements.txt
    ├── resources
    │   ├── article.py
    │   ├── diseases.py
    │   ├── employee.py
    │   ├── recommendation.py
    │   └── report.py
    └── src
        └── mongo.py
```

---

##  Modules

<details closed><summary>.</summary>

| File                                 | Summary                         |
| ---                                  | ---                             |
| [config.py](config.py)               | <code> Конфиг файл для апи</code> |
| [requirements.txt](requirements.txt) | <code>Зависимости бэкенда</code> |
| [Dockerfile](Dockerfile)             | <code>Скрипт для контейнера </code> |
| [app.py](app.py)                     | <code>Запуск бэкенда</code> |

</details>

<details closed><summary>resources</summary>

| File                                             | Summary                         |
| ---                                              | ---                             |
| [diseases.py](resources/diseases.py)             | <code>АПИ ручки для получения, редактирования, добавления и удаления заболеваний</code> |
| [recommendation.py](resources/recommendation.py) | <code>АПИ ручка для интелектульного получения рекомендаций. </code> |
| [employee.py](resources/employee.py)             | <code>АПИ ручки для получения, редактирования, добавления и удаления сотрудников </code> |
| [report.py](resources/report.py)                 | <code>АПИ ручка для добавления нового отзыва</code> |
| [article.py](resources/article.py)               | <code>АПИ ручки для получения, редактирования, добавления и удаления статьи</code> |

</details>

<details closed><summary>src</summary>

| File                     | Summary                         |
| ---                      | ---                             |
| [mongo.py](src/mongo.py) | <code>Файл установки соединения с MongoDB </code> |

</details>
