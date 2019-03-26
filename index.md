## CS381 Data Analysis Project
Team name: Data Rangers

Team members:
  1. Jatinkumar Patel
  2. Deep Shah
  3. Ramanjeet Singh
  4. Ning Wei
  5. Jingwei Chen
  6. Jiawei Yang
  7. Shengyou Zheng
  
### Business idea
Forecast sales using store data(ex, how far it is from competitors),Day of week, promotion(ex. If store runs promotion or not), holiday(sale on holiday) and competitor data.

Data mining problem in this case will be to clear out unnecessary data and make valid connection in between independent variables to minimize the error.

Supervised. 

Target variable will the sale of a store, it will add business value by helping the business to increase its sale and make more profit.

### Dataset infomation and instences

Dataset name: Rossmann Store Sales

Dataset URL: [https://www.kaggle.com/c/rossmann-store-sales/data](https://www.kaggle.com/c/rossmann-store-sales/data)

Data Instance selection is an important data pre-processing step that can be applied in many data mining tasks.

<image src="Store1_data_info.png" width="700" />

### Use scenarios
Get prediction results of the sales, try to find the relationship between sales , and independant variables

### Implement steps:
#### Step 1:  Target variable.

dependent variable: sales

#### Step 2:  Choose independent variable.

independent variable : DayOfWeek, Number of Customers, Promotion(true/false), SchoolHoliday.  

target variable depends on the above instances.

Predict the sales on a particular day.

#### Step 3 Data cleaning:

1.Reduce errors or missing data.

2.General analysis.


#### Step 4 Modeling
1. model selection : Linear Regression

#### Step 5 Testing
Using The Confusion Matrix to increase the accuracy.

Expected Value : EV = p(o1) · v(o1) + p(o2) · v(o2) + p(o3) · v(o3) ...

