import spacy
# Load the English language model
nlp = spacy.load("en_core_web_sm")
# Example sentence
sentence = "The really quick brown fox jumps over the lazy dog."
# Process the sentence
doc = nlp(sentence)
# Print dependency parsing results
for token in doc:
    print(f"{token.text:10} | {token.dep_:15} | {token.head.text}")