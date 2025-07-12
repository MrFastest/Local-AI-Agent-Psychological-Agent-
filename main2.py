from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector2 import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are an empathetic mental health assistant.

Here are some real-world text samples related to human emotions and thoughts: {reviews}
Now, based on these examples, please answer the following emotional or psychological question:

{question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    print("\n\n-------------------------------")
    question = input(" How may I Assist you , Ask any psychological question (q to quit): ")
    print("\n\n")
    if question.strip().lower() == "q":
        break

    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    print("\nResponse:\n", result)


#How to run this file
#Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
#.\venv\Scripts\Activate.ps1
# python main2.py