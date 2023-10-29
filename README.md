Copy code
# YouTube Data Collection and Analysis

## Overview
This project is written in Python and is designed to collect data from YouTube channels using their unique channel IDs. The gathered data is then stored in both SQL and MongoDB databases, enabling further analysis. The results of this analysis can be visualized through a Streamlit application.

## Process

### 1. Google Cloud Setup
To begin with, you will need to set up a **Google Cloud account**. This includes enabling the necessary extensions and generating API credentials. You can access the Google Cloud Console through the following link: [Google Cloud Console](https://console.cloud.google.com/apis/dashboard?project=skilled-text-400719).

### 2. YouTube Data Extraction
Utilize the generated **API key** to extract data from YouTube channels. For detailed information on how to use the functions to retrieve YouTube data, refer to the official documentation: [YouTube Data API Documentation](https://developers.google.com/youtube/v3/docs).

### 3. Data Storage

#### Structured Data (SQL)
The structured data is stored in a **SQL database**, providing a tabular and relational format for the collected information. This format is particularly suitable for data that adheres to a well-defined schema.

#### Unstructured Data (MongoDB)
Unstructured data, which may not conform to a fixed schema, is stored in **MongoDB Atlas**. MongoDB is a NoSQL database that accommodates flexible and dynamic data structures, making it a suitable choice for diverse or evolving data.

### 4. Data Analysis and Visualization
Access the stored data to uncover valuable insights from the YouTube channel. Visualize the data for user-friendly presentation, often using plotting techniques.

### 5. Streamlit Application
To interact with and visualize the collected data, run the **Streamlit application**.Please make sure you have the necessary requirements installed, including Python, Streamlit, SQLAlchemy, MongoDB, SQL databases, MySQL, googleapiclient, and Plotly. These dependencies are crucial for the proper functioning of the project.

Follow these steps:
1. Download the source files provided for download.
2. After downloading, navigate to the project directory in your terminal.
3. Run the following command to start the application:

```bash
streamlit run  Home.py 






