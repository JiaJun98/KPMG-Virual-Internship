import pandas as pd
import numpy as np
import datetime

Sprocket_Central_Pty_Ltd_df=pd.ExcelFile('KPMG_VI_New_raw_data_update_final.xlsx')
#create a function that shows the data frame besides the first row of the sheet of the excel file
#read each excel spreadsheet and filter incomplete or missing data

def data_frame_creater(file,spreadsheet):
    df=pd.read_excel(file,spreadsheet)
    header=df.iloc[0]
    edited_df=df[1:]
    edited_df.rename(columns=header,inplace=True) #remeber to put "inplace=True" or else the header wont be change
    return edited_df

def data_frame_creater_with_column_renamer(file,spreadsheet,start,stop):
    df=pd.read_excel(file,spreadsheet)
    df_copy=df.copy()
    for header in range(start,stop+1):
        no=header-start+1
        df_copy.iloc[0,header]='unknown_header'+str(header-start+1)
    header=df_copy.iloc[0]
    edited_df=df_copy[1:]
    edited_df.rename(columns=header,inplace=True) #remember to put "inplace=True" or else the header wont be change
    return edited_df
#reader for each of the spreadsheets

def excel_writer(Name,df):
    writer=pd.ExcelWriter(str(Name)+'.xlsx',engine='xlsxwriter')
    for sheet_name in df.keys():
        df[sheet_name].to_excel(writer,sheet_name=sheet_name,index=False)
    writer.save()

#To save edited df into new excel spreadsheets (TO BE TESTED)
#Transactions_df_copy.to_excel (r'C:\Users\jiakj\Desktop\NUS\External Python and Co\KPMG Data Quality Assessment\export_dataframe.xlsx', index = False, header=True)
#pathway C:\Users\jiakj\Desktop\NUS\External Python and Co\KPMG Data Quality Assessment

    
'''
dfs={'Transactions_empty':Transactions_df_copy_NAN
     ,'Transactions_mislabelled':Transactions_df_mislabelled
     , 'CustomerDemographic_empty':CustomerDemographic_df_copy_NAN
     ,'CustomerDemographic_mislabelled': CustomerDemographic_df_gender_mislabelled
     ,'CustomerDemographic_wrong_data_type':CustomerDemographic_df_wrong_data_type
     ,'NewCustomerList_empty':NewCustomerList_df_copy_NAN
     ,'NewCustomerList_df_wrong_data_type':NewCustomerList_df_wrong_data_type}
'''
    
#TRANSACTIONS SPREADSHEET
#Transactions_df_copy_NAN
#Transactions_df_mislabelled
    
#CUSTOMERDEMOGRAPHIC SPREADSHEET
    
#CustomerDemographic_df_copy_NAN
#CustomerDemographic_df_gender_mislabelled
#CustomerDemographic_df_wrong_data_type
    
#NEWCUSTOMERLIST SPREADSHEET
    
#NewCustomerList_df_copy_NAN
#NewCustomerList_df_wrong_data_type




Transactions_df=data_frame_creater('KPMG_VI_New_raw_data_update_final.xlsx',"Transactions")
CustomerDemographic_df=data_frame_creater('KPMG_VI_New_raw_data_update_final.xlsx',"CustomerDemographic")
#NewCustomerList_df=data_frame_creater('KPMG_VI_New_raw_data_update_final.xlsx',"NewCustomerList")
CustomerAddress_df=data_frame_creater('KPMG_VI_New_raw_data_update_final.xlsx',"CustomerAddress")



#CUSTOMERDEMOGRAPHIC SPREADSHEET (MASTER LIST)

#Remove and count missing data
CustomerDemographic_df_copy=CustomerDemographic_df.copy()
CustomerDemographic_df_copy_NAN=CustomerDemographic_df_copy[CustomerDemographic_df_copy.isna().any(axis=1)]
CustomerDemographic_df_copy.dropna(axis=0,inplace=True)
#print(CustomerDemographic_df_copy.count())
#4000-2630=1370

#Remove and count mislabled data #Not supposed to remove if there are numerical but most are catergorical
#CustomerDemographic_df_gender_mislabelled=CustomerDemographic_df_copy[~((CustomerDemographic_df_copy['gender']=="Male")|(CustomerDemographic_df_copy['gender']=="Female"))]
#CustomerDemographic_df_copy['gender']=CustomerDemographic_df_copy['gender'].replace(["F","Femal"],"Female").apply(np.str)


#Commented as renamed the mislablled data
CustomerDemographic_df_gender_mislabelled=CustomerDemographic_df_copy[~((CustomerDemographic_df_copy['gender']=="Male")|(CustomerDemographic_df_copy['gender']=="Female"))]
CustomerDemographic_df_copy=CustomerDemographic_df_copy[(CustomerDemographic_df_copy['gender']=="Male")|(CustomerDemographic_df_copy['gender']=="Female")]
#2630-2628=2

#Remove and count wrong data type (CORRECTION)* should just remove column "default" casue the numbers seemed irrelevant
CustomerDemographic_df_wrong_data_type=CustomerDemographic_df_copy[~((CustomerDemographic_df_copy['default'].apply(isinstance,args=(int,)))|(CustomerDemographic_df_copy['default'].apply(isinstance,args=(float,))))]
CustomerDemographic_df_copy=CustomerDemographic_df_copy[(CustomerDemographic_df_copy['default'].apply(isinstance,args=(int,)))|(CustomerDemographic_df_copy['default'].apply(isinstance,args=(float,)))]

#2628-380=2248

#CustomerDemographic_df_copy.drop(axis=1, labels=['default'], inplace=True)


