from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.database import get_db
from app.ml.diet_calculator import calculate_bmi, calculate_calories
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

class DietRequest(BaseModel):
    uid: str
    age: int
    gender: str
    height: float
    weight: float
    activity_level: str
    goal: str
    dietary_restrictions: list = []

class DietResponse(BaseModel):
    bmi: float
    bmi_category: str
    daily_calories: float
    macros: dict
    gemini_plan: str

def get_bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "🟦 Underweight"
    elif bmi < 25:
        return "🟩 Normal weight"
    elif bmi < 30:
        return "🟨 Overweight"
    else:
        return "🟥 Obese"

@router.post("/calculate", response_model=DietResponse)
async def calculate_diet_plan(request: DietRequest, db = Depends(get_db)):
    """Calculate diet plan with AI suggestions"""
    try:
        bmi = calculate_bmi(request.height, request.weight)
        bmi_category = get_bmi_category(bmi)
        
        calories = calculate_calories(
            age=request.age,
            gender=request.gender,
            height=request.height,
            weight=request.weight,
            activity_level=request.activity_level,
            goal=request.goal
        )
        
        macros = {
            "carbs_g": round(calories * 0.40 / 4),
            "protein_g": round(calories * 0.30 / 4),
            "fat_g": round(calories * 0.30 / 9)
        }
        
        gemini_plan = f"🥗 Daily meal plan: {calories:.0f} cal, {macros['protein_g']}g protein, {macros['carbs_g']}g carbs, {macros['fat_g']}g fat"
        
        diet_collection = db["diet_plans"]
        await diet_collection.insert_one({
            "uid": request.uid,
            "bmi": bmi,
            "calories": calories,
            "created_at": "2025-06-03T00:00:00Z"
        })
        
        return DietResponse(
            bmi=round(bmi, 1),
            bmi_category=bmi_category,
            daily_calories=round(calories, 0),
            macros=macros,
            gemini_plan=gemini_plan
        )
    except Exception as e:
        logger.error(f"Diet calculation error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/plans/{uid}", response_model=list)
async def get_user_diet_plans(uid: str, db = Depends(get_db)):
    """Get all diet plans for user"""
    try:
        diet_collection = db["diet_plans"]
        plans = await diet_collection.find({"uid": uid}).to_list(None)
        for plan in plans:
            plan["_id"] = str(plan.get("_id", ""))
        return plans
    except Exception as e:
        logger.error(f"Get diet plans error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
