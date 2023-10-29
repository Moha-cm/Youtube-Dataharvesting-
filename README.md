Copy code
# YouTube Data Collection and Analysis

## Overview
This project is written in Python and aims to collect data from YouTube channels using their channel IDs. The collected data is then stored in both SQL and MongoDB databases for further analysis, which can be visualized through a Streamlit application.

## Process

### 1. Google Cloud Setup
To get started, create a Google Cloud account, enable the necessary extensions, and generate API credentials.

### 2. YouTube Data Extraction
Utilize the generated API key to extract data from YouTube channels.

### 3. Data Storage

#### Structured Data (SQL)
The structured data is stored in a SQL database, providing a tabular and relational format for the collected information. This format is particularly suitable for data that adheres to a well-defined schema.

#### Unstructured Data (MongoDB)
Unstructured data, which may not conform to a fixed schema, is stored in MongoDB Atlas. MongoDB is a NoSQL database that accommodates flexible and dynamic data structures, making it a suitable choice for diverse or evolving data.

### 4. Data Analysis and Visualization
Access the stored data to uncover valuable insights from the YouTube channel. Visualize the data for user-friendly presentation, often using plotting techniques.

### 5. Streamlit Application
Run the Streamlit application to interact with and visualize the collected data. Use the following command to start the application:

```bash
streamlit run your_app_file.py
