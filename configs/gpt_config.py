import openai


def gpt_informations(prompt):

    openai.api_key = "YOURAPIKEY"
    model_engine = "text-davinci-002"

    completion = openai.Completion.create(
        engine=model_engine, 
        prompt=format(prompt), 
        max_tokens=1024, 
        n=1,stop=None,
        temperature=0.5)


    return completion