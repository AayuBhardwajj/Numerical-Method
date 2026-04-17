import json
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.cluster import KMeans

# ------------------ LOAD DATA ------------------
def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# ------------------ DOMAIN CLEANING ------------------
def extract_domain(url):
    if url.startswith("idle://"):
        return "idle"

    try:
        return url.split("//")[-1].split("/")[0].replace("www.", "")
    except:
        return "unknown"

# ------------------ PREPROCESS ------------------
def preprocess(data):
    records = []

    for key, value in data.items():
        if key == "historyData":
            continue

        date = key
        sessions = value.get("sessions", [])

        for s in sessions:
            try:
                records.append({
                    "date": date,
                    "start": datetime.fromtimestamp(s["startTime"] / 1000),
                    "duration": s["duration"],
                    "active": s["isActive"],
                    "domain": extract_domain(s["url"])
                })
            except:
                continue

    df = pd.DataFrame(records)

    if df.empty:
        print("No valid session data found.")
        return df

    df["hour"] = df["start"].dt.hour
    return df

# ------------------ PRODUCTIVITY PATTERN ------------------
def productivity_pattern(df):
    active_df = df[df["active"] == True]

    if active_df.empty:
        return None, None, None

    hourly = active_df.groupby("hour")["duration"].sum()

    best = hourly.idxmax()
    worst = hourly.idxmin()

    return best, worst, hourly

# ------------------ WEBSITE CLASSIFICATION ------------------
def classify_websites(df):
    grouped = df.groupby("domain").agg({
        "duration": "sum",
        "active": "sum"
    })

    grouped["focus_ratio"] = grouped["active"] / grouped["duration"]

    def tag(x):
        if x > 0.7:
            return "productive"
        elif x < 0.4:
            return "distracting"
        return "neutral"

    grouped["tag"] = grouped["focus_ratio"].apply(tag)

    return grouped.sort_values(by="duration", ascending=False)

# ------------------ FOCUS SCORE ------------------
def focus_score(df):
    total = df["duration"].sum()
    active = df[df["active"] == True]["duration"].sum()

    focus_ratio = active / total if total else 0

    daily = df.groupby("date")["duration"].sum()
    consistency = 1 / (1 + np.std(daily)) if len(daily) > 1 else 1

    avg_session = df["duration"].mean()

    score = (
        (focus_ratio * 0.5) +
        (consistency * 0.3) +
        (min(avg_session / 1800, 1) * 0.2)
    ) * 100

    return round(min(max(score, 0), 100), 2)

# ------------------ ANOMALY DETECTION ------------------
def detect_anomalies(df):
    anomalies = []

    daily = df.groupby("date")["duration"].sum()

    if len(daily) < 2:
        return anomalies

    avg = daily.mean()
    std = daily.std()

    today = daily.iloc[-1]

    if today > avg + 2 * std:
        anomalies.append("High usage spike detected")

    elif today < avg - 2 * std:
        anomalies.append("Low activity detected")

    return anomalies

# ------------------ CLUSTERING ------------------
def clustering(df):
    features = df.groupby("domain").agg({
        "duration": "sum",
        "active": "sum"
    })

    if len(features) < 2:
        return None

    kmeans = KMeans(n_clusters=2, random_state=0, n_init=10)
    features["cluster"] = kmeans.fit_predict(features)

    return features

# ------------------ INSIGHTS ------------------
def generate_insights(df):
    insights = []

    best, worst, _ = productivity_pattern(df)
    score = focus_score(df)
    anomalies = detect_anomalies(df)
    sites = classify_websites(df)

    if best is not None:
        insights.append(f"Most productive hour: {best}:00 - {best+1}:00")

    if score > 75:
        insights.append("Strong focus consistency")
    elif score < 40:
        insights.append("Focus needs improvement")

    distracting = sites[sites["tag"] == "distracting"]

    if not distracting.empty:
        worst_site = distracting.index[0]
        insights.append(f"Reduce time on {worst_site}")

    insights.extend(anomalies)

    return insights[:5]

# ------------------ MAIN ------------------
def main():
    data = load_data("data.json")
    df = preprocess(data)

    if df.empty:
        print("No data to analyze.")
        return

    print("\n===== ANALYTICS REPORT =====\n")

    best, worst, _ = productivity_pattern(df)

    if best is not None:
        print(f"Most productive hour: {best}:00 - {best+1}:00")
        print(f"Least productive hour: {worst}:00 - {worst+1}:00\n")

    print("Focus Score:", focus_score(df), "\n")

    print("Website Classification:\n")
    print(classify_websites(df), "\n")

    print("Anomalies:", detect_anomalies(df), "\n")

    print("Insights:")
    for ins in generate_insights(df):
        print("-", ins)

    print("\nClustering (ML):\n")
    print(clustering(df))


# ------------------ RUN ------------------
if __name__ == "__main__":
    main()