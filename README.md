# Clickbait Spoiler Generation using GPT-3

This repository contains code for fine-tuning and generating clickbait spoilers using GPT-3.

### Installation with Pipenv

This project includes a Pipfile and Pipfile.lock for managing dependencies with Pipenv. If you prefer to use Pipenv, you can follow the steps below:

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
This repository contains code that uses the OpenAI API to interact with your organization's OpenAI instance. 
Before using the clickbait spoiler generation script, you will need to set the following environment variables:

- **`ORGANIZATION_KEY`**: This is the key of the OpenAI organization you are using. You can find this key in the OpenAI dashboard under "Settings".
- **`OPENAI_API_KEY`**: This is your personal API key for OpenAI. You can generate this key in the OpenAI dashboard under "API Keys".

#### Setting up Environment Variables on Terminal

You can add the following lines to your **`.bashrc`** or **`.bash_profile`** file:

```bash
export ORGANIZATION_KEY=<your_organization_key>
export OPENAI_API_KEY=<your_api_key>
```

#### Setting up the environment variable file

To set up the environment variable file, you can create a file called **`.env`** in the root of the repository. You can use the **`.env.example`** file as a template for the **`.env`** file.

The **`.env.example`** file contains the following variables:
```
ORGANIZATION_KEY=<your_organization_key>
OPENAI_API_KEY=<your_api_key>
```
You will need to replace **`<your_organization_key>`** and **`<your_api_key>`** with your actual organization key and API key, respectively.

## References

Hagen, M., Fröbe, M., Jurk, A., & Potthast, M. (2022). _Clickbait Spoiling via Question Answering and Passage Retrieval_ (arXiv:2203.10282). arXiv. http://arxiv.org/abs/2203.10282 \
Matthias Hagen, Maik Fröbe, Artur Jurk, & Martin Potthast. (2022). _Webis Clickbait Spoiling Corpus 2022_ (1.0.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.6362726