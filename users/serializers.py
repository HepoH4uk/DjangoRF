from rest_framework import serializers
from materials.models import Course, Lesson
from .models import Payment, User


class PaymentSerializer(serializers.ModelSerializer):
    paid_course = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        required=False,
        allow_null=True
    )
    paid_lesson = serializers.PrimaryKeyRelatedField(
        queryset=Lesson.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Payment
        fields = ['id', 'user', 'paid_course', 'paid_lesson', 'amount', 'payment_date', 'payment_method']
        ordering = ["payment_date"]

    def validate(self, data):
        if not data.get("paid_course") and not data.get("paid_lesson"):
            raise serializers.ValidationError("Должен быть указан либо курс, либо урок")
        if data.get("paid_course") and data.get("paid_lesson"):
            raise serializers.ValidationError(
                "Можно указать только курс или только урок"
            )
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class PaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'