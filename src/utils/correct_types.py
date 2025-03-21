import pandas as pd

def convert_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts columns in the DataFrame to their appropriate data types.

    Args:
        df (pd.DataFrame): The DataFrame containing the dataset.
    
    Returns:
        pd.DataFrame: DataFrame with converted data types.
    """
    # Convert review/score to float (some values may need to be coerced to NaN)
    df['review/score'] = pd.to_numeric(df['review/score'], errors='coerce')

    # Convert review/time to datetime (assuming it's in Unix timestamp format)
    df['review/time'] = pd.to_datetime(df['review/time'], unit='s', errors='coerce')

    # Convert review/helpfulness to numeric (split '0/0' into two separate columns for example)
    df[['review/helpfulness_numerator', 'review/helpfulness_denominator']] = df['review/helpfulness'].str.split('/', expand=True)
    df['review/helpfulness_numerator'] = pd.to_numeric(df['review/helpfulness_numerator'], errors='coerce')
    df['review/helpfulness_denominator'] = pd.to_numeric(df['review/helpfulness_denominator'], errors='coerce')

    # Convert product/price to numeric (considering 'unknown' as NaN)
    df['product/price'] = pd.to_numeric(df['product/price'], errors='coerce')

    # Convert relevant columns to string (text data)
    df['product/title'] = df['product/title'].astype(str)
    df['review/summary'] = df['review/summary'].astype(str)
    df['review/text'] = df['review/text'].astype(str)

    return df

import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the DataFrame by converting columns to appropriate data types.
    
    Args:
        df (pd.DataFrame): The DataFrame containing the raw data.
    
    Returns:
        pd.DataFrame: The cleaned DataFrame with appropriate data types.
    """
    
    # Zmieniamy kolumny tekstowe na string
    text_columns = ['product/title', 'review/summary', 'review/text']
    df[text_columns] = df[text_columns].astype('string')
    
    # Zmieniamy kolumny liczbowe na float lub int
    df['product/price'] = pd.to_numeric(df['product/price'], errors='coerce')  # Zmiana na float
    df['review/score'] = pd.to_numeric(df['review/score'], errors='coerce')  # Zmiana na float
    df['review/helpfulness_numerator'] = pd.to_numeric(df['review/helpfulness'].str.split('/').str[0], errors='coerce')
    df['review/helpfulness_denominator'] = pd.to_numeric(df['review/helpfulness'].str.split('/').str[1], errors='coerce')
    
    # Zmieniamy czas na datetime
    df['review/time'] = pd.to_datetime(df['review/time'], unit='s', errors='coerce')
    
    # Zmieniamy kolumny z ID i nazwami na string (choć w zasadzie mogą pozostać object, string będzie bardziej optymalny)
    id_columns = ['product/productId', 'review/userId', 'review/profileName']
    df[id_columns] = df[id_columns].astype('string')
    
    return df
