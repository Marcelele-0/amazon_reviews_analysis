import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch

def load_data(file_path):
    """
    Load the dataset from the specified file path.

    Args:
        file_path (str): Path to the CSV file containing the dataset.

    Returns:
        pd.DataFrame: Loaded dataset as a pandas DataFrame.
    """
    return pd.read_csv(file_path)

def initialize_sentiment_analyzer(model_name, device):
    """
    Initialize the sentiment analysis pipeline.

    Args:
        model_name (str): Name of the pre-trained model to use.
        device (int): Device to use for computation (0 for GPU, -1 for CPU).

    Returns:
        pipeline: Sentiment analysis pipeline.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, device=device)

def analyze_sentiment(text, sentiment_analyzer):
    """
    Perform sentiment analysis on a given text.

    Args:
        text (str): Text to analyze.
        sentiment_analyzer (pipeline): Sentiment analysis pipeline.

    Returns:
        str: Sentiment label (e.g., 'POSITIVE', 'NEGATIVE').
    """
    result = sentiment_analyzer(text, truncation=True, max_length=512)
    return result[0]['label']

def save_results(df, output_path):
    """
    Save the DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): DataFrame to save.
        output_path (str): Path to save the CSV file.
    """
    df.to_csv(output_path, index=False)

def main():
    """
    Main function to perform sentiment analysis on Amazon reviews.
    """
    # Load the dataset
    input_file = "data/cleaned_amazon_reviews_v2.csv"
    df = load_data(input_file)

    # Initialize sentiment analysis pipeline
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    device = 0 if torch.cuda.is_available() else -1  # 0 = GPU, -1 = CPU
    print(f"Using device: {'GPU' if device == 0 else 'CPU'}")
    sentiment_analyzer = initialize_sentiment_analyzer(model_name, device)

    # Apply sentiment analysis
    df['sentiment'] = df['review/text'].apply(lambda text: analyze_sentiment(text, sentiment_analyzer))

    # Save results
    output_file = "data/output_with_sentiment.csv"
    save_results(df, output_file)
    print("Sentiment analysis complete and saved to output_with_sentiment.csv")

if __name__ == "__main__":
    main()