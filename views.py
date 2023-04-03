# import requests
# from bs4 import BeautifulSoup
import json
file_path = 'data.json'

class GetMixin:
    def get_data(self):
        with open(file_path) as file:
            return json.load(file)
    
    def get_id(self):
        with open('id.txt') as file:
            id = int(file.read())
            id += 1
        
        with open('id.txt', 'w') as file:
            file.write(str(id))
            return id


class CreateMixin(GetMixin):
    def create(self):
        data = super().get_data()
        try:
            new_car = {
                'id': super().get_id(),
                'mark': input('Введите марку авто: '),
                'model': input('Введите модель авто: '),
                'year': int(input('Введите год выпуска авто: ')),
                'engine_vol': float(input('Введите объем авто: ')),
                'color': input('Введите цвет авто: '),
                'body': input('Введите тип кузова: '),
                'mileage': int(input('Введите пробег авто: ')),
                'price': int(input('Введите стоимость авто: '))
            }
        except ValueError:
            print('Вы ввели некорректные данные')
            self.create()
        
        else:
            data.append(new_car)
            with open(file_path, 'w') as file:
                json.dump(data, file)
            print('Successfully created')

class ListingMixin(GetMixin):
    def listing(self):
        print('Список авто: ')
        data = super().get_data()
        for i in data:
            print(i)

class RetrieveMixin(GetMixin):
    def retrieve(self):
        data = super().get_data()

        try:
            id = int(input('Введите id авто: '))
        except ValueError:
            print('Ввели некорректные данные')
            self.retrieve()
        else:
            auto = list(filter(lambda x: x['id'] == id, data))
            if not auto:
                print('Такого авто нет')
            else:
                print(auto[0])

class UpdateMixin(GetMixin):
    def update(self):
        data = super().get_data()
        try:
            id = int(input('Введите id авто: '))
        except ValueError:
            print('Ввели некорректные данные')
            self.update()
        else:
            autos = list(filter(lambda x: x['id'] == id, data))
            if not autos:
                print('Такого авто нет')
            auto = data.index(autos[0])
            choice = int(input('Что вы хотите изменить? 1- mark, 2 - model, 3 - year, 4 - engine_vol, 5 - color, 6 - body, 7 - mileage, 8 - price: '))
            if choice == 1:
                data[auto]['mark'] = input('Введите новую марку: ')
            elif choice == 2:
                data[auto]['model'] = input('Введите новую модель: ')
            elif choice == 3:
                try:
                    data[auto]['year'] = int(input('Введите новый год: '))
                except ValueError:
                    print('----------------------')
            elif choice == 4:
                try:
                    data[auto]['engine_vol'] = float(input('Введите новый объем двигателя: '))
                except ValueError:
                    print('----------------------')
            elif choice == 5:
                data[auto]['color'] = input('Введите новый цвет')
            elif choice == 6:
                data[auto]['body'] = input('Введите новый кузов')
            elif choice == 7:
                try:
                    data[auto]['mileage'] = int(input('Введите новый пробег: '))
                except ValueError:
                    print('----------------------')
            elif choice == 8:
                try:
                    data[auto]['price'] = int(input('Введите новую цену: '))
                except ValueError:
                    print('----------------------')
            else:
                print('Такого поля нет')
                self.update()
            with open(file_path, 'w') as file:
                json.dump(data, file)

class DeleteMixin(GetMixin):
    def delete(self):
        data = super().get_data()
        try:
            id = int(input('Введите id авто: '))
        except ValueError:
            print('Ввели некорректные данные')
            self.delete()
        else:
            auto = list(filter(lambda x: x['id'] == id, data))
            if not auto:
                print('Такого авто нет')
            avto = data.index(auto[0])
            data.pop(avto)
            with open(file_path, 'w') as file:
                json.dump(data, file)
            print('Удалено')