#Remove data based on data types for within Series
#s[s.apply(isinstance, args=(str,))]
#s[s.apply(lambda x: isinstance(x, str))]

CustomerDemographic_df_copy=CustomerDemographic_df_copy.drop_duplicates(keep=False)
datetime_converter_customer_demographic=CustomerDemographic_df_copy["DOB"].apply(lambda x: x.strftime('%Y-%m-%d'))
CustomerDemographic_df_copy["DOB"]=datetime_converter_customer_demographic

#Remainder 380

#To be exported







#TRANSACTIONS SPREADSHEET

#Remove and count missing data

Transactions_df_copy=Transactions_df.copy()
Transactions_df_copy_NAN=Transactions_df_copy[Transactions_df_copy.isna().any(axis=1)]
Transactions_df_copy.dropna(axis=0,inplace=True)

#20,000-19,445=555

#Remove and count mislabled data
Transactions_df_mislabelled=Transactions_df_copy[Transactions_df_copy['product_id']==0]
Transactions_df_copy=Transactions_df_copy[~(Transactions_df_copy['product_id']==0)]

#19445-18288=1157
#Removed 1157 rows of data showing "0" for "product_id" column as the value of "0" seem to be mislabelled

Transactions_df_copy=Transactions_df_copy[(Transactions_df_copy['product_class']=="low")|(Transactions_df_copy['product_class']=="medium")|(Transactions_df_copy['product_class']=="high")]
Transactions_df_copy=Transactions_df_copy[(Transactions_df_copy['product_size']=="small")|(Transactions_df_copy['product_size']=="medium")|(Transactions_df_copy['product_size']=="large")]
#No mislabeling of column "product_class" and "product_size"


#convert all incorrect data types(datetime to strings)
datetime_converter_transactions=Transactions_df_copy["transaction_date"].apply(lambda x: x.strftime('%Y-%m-%d'))
Transactions_df_copy["transaction_date"]=datetime_converter_transactions





#NEWCUSTOMERLIST SPREADSHEET

#Replace empty headers with "unknown headers 1-5" as no data provided for column header
NewCustomerList_df=data_frame_creater_with_column_renamer('KPMG_VI_New_raw_data_update_final.xlsx',"NewCustomerList",16,20)
NewCustomerList_df_copy=NewCustomerList_df.copy()

#Remove and count missing data
NewCustomerList_df_copy_NAN=NewCustomerList_df_copy[NewCustomerList_df_copy.isna().any(axis=1)]
NewCustomerList_df_copy.dropna(axis=0,inplace=True)
#1000-715=225

#Remove and count duplicates
NewCustomerList_df_copy=NewCustomerList_df_copy.drop_duplicates(keep=False)
# No duplicates



#Remove and count mislabled data

#Double count
#NewCustomerList_df_gender_mislabelled=NewCustomerList_df_copy[~((NewCustomerList_df_copy['gender']=="Male")|(NewCustomerList_df_copy['gender']=="Female"))]
NewCustomerList_df_copy=NewCustomerList_df_copy[(NewCustomerList_df_copy['gender']=="Male")|(NewCustomerList_df_copy['gender']=="Female")]


#1000-983=17
# 17 rows of data for column 'gender' not labelled "Male" or "Female"

#Check and count data with incorrect data types(Run once and comment out)
#NewCustomerList_df_copy=NewCustomerList_df_copy[~(NewCustomerList_df_copy['DOB'].apply(isinstance,args=(str,)))]
# 715-676=39

#convert all incorrect data types(datetime to strings)

NewCustomerList_df_wrong_data_type=NewCustomerList_df_copy[~((NewCustomerList_df_copy['DOB'].apply(isinstance,args=(int,)))|(NewCustomerList_df_copy['DOB'].apply(isinstance,args=(float,))))]
datetime_rows=NewCustomerList_df_copy[~(NewCustomerList_df_copy['DOB'].apply(isinstance,args=(str,)))]
datetime_converter=datetime_rows["DOB"].apply(lambda x: x.strftime('%Y-%m-%d'))
datetime_rows["DOB"]=datetime_converter
NewCustomerList_df_copy[~(NewCustomerList_df_copy['DOB'].apply(isinstance,args=(str,)))]=datetime_rows



#CUSTOMERADDRESS SPREADSHEET

CustomerAddress_df=data_frame_creater('KPMG_VI_New_raw_data_update_final.xlsx',"CustomerAddress")

#Remove and count missing data
CustomerAddress_df_copy=CustomerAddress_df.copy()
CustomerAddress_df_copy.dropna(axis=0,inplace=True)
CustomerAddress_df_copy=CustomerAddress_df_copy.drop_duplicates(keep=False)
#0

#Remove and count mislabled data
#Doesn't seem to have much things to remove?

dfs={'Transactions_empty':Transactions_df_copy_NAN
     ,'Transactions_mislabelled':Transactions_df_mislabelled
     , 'CustomerDemographic_empty':CustomerDemographic_df_copy_NAN
     ,'CustomerDemographic_mislabelled': CustomerDemographic_df_gender_mislabelled
     ,'CustomerDemographic_DataType':CustomerDemographic_df_wrong_data_type
     ,'NewCustomerList_empty':NewCustomerList_df_copy_NAN
     ,'NewCustomerList_DataType':NewCustomerList_df_wrong_data_type}


#excel_writer(Outlier,dfs)


writer=pd.ExcelWriter('Outlier.xlsx',engine='xlsxwriter')

for sheet_name in dfs.keys():
    dfs[sheet_name].to_excel(writer,sheet_name=sheet_name,index=False)

writer.save()




