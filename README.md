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

## Useful commands

### Train a model

```
rasa train --data data --domain domain
```

### Talk to the bot

```
rasa inspect
```

### Run E2E tests

```
rasa test e2e e2e_tests/
```

More about e2e tests: https://rasa.com/docs/reference/testing/test-cases