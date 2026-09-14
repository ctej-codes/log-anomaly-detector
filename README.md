# Log Anomaly Detection Using Isolation Forest

## Overview

This project demonstrates a basic AIOps (Artificial Intelligence for IT Operations) use case by applying Machine Learning techniques to system logs. The solution parses structured log data, performs feature engineering, and leverages the Isolation Forest anomaly detection algorithm to identify potentially unusual system events for further investigation.

The script:

- Reads and parses log entries from a text file
- Extracts timestamps, log levels, and messages
- Converts log severity levels into numerical values
- Creates features suitable for machine learning
- Applies Isolation Forest for anomaly detection
- Labels logs as either **Normal** or **Anomaly**

---

## Features

✅ Parse structured system logs

✅ Convert log severity levels into numerical scores

✅ Generate features from log data

✅ Detect anomalies using Isolation Forest

✅ Classify logs as Normal or Anomalous

✅ Beginner-friendly AIOps implementation

---

## Technologies Used

- Python 3
- Pandas
- Scikit-Learn
- Isolation Forest

---

## Project Structure

```text
log-anomaly-detector/
│
├── aiops_log_analysis.py    # Main anomaly detection script
├── system_logs.txt          # Input log file
└── README.md                # Project documentation
```

---

## Sample Log Format

The log file should follow the format below:

```text
2025-07-01 10:15:22 INFO User login successful
2025-07-01 10:18:45 WARNING High memory usage detected
2025-07-01 10:20:31 ERROR Database connection failed
2025-07-01 10:25:12 CRITICAL Server unavailable
```

---

# Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/ctej-codes/log-anomaly-detector.git
```

```bash
cd log-anomaly-detector
```

---

## 2. Create a Virtual Environment

### Windows

Create the virtual environment:

```powershell
python -m venv venv
```

Activate the environment:

```powershell
venv\Scripts\activate
```

---

### Linux/macOS

Create the virtual environment:

```bash
python3 -m venv venv
```

Activate the environment:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

### Option 1: Install Packages Directly

```bash
pip install pandas scikit-learn
```

### Option 2: Using requirements.txt (Recommended)

Create a `requirements.txt` file:

```text
pandas
scikit-learn
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Verify installation:

```bash
pip list
```

---

# Running the Script

Ensure that the `system_logs.txt` file is present in the project directory.

Execute the script:

```bash
python aiops_log_analysis.py
```

---

# Sample Output

<img width="1559" height="334" alt="image" src="https://github.com/user-attachments/assets/189a853a-b3e5-4194-8647-29dcac1e55b6" />


> **Note:** The Isolation Forest model identifies anomalies based on the selected features (log severity level and message length). An anomaly label does not necessarily indicate a system failure or security incident. Rather, it highlights log entries that differ significantly from the majority of records according to the model.

---

# How It Works

## Feature Engineering

The model derives the following features from each log entry:

| Feature | Description |
|----------|-------------|
| level_mapping | Numerical score assigned to log severity |
| message_length | Length of the log message |

### Log Severity Mapping

```python
{
    "INFO": 1,
    "WARNING": 2,
    "ERROR": 3,
    "CRITICAL": 4
}
``
