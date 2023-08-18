from class_1 import Parse_data_class
import re


# Класс отвечает на вопрос "Самый дорогой/дешёвый ... вариант" и вернёт цену билета

def between_two(a, b, text):
    return re.findall(re.escape(a)+"(.*?)"+re.escape(b),text)
 
class Get_cost():
    def __init__(self, path_to_data, source, destination):
        self.path_to_data = path_to_data
        self.source = source
        self.destination = destination
        self.data = None
        self.get_data()


    def get_data(self):
        var = Parse_data_class(self.path_to_data, self.source, self.destination)   
        self.data = var.parse_data()


    def cost_flight(self):
        departure_fare_basis = self.data[0]['FareBasis']
        result = between_two('$', '_', departure_fare_basis)[0]
        return result
