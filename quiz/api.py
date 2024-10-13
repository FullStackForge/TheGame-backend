from ninja import Router
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from .schemas import ScoreSchema, SubmitScoreSchema
from authentication.auth import AuthBearer
from jose import jwt
from django.conf import settings
import datetime
from .models import Score  # Assuming Score model is defined elsewhere

router = Router()
User = get_user_model()

# Existing user signup and login endpoints

@router.post("/submit_score/", auth=AuthBearer())
def submit_score(request, score_data: SubmitScoreSchema):
    user_id = request.auth  # This should be the user_id obtained from the token
    user = User.objects.filter(id=user_id).first()  # Fetch the user from the database
    if not user:
        return {"error": "User not found"}, 404  # Return an error if user does not exist
    
    score = Score.objects.create(
        player=user,  # Use the user instance directly
        score=score_data.score,
        time_taken=score_data.time_taken
    )
    return {"success": True, "id": score.id}

@router.get("/top_players", response=list[ScoreSchema])
def get_top_players(request):
    top_players = Score.objects.order_by('-score', 'time_taken')[:10]  # Get top 10 players
    return [{"player": player.player.username,  # Access the username via player (User foreign key)
             "score": player.score,
             "time_taken": player.time_taken} 
            for player in top_players]