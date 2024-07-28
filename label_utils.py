from langchain.prompts import PromptTemplate
from prompt import label_prompt
from llm_utils import DouBaoClient
from env_fri_words import env_fri_words

debug = False
env_fri_words = env_fri_words
label_prompt = label_prompt
if debug:
    print(label_prompt)
    print(env_fri_words)
    

class LabelUtils:
    """
    用于对文本进行标签化的工具类
    """
    def __init__(self):
        self.client = DouBaoClient()
        self.env_fri_words = env_fri_words

    def label(self, raw_text):
        prompt = PromptTemplate(template=label_prompt, input_variables=["env_fri_words", "raw_text"])
        final_prompt = prompt.format(env_fri_words=self.env_fri_words, raw_text=raw_text)
        label_text = self.client.get_standard_response("", final_prompt)
        return label_text


if __name__ == '__main__':
    label_utils = LabelUtils()
    labeled_text = label_utils.label("环保非常重要")
    print(labeled_text)


