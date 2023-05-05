## Diploma-Project-Bauman-MSTU  
### Прогнозирование конечных свойств новых материалов (композиционных материалов)  
#### Prediction the final properties of new materials (composite materials)  
___________
В работе разработаны модели машинного обучения для прогнозирования ряда механических свойств композиционных материалов. На основе лучшей модели разработано web-приложение, прогнозирующее прочностные характеристики композитов. Кейс основан на реальных производственых задачах Центра НТИ "Цифровое материаловедение: новые материалы и вещества".
  
### Содержание  
[1. Разведочный анализ данных](https://github.com/Svkhorol/Diploma-Project-Bauman-MSTU/blob/main/notebooks/1_EDA.ipynb)  
[2. Выявление реальных и синтетических данных](https://github.com/Svkhorol/Diploma-Project-Bauman-MSTU/blob/main/notebooks/2_Synthetic_Data.ipynb)  
[3. Предобработка данных c удалением выбросов](https://github.com/Svkhorol/Diploma-Project-Bauman-MSTU/blob/main/notebooks/3_Processing.ipynb)  
[4. Предобработка данных c заменой выбросов](https://github.com/Svkhorol/Diploma-Project-Bauman-MSTU/blob/main/notebooks/3_Processing_save_outliers_in_real_data.ipynb)  
[5. Создание, тестирование и сравнение моделей](https://github.com/Svkhorol/Diploma-Project-Bauman-MSTU/blob/main/notebooks/4_Modeling.ipynb)  
[6. Подготовка модели для приложения](https://github.com/Svkhorol/Diploma-Project-Bauman-MSTU/blob/main/Flask/src/get_prediction_func.ipynb)  
  
### Инструкция по запуску приложения  
Для запуска web-приложения перейти в браузере по ссылке:  
  
http://svkhorol.pythonanywhere.com/  
  
Для запуска приложения на локальном сервере:  
  
- Требуется Python версии не ниже 3.10  
  
- Клонировать репозиторий:
```bash
git clone https://github.com/Svkhorol/Diploma-Project-Bauman-MSTU.git
```  
- Перейти в папку с проектом, создать и активировать в ней виртуальное окружение:  
```bash
cd Diploma-Project-Bauman-MSTU
python -m venv venv
source venv/Scripts/activate
```
 
- Установить зависимости из файла requirements.txt:
```bash
python -m pip install --upgrade pip  
pip install -r requirements.txt  
```
- В папке Diploma-Project-Bauman-MSTU перейти в папку Flask и запустить в ней исполняемый файл:  
```bash
cd Flask
python app.py 
```
- В терминале перейти по ссылке http://127.0.0.1:5000 на локальный сервер
