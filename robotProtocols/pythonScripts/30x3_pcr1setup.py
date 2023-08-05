def get_values(*names):
    import json
    _all_values = json.loads("""{"transfer_csv":"ot2set,reagent,source_labware,source_slot,source_well,asp_height,dest_labware,dest_slot,dest_well,transfer_volume\\nset1_xtnPlate1_e1,blood_p1.D1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D1,1,denvillewithaxygenbase_96_wellplate_200ul,2,A1,2\\nset1_xtnPlate1_e1,blood_p1.D1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D1,1,denvillewithaxygenbase_96_wellplate_200ul,5,A1,2\\nset1_xtnPlate1_e1,blood_p1.F1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F1,1,denvillewithaxygenbase_96_wellplate_200ul,2,B1,2\\nset1_xtnPlate1_e1,blood_p1.F1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F1,1,denvillewithaxygenbase_96_wellplate_200ul,5,B1,2\\nset1_xtnPlate1_e1,blood_p1.G1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G1,1,denvillewithaxygenbase_96_wellplate_200ul,2,C1,2\\nset1_xtnPlate1_e1,blood_p1.G1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G1,1,denvillewithaxygenbase_96_wellplate_200ul,5,C1,2\\nset1_xtnPlate1_e1,blood_p1.H1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H1,1,denvillewithaxygenbase_96_wellplate_200ul,2,D1,2\\nset1_xtnPlate1_e1,blood_p1.H1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H1,1,denvillewithaxygenbase_96_wellplate_200ul,5,D1,2\\nset1_xtnPlate1_e1,blood_p1.H6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H6,1,denvillewithaxygenbase_96_wellplate_200ul,2,G1,2\\nset1_xtnPlate1_e1,blood_p1.H6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H6,1,denvillewithaxygenbase_96_wellplate_200ul,5,G1,2\\nset1_xtnPlate1_e1,blood_p1.E8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E8,1,denvillewithaxygenbase_96_wellplate_200ul,2,H1,2\\nset1_xtnPlate1_e1,blood_p1.E8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E8,1,denvillewithaxygenbase_96_wellplate_200ul,5,H1,2\\nset1_xtnPlate1_e1,blood_p1.B9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B9,1,denvillewithaxygenbase_96_wellplate_200ul,2,A2,2\\nset1_xtnPlate1_e1,blood_p1.B9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B9,1,denvillewithaxygenbase_96_wellplate_200ul,5,A2,2\\nset1_xtnPlate1_e1,blood_p1.E10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E10,1,denvillewithaxygenbase_96_wellplate_200ul,2,B2,2\\nset1_xtnPlate1_e1,blood_p1.E10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E10,1,denvillewithaxygenbase_96_wellplate_200ul,5,B2,2\\nset1_xtnPlate1_e1,blood_xtnNeg_p1.C4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C4,1,denvillewithaxygenbase_96_wellplate_200ul,2,C2,2\\nset1_xtnPlate1_e1,blood_xtnNeg_p1.C4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C4,1,denvillewithaxygenbase_96_wellplate_200ul,5,C2,2\\nset1_xtnPlate1_e1,blood_p1.G10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G10,1,denvillewithaxygenbase_96_wellplate_200ul,2,D2,2\\nset1_xtnPlate1_e1,blood_p1.G10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G10,1,denvillewithaxygenbase_96_wellplate_200ul,5,D2,2\\nset1_xtnPlate1_e1,blood_p1.B11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B11,1,denvillewithaxygenbase_96_wellplate_200ul,2,E2,2\\nset1_xtnPlate1_e1,blood_p1.B11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B11,1,denvillewithaxygenbase_96_wellplate_200ul,5,E2,2\\nset1_xtnPlate1_e1,blood_p1.D11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D11,1,denvillewithaxygenbase_96_wellplate_200ul,2,F2,2\\nset1_xtnPlate1_e1,blood_p1.D11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D11,1,denvillewithaxygenbase_96_wellplate_200ul,5,F2,2\\nset1_xtnPlate1_e1,blood_p1.H11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H11,1,denvillewithaxygenbase_96_wellplate_200ul,2,G2,2\\nset1_xtnPlate1_e1,blood_p1.H11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H11,1,denvillewithaxygenbase_96_wellplate_200ul,5,G2,2\\nset1_xtnPlate1_e1,blood_p1.B12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B12,1,denvillewithaxygenbase_96_wellplate_200ul,2,H2,2\\nset1_xtnPlate1_e1,blood_p1.B12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B12,1,denvillewithaxygenbase_96_wellplate_200ul,5,H2,2\\nset2_xtnPlate1_e2,blood_p1.C6_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,C6,1,denvillewithaxygenbase_96_wellplate_200ul,2,E1,2\\nset2_xtnPlate1_e2,blood_p1.C6_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,C6,1,denvillewithaxygenbase_96_wellplate_200ul,5,E1,2\\nset2_xtnPlate1_e2,blood_p1.E6_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,E6,1,denvillewithaxygenbase_96_wellplate_200ul,2,F1,2\\nset2_xtnPlate1_e2,blood_p1.E6_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,E6,1,denvillewithaxygenbase_96_wellplate_200ul,5,F1,2\\nset3_xtnPlate2_e1,blood_p2.B2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B2,1,denvillewithaxygenbase_96_wellplate_200ul,2,B3,2\\nset3_xtnPlate2_e1,blood_p2.B2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B2,1,denvillewithaxygenbase_96_wellplate_200ul,5,B3,2\\nset3_xtnPlate2_e1,blood_p2.A3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A3,1,denvillewithaxygenbase_96_wellplate_200ul,2,C3,2\\nset3_xtnPlate2_e1,blood_p2.A3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A3,1,denvillewithaxygenbase_96_wellplate_200ul,5,C3,2\\nset3_xtnPlate2_e1,blood_p2.H3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H3,1,denvillewithaxygenbase_96_wellplate_200ul,2,D3,2\\nset3_xtnPlate2_e1,blood_p2.H3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H3,1,denvillewithaxygenbase_96_wellplate_200ul,5,D3,2\\nset3_xtnPlate2_e1,blood_p2.E4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E4,1,denvillewithaxygenbase_96_wellplate_200ul,2,E3,2\\nset3_xtnPlate2_e1,blood_p2.E4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E4,1,denvillewithaxygenbase_96_wellplate_200ul,5,E3,2\\nset3_xtnPlate2_e1,blood_p2.H5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H5,1,denvillewithaxygenbase_96_wellplate_200ul,2,F3,2\\nset3_xtnPlate2_e1,blood_p2.H5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H5,1,denvillewithaxygenbase_96_wellplate_200ul,5,F3,2\\nset3_xtnPlate2_e1,blood_p2.A10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A10,1,denvillewithaxygenbase_96_wellplate_200ul,2,G3,2\\nset3_xtnPlate2_e1,blood_p2.A10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A10,1,denvillewithaxygenbase_96_wellplate_200ul,5,G3,2\\nset3_xtnPlate2_e1,blood_p2.E10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E10,1,denvillewithaxygenbase_96_wellplate_200ul,2,H3,2\\nset3_xtnPlate2_e1,blood_p2.E10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E10,1,denvillewithaxygenbase_96_wellplate_200ul,5,H3,2\\nset3_xtnPlate2_e1,blood_p2.G10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G10,1,denvillewithaxygenbase_96_wellplate_200ul,2,A4,2\\nset3_xtnPlate2_e1,blood_p2.G10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G10,1,denvillewithaxygenbase_96_wellplate_200ul,5,A4,2\\nset3_xtnPlate2_e1,blood_p2.E11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E11,1,denvillewithaxygenbase_96_wellplate_200ul,2,B4,2\\nset3_xtnPlate2_e1,blood_p2.E11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E11,1,denvillewithaxygenbase_96_wellplate_200ul,5,B4,2\\nset3_xtnPlate2_e1,blood_p2.B12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B12,1,denvillewithaxygenbase_96_wellplate_200ul,2,C4,2\\nset3_xtnPlate2_e1,blood_p2.B12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B12,1,denvillewithaxygenbase_96_wellplate_200ul,5,C4,2\\nset3_xtnPlate2_e1,blood_xtnNeg_p2.C4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C4,1,denvillewithaxygenbase_96_wellplate_200ul,2,F4,2\\nset3_xtnPlate2_e1,blood_xtnNeg_p2.C4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C4,1,denvillewithaxygenbase_96_wellplate_200ul,5,F4,2\\nset4.1_xtnPlate2_e2,blood_p2.A1_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,2,A3,2\\nset4.1_xtnPlate2_e2,blood_p2.A1_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,5,A3,2\\nset4.2_bloodTubes,blood_t222_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A1,1,denvillewithaxygenbase_96_wellplate_200ul,2,D4,2\\nset4.2_bloodTubes,blood_t222_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A1,1,denvillewithaxygenbase_96_wellplate_200ul,5,D4,2\\nset4.2_bloodTubes,blood_t700_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B1,1,denvillewithaxygenbase_96_wellplate_200ul,2,E4,2\\nset4.2_bloodTubes,blood_t700_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B1,1,denvillewithaxygenbase_96_wellplate_200ul,5,E4,2\\nset4.2_bloodTubes,blood_t1183_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C1,1,denvillewithaxygenbase_96_wellplate_200ul,2,G4,2\\nset4.2_bloodTubes,blood_t1183_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C1,1,denvillewithaxygenbase_96_wellplate_200ul,5,G4,2\\nset4.2_bloodTubes,blood_t1275_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D1,1,denvillewithaxygenbase_96_wellplate_200ul,2,H4,2\\nset4.2_bloodTubes,blood_t1275_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D1,1,denvillewithaxygenbase_96_wellplate_200ul,5,H4,2\\nset5_fecalTubes1to24,fecal_t1_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A1,1,denvillewithaxygenbase_96_wellplate_200ul,2,A5,4\\nset5_fecalTubes1to24,fecal_t1_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A1,1,denvillewithaxygenbase_96_wellplate_200ul,5,A5,4\\nset5_fecalTubes1to24,fecal_t2_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B1,1,denvillewithaxygenbase_96_wellplate_200ul,2,B5,4\\nset5_fecalTubes1to24,fecal_t2_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B1,1,denvillewithaxygenbase_96_wellplate_200ul,5,B5,4\\nset5_fecalTubes1to24,fecal_t3_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C1,1,denvillewithaxygenbase_96_wellplate_200ul,2,C5,4\\nset5_fecalTubes1to24,fecal_t3_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C1,1,denvillewithaxygenbase_96_wellplate_200ul,5,C5,4\\nset5_fecalTubes1to24,fecal_t4_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D1,1,denvillewithaxygenbase_96_wellplate_200ul,2,D5,4\\nset5_fecalTubes1to24,fecal_t4_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D1,1,denvillewithaxygenbase_96_wellplate_200ul,5,D5,4\\nset5_fecalTubes1to24,fecal_t5_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A2,1,denvillewithaxygenbase_96_wellplate_200ul,2,E5,4\\nset5_fecalTubes1to24,fecal_t5_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A2,1,denvillewithaxygenbase_96_wellplate_200ul,5,E5,4\\nset5_fecalTubes1to24,fecal_t6_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B2,1,denvillewithaxygenbase_96_wellplate_200ul,2,F5,4\\nset5_fecalTubes1to24,fecal_t6_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B2,1,denvillewithaxygenbase_96_wellplate_200ul,5,F5,4\\nset5_fecalTubes1to24,fecal_t7_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C2,1,denvillewithaxygenbase_96_wellplate_200ul,2,G5,4\\nset5_fecalTubes1to24,fecal_t7_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C2,1,denvillewithaxygenbase_96_wellplate_200ul,5,G5,4\\nset5_fecalTubes1to24,fecal_t8_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D2,1,denvillewithaxygenbase_96_wellplate_200ul,2,H5,4\\nset5_fecalTubes1to24,fecal_t8_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D2,1,denvillewithaxygenbase_96_wellplate_200ul,5,H5,4\\nset5_fecalTubes1to24,fecal_t9_e2,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A3,1,denvillewithaxygenbase_96_wellplate_200ul,2,A6,4\\nset5_fecalTubes1to24,fecal_t9_e2,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A3,1,denvillewithaxygenbase_96_wellplate_200ul,5,A6,4\\nset5_fecalTubes1to24,fecal_t10_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B3,1,denvillewithaxygenbase_96_wellplate_200ul,2,B6,4\\nset5_fecalTubes1to24,fecal_t10_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B3,1,denvillewithaxygenbase_96_wellplate_200ul,5,B6,4\\nset5_fecalTubes1to24,tH2O.1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C3,1,denvillewithaxygenbase_96_wellplate_200ul,2,C6,4\\nset5_fecalTubes1to24,tH2O.1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C3,1,denvillewithaxygenbase_96_wellplate_200ul,5,C6,4\\nset5_fecalTubes1to24,fecal_t11_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D3,1,denvillewithaxygenbase_96_wellplate_200ul,2,D6,4\\nset5_fecalTubes1to24,fecal_t11_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D3,1,denvillewithaxygenbase_96_wellplate_200ul,5,D6,4\\nset5_fecalTubes1to24,fecal_t12_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A4,1,denvillewithaxygenbase_96_wellplate_200ul,2,E6,4\\nset5_fecalTubes1to24,fecal_t12_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A4,1,denvillewithaxygenbase_96_wellplate_200ul,5,E6,4\\nset5_fecalTubes1to24,fecal_t13_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B4,1,denvillewithaxygenbase_96_wellplate_200ul,2,F6,4\\nset5_fecalTubes1to24,fecal_t13_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B4,1,denvillewithaxygenbase_96_wellplate_200ul,5,F6,4\\nset5_fecalTubes1to24,fecal_t14_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C4,1,denvillewithaxygenbase_96_wellplate_200ul,2,G6,4\\nset5_fecalTubes1to24,fecal_t14_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C4,1,denvillewithaxygenbase_96_wellplate_200ul,5,G6,4\\nset5_fecalTubes1to24,fecal_t15_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D4,1,denvillewithaxygenbase_96_wellplate_200ul,2,H6,4\\nset5_fecalTubes1to24,fecal_t15_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D4,1,denvillewithaxygenbase_96_wellplate_200ul,5,H6,4\\nset5_fecalTubes1to24,fecal_t16_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A5,1,denvillewithaxygenbase_96_wellplate_200ul,2,A7,4\\nset5_fecalTubes1to24,fecal_t16_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A5,1,denvillewithaxygenbase_96_wellplate_200ul,5,A7,4\\nset5_fecalTubes1to24,fecal_t17_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B5,1,denvillewithaxygenbase_96_wellplate_200ul,2,B7,4\\nset5_fecalTubes1to24,fecal_t17_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B5,1,denvillewithaxygenbase_96_wellplate_200ul,5,B7,4\\nset5_fecalTubes1to24,fecal_t18_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C5,1,denvillewithaxygenbase_96_wellplate_200ul,2,C7,4\\nset5_fecalTubes1to24,fecal_t18_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C5,1,denvillewithaxygenbase_96_wellplate_200ul,5,C7,4\\nset5_fecalTubes1to24,fecal_t19_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D5,1,denvillewithaxygenbase_96_wellplate_200ul,2,D7,4\\nset5_fecalTubes1to24,fecal_t19_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D5,1,denvillewithaxygenbase_96_wellplate_200ul,5,D7,4\\nset5_fecalTubes1to24,fecal_t20_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A6,1,denvillewithaxygenbase_96_wellplate_200ul,2,E7,4\\nset5_fecalTubes1to24,fecal_t20_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A6,1,denvillewithaxygenbase_96_wellplate_200ul,5,E7,4\\nset5_fecalTubes1to24,tH2O.2,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B6,1,denvillewithaxygenbase_96_wellplate_200ul,2,F7,4\\nset5_fecalTubes1to24,tH2O.2,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B6,1,denvillewithaxygenbase_96_wellplate_200ul,5,F7,4\\nset5_fecalTubes1to24,fecal_t21_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C6,1,denvillewithaxygenbase_96_wellplate_200ul,2,G7,4\\nset5_fecalTubes1to24,fecal_t21_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C6,1,denvillewithaxygenbase_96_wellplate_200ul,5,G7,4\\nset5_fecalTubes1to24,fecal_t22_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D6,1,denvillewithaxygenbase_96_wellplate_200ul,2,H7,4\\nset5_fecalTubes1to24,fecal_t22_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D6,1,denvillewithaxygenbase_96_wellplate_200ul,5,H7,4\\nset6.1_fecalTubes25to32,fecal_t23_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A1,1,denvillewithaxygenbase_96_wellplate_200ul,2,A8,4\\nset6.1_fecalTubes25to32,fecal_t23_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A1,1,denvillewithaxygenbase_96_wellplate_200ul,5,A8,4\\nset6.1_fecalTubes25to32,fecal_t24_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B1,1,denvillewithaxygenbase_96_wellplate_200ul,2,B8,4\\nset6.1_fecalTubes25to32,fecal_t24_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B1,1,denvillewithaxygenbase_96_wellplate_200ul,5,B8,4\\nset6.1_fecalTubes25to32,fecal_t25_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C1,1,denvillewithaxygenbase_96_wellplate_200ul,2,C8,4\\nset6.1_fecalTubes25to32,fecal_t25_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C1,1,denvillewithaxygenbase_96_wellplate_200ul,5,C8,4\\nset6.1_fecalTubes25to32,fecal_t26_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D1,1,denvillewithaxygenbase_96_wellplate_200ul,2,D8,4\\nset6.1_fecalTubes25to32,fecal_t26_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D1,1,denvillewithaxygenbase_96_wellplate_200ul,5,D8,4\\nset6.1_fecalTubes25to32,fecal_t27_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A2,1,denvillewithaxygenbase_96_wellplate_200ul,2,E8,4\\nset6.1_fecalTubes25to32,fecal_t27_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A2,1,denvillewithaxygenbase_96_wellplate_200ul,5,E8,4\\nset6.1_fecalTubes25to32,fecal_t28_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B2,1,denvillewithaxygenbase_96_wellplate_200ul,2,F8,4\\nset6.1_fecalTubes25to32,fecal_t28_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B2,1,denvillewithaxygenbase_96_wellplate_200ul,5,F8,4\\nset6.1_fecalTubes25to32,fecal_t29_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C2,1,denvillewithaxygenbase_96_wellplate_200ul,2,G8,4\\nset6.1_fecalTubes25to32,fecal_t29_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C2,1,denvillewithaxygenbase_96_wellplate_200ul,5,G8,4\\nset6.1_fecalTubes25to32,fecal_t30_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D2,1,denvillewithaxygenbase_96_wellplate_200ul,2,H8,4\\nset6.1_fecalTubes25to32,fecal_t30_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D2,1,denvillewithaxygenbase_96_wellplate_200ul,5,H8,4\\nset6.2_xtnPlate3_e1,hair_p3.C5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C5,1,denvillewithaxygenbase_96_wellplate_200ul,2,B9,4\\nset6.2_xtnPlate3_e1,hair_p3.C5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C5,1,denvillewithaxygenbase_96_wellplate_200ul,5,B9,4\\nset6.2_xtnPlate3_e1,hair_xtnNeg_p3.C4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C4,1,denvillewithaxygenbase_96_wellplate_200ul,2,C9,4\\nset6.2_xtnPlate3_e1,hair_xtnNeg_p3.C4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C4,1,denvillewithaxygenbase_96_wellplate_200ul,5,C9,4\\nset6.2_xtnPlate3_e1,hair_p3.C10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C10,1,denvillewithaxygenbase_96_wellplate_200ul,2,G9,4\\nset6.2_xtnPlate3_e1,hair_p3.C10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C10,1,denvillewithaxygenbase_96_wellplate_200ul,5,G9,4\\nset6.2_xtnPlate3_e1,hair_p3.D10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D10,1,denvillewithaxygenbase_96_wellplate_200ul,2,H9,4\\nset6.2_xtnPlate3_e1,hair_p3.D10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D10,1,denvillewithaxygenbase_96_wellplate_200ul,5,H9,4\\nset6.2_xtnPlate3_e1,hair_p3.H10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H10,1,denvillewithaxygenbase_96_wellplate_200ul,2,A10,4\\nset6.2_xtnPlate3_e1,hair_p3.H10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H10,1,denvillewithaxygenbase_96_wellplate_200ul,5,A10,4\\nset7.1_xtnPlate3_e2,hair_p3.D2_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,D2,1,denvillewithaxygenbase_96_wellplate_200ul,2,A9,4\\nset7.1_xtnPlate3_e2,hair_p3.D2_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,D2,1,denvillewithaxygenbase_96_wellplate_200ul,5,A9,4\\nset7.1_xtnPlate3_e2,hair_p3.F6_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,F6,1,denvillewithaxygenbase_96_wellplate_200ul,2,D9,4\\nset7.1_xtnPlate3_e2,hair_p3.F6_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,F6,1,denvillewithaxygenbase_96_wellplate_200ul,5,D9,4\\nset7.1_xtnPlate3_e2,hair_p3.E7_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,E7,1,denvillewithaxygenbase_96_wellplate_200ul,2,E9,4\\nset7.1_xtnPlate3_e2,hair_p3.E7_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,E7,1,denvillewithaxygenbase_96_wellplate_200ul,5,E9,4\\nset7.1_xtnPlate3_e2,hair_p3.F7_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,F7,1,denvillewithaxygenbase_96_wellplate_200ul,2,F9,4\\nset7.1_xtnPlate3_e2,hair_p3.F7_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,F7,1,denvillewithaxygenbase_96_wellplate_200ul,5,F9,4\\nset7.2_xtnPlate4_e1,hair_p4.B4_e1,denvillewithaxygenbase_96_wellplate_200ul,1,B4,1,denvillewithaxygenbase_96_wellplate_200ul,2,E10,4\\nset7.2_xtnPlate4_e1,hair_p4.B4_e1,denvillewithaxygenbase_96_wellplate_200ul,1,B4,1,denvillewithaxygenbase_96_wellplate_200ul,5,E10,4\\nset7.2_xtnPlate4_e1,hair_p4.H8_e1,denvillewithaxygenbase_96_wellplate_200ul,1,H8,1,denvillewithaxygenbase_96_wellplate_200ul,2,B11,4\\nset7.2_xtnPlate4_e1,hair_p4.H8_e1,denvillewithaxygenbase_96_wellplate_200ul,1,H8,1,denvillewithaxygenbase_96_wellplate_200ul,5,B11,4\\nset7.2_xtnPlate4_e1,hair_xtnNeg_p4.C4_e1,denvillewithaxygenbase_96_wellplate_200ul,1,C4,1,denvillewithaxygenbase_96_wellplate_200ul,2,F11,4\\nset7.2_xtnPlate4_e1,hair_xtnNeg_p4.C4_e1,denvillewithaxygenbase_96_wellplate_200ul,1,C4,1,denvillewithaxygenbase_96_wellplate_200ul,5,F11,4\\nset7.3_xtnPlate4_e2,hair_p4.C1_e2,denvillewithaxygenbase_96_wellplate_200ul,4,C1,1,denvillewithaxygenbase_96_wellplate_200ul,2,B10,4\\nset7.3_xtnPlate4_e2,hair_p4.C1_e2,denvillewithaxygenbase_96_wellplate_200ul,4,C1,1,denvillewithaxygenbase_96_wellplate_200ul,5,B10,4\\nset7.3_xtnPlate4_e2,hair_p4.H2_e2,denvillewithaxygenbase_96_wellplate_200ul,4,H2,1,denvillewithaxygenbase_96_wellplate_200ul,2,C10,4\\nset7.3_xtnPlate4_e2,hair_p4.H2_e2,denvillewithaxygenbase_96_wellplate_200ul,4,H2,1,denvillewithaxygenbase_96_wellplate_200ul,5,C10,4\\nset7.3_xtnPlate4_e2,hair_p4.F3_e2,denvillewithaxygenbase_96_wellplate_200ul,4,F3,1,denvillewithaxygenbase_96_wellplate_200ul,2,D10,4\\nset7.3_xtnPlate4_e2,hair_p4.F3_e2,denvillewithaxygenbase_96_wellplate_200ul,4,F3,1,denvillewithaxygenbase_96_wellplate_200ul,5,D10,4\\nset7.3_xtnPlate4_e2,hair_p4.A5_e2,denvillewithaxygenbase_96_wellplate_200ul,4,A5,1,denvillewithaxygenbase_96_wellplate_200ul,2,F10,4\\nset7.3_xtnPlate4_e2,hair_p4.A5_e2,denvillewithaxygenbase_96_wellplate_200ul,4,A5,1,denvillewithaxygenbase_96_wellplate_200ul,5,F10,4\\nset7.3_xtnPlate4_e2,hair_p4.B5_e2,denvillewithaxygenbase_96_wellplate_200ul,4,B5,1,denvillewithaxygenbase_96_wellplate_200ul,2,G10,4\\nset7.3_xtnPlate4_e2,hair_p4.B5_e2,denvillewithaxygenbase_96_wellplate_200ul,4,B5,1,denvillewithaxygenbase_96_wellplate_200ul,5,G10,4\\nset7.3_xtnPlate4_e2,hair_p4.H5_e2,denvillewithaxygenbase_96_wellplate_200ul,4,H5,1,denvillewithaxygenbase_96_wellplate_200ul,2,H10,4\\nset7.3_xtnPlate4_e2,hair_p4.H5_e2,denvillewithaxygenbase_96_wellplate_200ul,4,H5,1,denvillewithaxygenbase_96_wellplate_200ul,5,H10,4\\nset7.3_xtnPlate4_e2,hair_p4.G8_e2,denvillewithaxygenbase_96_wellplate_200ul,4,G8,1,denvillewithaxygenbase_96_wellplate_200ul,2,A11,4\\nset7.3_xtnPlate4_e2,hair_p4.G8_e2,denvillewithaxygenbase_96_wellplate_200ul,4,G8,1,denvillewithaxygenbase_96_wellplate_200ul,5,A11,4\\nset7.4_hairTubes,hair_t1_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A1,1,denvillewithaxygenbase_96_wellplate_200ul,2,C11,4\\nset7.4_hairTubes,hair_t1_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A1,1,denvillewithaxygenbase_96_wellplate_200ul,5,C11,4\\nset7.4_hairTubes,hair_t2_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B1,1,denvillewithaxygenbase_96_wellplate_200ul,2,D11,4\\nset7.4_hairTubes,hair_t2_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B1,1,denvillewithaxygenbase_96_wellplate_200ul,5,D11,4\\nset7.4_hairTubes,hair_t7_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C1,1,denvillewithaxygenbase_96_wellplate_200ul,2,E11,4\\nset7.4_hairTubes,hair_t7_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C1,1,denvillewithaxygenbase_96_wellplate_200ul,5,E11,4\\nset7.4_hairTubes,hair_t23_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D1,1,denvillewithaxygenbase_96_wellplate_200ul,2,G11,4\\nset7.4_hairTubes,hair_t23_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D1,1,denvillewithaxygenbase_96_wellplate_200ul,5,G11,4\\nset7.4_hairTubes,hair_t49_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A2,1,denvillewithaxygenbase_96_wellplate_200ul,2,H11,4\\nset7.4_hairTubes,hair_t49_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A2,1,denvillewithaxygenbase_96_wellplate_200ul,5,H11,4\\nset7.4_hairTubes,hair_t55_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B2,1,denvillewithaxygenbase_96_wellplate_200ul,2,A12,4\\nset7.4_hairTubes,hair_t55_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B2,1,denvillewithaxygenbase_96_wellplate_200ul,5,A12,4\\nset7.4_hairTubes,hair_t62_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C2,1,denvillewithaxygenbase_96_wellplate_200ul,2,B12,4\\nset7.4_hairTubes,hair_t62_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C2,1,denvillewithaxygenbase_96_wellplate_200ul,5,B12,4\\nset7.4_hairTubes,hair_t76_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D2,1,denvillewithaxygenbase_96_wellplate_200ul,2,C12,4\\nset7.4_hairTubes,hair_t76_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D2,1,denvillewithaxygenbase_96_wellplate_200ul,5,C12,4\\nset7.4_hairTubes,hair_t86_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A3,1,denvillewithaxygenbase_96_wellplate_200ul,2,D12,4\\nset7.4_hairTubes,hair_t86_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A3,1,denvillewithaxygenbase_96_wellplate_200ul,5,D12,4\\nset7.4_hairTubes,hair_t96_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B3,1,denvillewithaxygenbase_96_wellplate_200ul,2,E12,4\\nset7.4_hairTubes,hair_t96_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B3,1,denvillewithaxygenbase_96_wellplate_200ul,5,E12,4\\nset7.4_hairTubes,hair_t110_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C3,1,denvillewithaxygenbase_96_wellplate_200ul,2,F12,4\\nset7.4_hairTubes,hair_t110_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C3,1,denvillewithaxygenbase_96_wellplate_200ul,5,F12,4\\nset7.4_hairTubes,hair_t169_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D3,1,denvillewithaxygenbase_96_wellplate_200ul,2,G12,4\\nset7.4_hairTubes,hair_t169_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D3,1,denvillewithaxygenbase_96_wellplate_200ul,5,G12,4\\nset7.4_hairTubes,hair_tx105B_e2,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A4,1,denvillewithaxygenbase_96_wellplate_200ul,2,H12,4\\nset7.4_hairTubes,hair_tx105B_e2,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A4,1,denvillewithaxygenbase_96_wellplate_200ul,5,H12,4\\nset8_water.mm,nf-water,denvillewithaxygenbase_96_wellplate_200ul,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A1,2\\nset8_water.mm,nf-water,denvillewithaxygenbase_96_wellplate_200ul,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A2,2\\nset8_water.mm,nf-water,denvillewithaxygenbase_96_wellplate_200ul,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A3,2\\nset8_water.mm,nf-water,denvillewithaxygenbase_96_wellplate_200ul,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A4,2\\nset8_water.mm,nf-water,denvillewithaxygenbase_96_wellplate_200ul,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A1,2\\nset8_water.mm,nf-water,denvillewithaxygenbase_96_wellplate_200ul,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A2,2\\nset8_water.mm,nf-water,denvillewithaxygenbase_96_wellplate_200ul,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A3,2\\nset8_water.mm,nf-water,denvillewithaxygenbase_96_wellplate_200ul,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A4,2\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A1,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A2,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A3,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A4,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A5,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A6,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A7,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A8,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A9,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A10,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A11,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A12,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A3,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A1,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A3,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A2,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A3,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A3,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A3,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A4,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A3,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A5,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A3,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A6,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A3,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A7,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A3,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A8,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A3,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A9,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A3,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A10,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A3,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A11,6\\nset8_water.mm,mastermix,denvillewithaxygenbase_96_wellplate_200ul,6,A3,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A12,6\\n","pipette_type_s20":"p20_single_gen2","pipette_mount_s20":"left","tip_type_s20":"opentrons_96_filtertiprack_20ul","tip_reuse_s20":"always", "pipette_type_m20":"p20_multi_gen2","pipette_mount_m20":"right","tip_type_m20":"opentrons_96_filtertiprack_20ul","tip_reuse_m20":"always"}""")
    return [_all_values[n] for n in names]


