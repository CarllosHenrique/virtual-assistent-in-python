import openai
import os

def get_gpt_key(): # https://beta.openai.com/account/api-keys    
    
    print("(To get your openai api key https://beta.openai.com/account/api-keys)")
    key = input("PASTE API KEY HERE: ")

    try:

        if os.stat('key/key.txt').st_size == 0: 
            arquivo = open("key/key.txt", "w")
            arquivo.write(f"{key}")
        else:
            pass

    except FileNotFoundError:
        arquivo = open('key/key.txt', 'w')
        arquivo.write(f"{key}")



def gpt_informations(prompt):

    arquivo = open("key/key.txt", "r")
    ki = arquivo.readline()

    openai.api_key = f"{ki}"

    model_engine = "text-davinci-002"

    completion = openai.Completion.create(
        engine=model_engine, 
        prompt=format(prompt), 
        max_tokens=1024, 
        n=1,stop=None,
        temperature=0.5)


    return completion
