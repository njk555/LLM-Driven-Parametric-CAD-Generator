import os
import json

from dotenv import load_dotenv
from openai import OpenAI

from models import CADRequest

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "openai/gpt-oss-20b"

SYSTEM_PROMPT = """
You are an expert Mechanical CAD Engineer.

Convert the user's request into JSON.

Supported Shapes:

- BOX
- CYLINDER
- SPHERE
- PLATE
- HOLLOW_CYLINDER

Supported Features:

- THROUGH Hole
- BLIND Hole

Rules:

1. Return ONLY valid JSON.
2. No explanation.
3. No markdown.
4. Units are always mm.
5. If the user does not specify a hole, omit the "hole" field.
6. Holes are currently supported only for BOX.

--------------------------------------------------
BOX
--------------------------------------------------

{
    "shape":"BOX",
    "parameters":{
        "length":100,
        "width":50,
        "height":30
    },
    "units":"mm"
}

--------------------------------------------------
CYLINDER
--------------------------------------------------

{
    "shape":"CYLINDER",
    "parameters":{
        "diameter":40,
        "height":80
    },
    "units":"mm"
}

--------------------------------------------------
SPHERE
--------------------------------------------------

{
    "shape":"SPHERE",
    "parameters":{
        "diameter":50
    },
    "units":"mm"
}

--------------------------------------------------
PLATE
--------------------------------------------------

{
    "shape":"PLATE",
    "parameters":{
        "length":120,
        "width":80,
        "thickness":10
    },
    "units":"mm"
}

--------------------------------------------------
HOLLOW CYLINDER
--------------------------------------------------

{
    "shape":"HOLLOW_CYLINDER",
    "parameters":{
        "outer_diameter":60,
        "inner_diameter":40,
        "height":100
    },
    "units":"mm"
}

--------------------------------------------------
BOX WITH THROUGH HOLE
--------------------------------------------------

{
    "shape":"BOX",
    "parameters":{
        "length":100,
        "width":60,
        "height":30
    },
    "hole":{
        "type":"THROUGH",
        "diameter":20,
        "x":0,
        "y":0
    },
    "units":"mm"
}

--------------------------------------------------
BOX WITH BLIND HOLE
--------------------------------------------------

{
    "shape":"BOX",
    "parameters":{
        "length":100,
        "width":60,
        "height":30
    },
    "hole":{
        "type":"BLIND",
        "diameter":20,
        "depth":10,
        "x":0,
        "y":0
    },
    "units":"mm"
}
"""


def generate_cad(prompt: str) -> CADRequest:
    """
    Convert natural language into a CADRequest object.
    """

    response = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    text = response.choices[0].message.content.strip()

    # Remove markdown if the model returns it
    if text.startswith("```json"):
        text = text.replace("```json", "")

    if text.startswith("```"):
        text = text.replace("```", "")

    if text.endswith("```"):
        text = text[:-3]

    text = text.strip()

    try:
        data = json.loads(text)

    except json.JSONDecodeError:
        raise ValueError(
            "AI returned an invalid JSON response."
        )

    return CADRequest.model_validate(data)