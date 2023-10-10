from transformers import AutoModelForXXX, AutoTokenizer

# Replace 'model_name' with the name of the model you want to download
model_name = "llama-2-7b-chat.ggmlv3.q8_0.bin"

# Initialize the model and tokenizer
model = AutoModelForXXX.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)



# Save the model and tokenizer to your GitHub repository
model.save_pretrained("model")
tokenizer.save_pretrained("model")