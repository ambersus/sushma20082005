from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Initialize the LLM (for generating recommendations)
llm = OpenAI(model="text-davinci-003")

# Create the RAG pipeline
rag_pipeline = RetrievalQA.from_chain_type(
    llm=llm, retriever=vector_store.as_retriever()
)

# Example user input (health data)
health_data = "My heart rate is high and I have only walked 3000 steps today."

# Get the relevant advice
response = rag_pipeline.run(health_data)
print(response)
