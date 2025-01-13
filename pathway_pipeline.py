import pathway as pw

# Read real-time health data stream
data_stream = pw.io.read("health_data.csv", format="csv")

# Define logic for detecting anomalies or thresholds
data_stream = data_stream.with_columns(
    high_heart_rate=(data_stream.heart_rate > 90),
    low_steps=(data_stream.steps < 5000)
)

# Query RAG for recommendations based on heart rate and steps
def get_health_recommendation(row):
    health_data = f"My heart rate is {row['heart_rate']} and I have walked {row['steps']} steps today."
    recommendation = rag_pipeline.run(health_data)
    return recommendation

# Apply the function to the data stream
data_stream = data_stream.with_columns(
    recommendations=data_stream.apply(get_health_recommendation)
)

# Output the updated stream
pw.io.write(data_stream, format="console")
