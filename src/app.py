from dataclasses import dataclass
from pathlib import Path

from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from litestar import Litestar, MediaType, Request, Response, get, post
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.enums import RequestEncodingType
from litestar.params import Body
from litestar.response_containers import Template
from litestar.static_files.config import StaticFilesConfig
from litestar.template.config import TemplateConfig
from typing_extensions import Annotated

from config import OpenAI
from utils import get_prompt

chain_create = LLMChain(
    llm=ChatOpenAI(
        temperature=0,
        model_name=OpenAI.model_name,
        openai_api_key=OpenAI.secret_key,
        request_timeout=120,
    ),
    prompt=get_prompt(),
    verbose=True,
)


@get(path="/", name="index")
def index() -> Template:
    return Template(name="index.html")


@dataclass
class Query:
    query: str
    df_info: str


@post(path="/ask", name="ask")
def ask(
    request: Request,
    data: Annotated[Query, Body(media_type=RequestEncodingType.MULTI_PART)],
) -> Response[str]:
    query = data.query
    df_info = data.df_info

    result = ""
    chain_result = chain_create.run(
        {
            "df_info": df_info,
            "query": query,
        }
    )
    result = chain_result.split("```python")[-1][:-3].strip()

    return Response(
        result,
        media_type=MediaType.TEXT,
    )


app = Litestar(
    route_handlers=[index, ask],
    static_files_config=[
        StaticFilesConfig(directories=["static"], path="/static", name="static"),
    ],
    template_config=TemplateConfig(
        engine=JinjaTemplateEngine, directory=Path("templates")
    ),
)
