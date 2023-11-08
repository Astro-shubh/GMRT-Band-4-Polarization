./read_stokes_GWB_raw $1 $2 $3 $4
python bandshape.py $4 50000
./Form_stokes_32_to_32bints $3 $2 $4
rm -f Read_stokes_RR.dat
rm -f Read_stokes_LL.dat
rm -f Read_stokes_lr.dat
rm -f Read_stokes_rl.dat
./dedispersion_I $2 $3 $4 $5 $6 $7 $8
./dedispersion_Q $2 $3 $4 $5 $6 $7 $8
./dedispersion_U $2 $3 $4 $5 $6 $7 $8
./dedispersion_V $2 $3 $4 $5 $6 $7 $8
rm -f Form_stokes_I.dat
rm -f Form_stokes_Q.dat
rm -f Form_stokes_U.dat
rm -f Form_stokes_V.dat
./collapse_chans_I $2 $4 $9
./collapse_chans_Q $2 $4 $9
./collapse_chans_U $2 $4 $9
./collapse_chans_V $2 $4 $9
rm -f Read_stokes_I_dedisp.dat
rm -f Read_stokes_Q_dedisp.dat
rm -f Read_stokes_U_dedisp.dat
rm -f Read_stokes_V_dedisp.dat
