from scipy.stats import f_oneway
import pandas as pd

class StatisticalAnalyzer:
    @staticmethod
    def perform_anova(df, target_column):
        """
        Esegue l'ANOVA sulle colonne discrete del DataFrame rispetto a una colonna target.

        :param df: Il DataFrame con le colonne su cui eseguire l'ANOVA
        :param target_column: La colonna di destinazione per l'ANOVA
        :return: DataFrame con i risultati dell'ANOVA (colonna e p-value)
        """
        # Converte colonna target in formato numerico
        df[target_column] = pd.to_numeric(df[target_column], errors='coerce')

        # Seleziona le colonne discrete ignorando le non numerice
        discrete_columns = df.select_dtypes(include=['int64', 'category']).columns
        anova_results = []

        for col in discrete_columns:
            if col != target_column:

                df[col] = pd.to_numeric(df[col], errors='coerce')

                # Esegue l'ANOVA (tranne per le righe non valide che hanno NaN)
                groups = [df[df[col] == value][target_column].dropna() for value in df[col].unique() if pd.notnull(value)]
                if len(groups) > 1:  # ANOVA funziona sono se ci sono almeno due colonne di input
                    f_stat, p_value = f_oneway(*groups)
                    anova_results.append({'Column': col, 'P-Value': p_value})

        return pd.DataFrame(anova_results)
