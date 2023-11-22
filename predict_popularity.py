import pandas as pd
from sklearn.linear_model import LinearRegression

# Загрузка данных
data = pd.read_csv('events_data.csv')

# Разделение данных на признаки (X) и целевую переменную (y)
X = data[['Season', 'Temperature', 'Expected_Participants', 'Ticket_Price']]
y = data['Actual_Participants']

# Создание и обучение модели линейной регрессии
model = LinearRegression()
model.fit(X, y)

# Ввод данных для прогнозирования
season = int(input("Введите сезон проведения мероприятия (1-4): "))
temperature = float(input("Введите температуру в градусах Цельсия: "))
expected_participants = int(input("Введите предполагаемое количество участников: "))
ticket_price = float(input("Введите стоимость билета: "))

# Прогноз фактического числа участников
predicted_actual_participants = model.predict([[season, temperature, expected_participants, ticket_price]])

print(f"Предполагаемое фактическое число участников: {predicted_actual_participants[0]:.2f}")
