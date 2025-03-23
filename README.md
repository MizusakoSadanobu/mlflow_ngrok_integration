# Overview
## Motivation
- Want to create a simple and low cost MLOps env

## Requiremets
- As a model developer, I want to manage experiment results and compare them. So I can find a suitable model config.
- As a team manager, I want to refer the experiment results by all members in a single view. So I can select a suitable model to implement.
- As a CICD developer, I want to have a model registory. So I can retrieve the identical model from any where.
- As a team manager, I do not want to use a paid service as much as possible. So I can save the team budget.
- As a team manager, I do not want anyone outside of the team to access our resources. So I can keep our invention private.

## Architecture
- **mlflow**: machine learning workflow manegemnt
- **google colab**: model development and experiment
- **google drive**: backend and model registory
- **central pc**: tracking server and proruction env
- **developer pc**: development env
- **ngrok**: enabling public access the mlflow ui hosted in local env
- **github / github actions**: code and CICD management

![image](doc/image/architecture.jpg)


## Limitation
- **ngrok** provides only one URL for a free plan

## Alternatives
- **DagsHub**: Has free plan but allows up to 100 runs
- **Databricks Communiy Edition**: Does not support remote option