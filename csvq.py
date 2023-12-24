import csv
import config



class GetDate():

    def __init__(self):
        self.year_position = 0  # на данной позиции находится год в файле csv
        self.position_za_year = 13
        self.average_value_for_the_year_all_pos = 14
        self.average_value_for_the_year_pos = 15
        self.mediana_pos = 16
        self.width = 20
        self.longitude = 21
        self.altitude_above_sea_level = 22
        self.country = 17
        self.region = 18
        self.station = 19

    def read_conf(self):
        with open("monthly_and_annual_precipitation_amounts.csv", encoding='utf-8') as r_file:
            # Создаем объект reader, указываем символ-разделитель ","
            file_reader = csv.reader(r_file, delimiter=",")
            # Счетчик для подсчета количества строк и вывода заголовков столбцов
            count = 0
            mas = []
            # Считывание данных из CSV файла
            for row in file_reader:

                if count != 0:
                    # print(row[width])
                    if not ((row[self.width] != "") and (float(row[self.width]) > 40.00) and (float(row[self.width]) < 47.00)):
                        continue
                    if not ((float(row[self.longitude]) > 40.00) and (float(row[self.longitude]) < 90.00)):
                        continue
                    if not ((int(row[self.altitude_above_sea_level].strip(" м.")) > 670) and (
                            int(row[self.altitude_above_sea_level].strip(" м.")) < 700)):
                        continue
                    if not ((int(row[self.year_position]) > 2008) and (int(row[self.year_position]) < 2018)):
                        continue
                    # Вывод строк
                    # if поля введённые не пустые то
                    # Организовать выбор через qlistwidgets (выпадающий список)
                    # 1-ый график (года от температур)

                    if ((row[self.position_za_year] != "@") and float(row[self.position_za_year]) != -999.0):
                        tup_n = (row[self.year_position], row[self.position_za_year])
                        mas.append(tup_n)
                        # print(float(row[position_za_year])==-999.0)
                    # 2-ой график (года от средних значений за год)

                count += 1
                # if count==7:
                #    break
            # print(mas)
        return mas

    def first_config(self,file_csv):
        dict1 = {}

        with open(file_csv, encoding='utf-8') as r_file:
            # Создаем объект reader, указываем символ-разделитель ","
            file_reader = csv.reader(r_file, delimiter=",")
            # Счетчик для подсчета количества строк и вывода заголовков столбцов
            count = 0

            for row in file_reader:

                if count != 0:
                    perem_new_country = row[self.country]
                    perem_new_region = row[self.region]
                    perem_new_station = row[self.station]

                    # добавляем элементы в словари и массивы
                    # добавляем уникальный элемент в словарь
                    if perem_new_country not in dict1:
                        dict1[perem_new_country] = {}

                    if perem_new_region not in dict1[perem_new_country]:
                        dict1[perem_new_country][perem_new_region] = []

                    # добавляем уникальный элемент в массив
                    if perem_new_station not in dict1[perem_new_country][perem_new_region]:
                        dict1[perem_new_country][perem_new_region].append(perem_new_station)

                count += 1

        return dict1





GetDate().first_config("monthly_and_annual_precipitation_amounts.csv")