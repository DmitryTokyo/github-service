# Github Service - тестовое задание

Данный проект позволяет проверить, в какие проекты указанный пользователь делал pull requests.

## Установка

Приложение разрабатывалось на [Python 3.9](https://www.python.org/downloads/release/python-390/)

Для установки на локальный компьютер рекомендуется создать виртуальное окружение. В моем случае это делается следующей командой:

```bash
python3.9 -m venv env
```

Клонировать приложение командой (на локальном компьютере должен быть установлен git):

```bash
git clone app link
```

В папке `github-project` нужно создать файл `.env` со следующими переменными окружения:

- SECRET_KEY (секретный ключ Django app)
- DEBUG (включение/выключение режима отладки)
- TOKEN (персональный токен, необходим для снятия ограничения по обращению к api github)

После этого установить необходимые зависимости:

```bash
pip install -r requirements.txt
```

В данном приложении база данных не применялась, поэтому можно сразу запустить приложение:

```bash
python manage.py runserver
```

## Использование

В поле ввода вводите имя пользователя на Github и получаете результаты по всем проектам, куда он делал pull requests.

## Резюме

Резюме доступно по ссылке на github [https://dmitrytokyo.github.io/resume/](https://dmitrytokyo.github.io/resume/)
