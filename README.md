![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# CLI-client для сервиса DaData.ru


## Запуск
**Внимание!**<br>
Прежде, чем развернуть проект, убедитесь, что у вас в системе установлен [Python3.10](https://www.python.org/downloads/)

### 1. Предпочтительный метод
Для развертывания приложения этим способ необходимо, чтобы была установлена система управления зависимостями [Poetry](https://python-poetry.org/docs/)
<br>
1.Перейдите в директорию, в которой планируете развернуть проект
```
mkdir some_dir
cd some_dir
```

2.Склонируйте репозиторий себе на локальный компьютер
```
git clone https://github.com/AgafonovSiberia/CLI_client_DaData.ru.git
```

3.Перейдите в директорию проекта 
```
cd CLI_client_DaDadata.ru
```

4.Установите зависимости и запустите приложение, выполнив следующие команды
```
poetry install
poetry run python -m main.py
```

### 2.Альтернативный метод
<ol>
  <li>Клонировать репозиторий <code>git clone https://github.com/AgafonovSiberia/CLI_client_DaData.ru.git</code>
  <li>Перейти в рабочий каталог <code>cd CLI_client_DaDadata.ru</code>
  <li>Создать виртуальное окружение <code>python3.10 -m venv venv</code>
  <li>Активировать виртуальное окружение <code>source venv/bin/activate</code>
  <li>Установить зависимости <code>pip install -r requirements.txt</code>
  <li>Запустить парсер <code>python main.py</code>
</ol>
________________________________________________________________

## Инструкция по работе
**Внимание!**<br>
Приложение работает только в консольном режиме.

1. При первом запуске приложения Вам необходимо будет ввести валидные Api-key и Token, полученные от сервиса [dadata.ru](https://dadata.ru/) после регистрации.
2. Навигация по меню осуществяется путём ввода соответствующих команд.

## Screenshots

![alt text](https://github.com/AgafonovSiberia/cli_client_DaData.ru/blob/master/data/3.png)
![alt text](https://github.com/AgafonovSiberia/cli_client_DaData.ru/blob/master/data/4.png)
