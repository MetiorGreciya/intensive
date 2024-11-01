import cianparser
import csv
import time
import random

# Создаем парсер для указанного местоположения
parser = cianparser.CianParser(location="Долгопрудный")

# Инициализируем список для хранения данных о квартирах
all_flats_data = []

# Проходим по страницам
for page in range(1, 2):
    try:
        # Получаем данные о квартирах
        data = parser.get_flats(deal_type="sale", rooms=(1), with_extra_data=True, additional_settings={"start_page": page, "end_page": page})

        print(data)
        print('--------------------------------------------------------------------------')

        # Обрабатываем каждую квартиру
        for flat in data:
            flat['author'] = flat.get('author', 'Не указано')
            flat['author_type'] = flat.get('author_type', 'Не указано')
            flat['url'] = flat.get('url', 'Не указано')
            flat['location'] = flat.get('location', 'Не указано')
            flat['deal_type'] = flat.get('deal_type', 'Не указано')
            flat['accommodation_type'] = flat.get('accommodation_type', 'Не указано')
            flat['floor'] = flat.get('floor', 'Не указано')
            flat['floors_count'] = flat.get('floors_count', 'Не указано')
            flat['rooms_count'] = flat.get('rooms_count', 'Не указано')
            flat['total_meters'] = flat.get('total_meters', 'Не указано')
            flat['price_per_month'] = flat.get('price_per_month', 'Не указано')
            flat['commissions'] = flat.get('commissions', 'Не указано')
            flat['price'] = flat.get('price', 'Не указано')
            flat['district'] = flat.get('district', 'Не указано')
            flat['street'] = flat.get('street', 'Не указано')
            flat['house_number'] = flat.get('house_number', 'Не указано')
            flat['underground'] = flat.get('underground', 'Не указано')
            flat['residential_complex'] = flat.get('residential_complex', 'Не указано')

            all_flats_data.append(flat)

    except Exception as e:
        print(f"Ошибка на странице {page}: {e}")
        break

# Сохранение данных в CSV файл
if all_flats_data:
    keys = all_flats_data[0].keys()
    with open("data.csv", 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writerows(all_flats_data)

    print("Данные успешно сохранены в data.csv")

time.sleep(random.uniform(3, 6))
print("Парсинг завершён.")
