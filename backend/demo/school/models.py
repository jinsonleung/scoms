from django.db import models


class Student(models.Model):
    """学生模型"""
    name = models.CharField(max_length=64, blank=False, null=False, verbose_name='学校名称')
    age = models.SmallIntegerField( verbose_name='年龄')
    sex = models.BooleanField(default=False, verbose_name='性别')

    class Meta:
        db_table = 'sch_student'
        verbose_name = '学生表'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name


class Course(models.Model):
    """课程模型"""
    name = models.CharField(max_length=64, blank=False, null=False, verbose_name='课程名称')
    sex = models.BooleanField(default=False, verbose_name='性别')

    class Meta:
        db_table = 'sch_teacher'
        verbose_name = '老师表'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name


class Teacher(models.Model):
    """老师模型"""
    name = models.CharField(max_length=64, verbose_name='老师姓名')
    teacher = models.ForeignKey("Teacher", on_delete=models.DO_NOTHING, related_name="course", db_constraint=False, verbose_name="老师外键")

    class Meta:
        db_table = 'sch_course'
        verbose_name = '课程表'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name


class Achievement(models.Model):
    """成绩模型"""
    score = models.DecimalField(default=0, max_digits=4, decimal_places=1, verbose_name='成绩')
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, related_name='s_achievement', db_constraint=False)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, related_name="c_achievement", db_constraint=False, verbose_name="老师外键")
    create_datetime = models.DateTimeField(auto_created=True)

    class Meta:
        db_table = 'sch_achievement'
        verbose_name = '成绩表'
        verbose_name_plural = verbose_name
        ordering = ['score']

    def __str__(self):
        return str(self.score)
