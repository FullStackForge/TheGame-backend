from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Score(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    score = models.IntegerField()
    time_taken = models.FloatField()  # or models.IntegerField() if you prefer seconds
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.username}: {self.score} in {self.time_taken} seconds"
