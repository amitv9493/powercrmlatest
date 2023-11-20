from django.db import models
from django.utils.translation import gettext_lazy as _

class contract_type(models.TextChoices):
         ElecAMR='ElecAMR',('ElecAMR')
         ElecDomestic='ElecDomestic',('ElecDomestic')
         ElecHH='ElecHH',('ElecHH')
         ElecHHp272='ElecHHp272',('ElecHHp272')
         ElecNHH='ElecNHH',('ElecNHH')
         GasAMR='GasAMR',('GasAMR')
         GasCommercial='GasCommercial',('GasCommercial')
         GasDomestic=' GasDomestic',('GasDomestic')

class Meter_detail(models.Model):
      site =  models.OneToOneField("sites.Site", on_delete=models.CASCADE)

      # Electricity_meter_detail
      e_mpan_topline=models.CharField(max_length=128, null=True, blank=True, verbose_name = "MPAN Topline")
      e_mpan_bottomline= models.CharField(max_length=128, null=True, blank=True, verbose_name = "MPAN Bottomline")
      e_meter_type= models.CharField(max_length=128, null=True, blank=True, verbose_name = "Meter Type")
      e_serial_number= models.CharField(max_length=128, null=True, blank=True, verbose_name = "Serial Number")
      e_capacity= models.CharField(max_length=128, null=True, blank=True, verbose_name = "Capacity")
      e_measurement_class= models.CharField(max_length=128, null=True, blank=True, verbose_name = "Measurement Class")
      e_smart_meter=models.BooleanField(default=None, null=True, blank=True, verbose_name = "Smart Meter")
      e_related_meter=models.BooleanField(default=None, null=True, blank=True, verbose_name = "Related Meter")
      e_ley_meter=models.BooleanField(default=None, null=True, blank=True, verbose_name = "Key Meter")
      e_green_deal=models.BooleanField(default=None, null=True, blank=True, verbose_name = "Green Deal")
      e_voltage = models.FloatField(verbose_name="Voltage")

      # Gas_meter_detail   
      g_mpr=models.CharField(max_length=128, null=True, blank=True,verbose_name="MPR")
      g_serial_number=models.CharField(max_length=128, null=True, blank=True, verbose_name = "Serial Number")
      g_smart_meter=models.BooleanField(default=None, null=True, blank=True, verbose_name = "Smart Meter")
      g_igt_meter= models.BooleanField(default=None, null=True, blank=True, verbose_name = "IGT Meter")
      g_green_deal=models.BooleanField(default=None, null=True, blank=True, verbose_name = "Green Deal")
            
      # def __str__(self):
      #       return self.site.site_name
      class Meta:
            
            verbose_name = "Meter Detail"  

