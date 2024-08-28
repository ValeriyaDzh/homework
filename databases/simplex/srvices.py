import datetime
import os

import requests


class ExcelManager:

    def __init__(self, filename):
        self.filename = filename

    def write(self, data):
        with open(self.filename, "wb") as file:
            file.write(data)

    def delete(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)


class SimplexDownloader:

    def get_files_links(self, year: int, month: int, day: int = 1):
        links = []
        str_data = datetime.date(year, month, day).isoformat().split("-")
        for d in range(day, 32):
            if d < 10:
                d = f"0{d}"
            url = f"https://spimex.com/upload/reports/oil_xls/oil_xls_{str_data[0]}{str_data[1]}{d}162000.xls"

            if self._is_valid(url):
                links.append(url)
        return links

    @staticmethod
    def _is_valid(url) -> bool:
        response = requests.head(url)
        return response.status_code == 200


# excel = ExcelManager("mmmm.xls")
# a = SimplexDownloader()
# res = a.get_files_links(2024, 8, 15)
# for r in res:
#     req = requests.get(r)
#     excel.write(req.content)
