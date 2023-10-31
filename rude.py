import openai
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts.chat import SystemMessage, HumanMessagePromptTemplate

openai.api_key = os.getenv("OPENAI_API_KEY")

template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                "You are a mean girl that re-writes the user's text to "
                "sound rude."
            )
        ),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)

llm = ChatOpenAI()
message = input("Send a message: ")
res = llm(template.format_messages(text=message))
print(res.content)