class Current_supplies(models.Model):
         
      site =  models.OneToOneField("sites.Site", on_delete=models.CASCADE)
      # Gas_current_supplies
      g_supplier=models.CharField(max_length=128,verbose_name="Supplier",null=True ,blank=True)
      g_product=models.CharField(max_length=128, verbose_name="Product", null=True ,blank=True)
      g_contract_type=models.CharField(choices=contract_type.choices,max_length=128,null=True, blank=True, verbose_name='Contract Type')
      g_igt_meter= models.BooleanField(default=False, null=True, blank=True, verbose_name="IGT Meter")
      g_green_deal=models.BooleanField(default=False, null=True,blank=True, verbose_name="Green Deal")
      g_won_date=models.DateField(null=True,blank=True, verbose_name="Won Date")
      g_contract_start_date=models.DateField(null=True, blank=True, verbose_name='Contract Start Date')
      g_contract_end_date=models.DateField(null=True, blank=True, verbose_name='Contract End Date')
      g_contract_length_months=models.PositiveIntegerField(_("Contract Length (Months)"), null=True, blank=True)
      g_contract_back_date=models.DateField(null=True, blank=True, verbose_name='Contract Back Date')
      g_supplier_reference=models.CharField(max_length=128,null=True, blank=True, verbose_name='Supplier Reference')
      g_supplier_information1=models.CharField(max_length=128, null=True, blank=True, verbose_name='Supplier Information 1')
      g_supplier_information2=models.CharField(max_length=128, null=True, blank=True, verbose_name='Supplier Information 2')
      g_supplier_information3=models.CharField(max_length=128, null=True, blank=True, verbose_name='Supplier Information 3')
      g_agent=models.BooleanField(default=None, null=True, blank=True, verbose_name='Agent')
      g_customer=models.BooleanField(default=None, null=True, blank=True, verbose_name='Customer')
      
      # Electricity_current_supplies
      e_supplier=models.CharField(max_length=128,null=True, blank=True, verbose_name='Supplier')
      e_product=models.CharField(max_length=128,null=True, blank=True, verbose_name='Product')
      e_contract_type=models.CharField(choices=contract_type.choices,max_length=128,blank=True, null=True, verbose_name='Contract')
      e_igt_meter= models.BooleanField(default=False, null=True, blank=True, verbose_name='IGT Meter')
      e_green_deal=models.BooleanField(default=False, null=True, blank=True, verbose_name='Green Deal')
      e_won_date=models.DateField(null=True,  blank=True, verbose_name='Won Date')
      e_contract_start_date=models.DateField(null=True, blank=True, verbose_name='Contract Start Date')
      e_contract_end_date=models.DateField(null=True, blank=True, verbose_name='')
      e_contract_length_months=models.CharField(max_length=128, null=True, blank=True, verbose_name='Contract End Date')
      e_contract_back_date=models.DateField(null=True, blank=True, verbose_name='Contract Back Date')
      e_supplier_reference=models.CharField(max_length=128, null=True, blank=True, verbose_name='Supplier Reference')
      e_supplier_information1=models.CharField(max_length=128, null=True, blank=True, verbose_name='Supplier Information 1')
      e_supplier_information2=models.CharField(max_length=128, null=True, blank=True, verbose_name='Supplier Information 2')
      e_supplier_information3=models.CharField(max_length=128, null=True, blank=True, verbose_name='Supplier Information 3')
      e_agent=models.BooleanField(default=False, null=True, blank=True, verbose_name='Agent')
      e_customer=models.BooleanField(default=False, null=True, blank=True, verbose_name='Customer')
      

      class Meta:
            verbose_name = "Current supplies"
            verbose_name_plural= "Current supplies"
        

