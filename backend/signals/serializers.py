from rest_framework import serializers
from .models import Signal


class SignalSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Signal
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        user = self.context.get('request').user

        # Blur targets and stop_loss for free users
        if user.is_authenticated and getattr(user, 'role', 'free') == 'free':
            rep['targets'] = '🔒 Upgrade to Premium'
            rep['stop_loss'] = '🔒 Upgrade to Premium'
        elif not user.is_authenticated:
            rep['targets'] = '🔒 Login to view'
            rep['stop_loss'] = '🔒 Login to view'

        return rep
