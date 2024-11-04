from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название курса')
    preview_image = models.ImageField(upload_to="course/image", verbose_name='Превью (картинка)', **NULLABLE)
    course_description = models.TextField(verbose_name='Описание курса', **NULLABLE)
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, verbose_name='Владелец', **NULLABLE)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=100, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока', **NULLABLE)
    preview_image = models.ImageField(upload_to="lesson/image", verbose_name='Превью (картинка)', **NULLABLE)
    video_link = models.URLField()
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, verbose_name='Владелец', **NULLABLE)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name


class CourseSubscription(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscriptions',
                             verbose_name='Владелец')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subscriptions')

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user} subscribed to {self.course}"
