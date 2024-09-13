import os
from datetime import datetime, timedelta

import requests
import pandas as pd

from database import Session
from models import SpimexTradingResults


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


class SpimexParser:

    def __init__(self, year: int, month: int):
        self.file = "spimex_data.xls"
        self.links = SpimexDownloader.get_files_links(year, month)
        self.session = Session()

    def _write_to_file(self, data):
        with open(self.file, "wb") as file:
            file.write(data)

    def _delete_file(self):
        if os.path.exists(self.file):
            os.remove(self.file)

    def _get_necessary_data(self, file) -> pd.DataFrame:
        df = pd.read_excel(file, sheet_name=0, header=6)
        df[df.columns[14]] = pd.to_numeric(df[df.columns[14]], errors="coerce")
        df = df[df[df.columns[14]] > 0]
        df = df.iloc[:-2, [1, 2, 3, 4, 5, -1]]
        df[df.columns[3]] = pd.to_numeric(df[df.columns[3]], errors="coerce")
        df[df.columns[4]] = pd.to_numeric(df[df.columns[4]], errors="coerce")

        return df

    def _seve_to_db(self, obj: list[SpimexTradingResults]):
        with self.session as s:
            s.add_all(obj)
            s.commit()
            s.close()

    def start(self):

        for date, link in self.links:
            response = requests.get(url=link, timeout=10)
            self._write_to_file(response.content)

            df_data = self._get_necessary_data(self.file)
            prepared_obj = []
            for _, row in df_data.iterrows():
                columns = row.to_list()
                obj = SpimexTradingResults(
                    exchange_product_id=columns[0],
                    exchange_product_name=columns[1],
                    oil_id=columns[0][:4],
                    delivery_basis_id=columns[0][4:7],
                    delivery_basis_name=columns[2],
                    delivery_type_id=columns[0][-1],
                    volume=columns[3],
                    total=columns[4],
                    count=columns[5],
                    date=date,
                )
                prepared_obj.append(obj)

            self._seve_to_db(prepared_obj)
            self._delete_file()
