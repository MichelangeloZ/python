# _*_coding:utf-8 _*_

# 测试函数
import unittest

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()


def get_formatted_name(first, middle, last):
    full_name = first + " " + middle + " " + last
    return full_name.title()


class NamesTestCase(unittest.TestCase):
    def test_name(self):
        formated_name = get_formatted_name("jay", "chou")
        # 断言方法用来核实得到的结果是否与期望的结果一致
        self.assertEqual(formated_name, "Jay Chou")
unittest.main()



def get_country_city_population(city, country, population=""):
    if population:
        full = city + ", "  + country + " population=" + str(population)
        return full
    else:
        full = city + ", "  + country
    return full.title()

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        full = get_country_city_population("beijing", "china")
        self.assertEqual(full, "Beijing, China")

    def test_city_country_population(self):
        full = get_country_city_population("beijing", "china", "1300000000")
        self.assertEqual(full, "beijing, china population=1300000000")

unittest.main()

