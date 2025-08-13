from rest_framework import serializers
from materials.models import Course, Lesson
from .models import Payment


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
        fields = ['id', 'user', 'paid_course', 'paid_lesson', 'amount', 'payment_date']
        ordering = ["payment_date"]

    def validate(self, data):
        if not data.get("paid_course") and not data.get("paid_lesson"):
            raise serializers.ValidationError("Должен быть указан либо курс, либо урок")
        if data.get("paid_course") and data.get("paid_lesson"):
            raise serializers.ValidationError(
                "Можно указать только курс или только урок"
            )
        return data