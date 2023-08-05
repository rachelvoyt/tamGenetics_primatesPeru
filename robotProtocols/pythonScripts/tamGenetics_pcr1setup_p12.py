def get_values(*names):
    import json
    _all_values = json.loads("""{"transfer_csv":"ot2set,reagent,source_labware,source_slot,source_well,asp_height,dest_labware,dest_slot,dest_well,transfer_volume\\nset1_xtnPlate1_e1,blood_p1.C1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C1,1,denvillewithaxygenbase_96_wellplate_200ul,2,C1,2\\nset1_xtnPlate1_e1,blood_p1.D1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D1,1,denvillewithaxygenbase_96_wellplate_200ul,2,D1,2\\nset1_xtnPlate1_e1,blood_p1.E1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E1,1,denvillewithaxygenbase_96_wellplate_200ul,2,E1,2\\nset1_xtnPlate1_e1,blood_p1.F1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F1,1,denvillewithaxygenbase_96_wellplate_200ul,2,F1,2\\nset1_xtnPlate1_e1,blood_p1.G1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G1,1,denvillewithaxygenbase_96_wellplate_200ul,2,G1,2\\nset1_xtnPlate1_e1,blood_p1.H1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H1,1,denvillewithaxygenbase_96_wellplate_200ul,2,H1,2\\nset1_xtnPlate1_e1,blood_p1.C2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C2,1,denvillewithaxygenbase_96_wellplate_200ul,2,C2,2\\nset1_xtnPlate1_e1,blood_p1.D2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D2,1,denvillewithaxygenbase_96_wellplate_200ul,2,D2,2\\nset1_xtnPlate1_e1,blood_p1.E2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E2,1,denvillewithaxygenbase_96_wellplate_200ul,2,E2,2\\nset1_xtnPlate1_e1,blood_p1.G2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G2,1,denvillewithaxygenbase_96_wellplate_200ul,2,G2,2\\nset1_xtnPlate1_e1,blood_p1.H2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H2,1,denvillewithaxygenbase_96_wellplate_200ul,2,H2,2\\nset1_xtnPlate1_e1,blood_p1.A3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A3,1,denvillewithaxygenbase_96_wellplate_200ul,2,A3,2\\nset1_xtnPlate1_e1,blood_p1.B3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B3,1,denvillewithaxygenbase_96_wellplate_200ul,2,B3,2\\nset1_xtnPlate1_e1,blood_p1.C3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C3,1,denvillewithaxygenbase_96_wellplate_200ul,2,C3,2\\nset1_xtnPlate1_e1,blood_p1.D3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D3,1,denvillewithaxygenbase_96_wellplate_200ul,2,D3,2\\nset1_xtnPlate1_e1,blood_p1.E3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E3,1,denvillewithaxygenbase_96_wellplate_200ul,2,E3,2\\nset1_xtnPlate1_e1,blood_p1.F3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F3,1,denvillewithaxygenbase_96_wellplate_200ul,2,F3,2\\nset1_xtnPlate1_e1,blood_p1.G3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G3,1,denvillewithaxygenbase_96_wellplate_200ul,2,G3,2\\nset1_xtnPlate1_e1,blood_p1.H3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H3,1,denvillewithaxygenbase_96_wellplate_200ul,2,H3,2\\nset1_xtnPlate1_e1,blood_p1.B4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B4,1,denvillewithaxygenbase_96_wellplate_200ul,2,B4,2\\nset1_xtnPlate1_e1,xtnNeg_p1.C4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C4,1,denvillewithaxygenbase_96_wellplate_200ul,2,C4,4\\nset1_xtnPlate1_e1,blood_p1.D4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D4,1,denvillewithaxygenbase_96_wellplate_200ul,2,D4,2\\nset1_xtnPlate1_e1,blood_p1.E4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E4,1,denvillewithaxygenbase_96_wellplate_200ul,2,E4,2\\nset1_xtnPlate1_e1,blood_p1.F4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F4,1,denvillewithaxygenbase_96_wellplate_200ul,2,F4,2\\nset1_xtnPlate1_e1,blood_p1.G4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G4,1,denvillewithaxygenbase_96_wellplate_200ul,2,G4,2\\nset1_xtnPlate1_e1,blood_p1.H4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H4,1,denvillewithaxygenbase_96_wellplate_200ul,2,H4,2\\nset1_xtnPlate1_e1,blood_p1.B5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B5,1,denvillewithaxygenbase_96_wellplate_200ul,2,B5,2\\nset1_xtnPlate1_e1,blood_p1.C5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C5,1,denvillewithaxygenbase_96_wellplate_200ul,2,C5,2\\nset1_xtnPlate1_e1,blood_p1.D5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D5,1,denvillewithaxygenbase_96_wellplate_200ul,2,D5,2\\nset1_xtnPlate1_e1,blood_p1.E5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E5,1,denvillewithaxygenbase_96_wellplate_200ul,2,E5,2\\nset1_xtnPlate1_e1,blood_p1.F5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F5,1,denvillewithaxygenbase_96_wellplate_200ul,2,F5,2\\nset1_xtnPlate1_e1,blood_p1.G5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G5,1,denvillewithaxygenbase_96_wellplate_200ul,2,G5,2\\nset1_xtnPlate1_e1,blood_p1.H5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H5,1,denvillewithaxygenbase_96_wellplate_200ul,2,H5,2\\nset1_xtnPlate1_e1,blood_p1.B6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B6,1,denvillewithaxygenbase_96_wellplate_200ul,2,B6,2\\nset1_xtnPlate1_e1,blood_p1.D6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D6,1,denvillewithaxygenbase_96_wellplate_200ul,2,D6,2\\nset1_xtnPlate1_e1,blood_p1.F6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F6,1,denvillewithaxygenbase_96_wellplate_200ul,2,F6,2\\nset1_xtnPlate1_e1,blood_p1.G6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G6,1,denvillewithaxygenbase_96_wellplate_200ul,2,G6,2\\nset1_xtnPlate1_e1,blood_p1.H6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H6,1,denvillewithaxygenbase_96_wellplate_200ul,2,H6,2\\nset1_xtnPlate1_e1,blood_p1.B7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B7,1,denvillewithaxygenbase_96_wellplate_200ul,2,B7,2\\nset1_xtnPlate1_e1,blood_p1.C7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C7,1,denvillewithaxygenbase_96_wellplate_200ul,2,C7,2\\nset1_xtnPlate1_e1,blood_p1.D7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D7,1,denvillewithaxygenbase_96_wellplate_200ul,2,D7,2\\nset1_xtnPlate1_e1,blood_p1.E7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E7,1,denvillewithaxygenbase_96_wellplate_200ul,2,E7,2\\nset1_xtnPlate1_e1,blood_p1.F7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F7,1,denvillewithaxygenbase_96_wellplate_200ul,2,F7,2\\nset1_xtnPlate1_e1,blood_p1.G7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G7,1,denvillewithaxygenbase_96_wellplate_200ul,2,G7,2\\nset1_xtnPlate1_e1,blood_p1.H7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H7,1,denvillewithaxygenbase_96_wellplate_200ul,2,H7,2\\nset1_xtnPlate1_e1,blood_p1.A8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A8,1,denvillewithaxygenbase_96_wellplate_200ul,2,A8,2\\nset1_xtnPlate1_e1,blood_p1.B8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B8,1,denvillewithaxygenbase_96_wellplate_200ul,2,B8,2\\nset1_xtnPlate1_e1,blood_p1.C8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C8,1,denvillewithaxygenbase_96_wellplate_200ul,2,C8,2\\nset1_xtnPlate1_e1,blood_p1.D8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D8,1,denvillewithaxygenbase_96_wellplate_200ul,2,D8,2\\nset1_xtnPlate1_e1,blood_p1.E8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E8,1,denvillewithaxygenbase_96_wellplate_200ul,2,E8,2\\nset1_xtnPlate1_e1,blood_p1.G8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G8,1,denvillewithaxygenbase_96_wellplate_200ul,2,G8,2\\nset1_xtnPlate1_e1,blood_p1.H8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H8,1,denvillewithaxygenbase_96_wellplate_200ul,2,H8,2\\nset1_xtnPlate1_e1,blood_p1.A9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A9,1,denvillewithaxygenbase_96_wellplate_200ul,2,A9,2\\nset1_xtnPlate1_e1,blood_p1.B9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B9,1,denvillewithaxygenbase_96_wellplate_200ul,2,B9,2\\nset1_xtnPlate1_e1,blood_p1.C9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C9,1,denvillewithaxygenbase_96_wellplate_200ul,2,C9,2\\nset1_xtnPlate1_e1,blood_p1.D9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D9,1,denvillewithaxygenbase_96_wellplate_200ul,2,D9,2\\nset1_xtnPlate1_e1,blood_p1.E9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E9,1,denvillewithaxygenbase_96_wellplate_200ul,2,E9,2\\nset1_xtnPlate1_e1,xtnNeg_p1.F9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F9,1,denvillewithaxygenbase_96_wellplate_200ul,2,F9,4\\nset1_xtnPlate1_e1,blood_p1.G9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G9,1,denvillewithaxygenbase_96_wellplate_200ul,2,G9,2\\nset1_xtnPlate1_e1,blood_p1.H9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H9,1,denvillewithaxygenbase_96_wellplate_200ul,2,H9,2\\nset1_xtnPlate1_e1,blood_p1.A10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A10,1,denvillewithaxygenbase_96_wellplate_200ul,2,A10,2\\nset1_xtnPlate1_e1,blood_p1.B10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B10,1,denvillewithaxygenbase_96_wellplate_200ul,2,B10,2\\nset1_xtnPlate1_e1,blood_p1.C10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C10,1,denvillewithaxygenbase_96_wellplate_200ul,2,C10,2\\nset1_xtnPlate1_e1,blood_p1.D10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D10,1,denvillewithaxygenbase_96_wellplate_200ul,2,D10,2\\nset1_xtnPlate1_e1,blood_p1.E10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E10,1,denvillewithaxygenbase_96_wellplate_200ul,2,E10,2\\nset1_xtnPlate1_e1,blood_p1.F10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F10,1,denvillewithaxygenbase_96_wellplate_200ul,2,F10,2\\nset1_xtnPlate1_e1,blood_p1.G10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G10,1,denvillewithaxygenbase_96_wellplate_200ul,2,G10,2\\nset1_xtnPlate1_e1,blood_p1.H10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H10,1,denvillewithaxygenbase_96_wellplate_200ul,2,H10,2\\nset1_xtnPlate1_e1,blood_p1.B11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B11,1,denvillewithaxygenbase_96_wellplate_200ul,2,B11,2\\nset1_xtnPlate1_e1,blood_p1.C11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C11,1,denvillewithaxygenbase_96_wellplate_200ul,2,C11,2\\nset1_xtnPlate1_e1,blood_p1.D11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D11,1,denvillewithaxygenbase_96_wellplate_200ul,2,D11,2\\nset1_xtnPlate1_e1,blood_p1.E11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E11,1,denvillewithaxygenbase_96_wellplate_200ul,2,E11,2\\nset1_xtnPlate1_e1,blood_p1.F11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F11,1,denvillewithaxygenbase_96_wellplate_200ul,2,F11,2\\nset1_xtnPlate1_e1,blood_p1.G11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G11,1,denvillewithaxygenbase_96_wellplate_200ul,2,G11,2\\nset1_xtnPlate1_e1,blood_p1.H11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H11,1,denvillewithaxygenbase_96_wellplate_200ul,2,H11,2\\nset1_xtnPlate1_e1,blood_p1.B12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B12,1,denvillewithaxygenbase_96_wellplate_200ul,2,B12,2\\nset1_xtnPlate1_e1,blood_p1.C12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C12,1,denvillewithaxygenbase_96_wellplate_200ul,2,C12,2\\nset1_xtnPlate1_e1,blood_p1.D12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D12,1,denvillewithaxygenbase_96_wellplate_200ul,2,D12,2\\nset1_xtnPlate1_e1,blood_p1.E12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E12,1,denvillewithaxygenbase_96_wellplate_200ul,2,E12,2\\nset1_xtnPlate1_e1,blood_p1.F12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F12,1,denvillewithaxygenbase_96_wellplate_200ul,2,F12,2\\nset1_xtnPlate1_e1,blood_p1.G12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G12,1,denvillewithaxygenbase_96_wellplate_200ul,2,G12,2\\nset1_xtnPlate1_e1,blood_p1.H12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H12,1,denvillewithaxygenbase_96_wellplate_200ul,2,H12,2\\nset2.1_xtnPlate1_e2,blood_p1.A5_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,A5,1,denvillewithaxygenbase_96_wellplate_200ul,2,A5,2\\nset2.1_xtnPlate1_e2,blood_p1.C6_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,C6,1,denvillewithaxygenbase_96_wellplate_200ul,2,C6,2\\nset2.1_xtnPlate1_e2,blood_p1.E6_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,E6,1,denvillewithaxygenbase_96_wellplate_200ul,2,E6,2\\nset2.1_xtnPlate1_e2,blood_p1.A7_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,A7,1,denvillewithaxygenbase_96_wellplate_200ul,2,A7,2\\nset2.1_xtnPlate1_e2,blood_p1.F8_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,F8,1,denvillewithaxygenbase_96_wellplate_200ul,2,F8,2\\nset2.1_xtnPlate1_e2,blood_p1.A11_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,A11,1,denvillewithaxygenbase_96_wellplate_200ul,2,A11,2\\nset2.1_xtnPlate1_e2,blood_p1.A12_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,A12,1,denvillewithaxygenbase_96_wellplate_200ul,2,A12,2\\nset2.2_xtnPlate1.tubes,blood_t1191_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A1,1,denvillewithaxygenbase_96_wellplate_200ul,2,A1,2\\nset2.2_xtnPlate1.tubes,blood_t1197_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B1,1,denvillewithaxygenbase_96_wellplate_200ul,2,B1,2\\nset2.2_xtnPlate1.tubes,blood_t700_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C1,1,denvillewithaxygenbase_96_wellplate_200ul,2,A2,2\\nset2.2_xtnPlate1.tubes,blood_t1183_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D1,1,denvillewithaxygenbase_96_wellplate_200ul,2,B2,2\\nset2.2_xtnPlate1.tubes,blood_t1275_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A2,1,denvillewithaxygenbase_96_wellplate_200ul,2,F2,2\\nset2.2_xtnPlate1.tubes,blood_t505_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B2,1,denvillewithaxygenbase_96_wellplate_200ul,2,A4,2\\nset2.2_xtnPlate1.tubes,blood_t354_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C2,1,denvillewithaxygenbase_96_wellplate_200ul,2,A6,2\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A1,8\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A2,8\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A3,8\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A4,8\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A5,8\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A6,8\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A7,8\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A8,8\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A9,8\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A10,8\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A11,8\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A12,8\\nset4_xtnPlate2_e1,blood_p2.B1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B1,1,denvillewithaxygenbase_96_wellplate_200ul,2,B1,2\\nset4_xtnPlate2_e1,blood_p2.C1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C1,1,denvillewithaxygenbase_96_wellplate_200ul,2,C1,2\\nset4_xtnPlate2_e1,blood_p2.D1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D1,1,denvillewithaxygenbase_96_wellplate_200ul,2,D1,2\\nset4_xtnPlate2_e1,blood_p2.E1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E1,1,denvillewithaxygenbase_96_wellplate_200ul,2,E1,2\\nset4_xtnPlate2_e1,blood_p2.F1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F1,1,denvillewithaxygenbase_96_wellplate_200ul,2,F1,2\\nset4_xtnPlate2_e1,blood_p2.G1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G1,1,denvillewithaxygenbase_96_wellplate_200ul,2,G1,2\\nset4_xtnPlate2_e1,blood_p2.A2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A2,1,denvillewithaxygenbase_96_wellplate_200ul,2,A2,2\\nset4_xtnPlate2_e1,blood_p2.B2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B2,1,denvillewithaxygenbase_96_wellplate_200ul,2,B2,2\\nset4_xtnPlate2_e1,blood_p2.C2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C2,1,denvillewithaxygenbase_96_wellplate_200ul,2,C2,2\\nset4_xtnPlate2_e1,blood_p2.D2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D2,1,denvillewithaxygenbase_96_wellplate_200ul,2,D2,2\\nset4_xtnPlate2_e1,blood_p2.E2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E2,1,denvillewithaxygenbase_96_wellplate_200ul,2,E2,2\\nset4_xtnPlate2_e1,blood_p2.F2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F2,1,denvillewithaxygenbase_96_wellplate_200ul,2,F2,2\\nset4_xtnPlate2_e1,blood_p2.G2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G2,1,denvillewithaxygenbase_96_wellplate_200ul,2,G2,2\\nset4_xtnPlate2_e1,blood_p2.H2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H2,1,denvillewithaxygenbase_96_wellplate_200ul,2,H2,2\\nset4_xtnPlate2_e1,blood_p2.A3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A3,1,denvillewithaxygenbase_96_wellplate_200ul,2,A3,2\\nset4_xtnPlate2_e1,blood_p2.B3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B3,1,denvillewithaxygenbase_96_wellplate_200ul,2,B3,2\\nset4_xtnPlate2_e1,blood_p2.C3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C3,1,denvillewithaxygenbase_96_wellplate_200ul,2,C3,2\\nset4_xtnPlate2_e1,blood_p2.D3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D3,1,denvillewithaxygenbase_96_wellplate_200ul,2,D3,2\\nset4_xtnPlate2_e1,blood_p2.E3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E3,1,denvillewithaxygenbase_96_wellplate_200ul,2,E3,2\\nset4_xtnPlate2_e1,blood_p2.F3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F3,1,denvillewithaxygenbase_96_wellplate_200ul,2,F3,2\\nset4_xtnPlate2_e1,blood_p2.G3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G3,1,denvillewithaxygenbase_96_wellplate_200ul,2,G3,2\\nset4_xtnPlate2_e1,blood_p2.H3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H3,1,denvillewithaxygenbase_96_wellplate_200ul,2,H3,2\\nset4_xtnPlate2_e1,blood_p2.A4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A4,1,denvillewithaxygenbase_96_wellplate_200ul,2,A4,2\\nset4_xtnPlate2_e1,blood_p2.B4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B4,1,denvillewithaxygenbase_96_wellplate_200ul,2,B4,2\\nset4_xtnPlate2_e1,xtnNeg_p2.C4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C4,1,denvillewithaxygenbase_96_wellplate_200ul,2,C4,4\\nset4_xtnPlate2_e1,blood_p2.D4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D4,1,denvillewithaxygenbase_96_wellplate_200ul,2,D4,2\\nset4_xtnPlate2_e1,blood_p2.E4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E4,1,denvillewithaxygenbase_96_wellplate_200ul,2,E4,2\\nset4_xtnPlate2_e1,blood_p2.F4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F4,1,denvillewithaxygenbase_96_wellplate_200ul,2,F4,2\\nset4_xtnPlate2_e1,blood_p2.G4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G4,1,denvillewithaxygenbase_96_wellplate_200ul,2,G4,2\\nset4_xtnPlate2_e1,blood_p2.H4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H4,1,denvillewithaxygenbase_96_wellplate_200ul,2,H4,2\\nset4_xtnPlate2_e1,blood_p2.B5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B5,1,denvillewithaxygenbase_96_wellplate_200ul,2,B5,2\\nset4_xtnPlate2_e1,blood_p2.C5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C5,1,denvillewithaxygenbase_96_wellplate_200ul,2,C5,2\\nset4_xtnPlate2_e1,blood_p2.D5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D5,1,denvillewithaxygenbase_96_wellplate_200ul,2,D5,2\\nset4_xtnPlate2_e1,blood_p2.E5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E5,1,denvillewithaxygenbase_96_wellplate_200ul,2,E5,2\\nset4_xtnPlate2_e1,blood_p2.F5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F5,1,denvillewithaxygenbase_96_wellplate_200ul,2,F5,2\\nset4_xtnPlate2_e1,blood_p2.G5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G5,1,denvillewithaxygenbase_96_wellplate_200ul,2,G5,2\\nset4_xtnPlate2_e1,blood_p2.H5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H5,1,denvillewithaxygenbase_96_wellplate_200ul,2,H5,2\\nset4_xtnPlate2_e1,blood_p2.A6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A6,1,denvillewithaxygenbase_96_wellplate_200ul,2,A6,2\\nset4_xtnPlate2_e1,blood_p2.B6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B6,1,denvillewithaxygenbase_96_wellplate_200ul,2,B6,2\\nset4_xtnPlate2_e1,blood_p2.C6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C6,1,denvillewithaxygenbase_96_wellplate_200ul,2,C6,2\\nset4_xtnPlate2_e1,blood_p2.D6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D6,1,denvillewithaxygenbase_96_wellplate_200ul,2,D6,2\\nset4_xtnPlate2_e1,blood_p2.E6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E6,1,denvillewithaxygenbase_96_wellplate_200ul,2,E6,2\\nset4_xtnPlate2_e1,blood_p2.F6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F6,1,denvillewithaxygenbase_96_wellplate_200ul,2,F6,2\\nset4_xtnPlate2_e1,blood_p2.G6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G6,1,denvillewithaxygenbase_96_wellplate_200ul,2,G6,2\\nset4_xtnPlate2_e1,blood_p2.H6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H6,1,denvillewithaxygenbase_96_wellplate_200ul,2,H6,2\\nset4_xtnPlate2_e1,blood_p2.A7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A7,1,denvillewithaxygenbase_96_wellplate_200ul,2,A7,2\\nset4_xtnPlate2_e1,blood_p2.B7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B7,1,denvillewithaxygenbase_96_wellplate_200ul,2,B7,2\\nset4_xtnPlate2_e1,blood_p2.C7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C7,1,denvillewithaxygenbase_96_wellplate_200ul,2,C7,2\\nset4_xtnPlate2_e1,blood_p2.D7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D7,1,denvillewithaxygenbase_96_wellplate_200ul,2,D7,2\\nset4_xtnPlate2_e1,blood_p2.E7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E7,1,denvillewithaxygenbase_96_wellplate_200ul,2,E7,2\\nset4_xtnPlate2_e1,blood_p2.F7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F7,1,denvillewithaxygenbase_96_wellplate_200ul,2,F7,2\\nset4_xtnPlate2_e1,blood_p2.B8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B8,1,denvillewithaxygenbase_96_wellplate_200ul,2,B8,2\\nset4_xtnPlate2_e1,blood_p2.C8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C8,1,denvillewithaxygenbase_96_wellplate_200ul,2,C8,2\\nset4_xtnPlate2_e1,blood_p2.D8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D8,1,denvillewithaxygenbase_96_wellplate_200ul,2,D8,2\\nset4_xtnPlate2_e1,blood_p2.E8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E8,1,denvillewithaxygenbase_96_wellplate_200ul,2,E8,2\\nset4_xtnPlate2_e1,blood_p2.F8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F8,1,denvillewithaxygenbase_96_wellplate_200ul,2,F8,2\\nset4_xtnPlate2_e1,blood_p2.G8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G8,1,denvillewithaxygenbase_96_wellplate_200ul,2,G8,2\\nset4_xtnPlate2_e1,blood_p2.H8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H8,1,denvillewithaxygenbase_96_wellplate_200ul,2,H8,2\\nset4_xtnPlate2_e1,blood_p2.B9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B9,1,denvillewithaxygenbase_96_wellplate_200ul,2,B9,2\\nset4_xtnPlate2_e1,blood_p2.C9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C9,1,denvillewithaxygenbase_96_wellplate_200ul,2,C9,2\\nset4_xtnPlate2_e1,blood_p2.D9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D9,1,denvillewithaxygenbase_96_wellplate_200ul,2,D9,2\\nset4_xtnPlate2_e1,blood_p2.E9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E9,1,denvillewithaxygenbase_96_wellplate_200ul,2,E9,2\\nset4_xtnPlate2_e1,xtnNeg_p2.F9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F9,1,denvillewithaxygenbase_96_wellplate_200ul,2,F9,4\\nset4_xtnPlate2_e1,blood_p2.G9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G9,1,denvillewithaxygenbase_96_wellplate_200ul,2,G9,2\\nset4_xtnPlate2_e1,blood_p2.H9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H9,1,denvillewithaxygenbase_96_wellplate_200ul,2,H9,2\\nset4_xtnPlate2_e1,blood_p2.A10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A10,1,denvillewithaxygenbase_96_wellplate_200ul,2,A10,2\\nset4_xtnPlate2_e1,blood_p2.B10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B10,1,denvillewithaxygenbase_96_wellplate_200ul,2,B10,2\\nset4_xtnPlate2_e1,blood_p2.C10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C10,1,denvillewithaxygenbase_96_wellplate_200ul,2,C10,2\\nset4_xtnPlate2_e1,blood_p2.D10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D10,1,denvillewithaxygenbase_96_wellplate_200ul,2,D10,2\\nset4_xtnPlate2_e1,blood_p2.E10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E10,1,denvillewithaxygenbase_96_wellplate_200ul,2,E10,2\\nset4_xtnPlate2_e1,blood_p2.F10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F10,1,denvillewithaxygenbase_96_wellplate_200ul,2,F10,2\\nset4_xtnPlate2_e1,blood_p2.G10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G10,1,denvillewithaxygenbase_96_wellplate_200ul,2,G10,2\\nset4_xtnPlate2_e1,blood_p2.H10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H10,1,denvillewithaxygenbase_96_wellplate_200ul,2,H10,2\\nset4_xtnPlate2_e1,blood_p2.A11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A11,1,denvillewithaxygenbase_96_wellplate_200ul,2,A11,2\\nset4_xtnPlate2_e1,blood_p2.B11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B11,1,denvillewithaxygenbase_96_wellplate_200ul,2,B11,2\\nset4_xtnPlate2_e1,blood_p2.C11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C11,1,denvillewithaxygenbase_96_wellplate_200ul,2,C11,2\\nset4_xtnPlate2_e1,blood_p2.E11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E11,1,denvillewithaxygenbase_96_wellplate_200ul,2,E11,2\\nset4_xtnPlate2_e1,blood_p2.F11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F11,1,denvillewithaxygenbase_96_wellplate_200ul,2,F11,2\\nset4_xtnPlate2_e1,blood_p2.G11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G11,1,denvillewithaxygenbase_96_wellplate_200ul,2,G11,2\\nset4_xtnPlate2_e1,blood_p2.H11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H11,1,denvillewithaxygenbase_96_wellplate_200ul,2,H11,2\\nset4_xtnPlate2_e1,blood_p2.A12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A12,1,denvillewithaxygenbase_96_wellplate_200ul,2,A12,2\\nset4_xtnPlate2_e1,blood_p2.B12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B12,1,denvillewithaxygenbase_96_wellplate_200ul,2,B12,2\\nset4_xtnPlate2_e1,blood_p2.D12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D12,1,denvillewithaxygenbase_96_wellplate_200ul,2,D12,2\\nset4_xtnPlate2_e1,blood_p2.E12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E12,1,denvillewithaxygenbase_96_wellplate_200ul,2,E12,2\\nset4_xtnPlate2_e1,blood_p2.F12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F12,1,denvillewithaxygenbase_96_wellplate_200ul,2,F12,2\\nset4_xtnPlate2_e1,blood_p2.G12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G12,1,denvillewithaxygenbase_96_wellplate_200ul,2,G12,2\\nset4_xtnPlate2_e1,blood_p2.H12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H12,1,denvillewithaxygenbase_96_wellplate_200ul,2,H12,2\\nset5.1_xtnPlate2_e2,blood_p2.A1_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,2,A1,2\\nset5.1_xtnPlate2_e2,blood_p2.H1_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,H1,1,denvillewithaxygenbase_96_wellplate_200ul,2,H1,2\\nset5.1_xtnPlate2_e2,blood_p2.A5_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,A5,1,denvillewithaxygenbase_96_wellplate_200ul,2,A5,2\\nset5.1_xtnPlate2_e2,blood_p2.G7_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,G7,1,denvillewithaxygenbase_96_wellplate_200ul,2,G7,2\\nset5.1_xtnPlate2_e2,blood_p2.H7_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,H7,1,denvillewithaxygenbase_96_wellplate_200ul,2,H7,2\\nset5.1_xtnPlate2_e2,blood_p2.A8_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,A8,1,denvillewithaxygenbase_96_wellplate_200ul,2,A8,2\\nset5.1_xtnPlate2_e2,blood_p2.A9_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,A9,1,denvillewithaxygenbase_96_wellplate_200ul,2,A9,2\\nset5.1_xtnPlate2_e2,blood_p2.D11_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,D11,1,denvillewithaxygenbase_96_wellplate_200ul,2,D11,2\\nset5.1_xtnPlate2_e2,blood_p2.C12_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,C12,1,denvillewithaxygenbase_96_wellplate_200ul,2,C12,2\\nset6_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A1,8\\nset6_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A2,8\\nset6_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A3,8\\nset6_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A4,8\\nset6_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A5,8\\nset6_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A6,8\\nset6_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A7,8\\nset6_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A8,8\\nset6_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A9,8\\nset6_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A10,8\\nset6_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A11,8\\nset6_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A12,8\\n","pipette_type_s20":"p20_single_gen2","pipette_mount_s20":"left","tip_type_s20":"opentrons_96_filtertiprack_20ul","tip_reuse_s20":"always", "pipette_type_m20":"p20_multi_gen2","pipette_mount_m20":"right","tip_type_m20":"opentrons_96_filtertiprack_20ul","tip_reuse_m20":"always"}""")
    return [_all_values[n] for n in names]


