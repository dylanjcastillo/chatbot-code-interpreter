# Chatbot Code Interpreter

This is a simple app meant to replicate some of the code interpreter capabilities of ChatGPT: it's a chatbot capable of running Python code on the browser. I created because I wanted to analyze and visualize data by "chatting" with it in plain English (see [deepshet](https://deepsheet.dylancastillo.co/))
 
If you're curious, check out the step-by-step [tutorial](https://dylancastillo.co/code-interpreter-chatbot-pyodide-langchain-openai/).

## Development

1. Install [Python 3.10](https://www.python.org/downloads/).
2. Install [Poetry](https://python-poetry.org/docs/#installation).
4. From the root folder of the project, install the dependencies:
   ```
   poetry config virtualenvs.in-project true
   poetry install
   ```
5. Update .env-example with your OpenAI secret key and save it as `.env`
6. To start the app, open a terminal in `src/app` and run `litestar run --reload --debug`
7. Go to `http://127.0.0.1`.

## Screenshots

The app looks like this:

<img src="https://github.com/dylanjcastillo/chatbot-code-interpreter/assets/7218756/bcc56ab2-15d6-4151-9899-bcfec9a0c37c" width="500">

## License

MIT.
