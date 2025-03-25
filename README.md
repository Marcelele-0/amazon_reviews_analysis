# Amazon Reviews Analysis

- Data Science project focused on exploratory analysis, sentiment classification, recommendation system, and clustering based on Amazon product reviews from the "Cell Phones & Accessories" category.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Project Structure](#project-structure)
4. [Installation & Setup](#installation-and-setup)
5. [Usage](#usage)
6. [Technologies](#technologies)
7. [Findings from EDA](#findings-from-eda)
8. [Planned Features](#planned-features)

---

## Project Overview
This project analyzes Amazon product reviews using Machine Learning and NLP techniques. The goal is to extract meaningful insights, build a sentiment analyzer, recommend top products, and cluster customer reviews.

---

## Dataset
Dataset used:  
**Amazon Cell Phones & Accessories reviews**  
Source: [Amazon Reviews](https://snap.stanford.edu/data/web-Amazon-links.html)

Format: `Cell_Phones_&_Accessories.txt.gz`

---

## Project Structure
```plaintext
amazon_reviews_analysis/
│
├── data/                      # Raw and cleaned datasets              
├── src/                       # Python modules for EDA, NLP, and ML pipelines
│   ├── preprocessing.py       # Data preprocessing script
│   ├── sentiment_analyzer.py  # Sentiment analysis script
│   └── utils/                 # Helper modules for parsing and cleaning
├── notebooks/                 # Jupyter notebooks for analysis
│   └── amazon_reviews_analysis.ipynb  # Main analysis notebook
├── notebook_summary.md        # Detailed analysis report                
├── environment.yml            # Conda environment setup
├── .gitignore                 # Git ignore file
└── README.md                  # Project documentation
```

## Installation and setup

1)

```bash
git clone https://github.com/marcelele-0/amazon_reviews_analysis.git
cd amazon_reviews_analysis
```

2)

```bash
conda env create -f environment.yaml
conda activate amazon_reviews
```

## Usage

To run the data preprocessing and analysis, execute the following command:

```bash
python src/preprocessing.py
```

## Technologies
  - python
  - pandas
  - numpy
  - scikit-learn
  - matplotlib

## Findings from EDA

 - look for them in report.md

## Planned Features
- [X] Exploratory Data Analysis (EDA)
- [X] Sentiment Analysis (Rule-based & ML)
- [ ] Recommendation Engine
- [X] Review Clustering 
- [ ] Optional: Interactive Dashboard (Plotly/Dash)