class New_supplies(models.Model):
      
         
      site =  models.OneToOneField("sites.Site", on_delete=models.CASCADE)
      
      # Gas_new_supplies
      
      g_supplier=models.CharField(max_length=128,  null=True, blank=True, verbose_name='Supplier')
      g_product=models.CharField(max_length=128,  null=True, blank=True, verbose_name='Product')
      
      g_contract_type=models.CharField(choices=contract_type.choices,max_length=128, null=True, blank=True, verbose_name="Contract Type")
      g_igt_meter= models.BooleanField(default=None,  null=True, blank=True, verbose_name='IGT Meter')
      g_green_deal=models.BooleanField(default=False,null=True, blank=True, verbose_name='Green Deal')
      g_won_date=models.DateField(null=True, blank=True, verbose_name='Won Date')
      g_contract_start_date=models.DateField(null=True, blank=True, verbose_name='Contract Start Date')
      g_contract_end_date=models.DateField(null=True, blank=True, verbose_name='Contract End Date')
      g_contract_length_months=models.PositiveIntegerField( null=True, blank=True, verbose_name='Contract Length (Months)')
      g_contract_back_date=models.DateField(null=True, blank=True, verbose_name='Contract Back Date')
      g_supplier_reference=models.CharField(max_length=128,null=True, blank=True, verbose_name='Supply Reference')
      g_supplier_information1=models.CharField(max_length=128,null=True, blank=True, verbose_name='Supplier Information 1')
      g_supplier_information2=models.CharField(max_length=128, null=True, blank=True, verbose_name='Supplier Information 2')
      g_supplier_information3=models.CharField(max_length=128,null=True, blank=True, verbose_name='Supplier Information 3')
      g_agent=models.BooleanField(default=None, null=True, blank=True, verbose_name='Agent')
      g_customer=models.BooleanField(default=None,null=True, blank=True, verbose_name='Customer')
      g_notes = models.TextField(null=True, blank=True)

      # Electricity_new_supplies
      e_supplier=models.CharField(max_length=128,null=True, blank=True, verbose_name='Supplier')
      e_product=models.CharField(max_length=128,null=True, blank=True, verbose_name='Product')
      e_contract_type=models.CharField(choices=contract_type.choices,max_length=128,null=True, blank=True, verbose_name='Contract Type')
      e_igt_meter= models.BooleanField(default=None, null=True, blank=True,verbose_name='IGT Meter')
      e_green_deal=models.BooleanField(default=None, null=True, blank=True, verbose_name='green Deal')
      e_won_date=models.DateField(null=True, blank=True,  verbose_name='Won Date')
      e_contract_start_date=models.DateField(null=True, blank=True,  verbose_name='Contract Start Date')
      e_contract_end_date=models.DateField(null=True, blank=True,  verbose_name='Contract End Date')
      e_contract_length_months=models.CharField(max_length=128,null=True, blank=True,  verbose_name='Contract Length months')
      e_contract_back_date=models.DateField(null=True, blank=True, verbose_name='Contract Back Date')
      e_supplier_reference=models.CharField(max_length=128,null=True, blank=True, verbose_name='Supplier reference')
      e_supplier_information1=models.CharField(max_length=128,null=True, blank=True, verbose_name=' Supplier Information 1')
      e_supplier_information2=models.CharField(max_length=128,null=True, blank=True, verbose_name=' Supplier Information 2')
      e_supplier_information3=models.CharField(max_length=128,null=True, blank=True, verbose_name=' Supplier Information 3')
      e_agent=models.BooleanField(default=None, null=True, blank=True, verbose_name='Agent')
      e_customer=models.BooleanField(default=None, null=True, blank=True, verbose_name='Customer')
      e_notes = models.TextField(null=True, blank=True)
      class Meta:
            verbose_name = "New supplies"
            verbose_name_plural= "New supplies"


class Supplies(models.Model):
      meter= models.ForeignKey(Meter_detail,on_delete=models.CASCADE)
      current_supply = models.ForeignKey(Current_supplies, on_delete=models.CASCADE)
      new_supply = models.ForeignKey(New_supplies, on_delete=models.CASCADE)
      
      
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# from django.db import models

# class Gas_meter_detail(models.Model):
#       mpr=models.CharField(max_length=128)
#       serial_number=models.CharField(max_length=128)
#       smart_meter=models.BooleanField(default=False)
#       igt_meter= models.BooleanField(default=False)
#       green_deal=models.BooleanField(default=False)

#       def __str__(self):
#           return self.mpr
#       class Meta:
#             verbose_name = "Gas meter detail"
#             verbose_name_plural= "Gas meter detail"

# class Electricity_meter_detail(models.Model):
#       mpan_topline=models.CharField(max_length=128)
#       mpan_bottomline= models.CharField(max_length=128)
#       meter_type= models.CharField(max_length=128)
#       serial_number= models.CharField(max_length=128)
#       capacity= models.CharField(max_length=128)
#       measurement_class= models.CharField(max_length=128)
#       smart_meter=models.BooleanField(default=False)
#       related_meter=models.BooleanField(default=False)
#       ley_meter=models.BooleanField(default=False)
#       green_deal=models.BooleanField(default=False)

#       def __str__(self):
#          return self.serial_number

#       class Meta:
#             verbose_name = "Electricity meter detail"
#             verbose_name_plural= "Electricity meter detail"


