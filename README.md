# WIP: Clickbait Spoiler Generation using GPT-3

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


### Example

**CLICKBAIT**:

A woman who interviewed over 100 people at Goldman Sachs says there's one question she always hoped candidates would ask her, but they never did


**ARTICLE**:

At some point toward the end of every job interview, the hiring manager will likely turn the tables and ask, "Do you have any questions for me?"
This is the time to ask smart, thoughtful questions — perhaps your final opportunity to assess whether the job would be a good fit, and your final chance to impress the hiring manager.
Business Insider recently spoke with Becca Brown, cofounder of Solemates, a brand of women's shoe-care products, who knows a thing or two about interviewing.
Before launching her own business, Brown, who has a bachelor's from Harvard University and an MBA from Columbia, spent a lot of time interviewing job candidates at Goldman Sachs, where she held various roles, including analyst, wealth adviser, and chief of staff.
She was also part of the investment bank's Harvard recruiting team, she says.
"I interviewed anywhere from 20 to 30 job candidates a year, so in total, I interviewed over 100 people at Goldman Sachs," she tells Business Insider.
She says that candidates asked her some impressive questions — like "What's the most challenging part of your job?" and "What's one of the most interesting projects you've worked on?" — but there was one question she always hoped she'd be asked, but almost never was: "Where do you see yourself in five years?"
"I like this question — and yet no one ever asked it — because it's difficult to answer," she says. "It's an important question for anyone to be asking him or herself, and so if ever a candidate were to ask this question, it would have stood out."
She continues:
I think this is a good question for interviewees to ask because, as a candidate, if you see where the person interviewing you is headed, you can decide if that trajectory is in line with your career objectives. While they don't have to be completely correlated, it's helpful for the candidate to have some indication of the interviewer's direction.
Get the latest Goldman Sachs stock price here.

###

**Expected Spoiler**: "Where do you see yourself in five years?";

**Spoiler Predicted**: "Where do you see yourself in five years?";

**Metrics**:
- Meteor: 0.9996243425995492;
- BLEU-4: 1.0;

## References

Hagen, M., Fröbe, M., Jurk, A., & Potthast, M. (2022). _Clickbait Spoiling via Question Answering and Passage Retrieval_ (arXiv:2203.10282). arXiv. http://arxiv.org/abs/2203.10282 \
Matthias Hagen, Maik Fröbe, Artur Jurk, & Martin Potthast. (2022). _Webis Clickbait Spoiling Corpus 2022_ (1.0.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.6362726
