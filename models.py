# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
