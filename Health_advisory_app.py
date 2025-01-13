import gradio as gr
import pathway as pw

# Function to generate health recommendations
def health_advisory(heart_rate, steps, calories, sleep_hours):
    recommendations = []
    if heart_rate > 90:
        recommendations.append("⚠️ Your heart rate is high. Take a rest or stay hydrated.")
    if steps < 5000:
        recommendations.append("🚶‍♂️ You need to walk more to meet your daily step goal of 10,000 steps!")
    if calories < 1200:
        recommendations.append("🔥 Your calorie burn is low. Consider some light exercise or a brisk walk.")
    if sleep_hours < 7:
        recommendations.append("😴 You haven't slept enough. Aim for at least 7-8 hours of sleep.")
    
    if not recommendations:
        return "✅ You're doing great! Keep it up! 💪"
    return "\n".join(recommendations)

# Create the Gradio interface using blocks
with gr.Blocks() as app:
    # Title and Introduction
    gr.Markdown("## 🩺 Health Advisory System")
    gr.Markdown("Enter your daily health metrics to receive personalized advice for a healthier lifestyle!")

    # Input Section
    with gr.Row():
        heart_rate = gr.Number(label="Heart Rate (BPM)", value=75)
        steps = gr.Number(label="Steps Taken Today", value=4000)
    with gr.Row():
        calories = gr.Number(label="Calories Burned", value=1000)
        sleep_hours = gr.Number(label="Sleep Hours", value=6)
    
    # Output Section
    output = gr.Textbox(label="Health Advisory", lines=5)
    submit = gr.Button("Get Advisory")
    
    # Button Action: Process input and show output
    submit.click(
        fn=health_advisory, 
        inputs=[heart_rate, steps, calories, sleep_hours], 
        outputs=output
    )
    
    # Footer
    gr.Markdown("### Stay healthy and keep moving! 🚀")

# Launch the app with sharing enabled
app.launch(share=True)
