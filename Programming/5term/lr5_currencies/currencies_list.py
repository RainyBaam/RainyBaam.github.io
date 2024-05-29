import requests
from xml.etree import ElementTree
import json


class CurrenciesList:

    def get_currencies(self, currencies_ids_lst: list):
        cur_res_str = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
        print(cur_res_str.content)
        result = []

        root = ElementTree.fromstring(cur_res_str.content)
        courses = root.findall("Valute")
        for _v in courses:
            course_id = _v.get('ID')
            course = {}
            if str(course_id) in currencies_ids_lst:
                course_cur_value, course_cur_name = _v.find('Value').text, _v.find('Name').text
                course_charcode = _v.find('CharCode').text
                course[course_charcode] = (course_cur_name, course_cur_value)
                print(course_cur_name, course_cur_value)
                result.append(course)
        return result


if __name__ == "__main__":
    course = CurrenciesList()
    course.get_currencies(["R01090B", "R01100"])
    print(course)

