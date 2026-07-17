from typing import Dict, Optional
from pydantic import BaseModel, Field


class Hole(BaseModel):
    """
    Represents a hole feature.
    """

    type: str = Field(
        default="THROUGH",
        description="THROUGH or BLIND"
    )

    diameter: float

    depth: Optional[float] = None

    x: float = 0
    y: float = 0


class CADRequest(BaseModel):
    """
    Request received from the LLM.
    """

    shape: str

    parameters: Dict[str, float]

    hole: Optional[Hole] = None

    units: str = "mm"