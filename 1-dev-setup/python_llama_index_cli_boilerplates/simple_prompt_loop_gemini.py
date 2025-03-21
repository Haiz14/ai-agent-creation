# NOTE: run pip install `llama-index-llms-google-genai==0.1.4` to actually run this script
"""
simple python script to run prompt loop from gemini

asks for a prompt from gemini, then prints the response. Doesn't remember previous conversations
"""
from os import getenv

from llama_index.llms.google_genai import GoogleGenAI

def ask_simple_prompt(llm: GoogleGenAI):
    prompt = input("What to ask to this helpful llm? Tell me the prompt: ")
    res = llm.complete(prompt=prompt)
    print(res)

def prompt_loop(llm: GoogleGenAI):
    while True:
        ask_simple_prompt(llm)

def init_llm(api_key: str | None = None):
    '''
    Initialize LLM, if api_key is not provided, it will try to read from GEMINI_API_KEY env var
    '''
    if not api_key:
        api_key = getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set. Pass api key at init or set GEMINI_API_KEY env var")
    return GoogleGenAI(api_key=api_key)

if __name__ == "__main__":
    llm = init_llm()
    prompt_loop(llm)

