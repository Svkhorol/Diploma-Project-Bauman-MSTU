import pickle

import numpy as np
from flask import Flask, render_template, request


def get_prediction(values: list) -> float:
    '''Функция для обработки данных и вычислений модели.'''

    # загрузка модели
    model = pickle.load(open('model/model_xgb.pkl', 'rb'))

    # загрузка масштабаторов
    scaler_X = pickle.load(open('model/scaler_X.pkl', 'rb'))
    scaler_y = pickle.load(open('model/scaler_y.pkl', 'rb'))

    # масштабирование входных значений
    X_scl = scaler_X.transform(np.array(values).reshape(1, -1))

    # прогноз
    y_pred_scl = model.predict(X_scl)

    # обратное масштабирование прогноза
    y_pred = scaler_y.inverse_transform(y_pred_scl.reshape(-1, 1))
    y_pred = round(float(y_pred), 2)

    return y_pred

names = ['Количество отвердителя, м.%',
         'Содержание эпоксидных групп, %',
         'Температура вспышки, С',
         'Потребление смолы, г/м2',
         'Угол нашивки, град',
         'Шаг нашивки',
         'Плотность нашивки',
         'Плотность, кг/м3',
         'Поверхностная плотность, г/м2',
         'Модуль упругости, ГПа',
         'Соотношение матрица-наполнитель']


app = Flask(__name__,
            template_folder='templates',
            static_folder='static')

# "Оборачиваем" функцию в декоратор для указания относительного
# пути, который она будет обрабатывать. Это главная страница сайта
# Также указываем доступные методы для запроса страницы
@app.route('/', methods= ['POST', 'GET'])
def main():
    '''Функция для рендеринга главной страницы main.html приложения.

    Сначала функция main проверяет метод запроса. Если это запрос на получение
    данных (GET),то функция рендерит страницу main.html с формами для заполнения.
    Если это запрос с отправкой данных на сервер (POST), то пользователь может
    ввести новые данные (или оставляет текущие, предварительно заполненные
    при рендеринге страницы). Затем происходит валидация введеных данных на
    нескольких уровнях. А именно - HTML формы имеют встроенную функциональность
    для валидации полей формы на стороне пользователя (в браузере).  Помимо этого реализована
    проверка вводимого диапазана данных непосредственно на сервере (список ошибок errors).
    '''

    # Обработка GET-запроса для получение страницы,
    if request.method == 'GET':
        return render_template('main.html')

    # Обработка POST-запроса для отправки данных на сервер
    if request.method == 'POST':
        input_values = []
        errors = []
        for field_name in names:
            # получаем значение из поля формы и добавляем это значение в список
            value = float(request.form.get(field_name))
            if not (0 <= value <= 7000):
                # если значение из поля формы выходит за диапазон значений,
                # добавляем ошибку в список
                errors.append(field_name)
            input_values.append(value)

        # запускаем расчет
        y = get_prediction(input_values)

        # Если какие-либо данные были вне диапазона допустимых значений
        if len(errors) > 0:
            # рендерим страницу с сообщением об ошибке
            return render_template('main.html', errors=errors)
        # Если ошибок нет - возвращам результат расчета модели
        return render_template('main.html', result=y)


if __name__ == '__main__':
    app.run()
