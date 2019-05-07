## CS381 Data Analysis Project
Team name: Data Rangers

Team members:
  1. Jatinkumar Patel
  2. Deep Shah
  3. Ramanjeet Singh
  4. Ning Wei
  5. Jingwei Chen
  6. Jiawei Yang
  
### A. Business Problem/Understanding

- Business goals
  - Company wants to imporve sales
- Data-mining goals
  - Predict sales based on day of week(which day has higher sales), promotion(If store runs promotion or not), holiday(sale on holiday) and number of customers.
- Success criteria
  - By identifying the relationship between promotions, holidays and day of week, we can find out how it leads to higer sales or lower sales, depends on the result, we can make the right desicion to help the company to increase its sales and make more profit.

### B. Data Understanding/Preparation/Source

Dataset name: Rossmann Store Sales

Dataset URL: [https://www.kaggle.com/c/rossmann-store-sales/data](https://www.kaggle.com/c/rossmann-store-sales/data)

Target variable will be the sales of a store, 

- Data Understanding
  - Selection criteria
    - We will use the data in train.csv, 
  - Describing data
- Data Preparation
##### a. Selecting data
##### b. Cleaning data
##### c. Constructing data
##### d. Integrating data
##### e. Formatting data

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


### C. Model
1. model selection : Linear Regression

### D. Model Evaluation

### E. Deployment
Using The Confusion Matrix to increase the accuracy.

Expected Value : EV = p(o1) · v(o1) + p(o2) · v(o2) + p(o3) · v(o3) ...