# class Gas_current_supplies(models.Model):
#       supplier=models.CharField(max_length=128)
#       product=models.CharField(max_length=128)
#       class contract_type(models.TextChoices):
#          ElecAMR='ElecAMR',('ElecAMR')
#          ElecDomestic='ElecDomestic',('ElecDomestic')
#          ElecHH='ElecHH',('ElecHH')
#          ElecHHp272='ElecHHp272',('ElecHHp272')
#          ElecNHH='ElecNHH',('ElecNHH')
#          GasAMR='GasAMR',('GasAMR')
#          GasCommercial='GasCommercial',('GasCommercial')
#          GasDomestic=' GasDomestic',('GasDomestic')
#       contract_type=models.CharField(choices=contract_type.choices,max_length=128,default="")
#       igt_meter= models.BooleanField(default=False)
#       green_deal=models.BooleanField(default=False)
#       won_date=models.DateField(null=True)
#       contract_start_date=models.DateField(null=True)
#       contract_end_date=models.DateField(null=True)
#       contract_length_months=models.CharField(max_length=128)
#       contract_back_date=models.DateField(null=True)
#       supplier_reference=models.CharField(max_length=128)
#       supplier_information1=models.CharField(max_length=128)
#       supplier_information2=models.CharField(max_length=128)
#       supplier_information3=models.CharField(max_length=128)
#       agent=models.BooleanField(default=False)
#       customer=models.BooleanField(default=False)

#       def __str__(self):
#           return self.supplier

#       class Meta:
#             verbose_name = "Gas current supplies"
#             verbose_name_plural= "Gas current supplies"
        
# class Electricity_current_supplies(models.Model):
#       supplier=models.CharField(max_length=128,default="")
#       product=models.CharField(max_length=128,default="")
#       class contract_type(models.TextChoices):
#          ElecAMR='ElecAMR',('ElecAMR')
#          ElecDomestic='ElecDomestic',('ElecDomestic')
#          ElecHH='ElecHH',('ElecHH')
#          ElecHHp272='ElecHHp272',('ElecHHp272')
#          ElecNHH='ElecNHH',('ElecNHH')
#          GasAMR='GasAMR',('GasAMR')
#          GasCommercial='GasCommercial',('GasCommercial')
#          GasDomestic=' GasDomestic',('GasDomestic')
#       contract_type=models.CharField(choices=contract_type.choices,max_length=128,default="")
#       igt_meter= models.BooleanField(default=False)
#       green_deal=models.BooleanField(default=False)
#       won_date=models.DateField(null=True)
#       contract_start_date=models.DateField(null=True)
#       contract_end_date=models.DateField(null=True)
#       contract_length_months=models.CharField(max_length=128,default="")
#       contract_back_date=models.DateField(null=True)
#       supplier_reference=models.CharField(max_length=128,default="")
#       supplier_information1=models.CharField(max_length=128,default="")
#       supplier_information2=models.CharField(max_length=128,default="")
#       supplier_information3=models.CharField(max_length=128,default="")
#       agent=models.BooleanField(default=False)
#       customer=models.BooleanField(default=False)

#       def __str__(self):
#           return self.supplier

#       class Meta:
#             verbose_name = "Electricity current supplies"
#             verbose_name_plural= "Electricity current supplies"

# class Gas_new_supplies(models.Model):
#       supplier=models.CharField(max_length=128)
#       product=models.CharField(max_length=128)
#       class contract_type(models.TextChoices):
#          ElecAMR='ElecAMR',('ElecAMR')
#          ElecDomestic='ElecDomestic',('ElecDomestic')
#          ElecHH='ElecHH',('ElecHH')
#          ElecHHp272='ElecHHp272',('ElecHHp272')
#          ElecNHH='ElecNHH',('ElecNHH')
#          GasAMR='GasAMR',('GasAMR')
#          GasCommercial='GasCommercial',('GasCommercial')
#          GasDomestic=' GasDomestic',('GasDomestic')
#       contract_type=models.CharField(choices=contract_type.choices,max_length=128,default="")
#       igt_meter= models.BooleanField(default=False)
#       green_deal=models.BooleanField(default=False)
#       won_date=models.DateField(null=True)
#       contract_start_date=models.DateField(null=True)
#       contract_end_date=models.DateField(null=True)
#       contract_length_months=models.CharField(max_length=128)
#       contract_back_date=models.DateField(null=True)
#       supplier_reference=models.CharField(max_length=128)
#       supplier_information1=models.CharField(max_length=128)
#       supplier_information2=models.CharField(max_length=128)
#       supplier_information3=models.CharField(max_length=128)
#       agent=models.BooleanField(default=False)
#       customer=models.BooleanField(default=False)

