import streamlit as st
import logging,sys,os
import openai
from dotenv import load_dotenv
from llama_index.agent import OpenAIAgent
from llama_index.llms import OpenAI
from llama_hub.tools.zapier.base import ZapierToolSpec

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

st.title('Github Archive Analysis :pencil2:')
sql_query=st.text_area('Enter your SQL query')
if sql_query:
    conn=st.experimental_connection('snowpark')
    df=conn.query(sql_query)
    st.write(df)
    st.line_chart(df,x="REPO_NAME",y="SUM_STARS")


top_repo=df.iloc[0,:]
#print(top_repo)
zapier_toolspec=ZapierToolSpec(api_key=os.getenv('ZAPIER_API_KEY'))

llm=OpenAI(model='gpt-3.5-turbo-0613')
agent=OpenAIAgent.from_tools(zapier_toolspec.to_tool_list(),verbose=True,llm=llm)
agent.chat(f"Send me an email on the details of {top_repo['REPO_NAME']},along with it's number of stars")
agent.chat(f"Quick add event to my Google calendar to check out {top_repo['REPO_NAME']} for September 2023")
