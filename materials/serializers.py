from rest_framework import serializers
from .models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для списка уроков"""
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'video_url', 'course', 'owner']


class LessonDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для детального просмотра урока"""
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(
        source='lessons.all',
        many=True,
        read_only=True,
        help_text="Список уроков курса"
    )
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'lesson_count', 'lessons']
        extra_kwargs = {
            'preview': {'read_only': True}
        }


