# Telecom User Analysis

## Overview
This project involves an in-depth analysis of a telecom dataset to gain insights into customer behavior, engagement, and satisfaction. By leveraging Exploratory Data Analysis (EDA), clustering techniques, and predictive modeling, the project aims to:

1. Understand user behavior and device usage.
2. Evaluate user engagement and quality of service.
3. Assess user satisfaction based on engagement and experience metrics.
4. Provide actionable insights for marketing and technical teams.

---

## Task Breakdown

### Task 1 - User Overview Analysis

**Objective:** Conduct an exploratory analysis of user behavior and device preferences.

1. **Device Analysis:**
   - Identify the top 10 handsets used by customers.
   - Identify the top 3 handset manufacturers.
   - List the top 5 handsets per top 3 handset manufacturers.
   - Provide recommendations for the marketing team based on the findings.

2. **xDR Application Analysis:**
   - Aggregate per user:
     - Number of xDR sessions.
     - Total session duration.
     - Total download (DL) and upload (UL) data.
     - Total data volume per application.

3. **EDA:**
   - Treat missing values and outliers.
   - Analyze variables and their data types.
   - Segment users into decile classes based on session duration and compute total data volume per decile.
   - Perform univariate and bivariate analysis.
   - Conduct correlation analysis on application data.
   - Perform dimensionality reduction using PCA and interpret results.

---

### Task 2 - User Engagement Analysis

**Objective:** Evaluate customer engagement across applications and identify key patterns.

1. **Engagement Metrics:**
   - Aggregate session frequency, duration, and total traffic (DL + UL) per user.
   - Report the top 10 users for each metric.

2. **Clustering:**
   - Normalize engagement metrics.
   - Perform k-means clustering (k=3).
   - Compute and visualize metrics (min, max, average, total) for each cluster.

3. **Application Analysis:**
   - Aggregate user traffic per application.
   - Identify the top 10 users per application.
   - Visualize the top 3 most used applications.

4. **Optimized Clustering:**
   - Use the elbow method to determine the optimal value of k for engagement clusters.

---

### Task 3 - Experience Analytics

**Objective:** Assess user experience based on network parameters and device characteristics.

1. **Network Parameters:**
   - Aggregate per customer:
     - Average TCP retransmission.
     - Average RTT.
     - Handset type.
     - Average throughput.

2. **Value Analysis:**
   - Compute the top, bottom, and most frequent values for TCP, RTT, and throughput.

3. **Distribution Analysis:**
   - Analyze the distribution of average throughput and TCP retransmission per handset type.

4. **Experience Clustering:**
   - Perform k-means clustering (k=3) to segment users based on experience metrics.
   - Provide a description of each cluster.

---

### Task 4 - Satisfaction Analysis

**Objective:** Analyze and predict customer satisfaction based on engagement and experience metrics.

1. **Score Assignment:**
   - Compute engagement score (Euclidean distance to the least engaged cluster).
   - Compute experience score (Euclidean distance to the worst experience cluster).

2. **Satisfaction Score:**
   - Calculate the average of engagement and experience scores as the satisfaction score.
   - Report the top 10 satisfied customers.

3. **Predictive Modeling:**
   - Build a regression model to predict satisfaction scores.

4. **Clustering:**
   - Perform k-means clustering (k=3) on engagement and experience scores.

   - Aggregate average satisfaction and experience scores per cluster.

5. **Export Results:**
   - Save the final table (user ID, engagement, experience, satisfaction scores) to a Postgres database.
   - Provide a screenshot of the exported data.

---

## Deliverables

1. **Python Scripts:**
   - Scripts for all tasks, including EDA, clustering, and predictive modeling.

2. **Visualizations:**
   - Graphs for univariate and bivariate analysis.
   - Cluster visualizations.
   - Application usage plots.

3. **Reports:**
   - Insights from analysis and clustering.
   - Recommendations for marketing and technical teams.

4. **Database Export:**
   - Postgres table with user scores and satisfaction metrics.

5. **Slide Presentation:**
   - Summary of findings and actionable insights.

---

## Technologies Used

- **Programming Language:** Python
- **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn, mlflow, sqlalchemy
- **Database:** Postgres
- **Clustering Algorithm:** k-means
- **Dimensionality Reduction:** PCA

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Semir1r/Telecom-Analysis.git
   cd telecom-analysis
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure MySQL database credentials in `config.py`.

---

## Usage

1. Run the Python scripts for each task:
   ```bash
   python main.py
   python task1.py
   python finaltask.py
   ```

2. Generate visualizations and export results as needed.

---

## Recommendations

1. Marketing teams should focus on popular handset models and manufacturers.
2. Optimize network resources for applications with high user engagement.
3. Monitor user experience clusters for targeted QoS improvements.

---

## Authors

Developed by Semir.
