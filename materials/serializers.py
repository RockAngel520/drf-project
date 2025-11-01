from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):

    lesson_count_in_course = SerializerMethodField()
    lessons = SerializerMethodField()

    def get_lesson_count_in_course(self, course):
        return course.lesson_set.count()

    def get_lessons(self, course):
        lessons = Lesson.objects.filter(course=course)
        return [lesson.name for lesson in lessons]

    class Meta:
        model = Course
        fields = ("name", "description", "image", "lesson_count_in_course", "lessons")
