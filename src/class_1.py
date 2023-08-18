from lxml import etree


# Класс отвечает на вопрос "Какие варианты перелёта из source в destination мы получили?"
class Parse_data_class():
    def __init__(self, data, source, destination):
        self.data = data
        self.source = source
        self.destination = destination

    def parse_data(self):
        final = []
        result = dict(Source=None,Destination=None,DepartureTimeStamp=None,
                      ArrivalTimeStamp=None,FareBasis=None,FlightNumber=None)
        tree = etree.parse(self.data)
        root = tree.getroot()
        base_nodes = root.xpath('//Flight')    # for range
        nodes_source = root.xpath('//Source') 
        nodes_destination = root.xpath('//Destination')
        nodes_flight_number = root.xpath('//FlightNumber') 
        nodes_departure = root.xpath('//DepartureTimeStamp') 
        nodes_arrival = root.xpath('//ArrivalTimeStamp')
        nodes_farebasis = root.xpath('//FareBasis') 
        for i in range(0, len(base_nodes) - 1, 1):
            i+= 1
            if nodes_source[i].text == self.source:
                if nodes_destination[i].text == self.destination:
                    result['Source'] = nodes_source[i].text
                    result['Destination'] = nodes_destination[i].text
                    result['DepartureTimeStamp'] = nodes_departure[i].text
                    result['ArrivalTimeStamp'] = nodes_arrival[i].text
                    result['FareBasis'] = nodes_farebasis[i].text
                    result['FlightNumber'] = nodes_flight_number[i].text
                    if result not in final:  # there are many duplicates
                        final.append(result)
        return final



