from langchain.llms import CTransformers
import os


def load_model(model_path=os.path.join(os.path.split(__file__)[0], 'llm_model')):
    config = {'max_new_tokens': 256, 'repetition_penalty': 1.1, 'temperature': 0.2, 'context_length': 1000}

    llm = CTransformers(model=model_path, model_file="zephyr-7b-beta.Q4_K_M.gguf", model_type="mistral", config=config)

    return llm, config


def prompt_template(context):
    template = f"""context: {context} Given the above context classify it among the classes:  digestive system
    diseases, cardiovascular diseases, neoplasms, nervous system diseases, general pathological conditions.Act as a
    medical assistant to give the answer.Give your answer in single word as mentioned as classes name. """
    return template


def result(context):
    llm, config = load_model()
    prompt = prompt_template(context)
    output = llm(prompt)
    return output