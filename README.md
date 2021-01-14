# KPMG-Virual-Internship
This repository consists of 3 tasks from the virtual internship. 
All datasets are properties of Forage pte ltd and they reserve the final rights.

## 1.Data Quality Assessment

In this task, I act as a junior data analyst in KPMG's Lighthouse and Innvation Team. I have coordinated with Sprocket Central Pty Ltd , a medium size bikes & cycling accessories organisation. Sprocket Central Pty Ltd requires help for its customer and transactions data.The organisation has a large dataset relating to its customers, but their team is unsure how to effectively analyse it to help optimise its marketing strategy. 

In the spreadsheet provided, there are 3 datasets:
 * Customer Demographic 
 * Customer Addresses
 * Transactions data in the past 3 months
 
Upon viewing the spreadsheet, I did some prelimary data exploration and conducted some data cleaning.

    i. For Customer Demographics, I removed missing, mislabelled, the column "default" and unmatcheed datasets.
    
   
   ![mislabeled categories](https://github.com/JiaJun98/KPMG-Virual-Internship/tree/main/Task1/Task 1 Pic 1.PNG)
   
    ii. For Transactions, I also removed missing, mislabelled and data in the column "product_id" as the value of "0" is mislabelled. I have converted all incorrect data types from datetime to strings
    
    iii. For NewCustomerList, I also removed missing, mislabeled, duplicated data. Afterwards, I replaced empty headers with "unknown headers 1-5" as no data provided      for the column header. I then converted all incorrect data types from datetime to strings. 



 
    

## 2. Data Insights 

After cleaning and assessing the quality of the data, I developed a predictive model using “TensorFlow” and “Keras” to predict high-value customers from relationships established between customer demographics and transactions via feature engineering

## 3.Data Insights and Presentations

In the last task, after performing customer profiling in the dataset, I built an interactive Tableau dashboard highlighting key trends in datasets on customer preferences and propensity to the client and propose growth strategies to improve customer targeting
