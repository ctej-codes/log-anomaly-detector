import pandas as pd
from sklearn.ensemble import IsolationForest

# Path to the log file that will be analyzed
log_file = "system_logs.txt"

# Read all log entries from the file
with open(log_file, "r") as file:
    logs = file.readlines()

# Store parsed log data
data = []

# Extract timestamp, log level, and message from each log entry
for log in logs:
    parts = log.strip().split(" ", 3)

    # Skip malformed log entries
    if len(parts) < 4:
        continue

    timestamp = parts[0] + " " + parts[1]
    level = parts[2]
    message = parts[3]

    data.append([timestamp, level, message])

# Create a DataFrame for easier analysis
df = pd.DataFrame(data, columns=["timestamp", "level", "message"])

# Convert timestamp column to datetime format
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Assign numerical severity scores to log levels
level_score = {
    "INFO": 1,
    "WARNING": 2,
    "ERROR": 3,
    "CRITICAL": 4
}

df["level_mapping"] = df["level"].map(level_score)

print(df)

# Generate a feature representing the length of each log message
df["message_length"] = df["message"].apply(len)

# Train an Isolation Forest model to identify anomalous logs
model = IsolationForest(
    contamination=0.1,
    random_state=42
)

# Predict anomalies using log severity and message length
df["anomaly_value"] = model.fit_predict(
    df[["level_mapping", "message_length"]]
)

# Convert model predictions into user-friendly labels
labels = []

for value in df["anomaly_value"]:
    if value == -1:
        labels.append("❌ Anomaly")
    else:
        labels.append("✅ Normal")

df["is_anomaly"] = labels

# Extract all anomalous log entries
anomalies = df[df["is_anomaly"] == "❌ Anomaly"]

# Display detected anomalies
print("\nDetected Anomalies:\n")
print(anomalies)
