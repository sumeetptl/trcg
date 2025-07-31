from rest_framework.test import APITestCase
from users.models import User
from signals.models import Signal


class SignalBlurTestCase(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_user(
            username="admin", password="pass", role="admin")
        self.free_user = User.objects.create_user(
            username="free", password="pass", role="free")

        self.signal = Signal.objects.create(
            coin="BTC",
            direction="buy",
            entry_price=42000,
            leverage=10,
            targets={"45000": "pending"},
            stop_loss=39000,
            created_by=self.admin
        )

    def test_free_user_sees_blurred_fields(self):
        self.client.force_authenticate(user=self.free_user)
        response = self.client.get('/api/signals/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['targets'], '🔒 Upgrade to Premium')

    def test_admin_user_sees_full_fields(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get('/api/signals/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['targets'], {"45000": "pending"})
