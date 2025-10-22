import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicates_df = person[['email']]
    return duplicates_df[duplicates_df.duplicated(subset=['email'])].drop_duplicates()

def duplicate_emails_grouby(person: pd.DataFrame) -> pd.DataFrame:
    contagens = person.groupby('email').agg('count')
    contagens_filtradas = contagens[contagens['id'] > 1]
    final = contagens_filtradas.reset_index()
    final = final[['email']]
    return final

