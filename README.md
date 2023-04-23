# Clickbait Spoiler Generation using GPT-3

This repository contains code for fine-tunning and  generating clickbait spoilers using GPT-3.

### Installation with Pipenv

This project also includes a Pipfile and Pipfile.lock for managing dependencies with Pipenv. If you prefer to use Pipenv, you can follow the steps below:

1. Clone the repository to your local machine:
```bash
git clone https://github.com/Daniel-EST/clickbait-spoilers
```

2. Navigate to the project directory
```bash
cd clickbait-spoilers
```

3. Install Pipenv
```bash
pip install pipenv
```

4. Install the required packages
```bash
pipenv install
```
This will install all the required packages in a virtual environment managed by Pipenv.

5. Activate the virtual environment:
```bash
pipenv shell
```

This will activate the virtual environment, allowing you to run the scripts with the correct dependencies.

### Environment Variables

Before using the clickbait spoiler generation script, you will need to set the following environment variables:

- **`ORGANIZATION_KEY`**: This is the key of the OpenAI organization you are using. You can find this key in the OpenAI dashboard under "Settings".
- **`OPENAI_API_KEY`**: This is your personal API key for OpenAI. You can generate this key in the OpenAI dashboard under "API Keys".

To set these environment variables, you can add the following lines to your .bashrc or .bash_profile file:

```bash
export ORGANIZATION_KEY=<your_organization_key>
export OPENAI_API_KEY=<your_api_key>
```