# 🌾 Smart Crop Advisor

This is a machine learning + web application that recommends the **best crop to cultivate** based on soil & climate conditions.  
It helps farmers or agricultural planners optimize their decisions.

---

## 🚀 Features
✅ Predicts best crop using:  
- Nitrogen, Phosphorus, Potassium (N, P, K)
- Temperature, Humidity, pH, Rainfall

✅ Live weather info for your city

✅ AI Agricultural Assistant (via Gemini)

---

## ⚙️ Tech Stack
- **Python**: Flask, Pandas, Scikit-Learn
- **Frontend**: HTML, CSS, Bootstrap, JS
- **ML**: Random Forest Classifier + scaling
- **WeatherAPI** for weather
- **Google Gemini API** for chat

---

## 📝 How does it work?

### 🔬 Machine Learning pipeline
- Used Kaggle crop recommendation dataset with soil nutrients & climate data.
- Did **EDA** using box plots & pair plots to visualize distributions & relationships.
- Checked for duplicates & missing values, dropped duplicates if needed.
- **Scaled features** with MinMaxScaler & StandardScaler so model treats all equally.
- Tried multiple classifiers:  
  - Logistic Regression, Decision Tree, KNN, Naive Bayes, Gradient Boosting, AdaBoost
- Finally selected **Random Forest** due to best accuracy.

### ✅ Model training (Jupyter notebook)
Example code:

    ```python
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import MinMaxScaler, StandardScaler
    import pandas as pd
    
    # Load dataset
    crop = pd.read_csv("Crop_recommendation.csv")
    
    # Drop duplicates if any
    crop = crop.drop_duplicates()
    
    # Split data
    X = crop.drop('label', axis=1)
    y = crop['label']
    
    # Scale features
    mms = MinMaxScaler()
    X_mms = mms.fit_transform(X)
    ss = StandardScaler()
    X_scaled = ss.fit_transform(X_mms)
    
    # Train model
    rf = RandomForestClassifier()
    rf.fit(X_scaled, y)

### 🌐 Web Interface (Flask)
app.py loads model + scalers and serves predictions via /predict.

index.html is a stylish glass UI with:

crop prediction form

live weather widget

AI assistant chat (Gemini)

🔥 Example backend code (app.py):

    @app.route("/predict", methods=['POST'])
    def predict():
        N = request.form['Nitrogen']
        P = request.form['Phosporus']
        K = request.form['Potassium']
        temp = request.form['Temperature']
        humidity = request.form['Humidity']
        ph = request.form['Ph']
        rainfall = request.form['Rainfall']
    
        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        scaled_features = ms.transform([feature_list])
        final_features = sc.transform(scaled_features)
        prediction = model.predict(final_features)

### Screenshots

![image](https://github.com/user-attachments/assets/3118bfa7-fc1b-41fb-b743-f90f78e4fb35)
![image](https://github.com/user-attachments/assets/08ef4eee-f9f2-4408-9e50-11dd2182d8d0)

