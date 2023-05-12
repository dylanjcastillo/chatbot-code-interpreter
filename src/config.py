from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv
import os

load_dotenv()


@dataclass
class OpenAI:
    secret_key: str = os.getenv("OPENAI_SECRET_KEY", "")
    model_name: str = os.getenv("MODEL_CREATE", "gpt-3.5-turbo")


@dataclass
class Paths:
    root: Path = Path(__file__).parent
    prompts: Path = root / "prompts"
