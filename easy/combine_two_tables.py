import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result_table = pd.merge(person, address, on='personId', how='left')
    result_table = result_table[['firstName', 'lastName', 'city', 'state']]
    return result_table
