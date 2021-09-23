# Data Engineering: Data warehouse tech stack with MySQL, DBT, Airflow, and Spark
## Overview
An AI startup deploys sensors to businesses, collects data from all activities in a business - from people’s
interaction to the smart appliances installed in the company to reading environmental and other relevant
information. Our startup is responsible to install all the required sensors, receive a stream of data from all
sensors, and analyze the data to provide key insights to the business. The objective of our contract with
the client is to reduce the cost of running the client facility as well as to increase the livability and
productivity of workers.
In this challenge we are tasked to create a scalable data warehouse tech-stack that will help us provide the
AI service to the client. By the end of this project, we aim to produce a tool that can be used as a basis for
the data warehouse needs of the startup.

## Requirements
This project requires the installation of ```Apache Airflow``` and ```dbt```. 
To install dependencies, type the following command
```
pip install -r requirements.txt
```

## Code
The ```pems_sorted``` folder contains the data, a large number of **.parquet** files. The ```data-engineering-dbt``` folder contains our **dbt project**. The ```airflow``` folder contains our **airflow dags**. The ```scripts``` folder contains python scripts that inserts all the data into a sql database.

