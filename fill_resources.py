import base64

from datetime import datetime
import requests

employees = [
    {
        "fio": "Макарова Яна",
        "specialization": [
            "клинический психолог",
            "нейробиолог",
            "когнитивно-поведенческий",
            "диалектико – поведенческий терапевт",
        ],
        "education": [
            "2008 - 2013 гг. - РГГУ, Институт психологии им.Л.С.Выготского",
            "2010 г. - Боткинская больница, кафедра нейрохирургии, г. Москва",
            "2012-2013 гг. - Психиатрическая клиническая больница №1 им Н.А. Алексеева, г. Москва",
            "2015 - 2017 гг. - СПбГУ, факультет биологии, специализация 'Нейробиология, психофизиология', г. Санкт - Петербург",
            "2017-2020 гг. - СЗГМУ им. И.И. Мечникова, повышение квалификации по направлениям «Когнитивно-поведенческая терапия», «Когнитивно-поведенческая терапия пар», г. Санкт – Петербург",
            "2021 г. – Центр Когнитивной Терапии, повышение квалификации по направлению «Терапия, сфокусированная на сострадании», г. Москва",
            "2021 г. - Доктор Дуглас Туркингтон (Dr.Douglas Turkington, Royal College of Psychiatrists): 'Когнитивно-поведенческая терапия психозов",
            "с 2021г. - член коллегии Ассоциации клинического психоанализа и психотерапии, участник регулярной интервизионной группы",
        ],
        "workExperience": [
            "2013-2015 гг. – Психиатрическая клиническая больница №1 им.Н.А.Алексеева, г. Москва",
            "2015 – 2020 гг. – Психоневрологический диспансер №5 г. Санкт-Петербург",
            "2020 г. – по настоящее время - Частная практика",
        ],
        "imageSrc": 
            open("./backend/assets/employees/Makarova.jpg", "rb")
        ,
        "appointmentLink": "https://n269840.yclients.com/company/262333/select-services?o=m772221",
        "isPopular": False,
    },
    {
        "fio": "Головаха Николай",
        "specialization": [
            "К.М.Н.",
            "психотерапевт",
            "когнитивно-поведенческий терапевт",
            "диалектико–поведенческий терапевт",
        ],
        "education": [
            "1998 г. - Алтайский государственный медицинский университет по специальности лечебное дело",
            "Ординатура по специальности психиатрия-наркология.",
            "Кандидат медицинских наук.",
            "Сертификат врача психотерапевта",
            "Когнитивно-поведенческая терапия",
            "Диалектическая поведенческая терапия в Behavioral Tech под руководством André Ivanoff, PhD",
            "Участвовал в международных стажировках и конференциях по лечению ожирения, лечению расстройств пищевого поведения, помощи людям с суицидальным поведением и самоповреждениями",
        ],
        "workExperience": [
            "Кандидат медицинских наук",
            "Сертификат врача психотерапевта",
        ],
        "imageSrc": 
            open("./backend/assets/employees/Golovaha.jpg", "rb")
        ,
        "appointmentLink": "https://n269840.yclients.com/company/262333/select-services?o=m772221",
        "isPopular": True,
    },
    {
        "fio": "Mariia Aarseth",
        "specialization": [
            "Клинический психолог",
            "преподаватель",
            "психологии",
        ],
        "education": [
            "2009 г - Санкт-Петербургский институт гуманитарного образования, специальность - психолог",
            "2020 г - Санкт-Петербургский Межотраслевой Институт Повышения Квалификации, специальность - Клиническая психология",
        ],
        "workExperience": [
            "EMDR терапевт с Европейской аккредитацией ( как взрослый, так и детский ), супервизор.",
            "Член ассоциаций Норвегия, Россия, Казахстан.",
            "TFP ( терапия сфокусированная на переносе Columbia University Weill Cornell Medical CollegeOtto Friedmann Kernberg",
            "Обучение в Heidelberg University Germany. Martin Bohus, а так же Universitetet i Oslo Lars Mehlum. DBT, DBT PTSD, CFT",
        ],
        "imageSrc": 
            open("./backend/assets/employees/Aarseth.jpg", "rb")
        ,
        "appointmentLink": "https://n269840.yclients.com/company/262333/select-services?o=m772221",
        "isPopular": True,
    },
]

