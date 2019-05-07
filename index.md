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
    - We will use the data in data.csv, it contains 9 fields.<br/>
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
  - Since we are going to predict a numerical value based on the historical data, linear regression algorithm are sufficient, because it can be used to predict our target variable and describe/explains the relationship between one or more independent variables.
- The selected model should be able to tell us how independent variable related to the target variable, for example if variable Promo show most siginifcance(P-VALUE > 0.05) in the model, Holiday, Day of Week, and Customer shows no significance(P-VALUE <= 0.05), then we know that giving out promotion on any day would increase our sale.
- Building model<br/>
<image src="model1.png" /><br/>
<image src="model2.png" /><br/>
<image src="split.png" /><br/>
<image src="plot.png" />

### D. Model Evaluation
- Use Cross Validation

- How good is the model?
- How result should be evaluated?

### E. Deployment
- How do you plan to deploy/use this model(How result will be deployed)(A strategy for putting it to work in your business)?
- Any issue the company should be aware of regarding deployment?
- Use scenarios
Get prediction results of the sales, try to find the relationship between sales , and independant variables