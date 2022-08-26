
import csv


FILE_RAW_DATA = 'cards'
FILE_CLEARED_DATA = 'clear_data'
FILE_CSV = '05.csv'


fieldnames = [
    'URL_товара',  # index 0
    'Название',  # index 1
    'Цена',  # index 2
    'Валюта',  # index 3
    'Наличие',  # index 4
    'Опт',  # index 5
    'Розница',  # index 6
    'Артикул',  # index 7
    'URL_фото',  # index 8
    'Категория',  # index 9
    'Полная_категория',  # index 10
    'Описание',  # index 11
    'Телефон_1',  # index 12
    'Телефон_2',  # index 13
    'Почта',  # index 14
    'Город',  # index 15
    'Координаты',  # index 16
    'Название_продавца',  # index 17
    'URL_продавца',  # index 18
    'Адрес_продавца',  # index 19
    'Самовывоз',  # index 20
    'Доставка_транспортной_компанией',  # index 21
    'Доставка_автопарком_компании',  # index 22
    'Доставка_курьером',  # index 23
    'Доставка_почтой',  # index 24
    'Доставка_металлопроката_в_речные_порты',  # index 25
    'Oстальные_способы_доставки',  # index 26
    'Характеристики',  # index 27
    'Условия_оплаты',  # index 28
    ]


def read_file_raw_data() -> list[str]:
    with open(FILE_RAW_DATA, "r", encoding="utf-8") as file:
        return file.readlines()


def clear_str(file_readed_lines: list[str]) -> None:
    with open(FILE_CLEARED_DATA, 'w', encoding='utf-8') as file:
        for item in file_readed_lines:
            if ';' in item:
                new_item = item.replace(';', '*')
                file.write(new_item)
                continue
            if '{"except":"NoSuchElementException"}\n' in item:
                continue
            if 'null' in item:
                continue
            if '{"response":"code not pulse.ru"}\n' in item:
                continue
            else:
                file.write(item)


def safe_csv():
    with open(FILE_CLEARED_DATA, "r", encoding="utf-8", newline='') as file:
        temp = file.readlines()
        with open(FILE_CSV, 'a', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            for line in temp:
                try:
                    data = eval(f'{line}')
                    writer.writerow(data)
                except:
                    continue


def main():
    file_readed_lines = read_file_raw_data()
    clear_str(file_readed_lines)
    safe_csv()


if __name__ == '__main__':
    main()
