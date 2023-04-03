from views import CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DeleteMixin
class Cars(CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DeleteMixin):
    pass
class Start:
    def start(self):
        car = Cars()
        try:
            choice = int(input('Добро пожаловать на наш портал, с чего начнём?\n 1 - добавить авто\n 2 - показать все авто\n 3 - показать выбранное авто\n 4 - изменить данные об авто\n 5 - удалить авто\n'))
        except ValueError:
            print('Введите число в соответствии с вашим выбором действия!')
            self.start()
        if choice == 1:
            car.create()
        elif choice == 2:
            car.listing()
        elif choice == 3:
            car.retrieve()
        elif choice == 4:
            car.update()
        elif choice == 5:
            car.delete()
        

begin = Start()
begin.start()
# car.create()
# car.listing()
# car.retrieve()
# car.update()
# car.delete()