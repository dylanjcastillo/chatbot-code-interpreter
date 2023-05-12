from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

from config import Paths


def get_prompt() -> ChatPromptTemplate:
    with open(Paths.prompts / "system.prompt") as f:
        system_template = f.read().strip()

    with open(Paths.prompts / "user.prompt") as f:
        human_template = f.read().strip()
        input_vars = ["query", "df_info"]

    return ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(system_template),
            HumanMessagePromptTemplate.from_template(human_template),
        ],
        input_variables=input_vars,
    )
