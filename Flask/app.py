import pickle

import flask
import numpy as np
#import sklearn
#import xgboost

from flask import render_template, request
#from sklearn.preprocessing import MinMaxScaler
#from xgboost import XGBRegressor


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


app = flask.Flask(__name__, template_folder='templates')

# Начальная страница
@app.route('/', methods= ['POST', 'GET'])
def main():
    '''Функция отработки web-формы страницы
    - получает со страницы значения
    - возвращает предсказанный результат.
    '''

    # Если происходит запрос методом GET
    if request.method == 'GET':
        return render_template('main.html')

    # Если происходит запрос методом POST
    if request.method == 'POST':

        # передаются данные с веб-форм
        X = []
        for field_name in names:
            # Получаем значение поля формы
            x = float(request.form.get(field_name))  # float(request.form[field_name])
            # Добавляем значение в список
            X.append(x)

        # запускается расчет
        y = get_prediction(X)   # y = get_prediction([[X]])

        # возвращается результат расчета модели
        return render_template('main.html', result=y)


if __name__ == '__main__':
    app.run()

# Тестовые входные значения
# 111.86, 22.26785714, 284.61538462, 220., 0., 5., 57., 2030., 210., 753., 2.77133106

#for field_name in request.form:
    # Получаем значение поля формы
    #x = float(field_name)
    # Добавляем значение в список
    #X.append(x)
