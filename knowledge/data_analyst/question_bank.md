# Data Analyst Interview Questions (Medium Level)

## 1. What are the main steps in the data analysis process?

**Answer:**
The data analysis process generally consists of:
- Defining the business problem
- Collecting data
- Cleaning and preprocessing data
- Performing Exploratory Data Analysis (EDA)
- Building insights using statistical techniques
- Visualizing the results
- Communicating findings and recommendations to stakeholders

---

## 2. What is Exploratory Data Analysis (EDA)?

**Answer:**
EDA is the process of understanding a dataset before modeling by identifying patterns, trends, anomalies, and relationships using summary statistics and visualizations.

Common techniques include:
- Histograms
- Box plots
- Correlation heatmaps
- Scatter plots

---

## 3. What is the difference between data cleaning and data preprocessing?

**Answer:**

Data Cleaning:
- Removes incorrect or inconsistent data.
- Handles duplicates and missing values.

Data Preprocessing:
- Converts data into a format suitable for analysis.
- Includes encoding, scaling, normalization, and feature engineering.

---

## 4. How do you handle missing values in a dataset?

**Answer:**

Common methods include:
- Removing rows or columns
- Filling with mean, median, or mode
- Forward fill or backward fill
- Predicting missing values using machine learning

The choice depends on the amount and importance of missing data.

---

## 5. What is the difference between INNER JOIN and LEFT JOIN?

**Answer:**

INNER JOIN:
Returns only matching records from both tables.

LEFT JOIN:
Returns all rows from the left table and matching rows from the right table. Non-matching rows contain NULL values.

---

## 6. What is the purpose of GROUP BY in SQL?

**Answer:**
GROUP BY groups rows having the same values into summary rows.

Example:
Calculating total sales for each region.

Often used with aggregate functions like:
- COUNT()
- SUM()
- AVG()
- MAX()
- MIN()

---

## 7. What is the difference between WHERE and HAVING?

**Answer:**

WHERE:
Filters individual rows before grouping.

HAVING:
Filters grouped data after GROUP BY.

---

## 8. What are window functions in SQL?

**Answer:**
Window functions perform calculations across related rows without collapsing them.

Examples:
- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- LEAD()
- LAG()

---

## 9. What is normalization in databases?

**Answer:**
Normalization organizes data to reduce redundancy and improve consistency.

Common normal forms:
- First Normal Form (1NF)
- Second Normal Form (2NF)
- Third Normal Form (3NF)

---

## 10. Why are indexes used in databases?

**Answer:**
Indexes improve query performance by allowing faster data retrieval.

Advantages:
- Faster SELECT queries

Disadvantages:
- Additional storage
- Slower INSERT, UPDATE, and DELETE operations

---

## 11. Explain the difference between NumPy and Pandas.

**Answer:**

NumPy:
- Efficient numerical computations
- Uses arrays

Pandas:
- Built on NumPy
- Provides DataFrames
- Better for tabular data analysis

---

## 12. What is a Pandas DataFrame?

**Answer:**
A DataFrame is a two-dimensional labeled data structure consisting of rows and columns.

It supports:
- Filtering
- Sorting
- Aggregation
- Merging
- Grouping

---

## 13. How do you remove duplicate records in Pandas?

**Answer:**

Use:

```python
df.drop_duplicates()
```

This removes duplicate rows while keeping the first occurrence by default.

---

## 14. What is data visualization and why is it important?

**Answer:**
Data visualization represents data graphically to identify patterns, trends, and outliers quickly.

Popular libraries:
- Matplotlib
- Seaborn
- Plotly

---

## 15. When would you use a bar chart instead of a line chart?

**Answer:**

Bar Chart:
Compares values across categories.

Line Chart:
Shows trends over time.

---

## 16. What is the difference between mean and median?

**Answer:**

Mean:
Average of all values.

Median:
Middle value after sorting.

Median is preferred when the dataset contains outliers.

---

## 17. What is standard deviation?

**Answer:**
Standard deviation measures how spread out the values are from the mean.

Low standard deviation:
Values are close to the mean.

High standard deviation:
Values vary widely.

---

## 18. What is hypothesis testing?

**Answer:**
Hypothesis testing determines whether there is enough statistical evidence to support a claim.

