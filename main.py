from gemini import GeminiAI

model_name = "gemini-pro"
your_ai = GeminiAI(model_name=model_name)

def response(input):
    return your_ai.generate_response(input_text=input)



if __name__ == "__main__":
    input = "how are you today?"
    print(response(input))


# https://ai.google.dev/tutorials/python_quickstart


