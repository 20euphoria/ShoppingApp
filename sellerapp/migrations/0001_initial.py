# Generated by Django 3.1 on 2022-04-20 04:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('seller_id', models.AutoField(primary_key=True, serialize=False)),
                ('shop_name', models.CharField(max_length=60)),
                ('shop_address_line1', models.CharField(max_length=60)),
                ('shop_address_line2', models.CharField(max_length=60)),
                ('shop_state', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'), ('Delhi', 'Delhi'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Ladakh', 'Ladakh'), ('Lakshadweep', 'Lakshadweep'), ('Puducherry', 'Puducherry')], max_length=45)),
                ('shop_city', models.CharField(max_length=45)),
                ('shop_pincode', models.IntegerField()),
                ('shop_mobile_number', models.IntegerField()),
                ('shop_mail_id', models.EmailField(max_length=254, unique=True)),
                ('shop_gstin_number', models.CharField(max_length=45)),
                ('pan_card_number', models.CharField(max_length=45, unique=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seller_Bank_Details',
            fields=[
                ('seller_bank_details_id', models.IntegerField(primary_key=True, serialize=False)),
                ('bank_name', models.CharField(max_length=60)),
                ('bank_branch_name', models.CharField(max_length=60)),
                ('account_number', models.IntegerField(unique=True)),
                ('ifsc_code', models.CharField(max_length=45)),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellerapp.seller')),
            ],
        ),
    ]