It involves:
- Null hypothesis (H₀)
- Alternative hypothesis (H₁)
- p-value
- Significance level

---

## 19. What is an A/B test?

**Answer:**
A/B testing compares two versions of a product or feature to determine which performs better based on user behavior.

Common metrics:
- Click-through rate
- Conversion rate
- Revenue

---

## 20. What are KPIs?

**Answer:**
Key Performance Indicators (KPIs) are measurable values used to evaluate business performance.

Examples:
- Revenue
- Customer Retention
- Sales Growth
- Conversion Rate

---

## 21. What is the difference between Power BI and Tableau?

**Answer:**

Power BI:
- Better integration with Microsoft products
- Cost-effective

Tableau:
- Strong visualization capabilities
- Preferred for complex dashboards

---

## 22. What is a dashboard?

**Answer:**
A dashboard is a visual interface displaying important business metrics using charts, tables, and KPIs.

It helps stakeholders monitor business performance.

---

## 23. What is data storytelling?

**Answer:**
Data storytelling combines data, visualizations, and business context to communicate insights effectively and support decision-making.

---

## 24. How would you analyze a sudden drop in sales?

**Answer:**

Steps:
- Verify data accuracy
- Compare historical trends
- Segment data by product, region, and customer
- Identify seasonal effects
- Investigate external factors
- Present findings with visualizations

---

## 25. Which SQL functions do Data Analysts use most frequently?

**Answer:**

Common aggregate functions:
- COUNT()
- SUM()
- AVG()
- MAX()
- MIN()

Common string functions:
- CONCAT()
- LENGTH()
- UPPER()
- LOWER()

Common date functions:
- NOW()
- DATE()
- YEAR()
# Data Analyst Interview Questions (Hard & Advanced Level)

## 1. Explain the difference between ROW_NUMBER(), RANK(), and DENSE_RANK().

**Answer:**

These are SQL window functions used for ranking records.

- **ROW_NUMBER()** assigns a unique sequential number to each row.
- **RANK()** assigns the same rank to ties but skips the next rank.
- **DENSE_RANK()** assigns the same rank to ties without skipping ranks.

Example:

Scores: 95, 90, 90, 80

- ROW_NUMBER(): 1,2,3,4
- RANK(): 1,2,2,4
- DENSE_RANK(): 1,2,2,3

---

## 2. Explain Common Table Expressions (CTEs). When would you use them?

**Answer:**

A CTE is a temporary named result set created using the `WITH` clause.

Advantages:
- Improves readability
- Simplifies complex SQL queries
- Supports recursive queries
- Easier debugging

Example:

```sql
WITH SalesCTE AS (
    SELECT region, SUM(sales) AS total_sales
    FROM Orders
    GROUP BY region
)
SELECT *
FROM SalesCTE;
```

---

## 3. How would you optimize a slow SQL query?

**Answer:**

Common optimization techniques:

- Add indexes
- Avoid SELECT *
- Use WHERE filters
- Optimize JOINs
- Analyze execution plans
- Partition large tables
- Remove unnecessary subqueries
- Use LIMIT when appropriate

---

## 4. What is query execution planning?

**Answer:**

The query optimizer determines the most efficient way to execute a SQL query.

Execution plans reveal:
- Index usage
- Table scans
- Join algorithms
- Estimated execution cost

They help identify performance bottlenecks.

---

## 5. Explain clustered and non-clustered indexes.

**Answer:**

**Clustered Index**
- Physically sorts table data
- Only one clustered index per table

**Non-Clustered Index**
- Separate structure pointing to data
- Multiple allowed per table

---

## 6. Explain ACID properties.

**Answer:**

ACID ensures reliable database transactions.

- Atomicity
- Consistency
- Isolation
- Durability

These properties maintain database integrity even during failures.

---

## 7. What are window functions? Give real-world applications.

**Answer:**

Window functions perform calculations across related rows while preserving individual records.

Examples:
- Running totals
- Employee ranking
- Monthly sales trends
- Year-over-year comparisons
- Moving averages

---

## 8. Difference between OLTP and OLAP.

**Answer:**

OLTP
- Handles transactional operations
- Frequent INSERT/UPDATE
- Normalized schema

