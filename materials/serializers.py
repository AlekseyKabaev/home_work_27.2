from rest_framework import serializers

from materials.models import Course, Lesson, CourseSubscription
from materials.validators import YouTubeLinkValidator


class LessonSerializer(serializers.ModelSerializer):
    video_link = serializers.URLField(validators=[YouTubeLinkValidator()])

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    count_lessons_of_course = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_count_lessons_of_course(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ('name', 'course_description', 'count_lessons_of_course', 'lessons')


class CourseSubscriptionSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    def get_is_subscribed(self, obj):
        user = self.context.get('request').user
        return CourseSubscription.objects.filter(user=user, course=obj).exists()

    class Meta:
        model = CourseSubscription
        fields = '__all__'
