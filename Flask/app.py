import pickle

import flask
import numpy as np

from flask import render_template, request

def get_prediction(values: list) -> float:
    '''Функция для обработки данных и вычислений'''

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

app = flask.Flask(__name__, template_folder='templates', static_folder='static')
# Начальная страница
@app.route('/', methods= ['POST', 'GET'])
def main():
    '''Функция отработки web-формы страницы.

    Получает со страницы значения и
    возвращает предсказанный результат.
    '''

    # Если происходит запрос методом GET, т.е. первичное обращение к странице
    if request.method == 'GET':
        return render_template('main.html')

    # Если происходит запрос методом POST, т.е. передаются данные в форме
    if request.method == 'POST':
        # передаются данные с веб-форм
        input_values = []
        for field_name in names:
            # получаем значение поля формы и добавляем значение в список
            input_values.append(float(request.form.get(field_name)))
        # запускается расчет
        y = get_prediction(input_values)
        # возвращается результат расчета модели
        return render_template('main.html', result=y)


if __name__ == '__main__':
    app.run()
