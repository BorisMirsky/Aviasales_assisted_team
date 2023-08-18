from class_2 import Compare_timestamps 
from class_3 import Get_cost  


# Класс отвечает на вопрос "оптимальный вариант"
class Main():
    def __init__(self, path_to_data, source, destination):
        self.path_to_data = path_to_data
        self.source = source
        self.destination = destination
        self.cost_class = Get_cost(self.path_to_data,
                                   self.source,
                                   self.destination)
        self.time_in_road_class = Compare_timestamps(self.path_to_data,
                                                     self.source,
                                                     self.destination)


    def func(self):
        cost = self.cost_class.cost_flight()
        time = self.time_in_road_class.compare_datetimes()
        print(cost, time)


#my_instance1 = Main('../data/RS_ViaOW.xml', 'DXB', 'BKK')  #255 9:00:00
#my_instance2 = Main('../data/RS_Via-3.xml', 'DXB', 'BKK')   #255 9:30:00
#my_instance1.func()
#my_instance2.func()



"""
Выводы
1. Из двух файлов с сотнями записей было только по одной, отвечающей условиям, не считая дубликатов.
2. При сравнение - цена одинакова, время в пути различается на полчаса.

"""




