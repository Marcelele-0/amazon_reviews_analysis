# Amazon Reviews Analysis Report

This report provides an in-depth analysis of Amazon product reviews, focusing on the reasoning behind each step, the challenges encountered, and the insights derived from the data.

---

## 1. Initial Data Loading

The dataset was loaded from a compressed `.gz` file. This step ensured that the raw data was accessible for further processing. Error handling mechanisms were implemented to address potential issues, such as missing files or corrupted data. This foundational step was critical to ensure the integrity of the analysis.

---

## 2. Data Cleaning and Formatting

The raw data was stored as key-value pairs in text format, which required significant preprocessing to make it analyzable. The following steps were taken:

- **Parsing and Structuring**: Lines were parsed into key-value pairs, grouped into individual records, and converted into a structured DataFrame.
- **Rationale**: This transformation was necessary to enable the use of Python libraries like `pandas` for efficient data manipulation.

---

## 3. Handling Missing and Problematic Data

### Observations:
- Missing values (`NaN`) and occurrences of the string `unknown` were prevalent in key columns like `review/userId` and `review/profileName`.
- Rows with multiple missing or problematic entries were identified.

### Actions Taken:
- Replaced `unknown` values with `NaN` for consistency.
- Highlighted rows with significant missing data for potential exclusion.

### Results:
- Improved data quality and consistency, enabling more reliable analysis in subsequent steps.

---

## 4. Dataset Description

### Key Insights:
- The dataset contained thousands of rows and multiple columns, each representing different aspects of the reviews.
- Unique value counts and descriptive statistics provided a comprehensive overview of the data.

### Importance:
Understanding the dataset's structure was crucial for identifying potential issues and planning the analysis strategy.

---

## 5. Addressing Product Price Issues

### Problem:
- Significant inconsistencies were found in the `product/price` column, including irrelevant or contradictory values.

### Solution:
- The `product/price` column was dropped, as it was deemed unreliable for analysis.
- The cleaned dataset was saved for future use.

### Outcome:
- Eliminating this problematic column reduced noise in the data and allowed the analysis to focus on more reliable features.

---

## 6. Sentiment Analysis

### Objective:
- To understand the sentiment of reviews and its relationship with other factors, such as review length and helpfulness.

### Findings:
- A weak correlation was observed between review length and helpfulness ratio.
- Visualizations highlighted trends and outliers, providing a deeper understanding of the data.

### Impact:
- These insights helped in identifying patterns that could inform clustering and other advanced analyses.

---

## 7. Clustering Reviews

### Methodology:
- KMeans clustering was applied to group reviews based on features like review score, helpfulness ratio, review length, and sentiment score.

### Results:
- **Cluster 0**: Medium-length, positive reviews with minor issues.
- **Cluster 1**: Short reviews with mixed sentiment.
- **Cluster 2**: Long, detailed, overwhelmingly positive reviews.
- **Cluster 3**: Medium-length, negative reviews highlighting product issues.

### Significance:
- Clustering provided actionable insights into the characteristics of different types of reviews, which could be valuable for targeted marketing or product improvement.

---

## 8. Analysis Summary

### Key Takeaways:
- The analysis revealed that helpfulness depends more on the quality of content than on review length.
- Clustering highlighted distinct patterns in review behavior, offering valuable insights for stakeholders.

### Conclusion:
This analysis demonstrated the importance of thorough data cleaning and thoughtful feature selection in deriving meaningful insights from complex datasets. The findings can inform strategies for improving customer experience and product offerings.