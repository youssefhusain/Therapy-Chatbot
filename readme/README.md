# Mental Therapy Chatbot

## Overview
This project is a mental therapy chatbot designed to provide conversational support in both Arabic and English. The chatbot leverages a fine-tuned T5-base model trained on a specialized mental therapy dataset. The primary objective is to create a continuous and adaptive system using LangChain.

## Dataset
The dataset is sourced from Hugging Face:
[hf://datasets/vibhorag101/phr-mental-therapy-dataset-conversational-format/](hf://datasets/vibhorag101/phr-mental-therapy-dataset-conversational-format/)

- The dataset contains a collection of question-answer pairs related to mental therapy.
- Preprocessing was performed to clean and structure the data for effective training.

## Model
- **Base Model:** T5-base
- **Training:** The model was fine-tuned using the cleaned dataset.
- **Variable Selection:** Careful selection of parameters was done to optimize performance. Details can be found in `parameter.md`.