diseases = [
    {
        "id": 1,
        "description": "Отчаянные попытки предотвратить реальное или воображаемое одиночество",
        "imageSrc": 
            open("./backend/assets/diseases/prl1.jpg", "rb")
        ,
    },
    {
        "id": 2,
        "description": "Повторяющиеся нестабильные и интенсивные межличностные отношения",
        "imageSrc": 
            open("./backend/assets/diseases/prl2.jpg", "rb")
        ,
    },
    {
        "id": 3,
        "description": "Временные параноидальные идеи, связанные со стрессом",
        "imageSrc": 
            open("./backend/assets/diseases/prl3.jpg", "rb")
        ,
    },
    {
        "id": 4,
        "description": "Расстройство идентичности: выраженная и стойкая нестабильность самооценки",
        "imageSrc": 
            open("./backend/assets/diseases/prl4.jpg", "rb")
        ,
    },
    {
        "id": 5,
        "description": "Импульсивность как минимум в двух областях, потенциально способных нанести вред",
        "imageSrc": 
            open("./backend/assets/diseases/prl5.jpg", "rb")
        ,
    },
    {
        "id": 6,
        "description": "Повторяющиеся суицидальные мысли, угрозы суицида",
        "imageSrc": 
            open("./backend/assets/diseases/prl6.jpg", "rb")
        ,
    },
    {
        "id": 7,
        "description": "Аффективная нестабильность",
        "imageSrc": 
            open("./backend/assets/diseases/prl7.jpg", "rb")
        ,
    },
    {
        "id": 8,
        "description": "Хроническое чувство пустоты",
        "imageSrc": 
            open("./backend/assets/diseases/prl8.jpg", "rb")
        ,
    },
    {
        "id": 9,
        "description": "Неуместный сильный гнев или трудности с контролем ярости или гнева",
        "imageSrc": 
            open("./backend/assets/diseases/prl9.jpg", "rb")
        ,
    },
]

articles = [
    {
        "id": 1,
        "title": "История DBT терапии",
        "author": "Головаха Николай",
        "description": "Диалектическая поведенческая терапия (DBT) – создана Маршей Линехан во второй половине 20 века, для людей ...",
        "imageSrc": 
            open("./backend/assets/articles/article1.jpg", "rb")
        ,
        "articleLink": "https://telegra.ph/Istoriya-DBT-terapii-10-21",
        "isPopular": True,
        "created": datetime.now(),
    },
    {
        "title": "Биосоциальная модель ПРЛ",
        "author": "Головаха Николай",
        "description": "Людям с ПРЛ сложно контролировать свои эмоции. Почему так происходит? Есть биологическая основа ...",
        "imageSrc": 
            open("./backend/assets/articles/article2.jpg", "rb")
        ,
        "articleLink": "https://telegra.ph/Biosocialnaya-model-pogranichnogo-10-21",
        "isPopular": True,
        "created": datetime.now(),
    },
    {
        "title": "Эмоциональная дисрегуляция при ПРЛ",
        "author": "Головаха Николай",
        "description": "В ДБТ считается, что не умение регулировать сильные эмоции, приводит к проблемному поведению. Это такое поведение ...",
        "imageSrc": 
            open("./backend/assets/articles/article3.jpg", "rb")
        ,
        "articleLink": "https://telegra.ph/EHmocionalnaya-disregulyaciya-pri-PRL-10-21",
        "isPopular": True,
        "created": datetime.now(),
    },
    {
        "title": "Возможности ДБТ при лечении ПРЛ",
        "author": "Головаха Николай",
        "description": "Мы не можем изменить повышенную врожденную эмоциональность. При этом, можно учиться регулировать свои эмоции с помощью  ...",
        "imageSrc": 
            open("./backend/assets/articles/article4.jpg", "rb")
        ,
        "articleLink": "https://telegra.ph/Vozmozhnosti-DBT-pri-lechenii-PRL-10-21",
        "isPopular": False,
        "created": datetime.now(),
    },
]

for employee in diseases:
    imageSrc = employee.pop("imageSrc")
    employee["token"] = "misha"
    response = requests.post("http://95.140.152.52:7777/diseases", headers={}, data=employee, files=[('imageSrc', ('file.jpg', imageSrc, 'image/jpeg'))])
    print(response.text)

# import requests

# url = "http://:7777/employees"

# payload = {'token': 'misha',
# 'fio': 'Исаков Михаил',
# 'specialization': 'Программист',
# 'specialization': 'Психолог',
# 'education': 'Программист',
# 'education': 'Школа',
# 'workExperience': 'Лаба СВТ',
# 'workExperience': 'МИЭМ',
# 'appointmentLink': 'https://n269840.yclients.com/company/262333/select-services?o=m772221',
# 'isPopular': 'True'}
# files=[
#   ('imageSrc',('Screenshot 2023-11-23 at 18.26.09.jpg',open('/Users/mikhailisakov/Downloads/Screenshot 2023-11-23 at 18.26.09.jpg','rb'),'image/jpeg'))
# ]
# headers = {}

# response = requests.request("POST", url, headers=headers, data=payload, files=files)

# print(response.text)