from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import validate_forbidden_urls


class CourseSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validate_forbidden_urls])
    description = serializers.CharField(
        required=False, allow_blank=True, validators=[validate_forbidden_urls]
    )

    subscription = serializers.SerializerMethodField()

    def get_subscription(self, course):
        request = self.context.get("request")
        subscription = Subscription.objects.filter(user=request.user, course=course)
        return subscription.exists()

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validate_forbidden_urls])
    description = serializers.CharField(
        required=False, allow_blank=True, validators=[validate_forbidden_urls]
    )

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):

    lesson_count_in_course = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()

    def get_lesson_count_in_course(self, course):
        return course.lesson_set.count()

    def get_lessons(self, course):
        lessons = Lesson.objects.filter(course=course)
        return [lesson.name for lesson in lessons]

    class Meta:
        model = Course
        fields = ("name", "description", "image", "lesson_count_in_course", "lessons")
