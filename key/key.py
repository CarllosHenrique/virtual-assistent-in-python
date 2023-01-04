import os

def get_gpt_key(): # https://beta.openai.com/account/api-keys    
    
    print("(To get your openai api key https://beta.openai.com/account/api-keys)")
    key = input("PASTE API KEY HERE: ")

    try:

        if os.stat('./key.txt').st_size == 0: 
            arquivo = open("key/key.txt", "w")
            arquivo.write(f"{key}")
        else:
            pass

    except FileNotFoundError:
        arquivo = open('key/key.txt', 'w')
        arquivo.write(f"{key}")
