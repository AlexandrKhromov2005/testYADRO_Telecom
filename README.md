# Проект для автоматизации HTTP-запросов с использованием Python, Docker и Ansible.

## Структура проекта
```
├── section1/            
│   └── http_checker.py
├── section2/            
│   └── Dockerfile
├── section3/            
│   ├── inventory.ini
│   └── playbook.yml
└── README.md
```


## Требования
- Python 3.8+
- Docker 20.10+
- Ansible 2.14+

## Быстрый старт

### 1. Запуск скрипта
```bash
cd section1
python3 http_checker.py
```

### 2. Сборка Docker-образа
```bash
cd section2
sudo docker build -t http-checker -f section2/Dockerfile .
sudo docker run --name http-checker-container http-checker
```

### 3. Автоматизация через Ansible
```bash
cd section3
ansible-galaxy collection install community.docker
ansible-playbook -i inventory.ini playbook.yml
```

## Подробная инструкция

### Раздел 1: Python-скрипт
**Функции:**
- Выполняет 5 HTTP-запросов к https://httpstat.us
- Логирует успешные ответы (1xx, 2xx, 3xx)
- Генерирует исключения для ошибок (4xx, 5xx)

**Пример вывода:**
```
INFO: Success: 200
INFO: Success: 201
ERROR: HTTP Error: 404
```

### Раздел 2: Docker
**Особенности образа:**
- Базовый образ: Ubuntu 24.04
- Автоматический запуск скрипта при старте контейнера

**Команды:**
```bash
# Просмотр логов
docker logs checker

# Остановка контейнера
docker rm -f checker
```

### Раздел 3: Ansible
**Что делает плейбук:**
1. Устанавливает Docker
2. Собирает образ
3. Запускает контейнер
4. Выводит логи

