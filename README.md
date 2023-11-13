# GMRT-Band-4-Polarization
This repository contains codes that can be used for band-4 GMRT polarization data analysis.

This set of codes performs Polarization analysis on the band-4 uGMRT data.


---------------------------------- Running code through scripts  ----------------------------------------------


1. Compile codes using following syntax,

./compile_codes.bash

2. Run the first part of analysis (steps 1-5 in the next section).

./run_codes.bash <raw file name> <total number of samples> <block size for processing> <number of channels> <time resolution> <DM> <Bandwidth> <Frequency of first chan> <Collapse factor for channels>

3. Now run folding,

./folding.bash <time resolution> <period (s)> <total number of samples> <number of channels> 

4. Last step is calibration. It is described in the step 7 of next section.


------------------------------   Individual Steps   -------------------------------------------------------------

1. In the first step of analysis, The raw file is read and four seperate files for RR,LL, Re(RL) Im(RL) are written.

./read_stokes_GWB_raw <filename> < number of samples> <blocksize> <channels>

2. The second step is to compute bandshape for these four files,

bandshape.py <number of channels> <number of samples to compute bandshape> 

3. Now, using the RR,lr,rl, and LL files and their bandshape stokes parameters are computed.

./Form_stokes_32_to_32bints <blocksize> <total samples> <channels>

4. Now the next step is de-dispersion. This is done for all four Stokes parameters.

./dedispersion <total samples> <block size> <channels> <time resolution (s)> <DM> <Bandwidth (MHz)> <first channel freq (MHz)>

5. Now collapse the channels to reduce the file size. Do it for Stokes parameters. 

./collapse_chans <total samples> <number of channels> <number of channels to collapse>

6. The stokes files are then folded using the folding_*py codes.

python folding_fil.py <time resolution> <period (s)> <total number of samples> <number of channels>

7. Now, the next part is calibration. This requires some human interaction in the process. 

python calibration.py 

Select the peak of profile and one off window from the shown profile. Enter it in the subsequent steps.

You will get a Phase versus frequency plot, select a reasonably clean window of channels and enter it in the next step.

This code will now store the data required for delay calibration in two seperate files.

Run calibrate_qu.py to apply the calibration on the profile.

python calibrate_qu.py

This will show both calibrated and uncalibrated profiles.
