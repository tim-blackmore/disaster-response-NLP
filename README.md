# disaster-response-NLP
A machine learning pipeline for classifying messages from natural disasters and allocating them to the correct services.

![image](https://user-images.githubusercontent.com/24419429/110096269-a5c9d880-7d95-11eb-8da2-7ff147628682.png)

# Contents
 - [Quickstart](#Quickstart) 
 - [Installation](#Installation) 
 - [How to run](#How-to-run) 
 - [Motivation](#Motivation) 
 - [Project files](#Project-files) 
 - [Project summary](#Project-summary) 
 - [Acknowledgements](#Acknowledgements) 
 
## Installation

The libraries used in this project are outlined in requirements.txt. They can be installed using the following command.

1. Install pipenv.
``` pip3 install pipenv```

2. Install packages in virtual environment
```pipenv install -r requirements.txt```

## How to run

To run the app locally. 
1. Run the following command and click the link in the terminal.<br>
``` pipenv run run.py```

To run the files individually.
1. Open a command line in the project folder.
2. Run the following commands (the second takes a long time to run).

This command will output a database that the next command will use.<br/>
``` pipenv run process_data.py -m messages.csv -c categories.csv -d disaster_db```<br/>

This will train the classifier.<br/>
``` pipenv run train_classifier.py```

## Motivation

This project fulfils one of the requirements for the completion of the Data Science nanodegree with Udacity. 

## Project files

- *requirements.txt* - Contains the required packages to set up the development envrironment.
- *process_data.py* - A python script which imports, merges and clean the dataset and stores it in a SQlite database.
- *train_classifier.py* - A python script which creates a machine learning pipeline and trains a random forest classifier.
- *custom_transformer.py* - A python cript which contains transform classes for text data.
- *models/model.joblib* - The trained model.
- *app/run.py* - The flask app that runs in the web browser.
- *app/create_figures.py* - Creates the Plotly figures ready for the app.
- *categories.csv* - the classes for each of the categories
- *messages.csv* - the mesages from which the classes relate too
- *disaster.db* - the database which is an output from prcoess data.py.

## Project summary

### 1. Business understanding
The goal is to complete the Data Science project as part of the Udacity nanodegree. 

We are tasked with training a machine learning model to predict the service categories related to a text based message. 

### 2. Data understanding
Data has been preconfigured by Figure Eight. It includes 2 files. Firstly messages.csv which includes real messages that have been sent during the occurence of a natural disaster. The second file, categories.csv, contains the associated service categories that the messages relate too. The categories data are multi class.

![image](https://user-images.githubusercontent.com/24419429/110096394-c5610100-7d95-11eb-95ee-2f06d16ceb61.png)

![image](https://user-images.githubusercontent.com/24419429/110096561-ecb7ce00-7d95-11eb-9b1e-e6c1ded66fd6.png)

### 3. Data preparation
The two data files are treated as follows;
1. Data are imported
2. Data are merged
3. Data are exported into an SQlite database called disaster_db.<br>

### 4. Modelling
A random forest classfier (with a multiclassfication wrapper) was chosen to classify the text data. The data were split into training and testing sets and then entered a pipeline. The pipeline includes a feature union which includes a number of transformers including tfidf and sentiment transformers. The model is trained using GridSearchCV. To account for the imbalance, I used a class weight set to 'balanced' in the classifier.

I would have like to have synthesise cases, but I found the area of research a little sparse with suggestions of SMOTE oversampling of text data as incorrect due to its hign dimensionality.

### 5. Evaluation
The F1 score was chosen to evaluate the model as it accounts for both precision an recall. Due to the large class imbalance, precision will be high so using that could give us a false impression of success. We want to reward classifying the correct response for both 1 and 0. Further to this, we used the F1 score 'macro' as this lends weight to the smaller class in the class imbalance.

The resulting average F Score was 0.56.

### 6. Deployment
N/A

## Acknowledgements
Some functions relating to the python scripts were taken from the Udacity training materials.<br>

The following articles also helped me with some decision making.

https://towardsdatascience.com/random-forest-hyperparameters-and-how-to-fine-tune-them-17aee785ee0d
https://www.analyticsvidhya.com/blog/2020/10/improve-class-imbalance-class-weights/

