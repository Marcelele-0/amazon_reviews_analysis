import pandas as pd

def parse_data(raw_lines: list) -> pd.DataFrame:
    """
    Parses the raw lines of dataset into a pandas DataFrame.
    Used when a column is not consistent in number of lines.

    Args:
        raw_lines (list): List of raw .txt lines.
    
    Returns:
        pd.DataFrame: DataFrame containing the parsed data.
    """
    reviews = []
    current_review = {}

    for line in raw_lines:
        # Skip empty lines
        if line.strip() == "":
            continue

        if line.startswith("product/productId:"):
            if current_review:                     # If current review is not empty, save it
                reviews.append(current_review)     # Save the current review before starting a new one
                current_review = {}                # Start a new review

        if ": " in line:
            key, value = line.split(":", 1)
            current_review[key.strip()] = value.strip()

    if current_review:  # Add the last review if it exists
        reviews.append(current_review)
    
    dataframe = pd.DataFrame(reviews)

    return dataframe

