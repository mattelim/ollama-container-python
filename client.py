import json
import requests
import sys

# NOTE: ollama must be running for this to work, start the ollama app or run `ollama serve`
model = "llama3.2"  # TODO: update this for whatever model you wish to use

# llama3.2-vision:latest    
# qwen2.5-coder:latest       
# codellama:13b             
# llama3.2:latest           
# llama3.1:latest           
# llama3:latest   

available_models = ["llama3.2", "codellama", "qwen2.5-coder:7b", "qwen2.5-coder:32b", "llama3.2-vision"]      

IS_DEBUG = False

def printd(*args, **kwargs):
    if IS_DEBUG:
        print("\033[2mDEBUG_START >> ", *args, **kwargs, end="\n DEBUG_END >> \n\n\033[0m")

def chat(messages, model="llama3.2"):
    if model not in available_models:
        raise Exception(f"Model {model} not available. Available models: {available_models}")
    r = requests.post(
        "http://0.0.0.0:11434/api/chat",
        json={
            "model": model, 
            "messages": messages, 
            # "stream": True
            "stream": False
            },
	# stream=True
    )
    r.raise_for_status()
    # output = ""
    
    # for line in r.iter_lines():
    #     body = json.loads(line)
    #     if "error" in body:
    #         raise Exception(body["error"])
    #     if body.get("done") is False:
    #         message = body.get("message", "")
    #         content = message.get("content", "")
    #         output += content
    #         # the response streams one token at a time, print that as we receive it
    #         print(content, end="", flush=True)

    #     if body.get("done", False):
    #         message["content"] = output
    #         return message

    printd("r.content", r.content)
    body = json.loads(r.content)
    printd(body["message"]["content"])
    printd('body["message"]', body)
    return body


def main():
    messages = []
    try:
        printd("sysargv[1]:", sys.argv[1])
        is_remember = sys.argv[1] == "True"
    except:
        is_remember = False

    while True:
        user_input = input("Enter a prompt: ")
        if not user_input:
            exit()
        print()
        curr_message = {"role": "user", "content": user_input}
        if is_remember:
            messages.append(curr_message)
            printd("messages", messages)
            curr_response = chat(messages)
        else:
            curr_response = chat([curr_message])
        printd("curr_response", curr_response)
        if is_remember:
            messages.append(curr_response)
        print("\n\n")


if __name__ == "__main__":
    main()