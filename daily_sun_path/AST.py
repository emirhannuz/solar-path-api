from .datetime_tools import time_to_seconds
from .EquationTime import EquationTime


class AST:

    def __init__(self, location):
        """
            :param location must be Location object
        """
        self.location = location
        self.longitude_correction = self.__calculate_longitude_correction()
        self.equation_time = EquationTime(location.date).equation_time
        self.ast = float(format(self.__calculate_ast(), '.2f'))
        self.day_light_saving = False

    def __calculate_ast(self):
        # ast = LST + LC + ET
        return (time_to_seconds(
            self.location.time) + round(self.longitude_correction) * 60 + round(self.equation_time) * 60) / 60 / 60

    def __calculate_longitude_correction(self):
        return -4 * (self.location.standard_longitude - self.location.local_longitude)
