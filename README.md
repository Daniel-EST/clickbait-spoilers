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

### Model Evaluation

In order to evaluate the performance of our model, we used three popular metrics: Meteor, BLEU-4, and BERTscore. The results are as follows:

- Meteor: 0.3958
- BLEU-4: 0.3085
- BERTscore Mean F1: 0.8931


### Example

You can find all the predicted data in the following folders:

- `./data/results/test.txt`
- `./data/results/validation.txt`

For example, you can check the predicted results for the test dataset in the file test.txt and the predicted results for the validation dataset in the file validation.txt. By analyzing these predicted results, you can gain insights into how well the model is performing and identify areas for improvement.

---

**CLICKBAIT:**

J.J. Abrams has an answer on if there will be a post-credits scene in the new 'Star Wars'


**ARTICLE:**

In the modern blockbuster world, post-credits scenes have become very popular. The films made by Marvel Studios are arguably best known for it, but fun stingers have also been found in the "X-Men" franchise movies as well as the latest "Terminator." Because of this, some have wondered if this could be something new for the "Star Wars" series as well... but now J.J. Abrams has definitely put an end to that conversation.
The subject came up when Abrams was on stage for a "Star Wars: The Force Awakens" press conference held today in Los Angeles. The filmmaker was directly asked if fans can expect to see a post-credits scene or Easter Egg at the end of the sequel, and he quickly dismissed the idea, saying:
"No, there’s not. All the scenes are actually in the movie."
Those of you who have been following updates and stories about "Star Wars: The Force Awakens" for a while will note that this dispels a rumor that has been going around for the last few months. Back in September it was rumored that the latest saga film would actually be teasing the first "Star Wars" story, "Rogue One." This made a degree of sense, given that the Gareth Edwards-directed feature has been filming since this past summer, and will surely have a good amount of footage ready by the time "Force Awakens" arrives in theaters. Now it sounds like that post-credits scene definitely isn’t happening – so instead maybe we can just expect the blockbuster to come with a trailer for the eighth live-action "Star Wars" movie during the coming attractions.
Post-credits scenes are definitely fun for fans, and a good incentive to get people to stick around and watch the credits – but I can’t say that I’m too upset that "Star Wars: The Force Awakens" won’t have one. After all, they aren’t exactly part of the franchise’s tradition (none of the previous movies have stingers), and it’s not a device that has to be used all over Hollywood. If everything the movie has to say can be fit between the opening scrawl and the end credits, more power to it.
Surely there will be some fans who will be disappointed by this news, but hopefully they’ll all get over it fairly quickly. After all, the feelings about the lack of a post-credits scene should be drowned out by the excitement that comes with the fact that we’re now less than two weeks away from the theatrical release of "Star Wars: The Force Awakens." As always, stay tuned for more about the movie, including our on-camera interviews with the cast and J.J. Abrams!

---

**Expected Spoiler:**
All the scenes are actually in the movie

**Predicted Spoiler:**
No

## TODO
- Compare with other models (BERT);
- Consider training the model with a more robust algorithm like Curie or Babbage


## References

Hagen, M., Fröbe, M., Jurk, A., & Potthast, M. (2022). _Clickbait Spoiling via Question Answering and Passage Retrieval_ (arXiv:2203.10282). arXiv. http://arxiv.org/abs/2203.10282 \
Matthias Hagen, Maik Fröbe, Artur Jurk, & Martin Potthast. (2022). _Webis Clickbait Spoiling Corpus 2022_ (1.0.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.6362726
