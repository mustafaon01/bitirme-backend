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


class Universities(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    rector = models.CharField(max_length=255, blank=True, null=True)
    province = models.ForeignKey('Provinces', models.DO_NOTHING, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'universities'


class GenelBilgilerLast2024(models.Model):
    pro_code = models.TextField(blank=True, null=True)
    number_0_12_0_06_katsayı_ile_yerleşen_son_kişinin_başarı_sıras = models.TextField(db_column='0,12 + 0,06 Katsayı ile Yerleşen Son Kişinin Başarı Sıras', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_0_12_0_06_katsayı_ile_yerleşen_son_kişinin_puanı_field = models.TextField(db_column='0,12 + 0,06 Katsayı ile Yerleşen Son Kişinin Puanı*', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_0_12_katsayı_ile_yerleşen_son_kişinin_başarı_sırası_field = models.TextField(db_column='0,12 Katsayı ile Yerleşen Son Kişinin Başarı Sırası*', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_0_12_katsayı_ile_yerleşen_son_kişinin_puanı_field = models.TextField(db_column='0,12 Katsayı ile Yerleşen Son Kişinin Puanı*', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_2022_de_yerleşip_2023_de_obp_si_kırılarak_yerleşen_sayısı = models.TextField(db_column="2022'de Yerleşip 2023'de OBP'si Kırılarak Yerleşen Sayısı", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_tavan_başarı_sırası_0_12_field = models.TextField(db_column='2023 Tavan Başarı Sırası(0,12)*', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_2023_tavan_puan_0_12_field = models.TextField(db_column='2023 Tavan Puan(0,12)*', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    boş_kalan_kontenjan = models.TextField(db_column='Boş Kalan Kontenjan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    burs_türü = models.TextField(db_column='Burs Türü', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ek_yerleşen = models.TextField(db_column='Ek Yerleşen', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fakülte_yüksekokul = models.TextField(db_column='Fakülte / Yüksekokul', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    genel_kontenjan = models.TextField(db_column='Genel Kontenjan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    genel_kontenjana_yerleşen = models.TextField(db_column='Genel Kontenjana Yerleşen', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    okul_birincisi_kontenjanı = models.TextField(db_column='Okul Birincisi Kontenjanı', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    okul_birincisi_kontenjanına_yerleşen = models.TextField(db_column='Okul Birincisi Kontenjanına Yerleşen', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    puan_türü = models.TextField(db_column='Puan Türü', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    toplam_kontenjan_field = models.TextField(db_column='Toplam Kontenjan**', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    toplam_yerleşen = models.TextField(db_column='Toplam Yerleşen', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    yerleşenlerin_ortalama_diploma_notu_field = models.TextField(db_column='Yerleşenlerin Ortalama Diploma Notu*', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    yerleşenlerin_ortalama_obp_si_field = models.TextField(db_column="Yerleşenlerin Ortalama OBP'si*", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    yerleşip_kayıt_yaptırmayan = models.TextField(db_column='Yerleşip Kayıt Yaptırmayan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ösym_program_kodu = models.TextField(db_column='ÖSYM Program Kodu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    üniversite = models.TextField(db_column='Üniversite', blank=True, null=True)  # Field name made lowercase.
    üniversite_türü = models.TextField(db_column='Üniversite Türü', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    i_lk_yerleşme_oranı = models.TextField(db_column='İlk Yerleşme Oranı', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bolum_adi = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genel_bilgiler_last_2024'


class Provinces(models.Model):
    province = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provinces'