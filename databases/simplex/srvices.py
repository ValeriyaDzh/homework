import datetime
import os

import requests
import pandas as pd


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

    def get_files_links(self, year: int, month: int, day: int = 1) -> list[tuple[str]]:
        links = []
        str_data = datetime.date(year, month, day).isoformat().split("-")
        for d in range(day, 32):
            if d < 10:
                d = f"0{d}"
            url = f"https://spimex.com/upload/reports/oil_xls/oil_xls_{str_data[0]}{str_data[1]}{d}162000.xls"

            if self._is_valid(url):
                data_file = datetime.date(year, month, d).isoformat()
                links.append((data_file, url))
        return links

    @staticmethod
    def _is_valid(url) -> bool:
        response = requests.head(url)
        return response.status_code == 200


class SimplexParser:

    def __init__(self):
        self.file = "simplex_data.xls"
        self.em = ExcelManager(self.file)
        self.dowloander = SimplexDownloader()

    def _get_necessary_data(self, file) -> pd.DataFrame:
        df = pd.read_excel(file, sheet_name=0, header=6)
        print(df.columns[14])
        df[df.columns[14]] = pd.to_numeric(df[df.columns[14]], errors="coerce")
        df = df[df[df.columns[14]] > 0]
        df = df.iloc[:-2, [1, 2, 3, 4, 5, -1]]
        df[df.columns[3]] = pd.to_numeric(df[df.columns[3]], errors="coerce")
        df[df.columns[4]] = pd.to_numeric(df[df.columns[4]], errors="coerce")
        df.to_excel("some_2file.xlsx")
        return df


# par = SimplexParser()
# print(par._get_necessary_data("mmmm.xls"))
