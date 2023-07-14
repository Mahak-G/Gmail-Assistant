import openai
import gradio
openai.api_key= "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"

messages = [{"role": "system", "content": "You are a gmail assistant"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Gmail Assistant")

demo.launch(share=True,enable_queue=True)