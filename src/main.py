from fastapi import FastAPI

from config import OPENAI_API_KEY
from strategy.activity_tracker import ActivityTracker
from strategy.assistant import Assistant
from strategy.nutrition_tracker import NutritionTracker

app = FastAPI()
assistant = Assistant(OPENAI_API_KEY)
activity_tracker = ActivityTracker()
nutrition_tracker = NutritionTracker()

# Routes for API endpoints
@app.get('/')
def read_root():
    return {'message': 'Welcome to FitGPT API!'}


@app.post('/assistant/recommendations')
def get_assistant_recommendations(user_input: str):
    recommendations = assistant.get_recommendations(user_input)
    return {'recommendations': recommendations}


@app.get('/activity/track')
def collect_activity_data():
    data = activity_tracker.collect_data()
    return {'data': data}


@app.post('/activity/analyze')
def analyze_activity_data(data: dict):
    feedback = activity_tracker.analyze_data(data)
    return {'feedback': feedback}


@app.post('/nutrition/track')
def add_food_entry(food: str):
    nutrition_tracker.add_food_entry(food)
    return {'message': 'Food entry added successfully.'}


@app.get('/nutrition/analyze')
def analyze_nutrition_data():
    nutrition_data = nutrition_tracker.analyze_nutrition()
    return {'nutrition_data': nutrition_data}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
