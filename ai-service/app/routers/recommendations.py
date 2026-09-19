from fastapi import APIRouter

try:
    from app.models.schemas import (
        WorkoutPreference,
        WorkoutRecommendation,
        FlowAnalysisRequest,
        FlowAnalysisResponse,
    )
except ImportError:
    from models.schemas import (
        WorkoutPreference,
        WorkoutRecommendation,
        FlowAnalysisRequest,
        FlowAnalysisResponse,
    )

router = APIRouter(prefix="/recommendations", tags=["Recommendations & Flow"])

@router.post("/routine", response_model=WorkoutRecommendation)
def generate_workout_recommendation(preference: WorkoutPreference) -> WorkoutRecommendation:
    """
    Generates tailored workout routines tuned for cognitive and physical flow state.
    """
    exercises = [
        "Dynamic Warmup & Mobility (5 min)",
        f"{preference.fitness_level.capitalize()} Core Circuit (15 min)",
        "Interval Flow Transition (10 min)",
        "Target Muscle Cool Down (5 min)",
    ]

    return WorkoutRecommendation(
        recommendation_id="rec_flow_101",
        routine_name=f"Flow-Optimized {preference.fitness_level.capitalize()} Routine",
        target_area=", ".join(preference.target_muscle_groups),
        estimated_duration_minutes=preference.available_time_minutes,
        flow_score=92.5,
        exercises=exercises,
    )

@router.post("/flow-analysis", response_model=FlowAnalysisResponse)
def analyze_user_flow(request: FlowAnalysisRequest) -> FlowAnalysisResponse:
    """
    Analyzes biomechanical and exertion telemetry to compute real-time user flow state.
    """
    avg_hr = sum(request.heart_rate_samples) / len(request.heart_rate_samples) if request.heart_rate_samples else 120.0
    flow_index = round((request.motion_smoothness_score * 60.0) + (min(avg_hr, 160.0) / 160.0 * 40.0), 2)
    in_flow = flow_index >= 70.0

    feedback = (
        "Optimal flow state detected. Pace and exertion balance are harmonious."
        if in_flow
        else "Flow state interrupted. Recommended: adjust pacing or take a brief hydration pause."
    )

    return FlowAnalysisResponse(
        session_id=request.session_id,
        in_flow_state=in_flow,
        flow_index=flow_index,
        feedback=feedback,
    )
