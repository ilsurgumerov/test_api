# Insurance Prediction API & Web App
Этот проект предоставляет REST API и веб-приложение для предсказания вероятности оформления страхового полиса на основе данных клиента. Используется модель машинного обучения, обученная на наборе данных с использованием алгоритма XGBoost.

---

## Содержание

- [Функционал](#функционал)
- [Установка](#установка)
- [Запуск](#запуск)
  - [FastAPI (Backend)](#fastapi-backend)
  - [Streamlit (Frontend)](#streamlit-frontend)
  - [Docker](#docker)
- [Формат запроса](#формат-запроса)
- [Описание модели](#описание-модели)
- [Данные](#данные)
- [Обратная связь](#обратная-связь)

---

## Функционал

- `/predict_model` — предсказание вероятности по входным данным.
- `/stats` — возвращает количество запросов.
- `/health` — проверка работоспособности API.
- Веб-интерфейс на Streamlit для интерактивного ввода данных и получения результата.

---

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/your_username/test_api.git
   cd test_api
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

---

## Запуск

### FastAPI (Backend)

Запуск сервера:
```bash
python app_api.py
```

Сервер будет доступен по адресу: `http://127.0.0.1:5000`

Доступные эндпоинты:
- `GET /health`
- `GET /stats`
- `POST /predict_model`

Пример запроса:
```bash
curl -X POST http://127.0.0.1:5000/predict_model \
     -H "Content-Type: application/json" \
     -d '{"Gender": "Male", "Age": 30, "Previously_Insured": 0, "Vehicle_Age": "1-2 Year", "Vehicle_Damage": "Yes"}'
```

### Streamlit (Frontend)

Запуск веб-приложения:
```bash
streamlit run streamlit_app.py
```

Веб-интерфейс подключается к API по адресу `http://127.0.0.1:5000`.

---

### Docker

Также доступен способ запуска через Docker:

Установка:
```bash
git clone https://github.com/ваш-username/microservices-example.git
cd microservices-example
```

Докер:
```bash
docker compose up -d 
```

После запуска сервисы будут работать в контейнерах. Это удобный способ развёртывания для продакшена или тестирования.

---

## Формат запроса

Пример JSON для предсказания:
```json
{
  "Gender": "Male",
  "Age": 30,
  "Previously_Insured": 0,
  "Vehicle_Age": "1-2 Year",
  "Vehicle_Damage": "Yes"
}
```

---

## Описание модели

- **Модель:** XGBoost Classifier
- **Файл модели:** `model_XGB.pkl`
- **Признаки:**
  - `Gender`
  - `Age`
  - `Previously_Insured`
  - `Vehicle_Age`
  - `Vehicle_Damage`

### Предобработка

Предобработка данных выполняется в файле `preprocessing.py`. Она включает:
- Кодирование категориальных признаков (`LabelEncoder`)
- Преобразование данных в формат, пригодный для подачи в модель

### Обучение

Модель обучалась в ноутбуке `train.ipynb`. В нем можно проследить процесс подготовки данных, обучения и сохранения модели.

---

## Данные

Исходный датасет будет доступен по [ссылке](https://example.com/data.csv).

---

## Обратная связь

Если вы нашли ошибку или у вас есть предложения по улучшению, создайте issue или pull request!
Вы также можете связаться с командой напрямую: **xxxxx@yandex.ru**