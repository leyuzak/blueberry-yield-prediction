# Blueberry Yield Prediction with Machine Learning

**Live Demo:** [Hugging Face Space](https://huggingface.co/spaces/leyuzak/Blueberry-Yield-Prediction-with-Machine-Learning)  
**Notebook:** [Kaggle Notebook](https://www.kaggle.com/code/leyuzakoksoken/blueberry-yield-prediction-with-machine-learning)

---

## 📋 Overview
This project aims to predict wild blueberry yields by analyzing various environmental and pollination-related factors. Using advanced gradient boosting techniques, the model processes features such as bee density (honeybees, bumblebees, androgrena, etc.), weather conditions (temperature, rain), and pollination efficiency to provide accurate yield estimations.

The goal is to provide a data-driven tool for farmers and researchers to optimize blueberry production based on complex environmental inputs.

## 🤖 Model & Methodology
The project utilizes the **HistGradientBoostingRegressor**, a high-performance gradient boosting algorithm optimized for large datasets. 

**Key Hyperparameters:**
- `learning_rate`: 0.05
- `max_iter`: 2000
- `max_leaf_nodes`: 64
- `min_samples_leaf`: 20

To ensure model stability and prevent overfitting, a **5-fold Cross-Validation** strategy was implemented.

## 📊 Performance Metrics
The model demonstrates strong predictive power with the following results:

- **Training RMSE:** ~510.62
- **Cross-Validation RMSE (Mean):** ~567.27
- **CV Standard Deviation:** ~16.41

The close proximity between training and cross-validation scores indicates a well-generalized model with low variance.

### Predicted vs True Values
![True vs Predicted](image_779dbf.png)

## 📁 Project Structure
- `app.py`: Streamlit-based web application for real-time predictions.
- `blueberry-yield-prediction-with-machine-learning.ipynb`: Full data science workflow including EDA, preprocessing, and model training.
- `blueberry_model.pkl`: The trained and serialized machine learning model.
- `submission.csv`: Final predictions on the test dataset.

## 🛠️ Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/blueberry-yield-prediction.git](https://github.com/your-username/blueberry-yield-prediction.git)
    cd blueberry-yield-prediction
    ```

2.  **Install dependencies:**
    ```bash
    pip install pandas scikit-learn streamlit joblib matplotlib seaborn numpy
    ```

3.  **Run the Application:**
    ```bash
    streamlit run app.py
    ```

## 🌐 Deployment
The model is live and accessible via **Hugging Face Spaces**, allowing for easy interaction without the need for local environment setup.

---
**Author:** Leyuza Köksöken
**Dataset Source:** Wild Blueberry Yield Prediction Dataset
