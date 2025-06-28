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

✅ CLI tool to get **7-day forecast**

---

## ⚙️ Tech Stack
- **Python**: Flask, Pandas, Scikit-Learn
- **Frontend**: HTML, CSS, Bootstrap, JS
- **ML**: Random Forest Classifier + scaling
- **WeatherAPI** for weather
- **Google Gemini API** for chat

---

## 📝 How does it work?

### 🔬 Machine Learning
Trained on crop recommendation dataset.  
Uses a **Random Forest** to classify which crop to grow.

Example from Jupyter notebook:

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd

# Load dataset
crop = pd.read_csv("Crop_recommendation.csv")

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
```

Model is saved as `model1.pkl`, `standscaler1.pkl` & `minmaxscaler1.pkl`.

---

### 🌐 Web Interface (Flask)
- `app.py` loads model + scalers and serves predictions.
- `index.html` is a stylish page with:
  - crop prediction form
  - live weather widget
  - AI assistant chat (Gemini)

#### 🔥 Example backend code (`app.py`):
```python
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
```

---

### ☁️ Weather CLI (`new.py`)
Run from terminal to see **7-day weather forecast**:

```bash
python new.py
```

Sample code:

```python
API_KEY = "your_weather_api_key"
CITY = input("Enter your city: ")
URL = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={CITY}&days=7"
data = requests.get(URL).json()

for day in data["forecast"]["forecastday"]:
    print(day["date"], day["day"]["avgtemp_c"], "°C")
```

---

## 📷 Screenshots
- 🏠 Home Page
- 🌾 Recommended Crop
- 🌤️ Weather Widget
- 🤖 AI Assistant
- 🖥️ CLI Weather Forecast

(Add images here using markdown like:  
`![Home Page](screenshots/home.png)` )

---

## 🚀 How to run

### 🔧 Clone and install
```bash
git clone https://github.com/yourusername/Smart-Crop-Advisor.git
cd Smart-Crop-Advisor
pip install -r requirements.txt
```

### 🐍 Run web app
```bash
python app.py
```
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)
