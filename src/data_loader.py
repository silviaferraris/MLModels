import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_all_sheets(self, skip_rows=3, na_values='MISSING'):
        """
        Carica tutti i fogli di un file Excel.

        :param skip_rows: Numero di righe da saltare all'inizio del file
        :param na_values: Valori da considerare come NaN
        :return: Dizionario con i DataFrame per ogni foglio
        """
        return pd.read_excel(self.file_path, sheet_name=None, skiprows=skip_rows, na_values=na_values)


