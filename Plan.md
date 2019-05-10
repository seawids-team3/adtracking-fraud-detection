## Goal
The goal is to detect the fradulant clicks based on recorded information from  approximately 200 million clicks information collected over 4 days. 
## Data processing     
- [ ] Done by 16th May

##### Download the data
The whole data set was consist of main train and test data sets and two other files of sample of train and test data sets. 
The original tarin data is about 11+ GB containing 184903890 rows. There is a a sample set of train data set. 
The sample train set is about 6.1+ MB and include 100000 random saple of original data set. 

In order to develop the model, we work on sample taining data set. 


###  Investigating the data
The training data set contains 8 features including 7 numerical features and one date-time feature. Features name are :
- ip: ip address of click.

- app: app id for marketing.

- device: device type id of user mobile phone (e.g., iphone 6 plus, iphone 7, huawei mate 7, etc.)

- os: os version id of user mobile phone

- channel: channel id of mobile ad publisher

- click_time: timestamp of click (UTC)

- attributed_time: if user download the app for after clicking an ad, this is the time of the app download

- is_attributed: the target that is to be predicted, indicating the app was downloaded
 
There are lots of missing value in click_time. If the clik is fradulant, the is_attributed feature is 1 otherwise it is 0. 

  ####  checking the distribution of features
  
  - tehre are 227 missing value in is_attributed feature.
  
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