metadata = {
    'apiLevel': '2.8',
    'protocolName': 'tamGenetics_pcr1setup_p12',
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
    s20.well_bottom_clearance.blow_out = 4
            
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

    # PAUSE 1: switch to xtnPlate1_e2 + blood xtn tubes
    protocol.pause("PAUSE 1: i) Remove xtnPlate1_e1. ii) Check pcr plates to ensure that sufficient xtn volume was transfered AND that no beads were transferred. iii) For any wells with insufficient volume and/or beads, remove beads and/or manually transfer the sample. iv) Seal xtnPlate1_e1 and place on ice, then place xtnPlate1_e2 & blood xtn tubes on magblock and resume run.")

    # transfers for SET 2: xtnPlate1_e2 + blood xtn tubes
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

    # PAUSE 2: switch to mastermix
    protocol.pause("PAUSE 2: i) Remove xtnPlate1_e2 & blood xtn tubes. ii) Check pcr plates to ensure that sufficient xtn volume was transfered AND that no beads were transferred. iii) For any wells with insufficient volume and/or beads, remove beads and/or manually transfer the sample. iv) Seal xtnPlate1_e2 and place on ice. Place mastermix and resume run.")

    # Transfers for SET 3: mastermix for pcr1Plate1
    for line in transfer_info:
        if line[0].startswith('set3'):
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

    # PAUSE 3: Run pcr1Plate1 & start plate 2
    protocol.pause("PAUSE 3: i) Remove pcr1Plate1 and seal with flat strip caps. Run in thermocycler with GTSEQ-D protocol. ii) Place xtnPlate2_e1 on OT2 deck and resume run.")
    
    # transfers for SET 4: xtnPlate2_e1
    magdeck.engage()
    for line in transfer_info:
        if line[0].startswith('set4'):
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

    # PAUSE 4: switch to xtnPlate2_e2 + blood xtn tubes
    protocol.pause("PAUSE 4: Remove xtnPlate2_e1. ii) Check pcr plates to ensure that sufficient xtn volume was transfered AND that no beads were transferred. iii) For any wells with insufficient volume and/or beads, remove beads and/or manually transfer the sample. iv) Seal xtnPlate2_e2 + blood xtn tubes and place on ice, then place xtnPlate2_e2 on magblock and blood xtn tubes on tuberack following **Deck plan: Set 4** on quip and resume run.")

    # transfers for SET 4: xtnPlate2_e2 + blood xtn tubes
    magdeck.engage()
    for line in transfer_info:
        if line[0].startswith('set4'):
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

    # PAUSE 4: switch to mastermix
    protocol.pause("PAUSE 4: i) Remove xtnPlate2_e2 & blood xtn tubes. ii) Check pcr plates to ensure that sufficient xtn volume was transfered AND that no beads were transferred. iii) For any wells with insufficient volume and/or beads, remove beads and/or manually transfer the sample. iv) Seal xtnPlate2_e2 & blood xtn tubes and place on ice, then place fecal xtn tubes 1 to 24 on tuberack following **Deck plan: Set 5** on quip and resume run.")

    # Transfers for SET 6: mastermix for pcr1Plate2
    for line in transfer_info:
        if line[0].startswith('set6'):
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