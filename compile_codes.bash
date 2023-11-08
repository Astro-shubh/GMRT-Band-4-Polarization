gcc read_stokes_GWB_raw.c -o read_stokes_GWB_raw
gcc Form_stokes_32_to_32bints.c -o Form_stokes_32_to_32bints -lm
gcc dedispersion_I.c -o dedispersion_I -lm
gcc dedispersion_Q.c -o dedispersion_Q -lm
gcc dedispersion_U.c -o dedispersion_U -lm
gcc dedispersion_V.c -o dedispersion_V -lm
gcc collapse_chans_I.c -o collapse_chans_I -lm
gcc collapse_chans_Q.c -o collapse_chans_Q -lm
gcc collapse_chans_U.c -o collapse_chans_U -lm
gcc collapse_chans_V.c -o collapse_chans_V -lm

