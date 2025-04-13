from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    city = models.CharField(max_length=100)
    address = models.TextField()

    class Meta:
        verbose_name_plural = "Companies"


    def __str__(self):
        return (f"Name: {self.name}\n" +
                f"City: {self.city}\n" +
                f"Address: {self.address}\n" +
                f"Description: {self.description}")

class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, related_name='vacancies', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Vacancies"


    def __str__(self):
        return f"Name: {self.name}\nCompany: {self.company.name}\nSalary: {self.salary}\nDescription: {self.description}"