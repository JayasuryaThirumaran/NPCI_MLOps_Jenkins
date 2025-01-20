## Assignment: Automating a Machine Learning Pipeline with Jenkins

### Objective:
Set up a Jenkins pipeline to automate the training and evaluation of a simple machine learning model.

### Instructions:

1. Set up Jenkins:
Install Jenkins on your local machine or use a cloud-based Jenkins service.
Ensure the necessary plugins are installed (e.g., Git, Pipeline, and any Python-related plugins if needed).

2. Create a GitHub Repository:
Create a repository (or use a provided one) with a simple machine learning script. For example:
A Python script (train.py) that trains a basic linear regression model using dummy data.
Save the trained model to a file (e.g., model.pkl).
Another script (evaluate.py) to evaluate the model on test data and output performance metrics.

3. Jenkins Pipeline Tasks:
Configure a Jenkins job to:
Pull the latest code from your GitHub repository.
Install dependencies using pip install -r requirements.txt.
Run the train.py script to train the model.
Run the evaluate.py script to evaluate the model.
Archive the trained model and evaluation metrics as build artifacts in Jenkins.

4. Add Build Triggers:
Configure the pipeline to trigger automatically when there is a code change in the repository.

### Deliverables:
A screenshot of the Jenkins job configuration.
A screenshot of a successful pipeline run with all stages completed.
The archived model and metrics as build artifacts.
