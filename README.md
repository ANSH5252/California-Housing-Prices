# 🏠 California Housing Price Prediction
This project is a Machine Learning-based regression system that predicts the median house value of districts in California. Leveraging housing and geographical data from the 1990 California Census, the model offers accurate insights into how different features (e.g., income, location, rooms, population) influence house prices.

## 🚀 Features
- Predicts house prices using multiple regression models

- Explores spatial housing trends in California using visualizations

- Comprehensive EDA and data cleaning pipeline

- Uses preprocessing techniques like imputation, scaling, and feature engineering

- Evaluates model performance using standard metrics like RMSE, MAE, and R²

- Designed to be deployed with Streamlit as a web app

## 📊 Tech Stack
- Language: Python 🐍

- Libraries:

  - pandas, numpy – Data manipulation

  - matplotlib, seaborn, plotly – Data visualization

  - scikit-learn – ML models and preprocessing

  - streamlit – For building the interactive web app

  - pickle – For saving the trained model and features

- Models Used:

  - Linear Regression

  - Ridge Regressor

  - Lasso Regressor

  - Random Forest Regressor

  - Gradient Boosting Regressor

  - K - Neighbors Regressor

- Metric Used:

  - Mean Absolute Error (MAE)

  - Mean Squared Error (MSE)

  - Root Mean Squared Error (RMSE)

  - R² Score

- Model Selection

  - Randomized Search CV

## 📁 Project Structure
```
California-Housing-Prices/
├── housing.csv             # Dataset
├── housing.ipynb           # Data Analysis and Model Training
├── description.txt         # Description of the Features of the Dataset
├── features.pkl            # A list containg Feature names
├── model.pkl               # Trained model file
├── scaler.pkl              # File containg scaler funtion to scale the Data
├── app.py                  # Streamlit web app
├── requirements.txt        # Python dependencies
└── README.md               # Project overview
```
## 📥 How to Run
-  1. Clone the Repository
```
git clone https://github.com/ANSH5252/California-Housing-Prices.git
cd California-Housing-Prices
```
- 2. Install Dependencies
```
pip install -r requirements.txt
```
- 3. Launch Streamlit Web App
```
streamlit run app.py
```
## 🧠 How It Works
- 1. Load & Explore Data
  - Uses median values across blocks (rows ≈ 20k)

  - Visualizes trends by geography (latitude/longitude)

- 2. Data Cleaning
  - Handles missing values (especially in total_bedrooms)

  - Removes extreme outliers

  - Converts categorical data if present (like ocean proximity)

- 3. Feature Engineering
  -  Creates rooms_per_household, bedrooms_ratio, population_per_household, etc.

  -  Uses scaling and transformation on skewed features

- 4. Model Training
  - Applies ML models with train-test split and cross-validation

  -  Selects best-performing model based on evaluation metrics

- 5. Model Deployment
  - Saves the trained model and features using pickle

  - Web app takes user input for features and displays predicted price

## 🧪 Example Usage

Open the Streamlit app by running the command in your terminal. Then enter the following values :  
``` 
    Median Income (in $1000s) = 3.5
    Housing Median Age = 30
    Total Rooms = 2000
    Total Bedrooms = 500
    Population = 1500
    Households = 300
    Latitude = 34.2
    Longitude = -118.3
    Ocean Proximity = Ocean Proximity
```
Output:  
🏡 Estimated House Price: $226,311

## 📸 Screenshots
![image](https://github.com/user-attachments/assets/81277421-98dd-4af1-9984-34082002ded6)
![image](https://github.com/user-attachments/assets/f95fa589-79b9-4c24-9d5a-dcf199590941)
[California House Price Prediction Demo.webm](https://github.com/user-attachments/assets/f20597f2-bd2c-4da4-8805-4c76045e3fa4)
## 🤝 Contributing
Contributions, suggestions, and feature requests are welcome!  
Feel free to:

- Fork this repository

- Create a new branch

- Submit a pull request

⭐ If you find this useful, give it a star and feel free to spread the word!

## 📄 License
This project is licensed under the MIT License.

## 🧑‍💻 Author
Anshuman Dash  
[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/ANSH5252)
