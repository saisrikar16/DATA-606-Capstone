# Health Insurance Fraud Claim Detection and Claim Amount Prediction

## Title and Author
- **Project Title:** Health Insurance Fraud Claim Detection and Claim Amount Prediction
- **Prepared for:** UMBC Data Science Master Degree Capstone by Ozgur Ozturk
- **Author Name:** Sai Srikar Gurthuru
- **GitHub Profile:** https://github.com/saisrikar16
- **LinkedIn Profile:** https://www.linkedin.com/in/sai-srikar-gurthuru-b06ba8179/
## Background
### What is it about?
This project aims to develop a system that can detect whether a health insurance claim is fraudulent or not, as well as create a model capable of accurately predicting the amount of the claim based on user information.

### Why does it matter?
Health insurance fraud claim prediction is crucial for protecting insurers from financial losses and maintaining trust in the system. Claim amount prediction ensures fair reimbursement, optimizing resource allocation, and providing better financial planning for insurance companies.

### Research Questions
1. Can we accurately predict whether a customer's insurance claim is fraudulent or not?
2. Can we accurately predict claim amount of customer based on customer details?
3. Which features have the most significant impact on predicting customer Health Insurance claim amount and predicting claim is fraudulent or not ?

## Data
### Data Sources
The dataset provided by the Insurance companies contains information on 15000 customers.

### Data Details
- **Data Size:** 1.23 MD
- **Data Shape:** 15000 rows, [Number of columns]
- **Time Period:** Not specified
- **Each Row Represents:** A customer's demographic and insurance information, along with their response to the previous insurance campaign.

### Data Dictionary
| Column Name        | Data Type | Definition                                                 | Potential Values                        |
|--------------------|-----------|------------------------------------------------------------|-----------------------------------------|
| RID                | -         | Customer ID                                                | -                                       |
| Age                | Numeric   | Customer's age in completed years                          | -                                       |
| Sum Insured        | Numeric   | Total Insurance amount that can be claimed                 | -                                       |
| Sex                | Binary    | Gender of the customer                                     | M, F                                    |
| Weight             | Numeric   | Weight of the customer                                     | -                                       |
| BMI                | Numeric   | Body mass Indicator                                        | -                                       |
| Hereditary diseases| String    | Existing Hereditary diseases                               | -                                       |
| No of dependents   | Numeric   | No of dependents                                           | -                                       |
| Smoker             | Binary    | Smoking History of the customer                            | 0, 1                                    |
| city               | String    | City of the customer                                       | -                                       |
| bloodpressure      | Numeric   | Blood pressure of the customer                             |                                         |
| diabetes           | Binary    | Does the customer have a diabetes?                         | 0, 1                                    |
| regular_ex         | Binary    | Do customers does regular execise?                         | 0, 1                                    |
| job_title          | String    | Job title of customer                                      | -                                       |
| claim              | Numeric   | Claim amount done by customer                              | -                                       |
| Label              | Binary    | claim is fraudulent or not                                 | 0, 1                                    |


### Target Variable
- **Label:** claim is fraudulent or not

### Features/Predictors
- RID,Age,Sum Insured,Sex,Weight,BMI,Hereditary diseases,No of dependents,Smoker,city,bloodpressure,diabetes,regular_ex,job_title,claim,Label.
