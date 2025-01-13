import pathway as pw

# Step 1: Read the input CSV file
data_stream = pw.io.read(
    path="health_data.csv",  # Path to your data source
    format="csv",
    schema={
        "timestamp": pw.ColumnType.STRING,
        "heart_rate": pw.ColumnType.INT,
        "steps": pw.ColumnType.INT,
        "calories": pw.ColumnType.INT,
        "sleep_hours": pw.ColumnType.FLOAT,
    }
)

# Step 2: Add insights based on thresholds
data_stream = data_stream.with_columns(
    high_heart_rate=(data_stream.heart_rate > 140),
    low_steps=(data_stream.steps < 5000),
    insights=pw.if_else(
        data_stream.high_heart_rate,
        "Your heart rate is high. Take a break.",
        pw.if_else(
            data_stream.low_steps,
            "You need more steps to meet your goal!",
            "All metrics look good. Keep it up!"
        )
    )
)

# Step 3: Write processed data to JSON
pw.io.write(
    data_stream,  # Processed data
    path="processed_data.json",  # Output file
    format="json",  # Output format
    mode="overwrite"  # Overwrite the file on updates
)

# Run the Pathway pipeline
pw.run()