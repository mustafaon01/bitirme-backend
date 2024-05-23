# myapp/models.py
from django.contrib.auth.models import *
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


class UniversityProgramsView2(models.Model):
    id = models.BigIntegerField(primary_key=True)
    program_kodu = models.TextField(blank=True, null=True)
    universite_turu = models.TextField(blank=True, null=True)
    universite = models.TextField(blank=True, null=True)
    fakultesi = models.TextField(blank=True, null=True)
    puan_turu = models.TextField(blank=True, null=True)
    burs_turu = models.TextField(blank=True, null=True)
    genel_kontenjan = models.TextField(blank=True, null=True)
    okul_birincisi_kontenjani = models.TextField(blank=True, null=True)
    toplam_kontenjan = models.TextField(blank=True, null=True)
    genel_kontenjana_yerlesen = models.TextField(blank=True, null=True)
    okul_birincisi_kontenjanina_yerlesen = models.TextField(blank=True, null=True)
    toplam_yerlesen = models.TextField(blank=True, null=True)
    bos_kalan_kontenjan = models.TextField(blank=True, null=True)
    ilk_yerlesme_orani = models.TextField(blank=True, null=True)
    yerlesip_kayit_yaptirmayan = models.TextField(blank=True, null=True)
    ek_yerlesen = models.TextField(blank=True, null=True)
    katsayi_0_12_puani = models.TextField(blank=True, null=True)
    katsayi_0_12_0_06_puani = models.TextField(blank=True, null=True)
    katsayi_0_12_basari_sirasi = models.TextField(blank=True, null=True)
    katsayi_0_12_0_06_basari_sirasi = models.TextField(blank=True, null=True)
    tavan_puan_2023 = models.TextField(blank=True, null=True)
    tavan_basari_sirasi_2023 = models.TextField(blank=True, null=True)
    obp_kirilmis_2022_2023 = models.TextField(blank=True, null=True)
    ortalama_obp = models.TextField(blank=True, null=True)
    ortalama_diploma_notu = models.TextField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'university_programs_view_3'