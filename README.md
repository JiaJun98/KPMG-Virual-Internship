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

i. For Customer Demographics, I removed missing, mislabelled, the column "default" and unmatched datasets.
   
   ![Customer Demographics](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%201/Task1_Pic1.PNG)
   
ii. For Transactions, I also removed missing, mislabelled and data in the column "product_id" as the value of "0" is mislabelled. I have converted all incorrect data types from datetime to strings
    
   ![Transactions](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%201/Task1_Pic2.PNG)
    
iii. For NewCustomerList, I also removed missing, mislabeled, duplicated data. Afterwards, I replaced empty headers with "unknown headers 1-5" as no data provided      for the column header. I then converted all incorrect data types from datetime to strings. 

   ![NewCustomerList](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%201/Task1_Pic3.PNG)

 
   
## 2. Data Insights 

In this task, Sprocket Central Pty Ltd has given us a new list of 1000 potential customers with their demographics and attributes but with no prior transaction history with the organisation. The marketing team believes that the data would reveal useful customer insights which could help optimise resource allocation for targeted marketing. Hence, improve performance by focusing on high value customers.

Gathering the insights is divided into 3 steps,

   ### i. Feature Engineering
I used the library "featuretools" to generate parent-child relationships for the column "customer id" in "CustomerDemographic" spreadsheet as the "parent" and the column "customer id" in "Transactions" spreadsheet as the "child".
       
Using "featuretools" library, I was able to see the types of feature; aggregation and transformative primitives
       
    Aggrevate Primitives
  ![Aggrevate Primitives](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/aggregate_primitive.PNG)
 
    Transformative Primitives
  ![Transformative Primitives](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/transformative_primitive.PNG)
   
       
Afterwards I used the features "mean", "max", "min", "std", "skew","count","n_most_common" as the aggregation primitives and "time_since_previous" as the transformative primitives and form the following dataframe.
  
  #### Screenshots of uncleaned dataframe after feature engineering
   * First 6 rows of the dataframe  
   ![Feature Engineering 1](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Ft_final(1).PNG)
   ![Feature Engineering 2](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Ft_final(2).PNG)
   ![Feature Engineering 3](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Ft_final(3).PNG)
   ![Feature Engineering 4](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Ft_final(4).PNG)
  
  
  After forming the dataframe using feature engineering, I cleaned it by:

  1) Remove all N_MOST_COMMON[1] & N_MOST_COMMON[1]

  2) For Column Mean and above

   * Numeric column- Fill in 0
   * Caterorical- Fill in "U"
   
   #### Screenshots of cleaned  dataframe after feature engineering
   *First 6 rows of the edited dataframe
   ![Feature Engineering Final 1](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Ft_edited(1).PNG)
   ![Feature Engineering Final 2](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Ft_edited(2).PNG)
   ![Feature Engineering Final 3](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Ft_edited(3).PNG)
   ![Feature Engineering Final 4](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Ft_edited(4).PNG)
  
   ### ii. Model building and Interpretation
   
   Using "Tensorflow" and "Keras" library, I used the dataframe from the feature engineering previously generated as the training set.
   The test set given by the client, shown in the below screenshot, will act as the test set.
   
   #### First 7 rows of dataframe of Test Set 
   ![Test Set](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Test_set.PNG)

   Afterwards, I created a Sequential Model with: 
   * 2 densely connected hidden layers (nn size =64)
   * Activation 'relu'
   * input_shape = [4] due to 4 numeric columns 
      * "past_3_years_bike_related_purchases"
      * "Age"
      * "tenure"
      * "property_valuation"
      
 ![Sequential Model](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Sequential_Model.PNG)
 
   #### Splitting features from labels
   I seperated the target value or "label" from the features. This label is the value that you will train the model to predict.
   
   In the screenshot below, I have used the training column "MEAN_Transactions_standard_cost" for the prediction of the Sequential Model
   
   ![MEAN_Transaction_standard_cost](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Split_features.PNG)
   
   ### Training
   I proceeded to use EPOCH = 1000 to train the model.
   
   ### Documentation of training
   Using tensorflow, I used the plotter to show the mean absolute error (MAE) vs the number of epochs
   
   ![MAE_MEAN_Transaction_standard_cost](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/MAE_EPOCH(2).PNG)
  
   I then used the plotter to show the mean square error (MSE) vs the number of epochs
   ![MSE_MEAN_Transaction_standard_cost](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/MSE_EPOCH.PNG)
  
   #### Early Stopping
   I experimented with "keras" early stopping to see if there are any improvements in the predictions.
   ![MEAN_Transaction_standard_cost](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Early_Stopping(1).PNG)
   ![MEAN_Transaction_standard_cost](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Early_Stopping(2).PNG)
   ![MEAN_Transaction_standard_cost](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Early_Stopping(3).PNG)
   
   ### iii. Predictions
   
   After repeating the process of training and testing for the rest of the columns. I have obtained the following dataframe
   ![Test](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Test(1).PNG)
   ![Test](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Test(2).PNG)
   ![Test](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Test(3).PNG)
   
   #### iv. Groupby
   
   I gathered all unique values and seperate them by interval ranges using groupby dataframe.This is an example for the column "past_3_years_bike_related_purchase
   ![Groupby](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Group_by.PNG)
   
   I then groupy each of the predicted columns based on their "sum" and "mean" and obtained this final dataframe as shown
   ![Final_Groupby](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Final(1).PNG)
   ![Final_Groupby](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Final(2).PNG)
   
Finally, I repeated the process for the different customer demographics for the columns "Gender_aggregate", "job_industry_category_aggregate", "wealth_segment_aggregate", "state_aggregate", "3_years_bike_purchases_agg", "Age_agg", "tenure_agg", "property_valuation_agg" and exported the dataframes as excel sheet

This is a screenshot of the column "Gender_aggregate"
![Final_Groupby](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%202/Final_excel_submission.PNG)


## 3.Data Insights and Presentations

In the last task, after performing customer profiling in the dataset, I built an interactive Tableau dashboard highlighting key trends in datasets on customer preferences and propensity to the client and propose growth strategies to improve customer targeting.

I have formed 3 dashboards, mainly "Social Dashboard", "Economic Dashboard" and "Australia Dashboard"

The social dashboard plots a faceted graph of the columns "Category by Age", "Category by Gender" and "Category by Industry Category" 
![Social Dashboard](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%203/Social_Dashboard.PNG)

The economic dashboard plots a faceted graph of the columns "past_3_years_bike_related_purchases" , "wealth_segment", "tenure", "property_valuation".
![Economic Dashboard](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%203/Economic_Dashboard.PNG)

The last dashboard shows the numerical value of each of the columns "MEAN_Transactions_standard_cost", "MEAN_Transactions_list_price",	"MAX_Transactions_standard_cost", "MAX_Transactions_list_price",	"MIN_Transactions_standard_cost","MIN_Transactions_list_price",	"STD_Transactions_standard_cost",	"STD_Transactions_list_price",	"SKEW_Transactions_standard_cost"	,"SKEW_Transactions_list_price",	"COUNT_Transactions" in the 3 regions of Australia

![Australia Dashboard](https://github.com/JiaJun98/KPMG-Virual-Internship/blob/main/Task%203/Australia_Dashboard.PNG)
