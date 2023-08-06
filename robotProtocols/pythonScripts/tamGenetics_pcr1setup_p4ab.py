def get_values(*names):
    import json
    _all_values = json.loads("""{"transfer_csv":"ot2set,reagent,source_labware,source_slot,source_well,asp_height,dest_labware,dest_slot,dest_well,transfer_volume\\nset1.1_xtnPlate4_e1,hair_p4.A1_e1,denvillewithaxygenbase_96_wellplate_200ul,1,A1,1,denvillewithaxygenbase_96_wellplate_200ul,2,A1,4\\nset1.1_xtnPlate4_e1,hair_p4.B1_e1,denvillewithaxygenbase_96_wellplate_200ul,1,B1,1,denvillewithaxygenbase_96_wellplate_200ul,2,B1,4\\nset1.1_xtnPlate4_e1,hair_p4.D1_e1,denvillewithaxygenbase_96_wellplate_200ul,1,D1,1,denvillewithaxygenbase_96_wellplate_200ul,2,D1,4\\nset1.1_xtnPlate4_e1,hair_p4.E1_e1,denvillewithaxygenbase_96_wellplate_200ul,1,E1,1,denvillewithaxygenbase_96_wellplate_200ul,2,E1,4\\nset1.1_xtnPlate4_e1,hair_p4.F1_e1,denvillewithaxygenbase_96_wellplate_200ul,1,F1,1,denvillewithaxygenbase_96_wellplate_200ul,2,F1,4\\nset1.1_xtnPlate4_e1,hair_p4.G1_e1,denvillewithaxygenbase_96_wellplate_200ul,1,G1,1,denvillewithaxygenbase_96_wellplate_200ul,2,G1,4\\nset1.1_xtnPlate4_e1,hair_p4.H1_e1,denvillewithaxygenbase_96_wellplate_200ul,1,H1,1,denvillewithaxygenbase_96_wellplate_200ul,2,H1,4\\nset1.1_xtnPlate4_e1,hair_p4.A2_e1,denvillewithaxygenbase_96_wellplate_200ul,1,A2,1,denvillewithaxygenbase_96_wellplate_200ul,2,A2,4\\nset1.1_xtnPlate4_e1,hair_p4.B2_e1,denvillewithaxygenbase_96_wellplate_200ul,1,B2,1,denvillewithaxygenbase_96_wellplate_200ul,2,B2,4\\nset1.1_xtnPlate4_e1,hair_p4.C2_e1,denvillewithaxygenbase_96_wellplate_200ul,1,C2,1,denvillewithaxygenbase_96_wellplate_200ul,2,C2,4\\nset1.1_xtnPlate4_e1,hair_p4.D2_e1,denvillewithaxygenbase_96_wellplate_200ul,1,D2,1,denvillewithaxygenbase_96_wellplate_200ul,2,D2,4\\nset1.1_xtnPlate4_e1,hair_p4.E2_e1,denvillewithaxygenbase_96_wellplate_200ul,1,E2,1,denvillewithaxygenbase_96_wellplate_200ul,2,E2,4\\nset1.1_xtnPlate4_e1,hair_p4.F2_e1,denvillewithaxygenbase_96_wellplate_200ul,1,F2,1,denvillewithaxygenbase_96_wellplate_200ul,2,F2,4\\nset1.1_xtnPlate4_e1,hair_p4.G2_e1,denvillewithaxygenbase_96_wellplate_200ul,1,G2,1,denvillewithaxygenbase_96_wellplate_200ul,2,G2,4\\nset1.1_xtnPlate4_e1,hair_p4.A3_e1,denvillewithaxygenbase_96_wellplate_200ul,1,A3,1,denvillewithaxygenbase_96_wellplate_200ul,2,A3,4\\nset1.1_xtnPlate4_e1,hair_p4.B3_e1,denvillewithaxygenbase_96_wellplate_200ul,1,B3,1,denvillewithaxygenbase_96_wellplate_200ul,2,B3,4\\nset1.1_xtnPlate4_e1,hair_p4.C3_e1,denvillewithaxygenbase_96_wellplate_200ul,1,C3,1,denvillewithaxygenbase_96_wellplate_200ul,2,C3,4\\nset1.1_xtnPlate4_e1,hair_p4.D3_e1,denvillewithaxygenbase_96_wellplate_200ul,1,D3,1,denvillewithaxygenbase_96_wellplate_200ul,2,D3,4\\nset1.1_xtnPlate4_e1,hair_p4.E3_e1,denvillewithaxygenbase_96_wellplate_200ul,1,E3,1,denvillewithaxygenbase_96_wellplate_200ul,2,E3,4\\nset1.1_xtnPlate4_e1,hair_p4.G3_e1,denvillewithaxygenbase_96_wellplate_200ul,1,G3,1,denvillewithaxygenbase_96_wellplate_200ul,2,G3,4\\nset1.1_xtnPlate4_e1,hair_p4.H3_e1,denvillewithaxygenbase_96_wellplate_200ul,1,H3,1,denvillewithaxygenbase_96_wellplate_200ul,2,H3,4\\nset1.1_xtnPlate4_e1,hair_p4.A4_e1,denvillewithaxygenbase_96_wellplate_200ul,1,A4,1,denvillewithaxygenbase_96_wellplate_200ul,2,A4,4\\nset1.1_xtnPlate4_e1,hair_p4.B4_e1,denvillewithaxygenbase_96_wellplate_200ul,1,B4,1,denvillewithaxygenbase_96_wellplate_200ul,2,B4,4\\nset1.1_xtnPlate4_e1,xtnNeg_p4.C4_e1,denvillewithaxygenbase_96_wellplate_200ul,1,C4,1,denvillewithaxygenbase_96_wellplate_200ul,2,C4,4\\nset1.1_xtnPlate4_e1,hair_p4.D4_e1,denvillewithaxygenbase_96_wellplate_200ul,1,D4,1,denvillewithaxygenbase_96_wellplate_200ul,2,D4,4\\nset1.1_xtnPlate4_e1,hair_p4.E4_e1,denvillewithaxygenbase_96_wellplate_200ul,1,E4,1,denvillewithaxygenbase_96_wellplate_200ul,2,E4,4\\nset1.1_xtnPlate4_e1,hair_p4.F4_e1,denvillewithaxygenbase_96_wellplate_200ul,1,F4,1,denvillewithaxygenbase_96_wellplate_200ul,2,F4,4\\nset1.1_xtnPlate4_e1,hair_p4.G4_e1,denvillewithaxygenbase_96_wellplate_200ul,1,G4,1,denvillewithaxygenbase_96_wellplate_200ul,2,G4,4\\nset1.1_xtnPlate4_e1,hair_p4.H4_e1,denvillewithaxygenbase_96_wellplate_200ul,1,H4,1,denvillewithaxygenbase_96_wellplate_200ul,2,H4,4\\nset1.1_xtnPlate4_e1,hair_p4.C5_e1,denvillewithaxygenbase_96_wellplate_200ul,1,C5,1,denvillewithaxygenbase_96_wellplate_200ul,2,C5,4\\nset1.1_xtnPlate4_e1,hair_p4.D5_e1,denvillewithaxygenbase_96_wellplate_200ul,1,D5,1,denvillewithaxygenbase_96_wellplate_200ul,2,D5,4\\nset1.1_xtnPlate4_e1,hair_p4.E5_e1,denvillewithaxygenbase_96_wellplate_200ul,1,E5,1,denvillewithaxygenbase_96_wellplate_200ul,2,E5,4\\nset1.1_xtnPlate4_e1,hair_p4.F5_e1,denvillewithaxygenbase_96_wellplate_200ul,1,F5,1,denvillewithaxygenbase_96_wellplate_200ul,2,F5,4\\nset1.1_xtnPlate4_e1,hair_p4.G5_e1,denvillewithaxygenbase_96_wellplate_200ul,1,G5,1,denvillewithaxygenbase_96_wellplate_200ul,2,G5,4\\nset1.1_xtnPlate4_e1,hair_p4.A6_e1,denvillewithaxygenbase_96_wellplate_200ul,1,A6,1,denvillewithaxygenbase_96_wellplate_200ul,2,A6,4\\nset1.1_xtnPlate4_e1,hair_p4.B6_e1,denvillewithaxygenbase_96_wellplate_200ul,1,B6,1,denvillewithaxygenbase_96_wellplate_200ul,2,B6,4\\nset1.1_xtnPlate4_e1,hair_p4.C6_e1,denvillewithaxygenbase_96_wellplate_200ul,1,C6,1,denvillewithaxygenbase_96_wellplate_200ul,2,C6,4\\nset1.1_xtnPlate4_e1,hair_p4.D6_e1,denvillewithaxygenbase_96_wellplate_200ul,1,D6,1,denvillewithaxygenbase_96_wellplate_200ul,2,D6,4\\nset1.1_xtnPlate4_e1,hair_p4.E6_e1,denvillewithaxygenbase_96_wellplate_200ul,1,E6,1,denvillewithaxygenbase_96_wellplate_200ul,2,E6,4\\nset1.1_xtnPlate4_e1,hair_p4.F6_e1,denvillewithaxygenbase_96_wellplate_200ul,1,F6,1,denvillewithaxygenbase_96_wellplate_200ul,2,F6,4\\nset1.1_xtnPlate4_e1,hair_p4.G6_e1,denvillewithaxygenbase_96_wellplate_200ul,1,G6,1,denvillewithaxygenbase_96_wellplate_200ul,2,G6,4\\nset1.1_xtnPlate4_e1,hair_p4.H6_e1,denvillewithaxygenbase_96_wellplate_200ul,1,H6,1,denvillewithaxygenbase_96_wellplate_200ul,2,H6,4\\nset1.1_xtnPlate4_e1,hair_p4.A7_e1,denvillewithaxygenbase_96_wellplate_200ul,1,A7,1,denvillewithaxygenbase_96_wellplate_200ul,2,A7,4\\nset1.1_xtnPlate4_e1,hair_p4.B7_e1,denvillewithaxygenbase_96_wellplate_200ul,1,B7,1,denvillewithaxygenbase_96_wellplate_200ul,2,B7,4\\nset1.1_xtnPlate4_e1,hair_p4.C7_e1,denvillewithaxygenbase_96_wellplate_200ul,1,C7,1,denvillewithaxygenbase_96_wellplate_200ul,2,C7,4\\nset1.1_xtnPlate4_e1,hair_p4.D7_e1,denvillewithaxygenbase_96_wellplate_200ul,1,D7,1,denvillewithaxygenbase_96_wellplate_200ul,2,D7,4\\nset1.1_xtnPlate4_e1,hair_p4.E7_e1,denvillewithaxygenbase_96_wellplate_200ul,1,E7,1,denvillewithaxygenbase_96_wellplate_200ul,2,E7,4\\nset1.1_xtnPlate4_e1,hair_p4.F7_e1,denvillewithaxygenbase_96_wellplate_200ul,1,F7,1,denvillewithaxygenbase_96_wellplate_200ul,2,F7,4\\nset1.1_xtnPlate4_e1,hair_p4.G7_e1,denvillewithaxygenbase_96_wellplate_200ul,1,G7,1,denvillewithaxygenbase_96_wellplate_200ul,2,G7,4\\nset1.1_xtnPlate4_e1,hair_p4.H7_e1,denvillewithaxygenbase_96_wellplate_200ul,1,H7,1,denvillewithaxygenbase_96_wellplate_200ul,2,H7,4\\nset1.1_xtnPlate4_e1,hair_p4.A8_e1,denvillewithaxygenbase_96_wellplate_200ul,1,A8,1,denvillewithaxygenbase_96_wellplate_200ul,2,A8,4\\nset1.1_xtnPlate4_e1,hair_p4.B8_e1,denvillewithaxygenbase_96_wellplate_200ul,1,B8,1,denvillewithaxygenbase_96_wellplate_200ul,2,B8,4\\nset1.1_xtnPlate4_e1,hair_p4.C8_e1,denvillewithaxygenbase_96_wellplate_200ul,1,C8,1,denvillewithaxygenbase_96_wellplate_200ul,2,C8,4\\nset1.1_xtnPlate4_e1,hair_p4.D8_e1,denvillewithaxygenbase_96_wellplate_200ul,1,D8,1,denvillewithaxygenbase_96_wellplate_200ul,2,D8,4\\nset1.1_xtnPlate4_e1,hair_p4.E8_e1,denvillewithaxygenbase_96_wellplate_200ul,1,E8,1,denvillewithaxygenbase_96_wellplate_200ul,2,E8,4\\nset1.1_xtnPlate4_e1,hair_p4.F8_e1,denvillewithaxygenbase_96_wellplate_200ul,1,F8,1,denvillewithaxygenbase_96_wellplate_200ul,2,F8,4\\nset1.1_xtnPlate4_e1,hair_p4.A9_e1,denvillewithaxygenbase_96_wellplate_200ul,1,A9,1,denvillewithaxygenbase_96_wellplate_200ul,2,A9,4\\nset1.1_xtnPlate4_e1,hair_p4.B9_e1,denvillewithaxygenbase_96_wellplate_200ul,1,B9,1,denvillewithaxygenbase_96_wellplate_200ul,2,B9,4\\nset1.1_xtnPlate4_e1,hair_p4.C9_e1,denvillewithaxygenbase_96_wellplate_200ul,1,C9,1,denvillewithaxygenbase_96_wellplate_200ul,2,C9,4\\nset1.1_xtnPlate4_e1,hair_p4.D9_e1,denvillewithaxygenbase_96_wellplate_200ul,1,D9,1,denvillewithaxygenbase_96_wellplate_200ul,2,D9,4\\nset1.1_xtnPlate4_e1,hair_p4.E9_e1,denvillewithaxygenbase_96_wellplate_200ul,1,E9,1,denvillewithaxygenbase_96_wellplate_200ul,2,E9,4\\nset1.1_xtnPlate4_e1,xtnNeg_p4.F9_e1,denvillewithaxygenbase_96_wellplate_200ul,1,F9,1,denvillewithaxygenbase_96_wellplate_200ul,2,F9,4\\nset1.1_xtnPlate4_e1,hair_p4.G9_e1,denvillewithaxygenbase_96_wellplate_200ul,1,G9,1,denvillewithaxygenbase_96_wellplate_200ul,2,G9,4\\nset1.1_xtnPlate4_e1,hair_p4.H9_e1,denvillewithaxygenbase_96_wellplate_200ul,1,H9,1,denvillewithaxygenbase_96_wellplate_200ul,2,H9,4\\nset1.1_xtnPlate4_e1,hair_p4.A10_e1,denvillewithaxygenbase_96_wellplate_200ul,1,A10,1,denvillewithaxygenbase_96_wellplate_200ul,2,A10,4\\nset1.1_xtnPlate4_e1,hair_p4.B10_e1,denvillewithaxygenbase_96_wellplate_200ul,1,B10,1,denvillewithaxygenbase_96_wellplate_200ul,2,B10,4\\nset1.2_xtnPlate4_e2,hair_p4.C1_e2,denvillewithaxygenbase_96_wellplate_200ul,4,C1,1,denvillewithaxygenbase_96_wellplate_200ul,2,C1,4\\nset1.2_xtnPlate4_e2,hair_p4.H2_e2,denvillewithaxygenbase_96_wellplate_200ul,4,H2,1,denvillewithaxygenbase_96_wellplate_200ul,2,H2,4\\nset1.2_xtnPlate4_e2,hair_p4.F3_e2,denvillewithaxygenbase_96_wellplate_200ul,4,F3,1,denvillewithaxygenbase_96_wellplate_200ul,2,F3,4\\nset1.2_xtnPlate4_e2,hair_p4.A5_e2,denvillewithaxygenbase_96_wellplate_200ul,4,A5,1,denvillewithaxygenbase_96_wellplate_200ul,2,A5,4\\nset1.2_xtnPlate4_e2,hair_p4.B5_e2,denvillewithaxygenbase_96_wellplate_200ul,4,B5,1,denvillewithaxygenbase_96_wellplate_200ul,2,B5,4\\nset1.2_xtnPlate4_e2,hair_p4.H5_e2,denvillewithaxygenbase_96_wellplate_200ul,4,H5,1,denvillewithaxygenbase_96_wellplate_200ul,2,H5,4\\nset1.2_xtnPlate4_e2,hair_p4.G8_e2,denvillewithaxygenbase_96_wellplate_200ul,4,G8,1,denvillewithaxygenbase_96_wellplate_200ul,2,G8,4\\nset1.2_xtnPlate4_e2,hair_p4.H8_e2,denvillewithaxygenbase_96_wellplate_200ul,4,H8,1,denvillewithaxygenbase_96_wellplate_200ul,2,H8,4\\nset1.3_xtnPlate.tamTiger1,hair_ptamTiger1.A1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,2,C10,4\\nset1.3_xtnPlate.tamTiger1,hair_ptamTiger1.B1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B1,1,denvillewithaxygenbase_96_wellplate_200ul,2,D10,4\\nset1.4_xtnPlate.tamTiger2,hair_ptamTiger2.A2_e1,nest_96_wellplate_100ul_pcr_full_skirt,10,A2,1,denvillewithaxygenbase_96_wellplate_200ul,2,F10,4\\nset1.5_xtnTubes,hair_t55_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A1,1,denvillewithaxygenbase_96_wellplate_200ul,2,E10,4\\nset1.5_xtnTubes,hair_t1_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B1,1,denvillewithaxygenbase_96_wellplate_200ul,2,G10,4\\nset1.5_xtnTubes,hair_t10_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C1,1,denvillewithaxygenbase_96_wellplate_200ul,2,H10,4\\nset1.5_xtnTubes,hair_t11.T1_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D1,1,denvillewithaxygenbase_96_wellplate_200ul,2,A11,4\\nset1.5_xtnTubes,hair_t12.T1_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A2,1,denvillewithaxygenbase_96_wellplate_200ul,2,B11,4\\nset1.5_xtnTubes,hair_t13.T1_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B2,1,denvillewithaxygenbase_96_wellplate_200ul,2,C11,4\\nset1.5_xtnTubes,hair_t14.T1_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C2,1,denvillewithaxygenbase_96_wellplate_200ul,2,D11,4\\nset1.5_xtnTubes,hair_t15_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D2,1,denvillewithaxygenbase_96_wellplate_200ul,2,E11,4\\nset1.5_xtnTubes,hair_t169_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A3,1,denvillewithaxygenbase_96_wellplate_200ul,2,F11,4\\nset1.5_xtnTubes,hair_t2_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B3,1,denvillewithaxygenbase_96_wellplate_200ul,2,G11,4\\nset1.5_xtnTubes,hair_t3_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C3,1,denvillewithaxygenbase_96_wellplate_200ul,2,H11,4\\nset1.5_xtnTubes,hair_t4_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D3,1,denvillewithaxygenbase_96_wellplate_200ul,2,A12,4\\nset1.5_xtnTubes,hair_t49_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A4,1,denvillewithaxygenbase_96_wellplate_200ul,2,B12,4\\nset1.5_xtnTubes,hair_t5_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B4,1,denvillewithaxygenbase_96_wellplate_200ul,2,C12,4\\nset1.5_xtnTubes,hair_t50_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C4,1,denvillewithaxygenbase_96_wellplate_200ul,2,D12,4\\nset1.5_xtnTubes,hair_t51_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D4,1,denvillewithaxygenbase_96_wellplate_200ul,2,E12,4\\nset1.5_xtnTubes,hair_t52_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A5,1,denvillewithaxygenbase_96_wellplate_200ul,2,F12,4\\nset1.5_xtnTubes,hair_t6_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B5,1,denvillewithaxygenbase_96_wellplate_200ul,2,G12,4\\nset1.5_xtnTubes,hair_t7_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C5,1,denvillewithaxygenbase_96_wellplate_200ul,2,H12,4\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A1,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A2,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A3,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A4,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A5,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A6,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A7,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A8,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A9,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A10,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A11,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A12,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A1,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A2,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A3,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A4,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A5,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A6,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A7,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A8,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A9,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A10,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A11,6\\nset2_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A12,6\\n","pipette_type_s20":"p20_single_gen2","pipette_mount_s20":"left","tip_type_s20":"opentrons_96_filtertiprack_20ul","tip_reuse_s20":"always", "pipette_type_m20":"p20_multi_gen2","pipette_mount_m20":"right","tip_type_m20":"opentrons_96_filtertiprack_20ul","tip_reuse_m20":"always"}""")
    return [_all_values[n] for n in names]

