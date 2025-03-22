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

## Implementation
- **Continuous Learning:** Implemented using LangChain to allow ongoing learning and adaptation.
- **Multilingual Support:** The chatbot supports both Arabic and English conversations.
- **Optimized Training:** Various optimizations, including batch size tuning and memory management, were implemented for efficient training.

## Files & Documentation
- `t5-base.md`: Contains details about the training process and model performance.
- `parameter.md`: Documents selected hyperparameters and their impact.
- `chatbot_code.py`: The main chatbot implementation.

## Future Enhancements
- Improving model accuracy with additional fine-tuning.
- Enhancing the chatbot’s contextual understanding.
- Expanding multilingual support.

## How to Use
1. Install dependencies.
2. Load the pre-trained model.
3. Interact with the chatbot for mental health support.

For more details, refer to `t5-base.md` and `parameter.md`.

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

## Implementation
- **Continuous Learning:** Implemented using LangChain to allow ongoing learning and adaptation.
- **Multilingual Support:** The chatbot supports both Arabic and English conversations.
- **Optimized Training:** Various optimizations, including batch size tuning and memory management, were implemented for efficient training.

## Files & Documentation
- `t5-base.md`: Contains details about the training process and model performance.
- `parameter.md`: Documents selected hyperparameters and their impact.
- `chatbot_code.py`: The main chatbot implementation.

## Future Enhancements
- Improving model accuracy with additional fine-tuning.
- Enhancing the chatbot’s contextual understanding.
- Expanding multilingual support.

## How to Use
1. Install dependencies.
2. Load the pre-trained model.
3. Interact with the chatbot for mental health support.

For more details, refer to `t5-base.md` and `parameter.md`.

