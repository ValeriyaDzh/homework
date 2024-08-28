import os
from datetime import datetime, timedelta

import requests
import pandas as pd

from database import Session
from models import SpimexTradingResults


class ExcelManager:

    def __init__(self, filename):
        self.filename = filename

    def write(self, data):
        with open(self.filename, "wb") as file:
            file.write(data)

    def delete(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)


class SpimexDownloader:

    @classmethod
    def get_files_links(cls, year: int, month: int, day: int = 1) -> list[tuple[str]]:
        links = []
        start_date = datetime(year, month, day).date()

        while True:

            day_str = start_date.strftime("%d")
            url = f"https://spimex.com/upload/reports/oil_xls/oil_xls_{start_date.strftime('%Y%m')}{day_str}162000.xls"

            if cls._is_valid(url):
                links.append((start_date.isoformat(), url))

            next_date = start_date + timedelta(days=1)
            if next_date.month != start_date.month:
                break

            start_date = next_date

        return links

    @staticmethod
    def _is_valid(url) -> bool:
        response = requests.head(url)
        return response.status_code == 200


class SpimexDatabase:

    def __init__(self):
        self.session = Session()

    def seve(self, obj: list[SpimexTradingResults]):

        with self.session as s:
            s.add_all(obj)
            s.commit()
            s.close()

    def prepare_data(
        self,
        ep_id: str,
        ep_n: str,
        oil_id: str,
        db_id: str,
        db_n: str,
        dt_id: str,
        volume: int,
        total: int,
        count: int,
        date: str,
    ):

        spimex_treding_res = SpimexTradingResults(
            exchange_product_id=ep_id,
            exchange_product_name=ep_n,
            oil_id=oil_id,
            delivery_basis_id=db_id,
            delivery_basis_name=db_n,
            delivery_type_id=dt_id,
            volume=volume,
            total=total,
            count=count,
            date=date,
        )
        return spimex_treding_res


class SpimexParser:

    def __init__(self, year: int, month: int):
        self.file = "spimex_data.xls"
        self.em = ExcelManager(self.file)
        self.links = SpimexDownloader.get_files_links(year, month)
        self.db = SpimexDatabase()

    def _get_necessary_data(self, file) -> pd.DataFrame:
        df = pd.read_excel(file, sheet_name=0, header=6)
        print(df.columns[14])
        df[df.columns[14]] = pd.to_numeric(df[df.columns[14]], errors="coerce")
        df = df[df[df.columns[14]] > 0]
        df = df.iloc[:-2, [1, 2, 3, 4, 5, -1]]
        df[df.columns[3]] = pd.to_numeric(df[df.columns[3]], errors="coerce")
        df[df.columns[4]] = pd.to_numeric(df[df.columns[4]], errors="coerce")
        df.to_excel("some_2file.xlsx")
        print(type(df))
        return df


# par = SpimexParser()
# print(par._get_necessary_data("mmmm.xls"))
s = SpimexDownloader()
print(s.get_files_links(2024, 8))
