## Pythor assistant

A personal assistant I created using ChatGPT (OpenAI api) and some Python libraries is called the Pythor Assistant.

### built

* [Python3](https://www.python.org/)
* [Speech recognition](https://pypi.org/project/SpeechRecognition/)
* [Os](https://pypi.org/project/os/)
* [pyttsx3](https://pypi.org/pyttsx3/os/)


### How the api key works

When running the program ```main.py``` in the terminal, the user will be prompted for the api key that was made available on the [openai](https://beta.openai.com/account/api-keys) website after logging in.
Once you have access to the key, copy it and paste it into your terminal to enable the bot's research access.
The api key will be created in the ```key/``` directory, where it can be found as ```key.txt``` and inside the key that the bot is using.

( The code I created that is used in the file ```key.py``` is very simple, in short, it first checks to see if the file exists before performing an mb count.
Try to determine whether the file has 0 megabits or is otherwise empty; if so, copy the content that the key contains; if not, pass.
If the document is missing, create a ```key.txt``` file in the ```key/``` directory using the already written api key.)


### Code

* ```Gpt_config.py``` - These are the settings and components that the bot uses for the search, which also includes key filtering.
* ```voice.py``` - Configurations on the voice that are presented as a research result, if you don't like them, you can choose to remove.
* ```test.py``` - The file where i make my test with python libraries before put in main code.
* ```main.py``` - Main file


### installation

1. clone the repo
   ```sh
   git clone 
   ```
2. install dependencies
   ```sh
   python main.py
   ``` 
## contributing
1. fork the project
2. create your feature branch 
```sh
git checkout -b feature/AmazingFeature
```
3. commit your changes
```sh
git commit -m 'Add some AmazingFeature'
```
4. push to the branch 
```sh
git push origin feature/AmazingFeature
```
5. open a pull request
