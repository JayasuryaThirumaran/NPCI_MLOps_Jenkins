import pickle
import numpy as np
from sklearn.metrics import mean_squared_error

# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Generate new test data
X_test = np.random.rand(20, 1) * 10
y_test = 2 * X_test + np.random.randn(20, 1) * 2

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Model Evaluation: Mean Squared Error = {mse}")
