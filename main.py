# Import Dependencies
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import nltk
import numpy as np
from nltk.corpus import treebank
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


app = FastAPI()
model = load_model('model_2.keras')
nltk.download('treebank')

# Load the dataset
sentences = treebank.sents()
corpus = [' '.join(sentence) for sentence in sentences]
tokenizer = Tokenizer()
tokenizer.fit_on_texts(corpus)

# Create input sequences
input_sequences = []
for line in corpus:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i + 1]
        input_sequences.append(n_gram_sequence)
max_sequence_length = max(len(x) for x in input_sequences)

class PredictionRequest(BaseModel):
    text: str

@app.post("/predict")
def predict(request: PredictionRequest):
    # Prepare the input text
    input_text = request.text
    input_sequence = tokenizer.texts_to_sequences([input_text])[0]
    input_sequence = pad_sequences([input_sequence], maxlen=max_sequence_length - 1, padding='pre')

    # Predict the next word
    predicted = model.predict(input_sequence, verbose=0)
    predicted_word_index = np.argmax(predicted, axis=-1)[0]
    predicted_word = tokenizer.index_word[predicted_word_index]

    return {"predicted_word": predicted_word}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
