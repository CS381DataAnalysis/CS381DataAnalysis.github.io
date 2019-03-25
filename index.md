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
Forecast sales using store, promotion, holiday and competitor data

### Dataset infomation and instences

Dataset name: Rossmann Store Sales

Dataset URL: [https://www.kaggle.com/c/rossmann-store-sales/data](https://www.kaggle.com/c/rossmann-store-sales/data)

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
1. model selection : linear 

#### Step 5 Testing
Using The Confusion Matrix to increase the accuracy.

Expected Value : EV = p(o1) · v(o1) + p(o2) · v(o2) + p(o3) · v(o3) ...
