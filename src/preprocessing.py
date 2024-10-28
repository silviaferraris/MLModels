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
