from utils.parser import parse_data
from utils.correct_types import convert_data_types, clean_data
import gzip

def main():
    """
    Loads raw Amazon review data, parses it into structured DataFrame,
    performs a quick overview, and saves cleaned data to CSV.
    """
    file_path = 'data/Cell_Phones_&_Accessories.txt.gz'

    # Read the .gz file
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        raw_lines = f.readlines()

    df = parse_data(raw_lines)
    df = clean_data(df)
    
    # Simple analysis
    print(df.head())
    print(df.info())
    print(df.isna().sum())

    # Save to CSV
    df.to_csv('data/cleaned_amazon_reviews.csv', index=False)

if __name__ == "__main__":
    main()