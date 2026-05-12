"""ML models for churn prediction and LTV forecasting"""

from typing import Dict, List

import numpy as np
from sklearn.ensemble import GradientBoostingClassifier, RandomForestRegressor
from sklearn.preprocessing import StandardScaler


class ChurnPredictor:
    """Predict customer churn probability"""

    def __init__(self):
        self.model = GradientBoostingClassifier(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
        self.is_trained = False

    def train(self, X_train: np.ndarray, y_train: np.ndarray) -> Dict:
        """Train churn prediction model"""
        X_scaled = self.scaler.fit_transform(X_train)
        self.model.fit(X_scaled, y_train)
        self.is_trained = True

        return {"status": "trained", "features": X_train.shape[1]}

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict churn probability (0-1)"""
        if not self.is_trained:
            raise ValueError("Model not trained yet")

        X_scaled = self.scaler.transform(X)
        return self.model.predict_proba(X_scaled)[:, 1]


class LTVForecaster:
    """Forecast customer lifetime value"""

    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
        self.is_trained = False

    def train(self, X_train: np.ndarray, y_train: np.ndarray) -> Dict:
        """Train LTV forecasting model"""
        X_scaled = self.scaler.fit_transform(X_train)
        self.model.fit(X_scaled, y_train)
        self.is_trained = True

        return {"status": "trained", "features": X_train.shape[1]}

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict customer LTV"""
        if not self.is_trained:
            raise ValueError("Model not trained yet")

        X_scaled = self.scaler.transform(X)
        predictions = self.model.predict(X_scaled)
        return np.maximum(predictions, 0)  # LTV cannot be negative
