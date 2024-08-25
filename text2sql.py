from dotenv import load_dotenv
import streamlit as st
import sqlite3
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system', 'you are a helpful personal assistant'),
        ('human', '{query}')
    ]
)

chain = prompt_template | model | StrOutputParser()

result = chain.invoke(dict(query='what is the capital of Nepal?'))

print(result)