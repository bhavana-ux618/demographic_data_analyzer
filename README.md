# Demographic Data Analyzer

A Python data analysis project that uses Pandas to explore and analyze demographic information from the 1994 U.S. Census database. This project was completed as part of the freeCodeCamp Data Analysis with Python Certification.

## Project Overview

The goal of this project is to analyze census data and answer key demographic questions using Pandas. The dataset contains information about age, education, occupation, race, sex, working hours, native country, and income levels.

## Features

The program analyzes the dataset and provides answers to the following questions:

* Number of people belonging to each race
* Average age of men
* Percentage of people with a Bachelor's degree
* Percentage of people with advanced education earning more than $50K
* Percentage of people without advanced education earning more than $50K
* Minimum number of work hours per week
* Percentage of people working minimum hours who earn more than $50K
* Country with the highest percentage of high-income earners
* Most popular occupation among high-income earners in India

## Technologies Used

* Python
* Pandas
* Jupyter Notebook / Google Colab

## Dataset

The project uses the Adult Census Income Dataset from the UCI Machine Learning Repository.

Dataset Attributes Include:

* Age
* Workclass
* Education
* Occupation
* Race
* Sex
* Hours per Week
* Native Country
* Income

## Project Structure

```text
demographic-data-analyzer/
│
├── demographic_data_analyzer.py
├── main.py
├── test_module.py
├── adult.data.csv
└── README.md
```

## Example Output

```python
{
    'race_count': race_count,
    'average_age_men': average_age_men,
    'percentage_bachelors': percentage_bachelors,
    'higher_education_rich': higher_education_rich,
    'lower_education_rich': lower_education_rich,
    'min_work_hours': min_work_hours,
    'rich_percentage': rich_percentage,
    'highest_earning_country': highest_earning_country,
    'highest_earning_country_percentage': highest_earning_country_percentage,
    'top_IN_occupation': top_IN_occupation
}
```

## Key Pandas Concepts Applied

* Data Loading with `read_csv()`
* Data Filtering
* Boolean Indexing
* Aggregation Functions (`mean`, `min`, `value_counts`)
* GroupBy Operations
* Percentage Calculations
* Data Exploration and Analysis

## Learning Outcomes

Through this project, I gained hands-on experience with:

* Data analysis using Pandas
* Real-world dataset exploration
* Data filtering and transformation
* GroupBy operations
* Statistical analysis
* Writing clean and maintainable Python code

## Certification Project

This project is part of the freeCodeCamp Data Analysis with Python Certification.

## Author

**Bhavana Ramaswaram**

GitHub: https://github.com/bhavana-ux618

LinkedIn: https://www.linkedin.com/in/ramaswaram-bhavana/
