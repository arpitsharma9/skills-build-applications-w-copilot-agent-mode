from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTestCase(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        Activity.objects.create(user=tony, type='Run', duration=30)
        Workout.objects.create(name='Avengers HIIT', description='HIIT for Marvel')
        Leaderboard.objects.create(user=tony, score=100)
    def test_user_team(self):
        tony = User.objects.get(email='tony@marvel.com')
        self.assertEqual(tony.team.name, 'Marvel')
    def test_leaderboard(self):
        tony = User.objects.get(email='tony@marvel.com')
        entry = Leaderboard.objects.get(user=tony)
        self.assertEqual(entry.score, 100)
