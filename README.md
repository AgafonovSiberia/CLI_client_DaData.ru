![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# CLI-client для сервиса DaData.ru


### Запуск
**Внимание!**<br>
Прежде, чем развернуть проект, убедитесь, что у вас в системе установлен [Python3.10](https://www.python.org/downloads/) и система управления зависимостями [Poetry](https://python-poetry.org/docs/)


1.Перейдите в директорию, в которой планируете развернуть проект
```
mkdir some_dir
cd some_dir
```

2.Склонируйте репозиторий себе на локальный компьютер
```
git clone git@github.com:AgafonovSiberia/CLI_client_DaData.ru.git
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

### Инструкция по работе
**Внимание!**<br>
Приложение работает только в консольном режиме.

1. При первом запуске приложения Вам необходимо будет ввести валидные Api-key и Token, полученные от сервиса [dadata.ru](https://dadata.ru/) после регистрации.
2. Навигация по меню осуществяется путём ввода соответствующих команд.

## Screenshots

![alt text](https://github.com/AgafonovSiberia/cli_client_DaData.ru/blob/master/data/3.png)
![alt text](https://github.com/AgafonovSiberia/cli_client_DaData.ru/blob/master/data/4.png)
