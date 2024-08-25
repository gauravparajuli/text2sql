from dotenv import load_dotenv
import streamlit as st
import sqlite3
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

# function to retrieve data from the database
def read_sql_query(sql, db):
    print(sql)
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    rows = cursor.execute(sql)
    # for row in rows:
    #     print(row)
    return rows

model = ChatOpenAI(model='gpt-4o-mini')

system_prompt = """
You are an expert in converting English questions to SQL code!
the sql database consists of table 'student' which has columns
'name', 'class' and 'section'.

Example 1:
Input: How many entries of records are present?
Output: SELECT COUNT(*) FROM student;

Example 2:
Input: List all the students in the frontend class.
Output: SELECT * FROM student WHERE class='frontend';

also, sql code should not have ``` in neither beginning nor end.

also, if given query cannot be converted to sql, return 
"Given query cannot be converted to SQL"
"""

prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system', system_prompt),
        ('human', '{input}')
    ]
)

chain = prompt_template | model | StrOutputParser()

# Streamlit app
st.set_page_config(
    page_title='I will retrieve any SQL query'
)
st.header('Retrieve SQL data in plain English')

question = st.text_input(label='Query the database', placeholder='Enter your query in plain english here')
submit = st.button('Query')

if submit:
    if question:
        sql = chain.invoke({'input': question})
        st.subheader('Generated SQL')
        st.write(sql)
        result = read_sql_query(sql, 'student_records.db')
        st.subheader('Retrieved Data')
        for row in result:
            st.write(row)