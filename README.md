# Laptop-Price-Predictor
Welcome to the Laptop Price Prediction project! In this repository, we explore the fascinating world of laptop pricing using data science techniques. The goal of this project is to develop a predictive model that can accurately forecast laptop prices based on various features such as specifications, brand, and market trends.

# Project Overview
In today's fast-paced technological landscape, laptops have become indispensable tools for work, education, and entertainment. However, with a myriad of options available in the market, determining the fair price of a laptop can be challenging for both consumers and sellers. This project aims to address this challenge by leveraging machine learning algorithms to predict laptop prices with greater precision.

# Key Highlights
- <b>Exploratory Data Analysis (EDA):</b> We employ Pandas and Seaborn to meticulously explore the dataset, gaining insights into the relationships between different features and laptop prices. Through visualizations and statistical analysis, we uncover patterns and trends that inform our modeling approach.
- <b>Data Preprocessing:</b> Before building our predictive model, we preprocess the data to ensure its quality and suitability for modeling. This includes textual data cleaning, encoding categorical variables, and feature engineering.
- <b>Model Construction:</b> Using Scikit-learn, we construct and fine-tune machine learning models to predict laptop prices. We experiment with various algorithms and techniques, optimizing hyperparameters to improve the model's accuracy and generalization capabilities.
- <b>Performance Evaluation:</b> We evaluate the performance of our models using relevant metrics such as the R2 score. By comparing different models and assessing their strengths and weaknesses, we identify the most effective approach for predicting laptop prices.

# How to Use This Repository
- <b>Data:</b> The dataset used in this project is available in the data directory. You can explore the raw data as well as the preprocessed dataset.
- <b>Notebooks:</b> The Jupyter notebooks namely "Laptop Price Predictor" details each step of the project, from data exploration to model evaluation. Feel free to follow along and experiment with the code.
- <b>Code:</b> In the "laptop_price_predictor" directory, you'll find Python scripts for deploying model onto production using Docker and Kubernetes.

# Deployment Instructions
### Kubernetes
- Apply the Kubernetes deployment YAML file:
  ```
  kubectl apply -f ./K8s/kubernetes_deployment.yml
  ```
- Apply the Kubernetes service YAML file:
  ```
  kubectl apply -f ./K8s/kubernetes_service.yml
  ```
- Check the status of the deployed service:
  ```
  kubectl get svc
  ```
### Docker
- Clean up any unused Docker resources
  ```
  docker system prune
  ```
- Build the Docker image
  ```
  docker build . -t aniketmm98/laptop_price_prediction
  ```
- Run the Docker container
  ```
  docker run --rm -it -p 8501:8501 --user=42420:42420 aniketmm98/laptop_price_prediction:latest
  ```
These instructions assume you have Docker and Kubernetes installed and configured properly on your system. Make sure to replace aniketmm98/laptop_price_prediction with the appropriate Docker image name and tag for your project.

# Contributions
Contributions to this project are welcome! Whether you'd like to suggest improvements, report issues, or add new features, please feel free to open an issue or submit a pull request. Together, we can enhance the accuracy and usability of the laptop price prediction model.
