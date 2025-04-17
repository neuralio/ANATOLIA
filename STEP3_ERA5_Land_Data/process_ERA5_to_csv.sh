#!/bin/bash 

# This script extracts the  variable from the netcdf files from SARAH 
# data sets 

## Path to ERA5_LAND data
path_ghi="/Users/paraskevivourlioti/Documents/NEURALIO/KYKLOS/DATA_KYKLOS/ERA5_DATA"

lat=( 35.075319	40.894192 35.13160399 40.82027063 40.44820015 39.50214298 36.28210594 40.76302758 38.514944 35.41307038 )
lon=( 24.9758 22.814086 26.12504899 23.03949019 23.42207053 22.58902834 28.06363117 21.87380121 23.073556 24.17562781 ) 

names=( agioi10 Mavroneri Sitia Assiros Palaiokastro Larisa Mesa1 Arnissa Radi Lagos )

# Run this once: 
#set -x 
for filename in ${path_ghi}/2mtemp_*.grib; do
base_name=$(basename ${filename})
#echo $base_name
filename2="${base_name%.*}".nc 
if [[ ! -f ${path_ghi}/$filename2 ]]; then 
echo $filename2 
cdo -f nc copy $filename ${path_ghi}/$filename2 
fi
done 

#if [  -f $path_ghi/merged_ERA5_LAND.nc ]; then 
#rm -f $path_ghi/merged_ERA5_LAND.nc
#fi 
if [ ! -f $path_ghi/merged_ERA5_LAND.nc ]; then 
cdo mergetime $path_ghi/*.nc  $path_ghi/merged_ERA5_LAND.nc 
fi 


#if [ -f $path_ghi/TminC_merged_ERA5_LAND.nc ]; then
#rm -f $path_ghi/TminC_merged_ERA5_LAND.nc 
#rm -f $path_ghi/Tmin_merged_ERA5_LAND.nc
#fi 

if [ ! -f $path_ghi/TminC_merged_ERA5_LAND.nc ]; then
cdo daymin $path_ghi/merged_ERA5_LAND.nc $path_ghi/Tmin_merged_ERA5_LAND.nc
cdo addc,-273.15 $path_ghi/Tmin_merged_ERA5_LAND.nc $path_ghi/TminC_merged_ERA5_LAND.nc
fi


#if [  -f $path_ghi/TmaxC_merged_ERA5_LAND.nc ]; then
#rm -rf $path_ghi/Tmax_merged_ERA5_LAND.nc
#rm -rf $path_ghi/TmaxC_merged_ERA5_LAND.nc
#fi
if [ ! -f $path_ghi/TmaxC_merged_ERA5_LAND.nc ]; then
cdo daymax $path_ghi/merged_ERA5_LAND.nc $path_ghi/Tmax_merged_ERA5_LAND.nc
cdo addc,-273.15 $path_ghi/Tmax_merged_ERA5_LAND.nc $path_ghi/TmaxC_merged_ERA5_LAND.nc
fi


#if [ -f $path_ghi/TmeanC_merged_ERA5_LAND.nc ]; then
#rm -f $path_ghi/Tmean_merged_ERA5_LAND.nc
#rm -f $path_ghi/TmeanC_merged_ERA5_LAND.nc
#fi

if [ ! -f $path_ghi/TmeanC_merged_ERA5_LAND.nc ]; then
cdo daymean $path_ghi/merged_ERA5_LAND.nc $path_ghi/Tmean_merged_ERA5_LAND.nc
cdo addc,-273.15 $path_ghi/Tmean_merged_ERA5_LAND.nc $path_ghi/TmeanC_merged_ERA5_LAND.nc
fi




#35.075319, 24.975800
count=0
rm -f ${path_ghi}/*.csv 
for i in "${lat[@]}"; do  
echo lon "${lon[$count]}" lat $i names "${names[$count]}"

cdo -outputtab,name,date,time,lon,lat,value -selname,var167  -remapnn,lon="${lon[$count]}"_lat="${lat[$count]}" $path_ghi/TmeanC_merged_ERA5_LAND.nc >& $path_ghi/Tmean_2T_"${names[$count]}".csv  

cdo -outputtab,name,date,time,lon,lat,value -selname,var167  -remapnn,lon="${lon[$count]}"_lat="${lat[$count]}" $path_ghi/TminC_merged_ERA5_LAND.nc >& $path_ghi/Tmin_2T_"${names[$count]}".csv  

cdo -outputtab,name,date,time,lon,lat,value -selname,var167  -remapnn,lon="${lon[$count]}"_lat="${lat[$count]}" $path_ghi/TmaxC_merged_ERA5_LAND.nc >& $path_ghi/Tmax_2T_"${names[$count]}".csv  

cdo -outputtab,name,date,time,lon,lat,value -selname,var235  -remapnn,lon="${lon[$count]}"_lat="${lat[$count]}" $path_ghi/TmeanC_merged_ERA5_LAND.nc >& $path_ghi/Tmean_SkinT_"${names[$count]}".csv  

cdo -outputtab,name,date,time,lon,lat,value -selname,var235  -remapnn,lon="${lon[$count]}"_lat="${lat[$count]}" $path_ghi/TminC_merged_ERA5_LAND.nc >& $path_ghi/Tmin_SkinT_"${names[$count]}".csv  

cdo -outputtab,name,date,time,lon,lat,value -selname,var235  -remapnn,lon="${lon[$count]}"_lat="${lat[$count]}" $path_ghi/TmaxC_merged_ERA5_LAND.nc >& $path_ghi/Tmax_SkinT_"${names[$count]}".csv  

count=$(( count + 1 ))
done 
