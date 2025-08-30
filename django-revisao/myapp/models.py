from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ClientQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(is_deleted=False)


class ClientManager(models.Manager):
    def get_queryset(self):
        return ClientQuerySet(self.model, using=self._db)

    def actives(self):
        return self.get_queryset().actives()


class Client(BaseModel):
    name = models.CharField(max_length=255, db_index=True)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    is_deleted = models.BooleanField(default=False)

    objects = ClientManager()
    active = ClientQuerySet()

    def delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
