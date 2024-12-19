# AIS24-DZ3out2

### ДЗ-3 без ДЗ-2. Микросервисы с использованием Docker и Nginx

Этот проект демонстрирует архитектуру микросервисов, реализованную с использованием Python Flask, Docker и Nginx. Проект состоит из трёх сервисов:

Проект состоит из трёх HTTP-сервисов:

- **Score Service** — рассчитывает "хорошесть" пользователя.
- **Auth Service** — проверяет, может ли пользователь войти в систему.
- **Composition Service** — сначала обращается к Score Service, а затем к Auth Service для проверки входа на основании оценки пользователя.

- **Score Service (Сервис оценки)**:
  - Точка входа: `/score`
  - Генерирует случайный рейтинг (score) для указанного логина.

- **Auth Service (Сервис аутентификации)**:
  - Точка входа: `/auth`
  - Проверяет аутентификацию пользователя по логину и паролю.

- **Composition Service (Сервис композиции)**:
  - Точка входа: `/composition`
  - Объединяет функциональность сервисов Score Service и Auth Service, используя балансировку нагрузки через Nginx.

### Как сделано

- **Сервисы в Docker-контейнерах**:
  - Каждый сервис работает в своём отдельном контейнере.
  - Управление осуществляется с помощью `docker-compose`.

### Балансировщик нагрузки:
- Nginx используется в качестве L7-балансировщика нагрузки для нескольких экземпляров Composition Service.


### Структура проекта
```
my_microservices/
├── auth_service/
│   ├── auth_service.py
│   ├── Dockerfile
│   └── requirements.txt
├── composition_service/
│   ├── composition_service.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env
├── score_service/
│   ├── score_service.py
│   ├── Dockerfile
│   └── requirements.txt
├── nginx.conf
├── docker-compose.yml
└── README.md
```

## Развёртывание и запуск

Должег быть устанлвен Docker и Docker Compose

Склонируйте репозиторий проекта:

    git clone https://github.com/FIIT24GP/AIS24-DZ3out2.git
    
    cd AIS24-DZ3out2

Соберите и запустите проект:
    sudo docker-compose up --build

Примеры запросов

    curl -X POST http://localhost:5001/score -H "Content-Type: application/json" -d '{"login": "user1"}'
     
    curl -X POST http://localhost:5002/auth -H "Content-Type: application/json" -d '{"login": "user1", "password": "password1"}'
    
    curl -X POST http://localhost:8080/composition -H "Content-Type: application/json" -d '{"login": "user1", "password": "password1"}'

