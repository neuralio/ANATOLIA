#!/bin/bash 

# This script extracts the SID variable from the netcdf files from SARAH 
# data sets 

##### Sarah Data (satellite data): 
# https://wui.cmsaf.eu/safira/action/viewUserOrderList
# Oreder manual and then an email comes to neuralio with the wget command, the wget is 
# available for few days 
# wget: wget -r -np -nH --cut-dirs=1 --reject="index.html" --user=$user --password=$password https://cmsaf.dwd.de/data/ORD49425/
##### 

## Path to Satellite GHI data
path_ghi="/Users/paraskevivourlioti/Documents/NEURALIO/KYKLOS/DATA_KYKLOS/SARAH_DATA/GHI/ORD49156"

lat=( 35.075319	40.894192 35.13160399 40.82027063 40.44820015 39.50214298 36.28210594 40.76302758 38.514944 35.41307038 )
lon=( 24.9758 22.814086 26.12504899 23.03949019 23.42207053 22.58902834 28.06363117 21.87380121 23.073556 24.17562781 ) 


#cdo mergetime $path_ghi/*.nc  $path_ghi/merged_GHI.nc 
#35.075319, 24.975800
count=0
for i in "${lat[@]}"; do  
echo lon "${lon[$count]}" lat $i
cdo -outputtab,name,date,time,lon,lat,value -selname,SID  -remapnn,lon=24.975800_lat=35.075319 $path_ghi/merged_GHI.nc >& $path_ghi/merged_GHI_${count}.csv  

count=$(( count + 1 ))
done 
