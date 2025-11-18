# Finance Banking Agent Template

A lightweight banking conversational agent template for the fictional **Fenlo Bank** that handles account management, card services, and money transfers.

This bot is from [Hello Rasa](https://hello.rasa.ai/).

**Important** This is configured to use OpenAI models. See [config.yml](config.yml)

Use with Rasa-Pro 3.13

## 🚀 What's Included

This template provides a banking assistant with:

- **Account Management**: Balance checking and statement downloads
- **Card Services**: Card activation, blocking, replacement, and listing  
- **Money Transfers**: Account-to-account transfers and third-party payments
- **Contact Management**: Add, list, and remove trusted contacts
- **Bill Management**: Bill payment reminders and scheduling
- **Banking Knowledge**: FAQ system with Fenlo Bank documentation

## 📁 Directory Structure

```
├── actions/         # Custom Python logic for banking operations
├── data/            # Banking conversation flows and training data
├── domain/          # Banking agent configuration
├── db/              # Mock JSON database for testing
├── docs/            # Fenlo Bank knowledge base and FAQ documents
└── config.yml       # Training pipeline configuration
```

### Installation

Prerequisites:
- Rasa Pro license
- Python - supported Python versions: `>=3.10.0,<3.14`. For example, you can use [pyenv](https://github.com/pyenv/pyenv) to install Python 3.11.11: `pyenv install 3.11.11`

After you cloned the repository, follow these installation steps:

1. Navigate to the cloned repo:
   ```bash
   cd lena-hello-rasa
   ```

2. Set up the Python environment with `pyenv` or any other tool that manages Python versions:
   ```bash
   pyenv virtualenv 3.11.11 hello-rasa  # create a virtual environment
   pyenv activate hello-rasa             # activate your virtual environment
   pyenv local hello-rasa                # set auto-activation for this directory
   ```

3. Install the dependencies using `uv`:
   ```bash
   pip install uv
   uv pip install -r requirements.txt
   ```

4. Create an environment file `.env` in the root of the project with the following 
   content:
   ```bash
   RASA_PRO_LICENSE=<your rasa pro license key>
   OPENAI_API_KEY=<your openai api key>
   ```

## Useful commands

### Train a model

```commandline
rasa train --data data --domain domain
```

### Talk to the bot

GUI-based interaction using Rasa inspector:

```commandline
rasa inspect
```

### Run E2E tests

```commandline
rasa test e2e e2e_tests/
```

More about e2e tests: https://rasa.com/docs/reference/testing/test-cases