metadata = {
    'apiLevel': '2.8',
    'protocolName': '30x3_pcr1setup',
    'author': 'Rachel Voyt',
    'source': 'Custom Protocol Request',
    'description': '''This protocol is a modified version of the 'Custom CSV Transfer' protocol from OT2. The protocol includes steps to transfer mastermix & samples, with adjustments to add a blowout after each transfer as well as a mix step after the water/mastermix transfer. The protocol also allows for the use of two pipette types (p20_single and p20_multi, both with filter tips) and includes pauses to switch out xtn plates & tubes.'''
}

def run(protocol):

    [pipette_type_s20,
     pipette_mount_s20,
     tip_type_s20,
     tip_reuse_s20,
     pipette_type_m20,
     pipette_mount_m20,
     tip_type_m20,
     tip_reuse_m20,
     transfer_csv] = get_values(  # noqa: F821
        "pipette_type_s20",
        "pipette_mount_s20",
        "tip_type_s20",
        "tip_reuse_s20",
        "pipette_type_m20",
        "pipette_mount_m20",
        "tip_type_m20",
        "tip_reuse_m20",
        "transfer_csv")

    # strip headers
    transfer_info = [[val.strip().lower() for val in line.split(',')]
                     for line in transfer_csv.splitlines()
                     if line.split(',')[0].strip()][1:]

    # load labware
    for line in transfer_info:
        s_lw, s_slot, d_lw, d_slot = line[2:4] + line[6:8]
        for slot, lw in zip([s_slot, d_slot], [s_lw, d_lw]):
            if not int(slot) in protocol.loaded_labwares:
                if slot == '7' and lw.lower() == 'nest_96_wellplate_100ul_pcr_full_skirt':
                    # Load the magnetic module
                    magdeck = protocol.load_module('magnetic module gen2', slot)

                    # Load the labware onto the magnetic module
                    nestMagblock = magdeck.load_labware('nest_96_wellplate_100ul_pcr_full_skirt')
                else:
                    # Load other regular labware not compatible with the magnetic module
                    protocol.load_labware(lw.lower(), slot)

    # load tipracks
    tipracks_s20 = [protocol.load_labware(tip_type_s20, slot)
            for slot in ['10', '11']]
    tipracks_m20 = [protocol.load_labware(tip_type_m20, slot)
            for slot in ['8', '9']]

    # load pipettes
    s20 = protocol.load_instrument(pipette_type_s20, pipette_mount_s20, tip_racks=tipracks_s20)
    m20 = protocol.load_instrument(pipette_type_m20, pipette_mount_m20, tip_racks=tipracks_m20)

    s20.flow_rate.aspirate = 1
    s20.flow_rate.dispense = 1
            
    tip_count_s20 = 0
    tip_count_m20 = 0

    tip_max_s20 = len(tipracks_s20*96)
    tip_max_m20 = len(tipracks_m20*96)

    def pick_up_s20():
        nonlocal tip_count_s20
        if tip_count_s20 == tip_max_s20:
            protocol.pause('Please refill 20 ul tipracks for s20 before resuming.')
            s20.reset_tipracks()
            tip_count_s20 = 0
        s20.pick_up_tip()
        tip_count_s20 += 1

    def pick_up_m20():
        nonlocal tip_count_m20
        if tip_count_m20 == tip_max_m20:
            protocol.pause('Please refill 20 ul tipracks for m20 before resuming.')
            m20.reset_tipracks()
            tip_count_m20 = 0
        m20.pick_up_tip()
        tip_count_m20 += 8

    def parse_well(well):
        letter = well[0]
        number = well[1:]
        return letter.upper() + str(int(number))

    if tip_reuse_s20 == 'never':
        pick_up_s20()
    if tip_reuse_m20 == 'never':
        pick_up_m20()

    # transfers for SET 1: xtnPlate1_e1
    magdeck.engage()
    for line in transfer_info:
        if line[0].startswith('set1'):
            _, _, _, s_slot, s_well, h, _, d_slot, d_well, vol = line[:10]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)]
            if tip_reuse_s20 == 'always':
                pick_up_s20()
            s20.transfer(float(vol),
                        source,
                        dest,
                        blow_out = True,
                        blowout_location = 'destination well',
                        new_tip = 'never')
            if tip_reuse_s20 == 'always':
                s20.drop_tip()
    if s20.hw_pipette['has_tip']:
        s20.drop_tip()

    magdeck.disengage()

    # PAUSE 1: switch to xtnPlate1_e2
    protocol.pause("PAUSE 1: i) Remove xtnPlate1_e1. Seal and place on ice. ii) Check pcr plates to ensure that sufficient xtn volume was transfered AND that no beads were transferred. iii) For any wells with insufficient volume and/or beads, remove beads and/or manually transfer the sample. iv) Place xtnPlate1_e2 on magblock and resume run.")

    # transfers for SET 2: xtnPlate1_e2
    magdeck.engage()
    for line in transfer_info:
        if line[0].startswith('set2'):
            _, _, _, s_slot, s_well, h, _, d_slot, d_well, vol = line[:10]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)]
            if tip_reuse_s20 == 'always':
                pick_up_s20()
            s20.transfer(float(vol),
                        source,
                        dest,
                        blow_out = True,
                        blowout_location = 'destination well',
                        new_tip = 'never')
            if tip_reuse_s20 == 'always':
                s20.drop_tip()
    if s20.hw_pipette['has_tip']:
        s20.drop_tip()

    magdeck.disengage()

    # PAUSE 2: switch to xtnPlate2_e1
    protocol.pause("PAUSE 2: i) Remove xtnPlate1_e2. Seal and place on ice. ii) Check pcr plates to ensure that sufficient xtn volume was transfered AND that no beads were transferred. iii) For any wells with insufficient volume and/or beads, remove beads and/or manually transfer the sample. iv) Place xtnPlate2_e1 on magblock and resume run.")

    # transfers for SET 3: xtnPlate2_e1
    magdeck.engage()
    for line in transfer_info:
        if line[0].startswith('set3'):
            _, _, _, s_slot, s_well, h, _, d_slot, d_well, vol = line[:10]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)]
            if tip_reuse_s20 == 'always':
                pick_up_s20()
            s20.transfer(float(vol),
                        source,
                        dest,
                        blow_out = True,
                        blowout_location = 'destination well',
                        new_tip = 'never')
            if tip_reuse_s20 == 'always':
                s20.drop_tip()
    if s20.hw_pipette['has_tip']:
        s20.drop_tip()
    
    magdeck.disengage()

    # PAUSE 3: switch to xtnPlate2_e2 + blood xtn tubes
    protocol.pause("PAUSE 3: Remove xtnPlate2_e1. Seal and place on ice. ii) Check pcr plates to ensure that sufficient xtn volume was transfered AND that no beads were transferred. iii) For any wells with insufficient volume and/or beads, remove beads and/or manually transfer the sample. iv) Place xtnPlate2_e2 on magblock and blood xtn tubes on tuberack following **Deck plan: Set 4** on quip and resume run.")

    # transfers for SET 4: xtnPlate2_e2 + blood xtn tubes
    magdeck.engage()
    for line in transfer_info:
        if line[0].startswith('set4.1'):
            _, _, _, s_slot, s_well, h, _, d_slot, d_well, vol = line[:10]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)]
            if tip_reuse_s20 == 'always':
                pick_up_s20()
            s20.transfer(float(vol),
                        source,
                        dest,
                        blow_out = True,
                        blowout_location = 'destination well',
                        new_tip = 'never')
            if tip_reuse_s20 == 'always':
                s20.drop_tip()
        if line[0].startswith('set4.2'):
            _, _, _, s_slot, s_well, h, _, d_slot, d_well, vol = line[:10]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)]
            if tip_reuse_s20 == 'always':
                pick_up_s20()
            s20.transfer(float(vol),
                        source,
                        dest,
                        blow_out = True,
                        blowout_location = 'destination well',
                        new_tip = 'never')
            if tip_reuse_s20 == 'always':
                s20.drop_tip()
    if s20.hw_pipette['has_tip']:
        s20.drop_tip()

    magdeck.disengage()

    # PAUSE 4: switch to fecal xtn tubes 1 to 24
    protocol.pause("PAUSE 4: i) Remove xtnPlate2_e2. Seal and place on ice. ii) Check pcr plates to ensure that sufficient xtn volume was transfered AND that no beads were transferred. iii) For any wells with insufficient volume and/or beads, remove beads and/or manually transfer the sample. iv) Place fecal xtn tubes 1 to 24 on tuberack following **Deck plan: Set 5** on quip and resume run.")

    # transfers for SET 5: fecal xtn tubes 1 to 24
    for line in transfer_info:
        if line[0].startswith('set5'):
            _, _, _, s_slot, s_well, h, _, d_slot, d_well, vol = line[:10]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)]
            if tip_reuse_s20 == 'always':
                pick_up_s20()
            s20.transfer(float(vol),
                        source,
                        dest,
                        blow_out = True,
                        blowout_location = 'destination well',
                        new_tip = 'never')
            if tip_reuse_s20 == 'always':
                s20.drop_tip()
    if s20.hw_pipette['has_tip']:
        s20.drop_tip()

    # PAUSE 5: switch to fecal xtn tubes 25 to 32 + xtnPlate3_e1
    protocol.pause("PAUSE 5: i) Remove fecal xtn tubes 1 to 24 and place on ice. ii) Check pcr plates to ensure that sufficient xtn volume was transfered AND that no beads were transferred. iii) For any wells with insufficient volume and/or beads, remove beads and/or manually transfer the sample. iv) Place fecal xtn tubes 25 to 32 on tuberack and xtnPlate3_e1 on magblock following **Deck plan: Set 6** on quip and resume run.")

    # transfers for SET 6: fecal xtn tubes 25 to 32 + xtnPlate3_e1
    magdeck.engage()
    for line in transfer_info:
        if line[0].startswith('set6.1'):
            _, _, _, s_slot, s_well, h, _, d_slot, d_well, vol = line[:10]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)]
            if tip_reuse_s20 == 'always':
                pick_up_s20()
            s20.transfer(float(vol),
                        source,
                        dest,
                        blow_out = True,
                        blowout_location = 'destination well',
                        new_tip = 'never')
            if tip_reuse_s20 == 'always':
                s20.drop_tip()
        if line[0].startswith('set6.2'):
            _, _, _, s_slot, s_well, h, _, d_slot, d_well, vol = line[:10]
            source = protocol.loaded_labwares[
            int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)]
            if tip_reuse_s20 == 'always':
                pick_up_s20()
            s20.transfer(float(vol),
                        source,
                        dest,
                        blow_out = True,
                        blowout_location = 'destination well',
                        new_tip = 'never')
            if tip_reuse_s20 == 'always':
                s20.drop_tip()
    if s20.hw_pipette['has_tip']:
        s20.drop_tip()

    magdeck.disengage()

    # PAUSE 6: switch to xtnPlate3_e2 + xtnPlate4_e1 + xtnPlate4_e2 + hair xtn tubes
    protocol.pause("PAUSE 6: i) Remove fecal xtn tubes 25 to 32 + xtnPlate3_e1. Seal and place on ice. ii) Check pcr plates to ensure that sufficient xtn volume was transfered AND that no beads were transferred. iii) For any wells with insufficient volume and/or beads, remove beads and/or manually transfer the sample. iv) Place xtnPlate3_e2 + xtnPlate4_e1 + xtnPlate4_e2 + hair xtn tubes on OT2 deck following **Deck plan: Set 7** on quip.")

    # transfers for SET 7: xtnPlate3_e2 + xtnPlate4_e1 + xtnPlate4_e2 + hair xtn tubes
    magdeck.engage()
    for line in transfer_info:
        if line[0].startswith('set7.1'):
            _, _, _, s_slot, s_well, h, _, d_slot, d_well, vol = line[:10]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)]
            if tip_reuse_s20 == 'always':
                pick_up_s20()
            s20.transfer(float(vol),
                        source,
                        dest,
                        blow_out = True,
                        blowout_location = 'destination well',
                        new_tip = 'never')
            if tip_reuse_s20 == 'always':
                s20.drop_tip()
        if line[0].startswith('set7.2'):
            _, _, _, s_slot, s_well, h, _, d_slot, d_well, vol = line[:10]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)]
            if tip_reuse_s20 == 'always':
                pick_up_s20()
            s20.transfer(float(vol),
                        source,
                        dest,
                        blow_out = True,
                        blowout_location = 'destination well',
                        new_tip = 'never')
            if tip_reuse_s20 == 'always':
                s20.drop_tip()
        if line[0].startswith('set7.3'):
            _, _, _, s_slot, s_well, h, _, d_slot, d_well, vol = line[:10]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)]
            if tip_reuse_s20 == 'always':
                pick_up_s20()
            s20.transfer(float(vol),
                        source,
                        dest,
                        blow_out = True,
                        blowout_location = 'destination well',
                        new_tip = 'never')
            if tip_reuse_s20 == 'always':
                s20.drop_tip()
        if line[0].startswith('set7.4'):
            _, _, _, s_slot, s_well, h, _, d_slot, d_well, vol = line[:10]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)]
            if tip_reuse_s20 == 'always':
                pick_up_s20()
            s20.transfer(float(vol),
                        source,
                        dest,
                        blow_out = True,
                        blowout_location = 'destination well',
                        new_tip = 'never')
            if tip_reuse_s20 == 'always':
                s20.drop_tip()
    if s20.hw_pipette['has_tip']:
        s20.drop_tip()

    magdeck.disengage()

    # PAUSE 7: switch to water/mastermix
    protocol.pause("PAUSE 7: i) Remove xtnPlate3_e2, xtnPlate4_e1, xtnPlate4_e2, and fecal xtn tubes. Seal and place on ice. ii) Check pcr plates to ensure that sufficient xtn volume was transfered AND that no beads were transferred. iii) For any wells with insufficient volume and/or beads, remove beads and/or manually transfer the sample. iv) Place reagent plate with water and mastermix on OT2 deck following **Deck plan: Set 8** on quip.")

    # transfers for SET 8: water & mastermix
    for line in transfer_info:
        if line[0].startswith('set8'):
            _, _, _, s_slot, s_well, h, _, d_slot, d_well, vol = line[:10]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)]
            if tip_reuse_m20 == 'always':
                pick_up_m20()
            if float(vol) < 4:
                m20.flow_rate.aspirate = 1
                m20.flow_rate.dispense = 1
                m20.transfer(float(vol),
                        source,
                        dest,
                        blow_out = True,
                        blowout_location = 'destination well',
                        new_tip = 'never')
                if tip_reuse_m20 == 'always':
                        m20.drop_tip()
            else:
                m20.flow_rate.aspirate = 7.6
                m20.flow_rate.dispense = 7.6
                m20.transfer(float(vol),
                            source,
                            dest,
                            mix_before = (3, 10),
                            mix_after = (5, 5),
                            blow_out = True,
                            blowout_location = 'destination well',
                            new_tip = 'never')
                if tip_reuse_m20 == 'always':
                        m20.drop_tip()
    if m20.hw_pipette['has_tip']:
        m20.drop_tip()