# Streamlit Telecommunication User Analysis Dashboard

This dashboard is designed to analyze telecommunication user data and provide insights into user behavior, engagement, experience, and satisfaction. It uses PostgreSQL as the data source and Streamlit for the user interface.

## Prerequisites

### 1. Install Python
Make sure you have Python 3.8 or above installed on your system. You can download Python from [python.org](https://www.python.org/).

### 2. Install Required Libraries
Run the following command to install the necessary Python libraries:

```bash
pip install psycopg2 pandas streamlit seaborn matplotlib python-dotenv
```

### 3. Set Up PostgreSQL Database
Ensure that your PostgreSQL database is running and contains the necessary tables (`xdr_data` and `user_scores`). Update the environment variables or `.env` file with your database credentials:

- `DB_HOST`: Hostname of your database
- `DB_PORT`: Port number (default is `5432`)
- `DB_NAME`: Name of your database
- `DB_USER`: Database username
- `DB_PASSWORD`: Database password

### 4. Create a `.env` File
Create a `.env` file in the root directory of the project and add the database credentials in the following format:

```env
DB_HOST=your_database_host
DB_PORT=your_database_port
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
```

## How to Run the Dashboard

1. Clone the repository or download the project files.
2. Navigate to the project directory using a terminal or command prompt.
3. Run the Streamlit app with the following command:

```bash
streamlit run app/main.py
```

4. Open the URL displayed in the terminal (usually `http://localhost:8501`) in your web browser to access the dashboard.

## Dashboard Features

### User Overview Analysis
- Displays the top 3 handset manufacturers by user count.
- Visualizes the top 10 handset types by usage using a bar chart.

### User Engagement Analysis
- Displays user engagement data.
- Visualizes the top 10 customers by session frequency using a bar chart.

### Experience Analysis
- Displays user experience data.
- Visualizes the distribution of average throughput by the top 10 handset types using a box plot.

### Satisfaction Analysis
- Displays user satisfaction data.
- Visualizes satisfaction scores for the top 10 users using a bar chart.

## Troubleshooting

- **Error Connecting to the Database:**
  Ensure that the PostgreSQL database is running, and the credentials in the `.env` file are correct.

- **Missing Python Libraries:**
  Ensure all required libraries are installed by running:

  ```bash
  pip install -r requirements.txt
  ```

  If `requirements.txt` is missing, manually install the libraries listed in the prerequisites.

- **No Data Found:**
  Ensure the required tables (`xdr_data` and `user_scores`) exist in the database and contain data.

## Customization

To modify the SQL queries used in the dashboard, edit the query functions in the `app.py` file, such as:

```python
def get_user_overview_data():
    query = "SELECT * FROM xdr_data"
    return fetch_data_from_db(query)
```

Replace the SQL query as per your database schema and analysis requirements.


