##  Описание
Фронтенд реализован на фреймфорке Vue JS и использует стили библиотек bootstrap и мгузук

---

##  Особенности

Содержит следующие страницы:
1. Главная страница
2. Информация о компании
3. Блог со статьями о психологии
4. Информация о cпециалистах
5. Интеллектуальный подбор специалиста

---

##  Структура фронтенд части

```sh
└── src/
    ├── App.vue
    ├── components
    │   ├── AboutView
    │   │   ├── BasicInfoBlock.vue
    │   │   ├── MotivationBlock.vue
    │   │   └── ValuesBlock.vue
    │   ├── BlogView
    │   │   └── ArticleInfo.vue
    │   ├── ChooseView
    │   │   └── SearchBar.vue
    │   ├── EmployeesView
    │   │   └── EmployeeInfo.vue
    │   ├── HelloWorld.vue
    │   ├── MainView
    │   │   ├── AppointmentBlock.vue
    │   │   ├── ChooseBlock.vue
    │   │   ├── DiseaseInfo.vue
    │   │   └── GreetingBlock.vue
    │   ├── TheFooter.vue
    │   └── TheHeader.vue
    ├── main.js
    ├── router
    │   └── index.js
    └── views
        ├── AboutView.vue
        ├── BlogView.vue
        ├── ChooseView.vue
        ├── EmployeesView.vue
        ├── HomeView.vue
        └── ReportView.vue
```

---

##  Modules

<details open><summary>.</summary>

| File               | Summary                         |
| ---                | ---                             |
| [App.vue](App.vue) | <code>Главный vue файл проекта </code> |
| [main.js](main.js) | <code>Файл запуска проекта</code> |

</details>

<details open><summary>components</summary>

| File                                        | Summary                         |
| ---                                         | ---                             |
| [TheFooter.vue](components/TheFooter.vue)   | <code>Содержит html, css и js для футера</code> |
| [TheHeader.vue](components/TheHeader.vue)   | <code>Содержит html, css и js для хедера</code> |

</details>

<details open><summary>components.AboutView</summary>

| File                                                            | Summary                         |
| ---                                                             | ---                             |
| [MotivationBlock.vue](components/AboutView/MotivationBlock.vue) | <code>Содержит html, css и js для блока мотивации</code> |
| [BasicInfoBlock.vue](components/AboutView/BasicInfoBlock.vue)   | <code>Содержит html, css и js для блока общей информации</code> |
| [ValuesBlock.vue](components/AboutView/ValuesBlock.vue)         | <code>Содержит html, css и js для ценностей компании</code> |

</details>

<details open><summary>components.BlogView</summary>

| File                                                   | Summary                         |
| ---                                                    | ---                             |
| [ArticleInfo.vue](components/BlogView/ArticleInfo.vue) | <code>Содержит html, css и js для блока статьи</code> |

</details>

<details open><summary>components.MainView</summary>

| File                                                             | Summary                         |
| ---                                                              | ---                             |
| [AppointmentBlock.vue](components/MainView/AppointmentBlock.vue) | <code>Содержит html, css и js для блока записи</code> |
| [ChooseBlock.vue](components/MainView/ChooseBlock.vue)           | <code>Содержит html, css и js для блока выбора специалиста</code> |
| [GreetingBlock.vue](components/MainView/GreetingBlock.vue)       | <code>Содержит html, css и js для приветственного блока</code> |
| [DiseaseInfo.vue](components/MainView/DiseaseInfo.vue)           | <code>Содержит html, css и js для блока заболеваний</code> |

</details>

<details open><summary>components.ChooseView</summary>

| File                                                 | Summary                         |
| ---                                                  | ---                             |
| [SearchBar.vue](components/ChooseView/SearchBar.vue) | <code>Содержит html, css и js для блока поиска специалиста</code> |

</details>

<details open><summary>components.EmployeesView</summary>

| File                                                          | Summary                         |
| ---                                                           | ---                             |
| [EmployeeInfo.vue](components/EmployeesView/EmployeeInfo.vue) | <code>Содержит html, css и js для блока информации о специалисте</code> |

</details>

<details open><summary>views</summary>

| File                                         | Summary                         |
| ---                                          | ---                             |
| [AboutView.vue](views/AboutView.vue)         | <code>Содержит html, css и js для страницы о компании</code> |
| [ChooseView.vue](views/ChooseView.vue)       | <code>Содержит html, css и js для страницы интеллектуального выбора</code> |
| [HomeView.vue](views/HomeView.vue)           | <code>Содержит html, css и js для главной страницы</code> |
| [EmployeesView.vue](views/EmployeesView.vue) | <code>Содержит html, css и js для страницы просмотра сотрудников</code> |
| [BlogView.vue](views/BlogView.vue)           | <code>Содержит html, css и js для страницы блога со статьями</code> |

</details>

<details open><summary>router</summary>

| File                        | Summary                         |
| ---                         | ---                             |
| [index.js](router/index.js) | <code>Содержит JS код для роутинга страниц</code> |

</details>
