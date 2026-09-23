from transformers import AutoTokenizer

# -------------------------------------------------
# 1. Load a pretrained tokenizer
# -------------------------------------------------

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")


# -------------------------------------------------
# 2. Input text
# -------------------------------------------------

text = "I love machine learning and artificial intelligence."


# -------------------------------------------------
# 3. Text -> Tokens
# -------------------------------------------------

tokens = tokenizer.tokenize(text)

print("TOKENS:")
print(tokens)


# -------------------------------------------------
# 4. Tokens -> Token IDs
# -------------------------------------------------

token_ids = tokenizer.convert_tokens_to_ids(tokens)

print("\nTOKEN IDs:")
print(token_ids)


# -------------------------------------------------
# 5. Directly encode complete text
#    This also adds special tokens like [CLS] and [SEP]
# -------------------------------------------------

encoded = tokenizer.encode(text)

print("\nENCODED TOKEN IDs:")
print(encoded)


# -------------------------------------------------
# 6. Convert encoded IDs back to tokens
# -------------------------------------------------

encoded_tokens = tokenizer.convert_ids_to_tokens(encoded)

print("\nENCODED TOKENS:")
print(encoded_tokens)


# -------------------------------------------------
# 7. Decode Token IDs -> Text
# -------------------------------------------------

decoded_text = tokenizer.decode(encoded)

print("\nDECODED TEXT:")
print(decoded_text)


# -------------------------------------------------
# 8. Get complete model-ready input
# -------------------------------------------------

model_input = tokenizer(
    text,
    return_tensors="pt",
    padding=True,
    truncation=True
)

print("\nMODEL INPUT:")
print(model_input)


# -------------------------------------------------
# 9. Important values
# -------------------------------------------------

print("\nINPUT IDs:")
print(model_input["input_ids"])

print("\nATTENTION MASK:")
print(model_input["attention_mask"])


# -------------------------------------------------
# 10. Token-by-token mapping
# -------------------------------------------------

print("\nTOKEN -> TOKEN ID")

for token, token_id in zip(encoded_tokens, encoded):
    print(f"{token:15} -> {token_id}")
