class WeatherErrors(Exception):
    pass

class CityNameError(WeatherErrors):
    error = ('\n|Invalid city name. |\n|Please try again...|')
    def __init__(self):
        super().__init__()
        self.msg = self.error

    def __str__(self):
        return self.msg

class NoCityFoundError(WeatherErrors):
    error = '\n|There is no city found with that name.|'
    '\n|Please try again...                   |'
    def __init__(self):
        super().__init__()
        self.msg = self.error

    def __str__(self):
        return self.msg
    
class KeyError(WeatherErrors):
    error = ('\n|Invalid URL.       | \n|Please try again...')
    def __init__(self):
        super().__init__()
        self.msg = self.error_message

    def __str__(self):
        return self.msg