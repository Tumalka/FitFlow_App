from typing import List, Optional
from pydantic import BaseModel, Field

class WorkoutPreference(BaseModel):
    user_id: str = Field(..., description="Unique user identifier")
    fitness_level: str = Field("intermediate", description="beginner, intermediate, or advanced")
    target_muscle_groups: List[str] = Field(default_factory=lambda: ["full_body"])
    available_time_minutes: int = Field(45, ge=10, le=180)
    preferred_intensity: str = Field("medium", description="low, medium, or high")

class WorkoutRecommendation(BaseModel):
    recommendation_id: str
    routine_name: str
    target_area: str
    estimated_duration_minutes: int
    flow_score: float
    exercises: List[str]

class FlowAnalysisRequest(BaseModel):
    session_id: str
    heart_rate_samples: List[int] = Field(default_factory=list)
    motion_smoothness_score: float = Field(0.85, ge=0.0, le=1.0)
    perceived_exertion: int = Field(5, ge=1, le=10)

class FlowAnalysisResponse(BaseModel):
    session_id: str
    in_flow_state: bool
    flow_index: float
    feedback: str
