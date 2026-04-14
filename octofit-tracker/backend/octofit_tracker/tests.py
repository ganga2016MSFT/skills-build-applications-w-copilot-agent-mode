from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import User, Team, Workout, Activity, Leaderboard

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='pass', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc')
        self.activity = Activity.objects.create(user=self.user, workout=self.workout, duration=30)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=50)

    def test_user_list(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, 200)

    def test_team_list(self):
        response = self.client.get(reverse('team-list'))
        self.assertEqual(response.status_code, 200)

    def test_workout_list(self):
        response = self.client.get(reverse('workout-list'))
        self.assertEqual(response.status_code, 200)

    def test_activity_list(self):
        response = self.client.get(reverse('activity-list'))
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_list(self):
        response = self.client.get(reverse('leaderboard-list'))
        self.assertEqual(response.status_code, 200)
