import pandas as pd

class DataPreprocessor:
    @staticmethod
    def rename_columns(df):
        """
        Rinomina le colonne del DataFrame in minuscolo e sostituisce gli spazi con underscore.

        :param df: Il DataFrame con le colonne da rinominare
        :return: DataFrame con colonne rinominate
        """
        df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace(r'[^\w\s]', '', regex=True)
        return df

    @staticmethod
    def drop_columns_with_missing_data(df, threshold=50):
        """
        Rimuove le colonne che superano la percentuale massima di valori mancanti.

        :param df: Il DataFrame da pulire
        :param threshold: Percentuale massima di valori mancanti accettata
        :return: DataFrame pulito
        """
        missing_percentage = df.isnull().mean() * 100
        return df.loc[:, missing_percentage < threshold]

    @staticmethod
    def categorize_column(df, column, method='binning', bins=None, labels=None):
        """
        Trasforma una colonna continua in categorie secondo un metodo specifico.

        :param df: Il DataFrame contenente i dati
        :param column: Nome della colonna da trasformare
        :param method: Metodo di categorizzazione ('binning', 'rounding', 'percentiles')
        :param bins: Lista dei bordi degli intervalli (solo per 'binning')
        :param labels: Etichette per i gruppi (solo per 'binning')
        :return: DataFrame con la colonna trasformata
        """
        if method == 'binning':
            if bins is None or labels is None:
                raise ValueError("Binning method requires 'bins' and 'labels'")
            df[f"{column}_categorized"] = pd.cut(df[column], bins=bins, labels=labels)

        elif method == 'percentiles':
            # Divide la colonna in quartili
            df[f"{column}_categorized"] = pd.qcut(df[column], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

        else:
            raise ValueError("Method must be 'binning' or 'percentiles'")

        return df
