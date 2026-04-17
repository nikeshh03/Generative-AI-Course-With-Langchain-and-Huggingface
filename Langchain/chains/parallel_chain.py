from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatOpenAI(
                model = 'openai/gpt-4o-mini',
                base_url = 'https://openrouter.ai/api/v1'
)

llm = HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.1-8B-Instruct',
    task="text-generation"
)

model2 = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template = "Genrate short and simple notes from the following text \n {text}",
    input_variables = ['text']
)

prompt2 = PromptTemplate(
    template = "Genrate 5 short question answers from the following text \n {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document \n notes-> {notes} and quiz -> {quiz}",
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes' : prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
This project report details the development of an Image Caption Generator, a sophisticated system designed to automatically generate descriptive textual captions for given input images. Leveraging the power of supervised deep learning techniques, this system addresses the growing demand for automated image understanding and description across various applications, including accessibility for visually impaired individuals, content indexing, and intelligent search. The core architecture integrates a Convolutional Neural Network (CNN) for robust image feature extraction and a Recurrent Neural Network (RNN), specifically an Long Short-Term Memory (LSTM) network, for sequential caption generation. The model is trained on large-scale datasets comprising image-caption pairs, enabling it to learn complex mappings between visual content and linguistic descriptions. This report outlines the problem statement, project objectives, the necessity of such a system, and its scope. It further delves into the theoretical foundations of deep learning architectures pertinent to image captioning, details the software and hardware requirements, and provides a comprehensive overview of the implementation methodology, including data preprocessing, model training, and evaluation metrics. Finally, a pseudo-code representation of the core algorithm is presented, followed by a conclusion summarizing the project's achievements and potential future enhancements. The successful implementation of this project demonstrates the efficacy of supervised learning in bridging the semantic gap between visual and textual modalities.

"""

result = chain.invoke({'text': text})

print(result)

chain.get_graph().print_ascii()