## Goal
The goal is to detect the fraudulent clicks based on recorded information from  approximately 200 million clicks 
information collected over 4 days. 
## Data processing     
- [ ] Done by 16th May

##### Download the data
The whole data set consists of main train and test data sets, a smaller training subsample, and an undocumented
test supplement.
The full training data is about 11+ GB containing 184903890 rows. 
The smaller training set is about 6.1+ MB and includes 100000 random rows of the full data set. 

In order to develop the model, we are starting with the sample training data set. 


###  Investigating the data
The training data set contains 7 predictors and one target feature.  The predictors include 5 numerical identifier features and 
two date-time features. Features are:

- ip: ip address of click.

- app: app id for marketing.

- device: device type id of user mobile phone (e.g., iphone 6 plus, iphone 7, huawei mate 7, etc.)

- os: os version id of user mobile phone

- channel: channel id of mobile ad publisher

- click_time: timestamp of click (UTC)

- attributed_time: if user download the app for after clicking an ad, this is the time of the app download

- is_attributed: the target that is to be predicted, indicating the app was downloaded
 
There are lots of missing value in attributed_time: If is_attributed is 0, this is empty.

####  checking the distribution of features (training subsample)
  
  - There are 227 missing value in is_attributed feature.
  
  - whitin this data there are:
    - 34857 unique ip
    - 161 unique app
    - 100 unique device
    - 130 unique os
    - 161 unique channel
    - 80350 unique click_time
    
   It shows that about 19650 click_time are simmilar.

####  calculating some descriptive information
  
#### Checking correlation between data

### Extracting more features from existing data

### visualization the features

## Building the model
- [ ] Done by 23rd May

Build The model based on the sample train data. 

### developing the model
### evaluating the model

## Run the final model based on the original data set on a cloud. 
- [ ] Done by 30th May

### write a report and make a presentation





