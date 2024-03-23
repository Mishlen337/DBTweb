import os
# from transformers import pipeline


MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = int(os.getenv("MONGO_PORT"))
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_BASE = os.getenv('MONGO_BASE')

token = os.getenv("TOKEN")

# recommendation_pipe = pipeline("text-classification", model="nebiyu29/fintunned-v2-roberta_GA", device='cpu')
# translation_pipe = pipeline("text-classification", model="nebiyu29/fintunned-v2-roberta_GA", device='cpu')