# Global Value Chain - World Input Output Data (WIOD) Data Analysis
<h3> This repository 
contains Trade-in Value Added (TiVA) data among countries as mentioned in the 
2016 release of World Input Output Tables of World Input Output DataBase (WIOD) 
created under European Commission for the years (2000,...,2014)
<br><br>
The data is currently managed by University of Groningen's  
Groningen Growth and Development Centre under Faculty of Economics and Business.
</h3>
<br>
I have used the data for my major project in my Masters of Business Economics in 
Finance and Analytics with the title "India's Global Value Chain Participation in Automotive, 
Pharmaceutical and Textiles industries" with due references and courteous mentions to all those sources of 
information which helped me in my research.
<br>

<h3> Tools Used : </h3>
1. Programming Language : <b>Python</b>:- Pandas, Matplotlib <br>
2. Version Control : Git: GitHub
<br>
<hr>
<h3> Aim  -> Facelift the existing work in form of a web application to make it user-friendly especially for economists. </h3>

Build a web-application (website in layman terms) that automates the process of creating analysis. 
Users will be able to import the data fromthe excel/csv files of databases such as OECD and WIOD 
for Trade-in Value Added data and get analysis report accordingly.

There will be Two Services:-
<h4> 
1. Data
2. Cleaner
3. Analysis
</h4>


<b> Data Serivce </b> : This service will be responsible for collecting the flattened data in the database. <br><br>
<b> Cleaner Serivce </b> : This service will be responsible for cleaning the data and storing the data 
in the database. <br><br>
<b> Analysis Application </b> : This service will be responsible for preprocessing the data for analysis and running
machine learning models
<br>

<br> <br>
##################################### <br>
<h3> Sprint 1:- </h3> <br>
####################################<br>

1. Configure Swagger and create api endpoints &emsp;&emsp; <br>
2. Create schema for data reader service. <br>
3. Create bare bones for data analysis service.<br>
4. Create schema for data cleaning service.<br>
5. Create methods to clean the dataset using pandas. <br>
6. Create schema for data analysis service.<br>
7. Create FE for Data service. <br>

<br> <br>
##################################### <br>
<h3> Sprint 2:- </h3> <br>
####################################<br>

8. Create token based access <br>
9. Configure and use asyncio in data cleaning service to obtain cleaned data asynchronously. <br>
10. Create front end for customer application (service) <br>
