import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate synthetic training data (Replace with real network traffic dataset)
def generate_data():
    data = pd.DataFrame({
        "packet_size": np.random.randint(50, 1500, 1000),
        "ttl": np.random.randint(30, 255, 1000),
        "is_tcp": np.random.randint(0, 2, 1000),
        "is_udp": np.random.randint(0, 2, 1000),
        "label": np.random.randint(0, 2, 1000)  # 0: Normal, 1: Anomaly
    })
    return data

# Train and save the ML model
def train_model():
    data = generate_data()
    X = data.drop("label", axis=1)
    y = data["label"]
    
    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    # Evaluate model performance
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model trained with accuracy: {accuracy:.2f}")

    # Save the trained model
    joblib.dump(model, "models/ids_model.pkl")
    print("Model saved as 'models/ids_model.pkl'")

if __name__ == "__main__":
    train_model()
