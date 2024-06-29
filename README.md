# Real Estate Price Prediction Web Application

## Table of Contents
1. [Project Summary](#project-summary)
2. [Installation](#installation)
3. [Usage](#usage)
4. [System Development Approach](#system-development-approach)
5. [Algorithm & Model Training](#algorithm--model-training)
6. [Web Application](#web-application)
7. [Results](#results)
8. [Future Scope](#future-scope)
9. [Contributing](#contributing)
10. [License](#license)
11. [References](#references)

## Project Summary
The Real Estate Price Prediction Web Application is designed to predict real estate prices based on various property features. The application leverages a machine learning model to provide users with an estimated price by inputting details such as area type, location, total square footage, size, number of bathrooms, and balconies. Additionally, the application displays a comparison of actual and predicted prices for a sample of properties, along with visualizations of price distributions by area type.

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/Mogan-ram/Real-Estate-Price-Prediction-for-banglore-using-data-science.git
    cd real-estate-price-prediction
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download and place the dataset:**
    - Place your dataset (`bengaluru_prices_preprocessed-100.csv`) in the `data` directory.

5. **Train the model:**
    - Run the Jupyter notebook `main.ipynb` to preprocess the data, train the model, and save the results.

## Usage
1. **Run the Flask application:**
    ```bash
    python app.py
    ```

2. **Open your browser and navigate to:**
    ```
    http://127.0.0.1:5000/
    ```

3. **Input property details to get a price prediction and view visualizations.**

## System Development Approach
- **Technology Stack:**
  - **Backend:** Flask
  - **Frontend:** HTML, CSS, JavaScript
  - **Machine Learning:** scikit-learn, pandas
  - **Visualization:** Plotly

- **Data Processing:**
  - Data cleaning and preprocessing
  - Feature engineering and transformation

- **Model Training:**
  - Train and evaluate a RandomForestRegressor model

## Algorithm & Model Training
### Algorithm: RandomForestRegressor
- **Ensemble learning method combining multiple decision trees.**
- **Handles both numerical and categorical features.**
- **Provides high accuracy and controls overfitting.**

### Model Training
- **Preprocessing steps include handling missing values and one-hot encoding.**
- **Model trained on features such as area type, location, size, total square footage, number of bathrooms, and balconies.**
- **Evaluation Metrics:**
  - **R² Score:** 0.7245813356228716
  - **RMSE:** 58.45149432376845

## Web Application
- **Flask-based server handling user inputs, model prediction, and data visualization.**
- **Interactive visualizations created using Plotly.**
- **User-friendly interface allowing real-time price predictions based on user input.**

## Results
- **Functional web application providing accurate real estate price predictions.**
- **Displayed actual and predicted prices for a sample of properties.**
- **Visualized price distributions by area type.**

## Future Scope
- **Enhance the model with more data and advanced features.**
- **Integrate additional property attributes like amenities and proximity to landmarks.**
- **Implement user authentication and personalized dashboards.**
- **Extend the application to predict prices for other cities or regions.**

## Contributing
1. **Fork the repository.**
2. **Create a new branch:**
    ```bash
    git checkout -b feature-branch-name
    ```
3. **Make your changes and commit them:**
    ```bash
    git commit -m 'Add some feature'
    ```
4. **Push to the branch:**
    ```bash
    git push origin feature-branch-name
    ```
5. **Submit a pull request.**

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## References
- Flask documentation: https://flask.palletsprojects.com/
- scikit-learn documentation: https://scikit-learn.org/
- pandas documentation: https://pandas.pydata.org/
- Plotly documentation: https://plotly.com/python/
- Joblib documentation: https://joblib.readthedocs.io/