#       def __str__(self):
#           return self.supplier
#       class Meta:
#             verbose_name = "Gas new supplies"
#             verbose_name_plural= "Gas new supplies"

# class Electricity_new_supplies(models.Model):
#       supplier=models.CharField(max_length=128,default="")
#       product=models.CharField(max_length=128,default="")
#       class contract_type(models.TextChoices):
#          ElecAMR='ElecAMR',('ElecAMR')
#          ElecDomestic='ElecDomestic',('ElecDomestic')
#          ElecHH='ElecHH',('ElecHH')
#          ElecHHp272='ElecHHp272',('ElecHHp272')
#          ElecNHH='ElecNHH',('ElecNHH')
#          GasAMR='GasAMR',('GasAMR')
#          GasCommercial='GasCommercial',('GasCommercial')
#          GasDomestic=' GasDomestic',('GasDomestic')
#       contract_type=models.CharField(choices=contract_type.choices,max_length=128,default="")
#       igt_meter= models.BooleanField(default=False)
#       green_deal=models.BooleanField(default=False)
#       won_date=models.DateField(null=True)
#       contract_start_date=models.DateField(null=True)
#       contract_end_date=models.DateField(null=True)
#       contract_length_months=models.CharField(max_length=128,default="")
#       contract_back_date=models.DateField(null=True)
#       supplier_reference=models.CharField(max_length=128,default="")
#       supplier_information1=models.CharField(max_length=128,default="")
#       supplier_information2=models.CharField(max_length=128,default="")
#       supplier_information3=models.CharField(max_length=128,default="")
#       agent=models.BooleanField(default=False)
#       customer=models.BooleanField(default=False)

#       def __str__(self):
#           return self.supplier
#       class Meta:
#             verbose_name = "Electricity new supplies"
#             verbose_name_plural= "Electricity new supplies"



   
# # # Create your models here.
# # class Old_Meter_detail(models.Model):

# #       site =  models.OneToOneField("sites.Site", on_delete=models.CASCADE)
# #       gas_meter_detail=models.ForeignKey(Gas_meter_detail,on_delete=models.CASCADE,verbose_name="GAS")
# #       electricity_meter_detail=models.ForeignKey(Electricity_meter_detail,on_delete=models.CASCADE,verbose_name="ELECTRICITY")

# #     #   def __str__(self):
# #     #      return self.gas_meter_detail.mpr
# #       class Meta:
# #             verbose_name = "Meter detail"
# #             verbose_name_plural= "Meter detail"

# # class Old_Current_supplies(models.Model):
# #       site =  models.OneToOneField("sites.Site", on_delete=models.CASCADE)
      
# #       gas_current_supplies=models.ForeignKey(Gas_current_supplies,on_delete=models.CASCADE,verbose_name="GAS")
# #       electricity_current_supplies=models.ForeignKey(Electricity_current_supplies,on_delete=models.CASCADE,verbose_name="ELECTRICITY")

# #     #   def __str__(self):
# #     #      return self.gas_meter_detail.mpr
# #       class Meta:
# #             verbose_name = "Current supplies"
# #             verbose_name_plural= "Current supplies"

# # class Old_New_supplies(models.Model):
# #       site =  models.OneToOneField("sites.Site", on_delete=models.CASCADE)
      
# #       gas_new_supplies=models.ForeignKey(Gas_new_supplies,on_delete=models.CASCADE,verbose_name="GAS")
# #       electricity_new_supplies=models.ForeignKey(Electricity_new_supplies,on_delete=models.CASCADE,verbose_name="ELECTRICITY")


# #       class Meta:
# #             verbose_name = "New supplies"
# #             verbose_name_plural= "New supplies"


