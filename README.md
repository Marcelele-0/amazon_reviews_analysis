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
├── data/                      # Raw dataset              
├── src/                       # Python modules (EDA, NLP, ML pipelines)
│   ├── ...
├── notebooks/
│   └── amazon_reviews_analysis.ipynb  # Main notebook
├── .gitignore
├── environment.yml            # Conda environment setup
└── README.md 
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

1. **Missing Values**:
   - Significant number of missing values in `product/price` and `review/userId`.
   - `review/profileName` also has a considerable amount of missing values.

2. **Unknown Values**:
   - Many entries have 'unknown' as the value for `product/price`, `review/userId`, and `review/profileName`.

3. **Data Types**:
   - `review/score` is converted to float.
   - `review/time` is converted to datetime.
   - `review/helpfulness` is split into `review/helpfulness_numerator` and `review/helpfulness_denominator`.

4. **Inconsistent Prices**:
   - Products with the same `productId` or `product/title` have different prices, indicating potential data quality issues.

5. **General Statistics**:
   - The dataset contains 236,243 rows and 10 columns after cleaning.
   - The percentage of missing data for each column is significant, especially for `product/price`.

## Planned Features
- [ ] Exploratory Data Analysis (EDA)
- [ ] Sentiment Analysis (Rule-based & ML)
- [ ] Recommendation Engine
- [ ] Review Clustering & Topic Modeling
- [ ] Optional: Interactive Dashboard (Plotly/Dash)
