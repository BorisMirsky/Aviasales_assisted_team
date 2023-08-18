from class_1 import Parse_data_class
from datetime import datetime
import time


# Класс отвечает на вопрос "Самый быстрый/долгий ... вариант" и вернёт расчётное время в пути.
class Compare_timestamps():
    def __init__(self, path_to_data, source, destination):
        self.path_to_data = path_to_data
        self.source = source
        self.destination = destination
        self.data = None
        self.get_data()

    def get_data(self):
        var = Parse_data_class(self.path_to_data, self.source, self.destination)   
        self.data = var.parse_data()
        
    def departure_ts_processing(self):
        departure_ts = self.data[0]['DepartureTimeStamp']
        departure_ts_splitted_0 = departure_ts.split('T')[0]
        departure_ts_splitted_1 = departure_ts.split('T')[1]
        departure_y = int(departure_ts_splitted_0.split('-')[0])
        departure_mo = int(departure_ts_splitted_0.split('-')[1])
        departure_d = int(departure_ts_splitted_0.split('-')[2])
        departure_h = int(departure_ts_splitted_1[:2])
        departure_mi = int(departure_ts_splitted_1[2:])
        departure_datetime = datetime(departure_y, departure_mo, departure_d, departure_h, departure_mi) #, 0)
        return departure_datetime

    def arrival_ts_processing(self):
        arrival_ts = self.data[0]['ArrivalTimeStamp']
        arrival_ts_splitted_0 = arrival_ts.split('T')[0]
        arrival_ts_splitted_1 = arrival_ts.split('T')[1]
        arrival_y = int(arrival_ts_splitted_0.split('-')[0])
        arrival_mo = int(arrival_ts_splitted_0.split('-')[1])
        arrival_d = int(arrival_ts_splitted_0.split('-')[2])
        arrival_h = int(arrival_ts_splitted_1[:2])
        arrival_mi = int(arrival_ts_splitted_1[2:])
        arrival_ts = self.data[0]['ArrivalTimeStamp']
        arrival_datetime = datetime(arrival_y, arrival_mo, arrival_d, arrival_h, arrival_mi) #, 0)
        return arrival_datetime

    def compare_datetimes(self):
        departure_datetime = self.departure_ts_processing()
        arrival_datetime = self.arrival_ts_processing()
        datetime_difference = arrival_datetime - departure_datetime
        return datetime_difference
        





