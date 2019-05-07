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

- Data Understanding
  - Selection criteria
    - We will use the data in train.csv, it contains 9 fields.<br/>
    <image src="identify.png" />
  - Describing data<br/>
    <image src="describe.png" />
    - Store means different store numbers, Day of week ranges from 1 - 7 indicates Monday - Sunday, Date has exactly day, month, year, Sales is the total sale for one day, Customer is the # of people who visits the store, Open indicates the store is open if is 1, closed if it is 0, Promo indicates either store is offering promotion with 0 or 1, State Holiday has #0 or 1, 0 means no state holiday, 1 means there is state holiday, School Holiday contains the major holidays, 0 means there is no school holiday, 1 mean there is school holiday.
- Data Preparation
  - Selecting data
    - In the table above we will select Day of week, Sales, Customers, Promo, School Holiday for us to use.
  - Cleaning data
	- Since we are not doing competition we will filter to only 1 store, Date will be removed because we only care about which day of the week, we will filter Open to 1 because if the store is closed there will be no income, we will also remove State Holiday because we only care about the major holiday, and not every place has state holiday.<br/>
	<image src="clean.png" />
  - Formatting data
    - We will format/arrange the order of these field for later use.<br/>
    <image src="format.png" />
	- Now we will have sales as our target/dependent variable, Day of Week, Customers, Promo, School Holiday as our independent varible.

### C. Model
- Model Selection
  - We will build the model using Linear Regression(Supervised).
- Alternative choice/Pros and Cons
  - Since we are going to predict a numerical value based on the historical data, linear regression algorithm are sufficient, because it can be used to predict our target variable and describe/explains the relationship between one or more independent variable.
- Why and how selected model would solve business problems?
- Designing test set
- Building model

### D. Model Evaluation
- What technique used?
- How good is the model?
- How result should be evaluated?
- Explicitly state whether you have reached the business goals defined at the start of the project.

<!-- Using The Confusion Matrix to increase the accuracy.
Expected Value : EV = p(o1) · v(o1) + p(o2) · v(o2) + p(o3) · v(o3) ... -->

### E. Deployment
- How do you plan to deploy/use this model(How result will be deployed)(A strategy for putting it to work in your business)?
- Any issue the company should be aware of regarding deployment?

- Use scenarios
Get prediction results of the sales, try to find the relationship between sales , and independant variables