OLAP
- Handles analytical queries
- Large aggregations
- Denormalized schema
- Optimized for reporting

---

## 9. What is a star schema?

**Answer:**

A star schema consists of:

- One Fact Table
- Multiple Dimension Tables

Advantages:
- Faster analytical queries
- Easy reporting
- Widely used in data warehouses

---

## 10. What is data warehousing?

**Answer:**

A data warehouse is a centralized repository that integrates data from multiple sources for reporting and business intelligence.

Examples:
- Snowflake
- Amazon Redshift
- Google BigQuery
- Azure Synapse

---

## 11. Explain ETL.

**Answer:**

ETL stands for:

Extract
Transform
Load

Process:
1. Extract data from sources
2. Clean and transform it
3. Load into a data warehouse

---

## 12. Difference between ETL and ELT.

**Answer:**

ETL
- Transform before loading

ELT
- Load first
- Transform inside the data warehouse

ELT is preferred for cloud data platforms.

---

## 13. What are outliers? How would you detect them?

**Answer:**

Outliers are observations significantly different from the rest.

Detection methods:
- Box Plot
- IQR Method
- Z-score
- Isolation Forest
- DBSCAN

---

## 14. Explain the Central Limit Theorem.

**Answer:**

The Central Limit Theorem states that the sampling distribution of the sample mean approaches a normal distribution as sample size increases, regardless of the original population distribution.

It is fundamental for hypothesis testing and confidence intervals.

---

## 15. What is multicollinearity?

**Answer:**

Multicollinearity occurs when predictor variables are highly correlated.

Problems:
- Unstable coefficients
- Difficult interpretation

Detection:
- Correlation Matrix
- Variance Inflation Factor (VIF)

---

## 16. Explain p-value in hypothesis testing.

**Answer:**

The p-value measures the probability of obtaining observed results assuming the null hypothesis is true.

Common rule:

- p < 0.05 → Reject null hypothesis
- p ≥ 0.05 → Fail to reject null hypothesis

---

## 17. What is Simpson's Paradox?

**Answer:**

Simpson's Paradox occurs when a trend appears in separate groups but disappears or reverses after combining the groups.

It highlights the importance of considering hidden variables before drawing conclusions.

---

## 18. How would you detect data leakage?

**Answer:**

Methods:

- Review feature creation
- Ensure future information isn't used
- Time-based train-test split
- Check suspiciously high accuracy
- Validate business logic

Data leakage leads to unrealistically high model performance.

---

## 19. Explain feature engineering.

**Answer:**

Feature engineering involves creating new variables from existing data to improve predictive performance.

Examples:
- Date decomposition
- Interaction features
- Target encoding
- Binning
- Log transformation

---

## 20. Explain dimensionality reduction.

**Answer:**

Dimensionality reduction decreases the number of input variables while preserving important information.

Techniques:
- PCA
- t-SNE
- UMAP

Benefits:
- Faster models
- Reduced overfitting
- Better visualization

---

## 21. How would you build an executive dashboard?

**Answer:**

Steps:

- Understand stakeholder goals
- Identify KPIs
- Design clear visualizations
- Add interactive filters
- Optimize performance
- Validate accuracy
- Publish and monitor usage

---

## 22. A company reports declining revenue. How would you investigate?

**Answer:**

Approach:

- Validate data quality
- Compare historical trends
- Segment by region, product, customer
- Analyze pricing changes
- Study customer churn
- Review marketing campaigns
- Present findings using dashboards

---

## 23. Explain data governance.

**Answer:**

Data governance ensures data quality, security, compliance, ownership, and consistency across an organization.

Components:
- Data quality
- Metadata
- Privacy
- Security
- Policies
- Stewardship

---

## 24. How would you validate a dashboard before publishing?

**Answer:**

Validation checklist:

- Verify KPIs
- Cross-check calculations
- Test filters
- Validate joins
- Check missing values
- Compare with source systems
- Test performance
- Obtain stakeholder approval

---

## 25. A stakeholder says your analysis is incorrect. What would you do?

**Answer:**

Professional approach:

- Listen carefully
- Review assumptions
- Validate the underlying data
- Reproduce calculations
- Discuss business context
- Correct genuine mistakes if found
- Explain methodology with supporting evidence
- Update the report transparently if necessary