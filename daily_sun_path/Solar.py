from .math_tools import *
from .datetime_tools import day_of_year


class Solar:
    def __init__(self, ast, latitude):
        """
            :param ast must be AST object
            :param latitude must be number
        """
        self.ast = ast
        self.latitude = latitude
        self.hour_angle = self.__calculate_hour_angle()
        self.declination = self.__calculate_declination()
        self.altitude = float(format(self.__calculate_altitude(), '.2f'))
        self.azimuth = float(format(self.__calculate_azimuth(), '.2f'))

    def __calculate_hour_angle(self):
        return (self.ast.ast - 12) * 15

    def __calculate_declination(self):
        return 23.45 * sind(360 / 365 * (284 + day_of_year(self.ast.location.date)))

    def __calculate_altitude(self):
        a = sind(self.latitude) * sind(self.declination) + cosd(self.latitude) * cosd(
            self.declination) * cosd(self.hour_angle)
        return asind(a)

    def __calculate_azimuth(self):
        z = cosd(self.declination) * sind(self.hour_angle) / cosd(self.altitude)
        return asind(z)
