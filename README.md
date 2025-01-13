# Health Advisory System

this repository contains all codes with video demo and a detail explaination presentation

## Step-by-Step Approach

### 1. Install WSL and Set Up Project Directory
- Install **WSL** on your system.
- Create a directory named `my_project` where all necessary files and Python scripts will be stored.

### 2. Create a Virtual Environment
- Inside the `my_project` directory, create a virtual environment and activate it.
- Install the required packages:
  ```bash
  pip install pathway gradio
  ```
- Create a Python file named `health_advisory_app.py` to contain the **Gradio frontend code**.

### 3. Simulate Data Generation
- Create a Python script named `simulate_data.py`.
- This script generates random data fields:
  - **Timestamp**
  - **Heartrate**
  - **Steps**
  - **Calories**
  - **Sleep hours**
- Save the generated data to a CSV file named `health_data.csv`.

### 4. Stream Data to the Website
- Create another Python file named `stream_data.py`.
- This script ensures data streams seamlessly to the website.

### 5. Connect Gradio and Pathway
- Create a Python file named `pathway_pipeline.py`.
- This script integrates **Gradio** with **Pathway**.

### 6. Clone the Pathway LLM-App Repository
- Clone the **Pathway LLM-App** repository to connect **RAG** (Retrieval-Augmented Generation) with **Pathway**.
  ```bash
  git clone <pathway-llm-app-repository-url>
  ```

### 7. Run the Application
- Execute the `health_advisory_app.py` file to launch the website:
  ```bash
  python health_advisory_app.py
  
