from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# Model load (flan-t5-small)
model_name = "google/flan-t5-small"

# Pipeline
chatbot = pipeline("text2text-generation", model=model_name)

# Ask function
def ask_health_bot(query):
    prompt = f"Answer this health query: {query}"
    response = chatbot(prompt, max_length=100, do_sample=True)
    return response[0]['generated_text']
