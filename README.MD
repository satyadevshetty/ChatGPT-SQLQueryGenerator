<p align = "center"><img src = "./assets/database.jpg" height = 400 width = 400></p>

Generate SQL queries using Generative AI built with Python and Streamlit


## Tech Stack 💻

- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- Streamlit
- OpenAI GPT3

## Demo 👇

**v.0.0.1** - ([Sample SQL Schema & Query : customers & orders](./assets/example_tables_query.txt))

<p align = "center"><img src = "./assets/snapshots/example_query.PNG" height = 300 width = 600></p>



## Set-Up ⚒️

<p align = "center"><img src = "./assets/setup.gif" height = 300 alt = "SetUp Icon"></p>

- Ensure you have the latest stable version of [Python](https://www.python.org/downloads/) in your system

- Open your terminal / command prompt. 

- Clone the repository 
    ```
    git clone https://github.com/satyadevshetty/ChatGPT-SQLQueryGenerator.git
    ```
- Change the directory to the cloned project
    
    ```
    cd ChatGPT-SQLQueryGenerator
    ```

- Create a virtual environment

    ```
    python -m venv env
    ```

- Activate the virtual environment

    - Windows
        ```
         env/Scripts/Activate.ps1
        ```
    
    - Linux/Mac
        ```
        source env/bin/activate
        ```

- Check if the virtual environment in the concerned repository is used for python shell

    ```
    which python
    ```

- Upgrage `pip` package manager

    ```
    python -m pip install --upgrade pip
    ```

- Install the dependencies

    ```
    pip install -r requirements.txt
    ```

- Sign Up for OpenAI API, Go to Settings and Get the API Key


- Load the application

    ```
    streamlit run ./Home.py
    ```

- If the app does not load by itself in your default browser, open a browser of your choice and navigate to  `http://localhost:8501`

- To stop the application, press `CTRL + C` in your terminal

- To deactive the python environment, type in your terminal

    ```
    deactivate
    ```


## Acknowledgements 🙏


- **Open AI GPT-3 Text Completion Model**: [OpenAI GPT3](https://openai.com) 
    - [Documentation](https://beta.openai.com/docs/)
    - [Playground](https://beta.openai.com/playground)
- **Animations**: [LottieFiles](https://lottiefiles.com)
