import cdsapi
from datetime import datetime
from datetime import timedelta
import os
import sys
from dateutil.relativedelta import relativedelta


### ############################################################
####  Download FROM CDS API temperature a2m ans skin hourly data#
#################################################################
#  


#os.environ['OPENBLAS_NUM_THREADS'] = '1'
c = cdsapi.Client()

back_date = datetime.strptime(sys.argv[1]+"_"+sys.argv[2], "%Y-%m-%d_%H")   

print(back_date)


DATE=datetime.strftime(back_date, "%Y-%m-%d")

hour_string=365 
hour_sys=int(hour_string)
stop_date = back_date + timedelta(days=hour_sys)   

stop = datetime.strftime(stop_date, "%Y-%m-%d_%H")
stop_2 = datetime.strptime(stop, "%Y-%m-%d_%H")

print(DATE, stop_2)




out_path="/Users/paraskevivourlioti/Documents/NEURALIO/KYKLOS/DATA_KYKLOS/ERA5_DATA"
if not os.path.exists(out_path):

   os.makedirs(out_path)



os.chdir(out_path)

while back_date <= stop_2:
   #print(back_date)
   #print(type(back_date))
   str_name=back_date.strftime("%Y%m")
   name="2mtemp_" + str_name + ".grib"
   year=back_date.strftime("%Y")
   month=back_date.strftime("%m") 
   day=back_date.strftime("%d")   
   hour=back_date.strftime("%H")
   file_1=os.path.join(out_path,name)
   # file_1=pathlib.Path(out_path+name)
   print(file_1)
   if os.path.isfile(file_1) :
        print("File exists") 
        back_date = back_date + relativedelta(months=1)  
   else:
    print("File does not exist")
    c.retrieve(
    'reanalysis-era5-land',
    {
        'product_type': 'reanalysis',
        'format': 'grib',
        'variable': [
            '2m_temperature',
            'skin_temperature', 
        ],
        'year': year,
        'month': month,
        'day': [
               '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'time': [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',
        ],
        'area': [
            65, -15, 35,
            45,
        ],
    },
    name)
    back_date = back_date + relativedelta(months=1)  # increase day one by one

