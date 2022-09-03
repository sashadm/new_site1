from django.db import models




class CarColor(models.Model):
    color_name = models.CharField(max_length=12)

    def __str__(self):
        return self.color_name



class CarMark(models.Model):
    mark_name = models.CharField(max_length=12)

    def __str__(self):
        return self.mark_name



class CarModel(models.Model):
    model_name = models.CharField(max_length=12)

    def __str__(self):
        return self.model_name




class Cars(models.Model):
    class Meta:
        verbose_name = 'car'
    COLOR_CHOICES = (
        ('black', 'black'),
        ('white', 'white'),
        ('red', 'red'),
        ('green', 'green')
    )
    class Meta:
        verbose_name = 'car'
    MARK_CHOICES = (
        ('bmw', 'bmw'),
        ('mercedes', 'mercedes'),
        ('toyota', 'toyota'),
        ('audi', 'audi')
    )
    mark = models.ForeignKey(CarMark,verbose_name='mark',null=True,on_delete=models.SET_NULL)
    model = models.ForeignKey(CarModel,verbose_name='model',null=True,on_delete=models.SET_NULL)
    data_number = models.IntegerField(default=0)
    data_month = models.IntegerField(default=0)
    data_year = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    color = models.ForeignKey(CarColor,verbose_name='color',null=True,on_delete=models.SET_NULL)
    photo = models.ImageField(upload_to='upload/',null=True)




class Comment(models.Model):
    text = models.TextField(blank=False)
    car = models.ForeignKey(Cars,verbose_name='car',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=False)
