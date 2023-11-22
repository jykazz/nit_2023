import random
import pandas as pd

# Генерация данных для мероприятий
def generate_data(num_events):
    data = []
    for _ in range(num_events):
        season = random.randint(1, 4)  # 1 - Весна, 2 - Лето, 3 - Осень, 4 - Зима
        temperature = random.uniform(-10, 35)  # Температура в градусах Цельсия
        expected_participants = random.randint(10, 1000)
        ticket_price = random.uniform(10, 200)

        # Генерация фактического числа участников (может быть больше, меньше или равно ожидаемому)
        actual_participants = random.randint(expected_participants - 100, expected_participants + 100)

        data.append([season, temperature, expected_participants, actual_participants, ticket_price])

    df = pd.DataFrame(data, columns=['Season', 'Temperature', 'Expected_Participants', 'Actual_Participants', 'Ticket_Price'])
    df.to_csv('events_data.csv', index=False)

if __name__ == '__main__':
    num_events = 1000  # Количество мероприятий для генерации
    generate_data(num_events)
