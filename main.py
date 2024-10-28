from src.data_loader import DataLoader
from src.preprocessing import DataPreprocessor
import os

def main():

    file_path = './data/data.xlsx'
    output_folder = './processed_data/'
    os.makedirs(output_folder, exist_ok=True)

    # Caricamento dell'intero file
    data_loader = DataLoader(file_path)
    all_sheets = data_loader.load_all_sheets()

    # Fogli che vogliamo processare. Al momento solo il foglio Massa perchè gli altri due fogli sono identici - chiedere chiarimenti
    # selected_sheets = ['Massa', 'Organic F.C.', 'Metallic F.C.']
    selected_sheets = ['Massa']

    # Fase di preprocessing dei dati
    preprocessor = DataPreprocessor()

    for sheet_name in selected_sheets:

        if sheet_name in all_sheets:
            df = all_sheets[sheet_name]
            print(f"Processando il foglio: {sheet_name}")

            # Rinomina le colonne in modo che rispettino la convenzione tutto minuscolo senza spazi
            df_cleaned = DataPreprocessor.rename_columns(df)

            # Elimina i valori mancanti
            df_cleaned = preprocessor.drop_columns_with_missing_data(df)

            # TODO: Trasforma i valori decimali in interi o comunque valori accettabili per fare ANOVA

            # Salva il DataFrame processato in un nuovo file Excel per testare il risultato ottenuto
            output_file = os.path.join(output_folder, f"{sheet_name}_processed.xlsx")
            df_cleaned.to_excel(output_file, index=False)
            print(f"Foglio processato salvato in: {output_file}")

        else:
            print(f"Il foglio '{sheet_name}' non è presente nel file Excel.")


if __name__ == "__main__":
    main()
