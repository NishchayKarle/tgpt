# TGPT - ChatGPT on the terminal

### Example usage
![Ex1](./tgpt%20ex1.png)
![Ex2](./tgpt%20ex2.png)
![Ex3](./tgpt%20ex3.png)

---

### Usecase
+ I wrote this app for the purpose of quickly accessing ChatGPT without the need to open a browser. As a result, it does not support ongoing conversations. 
+ It can be a time-saving tool for googling information while you are working.

---

### Install

+ **STEP 1**: Add OpenAI API key to the environment. (OpenAI API Key can be created [here](https://platform.openai.com/api-keys))

    ```echo "export OPENAI_API_KEY=<your_api_key>" >> ~/.zshrc```

    or

    ```echo "export OPENAI_API_KEY=<your_api_key>" >> ~/.bashrc```

    Quit and re-open the terminal.

+ **STEP 2**: Clone this repository and open it.

    ```git clone https://github.com/NishchayKarle/tgpt.git```

    ```cd tgpt```

+ **STEP 3**: Run install script

    ```./install.sh```

DONE!

---


### Uninstall
+ Run ```./clean.sh```