metadata = {
    'apiLevel': '2.8',
    'protocolName': 'tamGenetics_pcr1setup_p4ab',
    'author': 'Rachel Voyt',
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
    pcr1Plates = [protocol.load_labware("denvillewithaxygenbase_96_wellplate_200ul", slot)
                  for slot in ['2', '5']]
    for line in transfer_info:
        s_lw, s_slot, d_lw, d_slot = line[2:4] + line[6:8]
        for slot, lw in zip([s_slot, d_slot], [s_lw, d_lw]):
            if not int(slot) in protocol.loaded_labwares:
                protocol.load_labware(lw.lower(), slot)

    # load tipracks
    tipracks_s20 = [protocol.load_labware(tip_type_s20, slot)
            for slot in ['11']]
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

    # transfers for SET 1: xtnPlate4_e1 + xtnPlate4_e2 + tamTiger12 + hair xtn tubes
    for line in transfer_info:
        if line[0].startswith('set1'):
            _, _, _, s_slot, s_well, h, _, d_slot, d_well, vol = line[:10]
            source_plate = protocol.loaded_labwares[int(s_slot)]
            source_well = source_plate.wells_by_name()[parse_well(s_well)].bottom(float(h))
            dest_wells = [plate.wells_by_name()[parse_well(d_well)] for plate in pcr1Plates]
            if tip_reuse_s20 == 'always':
                pick_up_s20()
            s20.distribute(float(vol),
                           source_well,
                           dest_wells,
                           touch_tip = True,
                           new_tip = 'never',
                           disposal_volume = 1,
                           blow_out = True,
                           blowout_location = 'source well')
            if tip_reuse_s20 == 'always':
                s20.drop_tip()
    if s20.hw_pipette['has_tip']:
        s20.drop_tip()

    # PAUSE 1: switch to mastermix
    protocol.pause("PAUSE 1: i) Remove xtns and set aside. ii) Check pcr plates to ensure that sufficient xtn volume was transfered. iii) For any wells with insufficient volume, manually transfer the sample. iv) Seal xtn plates & tubes and place on ice. Place mastermix and resume run.")

    # Transfers for SET 2: mastermix for pcr1Plate4a/b
    for line in transfer_info:
        if line[0].startswith('set2'):
            _, _, _, s_slot, s_well, h, _, d_slot, d_well, vol = line[:10]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)]
            if tip_reuse_m20 == 'always':
                pick_up_m20()
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