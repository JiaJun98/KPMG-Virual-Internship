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
   
   ![Customer Demographics](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%201/Task1_Pic1.PNG)
   
   ii. For Transactions, I also removed missing, mislabelled and data in the column "product_id" as the value of "0" is mislabelled. I have converted all incorrect data types from datetime to strings
    
   ![Transactions](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%201/Task1_Pic2.PNG)
    
   iii. For NewCustomerList, I also removed missing, mislabeled, duplicated data. Afterwards, I replaced empty headers with "unknown headers 1-5" as no data provided      for the column header. I then converted all incorrect data types from datetime to strings. 

   ![NewCustomerList](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%201/Task1_Pic3.PNG)

 
   
## 2. Data Insights 

In this task, Sprocket Central Pty Ltd has given us a new list of 1000 potential customers with their demographics and attributes but with no prior transaction history with the organisation. The marketing team believes that the data would reveal useful customer insights which could help optimise resource allocation for targeted marketing. Hence, improve performance by focusing on high value customers.

Gathering the insights is divided into 3 steps,

    i. Feature Engineering
-I used the library "featuretools" to generate parent-child relationships for the column "customer id" in "CustomerDemographic" spreadsheet as the "parent" and the column "customer id" in "Transactions" spreadsheet as the "child".
       
 -Using "featuretools" library, I was able to see the types of feature-aggregation and transformative primitives
       
    Aggrevate Primitives
  ![Aggrevate Primitives](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/aggregate_primitive.PNG)
 
    Transformative Primitives
  ![Transformative Primitives](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/transformative_primitive.PNG)
   
       
 -I then used the features "mean", "max", "min", "std", "skew","count","n_most_common" as the aggregation primitives and "time_since_previous" as the transformative primitives.

     



## 3.Data Insights and Presentations

In the last task, after performing customer profiling in the dataset, I built an interactive Tableau dashboard highlighting key trends in datasets on customer preferences and propensity to the client and propose growth strategies to improve customer targeting
