def get_values(*names):
    import json
    _all_values = json.loads("""{"transfer_csv":"ot2set,reagent,source_labware,source_slot,source_well,asp_height,dest_labware,dest_slot,dest_well,transfer_volume\\nset1_xtnPlate3_e1,hair_p3.A1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,2,A1,4\\nset1_xtnPlate3_e1,hair_p3.A1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,5,A1,4\\nset1_xtnPlate3_e1,hair_p3.C1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C1,1,denvillewithaxygenbase_96_wellplate_200ul,2,C1,4\\nset1_xtnPlate3_e1,hair_p3.C1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C1,1,denvillewithaxygenbase_96_wellplate_200ul,5,C1,4\\nset1_xtnPlate3_e1,hair_p3.E1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E1,1,denvillewithaxygenbase_96_wellplate_200ul,2,E1,4\\nset1_xtnPlate3_e1,hair_p3.E1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E1,1,denvillewithaxygenbase_96_wellplate_200ul,5,E1,4\\nset1_xtnPlate3_e1,hair_p3.F1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F1,1,denvillewithaxygenbase_96_wellplate_200ul,2,F1,4\\nset1_xtnPlate3_e1,hair_p3.F1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F1,1,denvillewithaxygenbase_96_wellplate_200ul,5,F1,4\\nset1_xtnPlate3_e1,hair_p3.H1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H1,1,denvillewithaxygenbase_96_wellplate_200ul,2,H1,4\\nset1_xtnPlate3_e1,hair_p3.H1_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H1,1,denvillewithaxygenbase_96_wellplate_200ul,5,H1,4\\nset1_xtnPlate3_e1,hair_p3.C2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C2,1,denvillewithaxygenbase_96_wellplate_200ul,2,C2,4\\nset1_xtnPlate3_e1,hair_p3.C2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C2,1,denvillewithaxygenbase_96_wellplate_200ul,5,C2,4\\nset1_xtnPlate3_e1,hair_p3.E2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E2,1,denvillewithaxygenbase_96_wellplate_200ul,2,E2,4\\nset1_xtnPlate3_e1,hair_p3.E2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E2,1,denvillewithaxygenbase_96_wellplate_200ul,5,E2,4\\nset1_xtnPlate3_e1,hair_p3.F2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F2,1,denvillewithaxygenbase_96_wellplate_200ul,2,F2,4\\nset1_xtnPlate3_e1,hair_p3.F2_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F2,1,denvillewithaxygenbase_96_wellplate_200ul,5,F2,4\\nset1_xtnPlate3_e1,hair_p3.A3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A3,1,denvillewithaxygenbase_96_wellplate_200ul,2,A3,4\\nset1_xtnPlate3_e1,hair_p3.A3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A3,1,denvillewithaxygenbase_96_wellplate_200ul,5,A3,4\\nset1_xtnPlate3_e1,hair_p3.B3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B3,1,denvillewithaxygenbase_96_wellplate_200ul,2,B3,4\\nset1_xtnPlate3_e1,hair_p3.B3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B3,1,denvillewithaxygenbase_96_wellplate_200ul,5,B3,4\\nset1_xtnPlate3_e1,hair_p3.C3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C3,1,denvillewithaxygenbase_96_wellplate_200ul,2,C3,4\\nset1_xtnPlate3_e1,hair_p3.C3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C3,1,denvillewithaxygenbase_96_wellplate_200ul,5,C3,4\\nset1_xtnPlate3_e1,hair_p3.E3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E3,1,denvillewithaxygenbase_96_wellplate_200ul,2,E3,4\\nset1_xtnPlate3_e1,hair_p3.E3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E3,1,denvillewithaxygenbase_96_wellplate_200ul,5,E3,4\\nset1_xtnPlate3_e1,hair_p3.F3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F3,1,denvillewithaxygenbase_96_wellplate_200ul,2,F3,4\\nset1_xtnPlate3_e1,hair_p3.F3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F3,1,denvillewithaxygenbase_96_wellplate_200ul,5,F3,4\\nset1_xtnPlate3_e1,hair_p3.G3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G3,1,denvillewithaxygenbase_96_wellplate_200ul,2,G3,4\\nset1_xtnPlate3_e1,hair_p3.G3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G3,1,denvillewithaxygenbase_96_wellplate_200ul,5,G3,4\\nset1_xtnPlate3_e1,hair_p3.H3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H3,1,denvillewithaxygenbase_96_wellplate_200ul,2,H3,4\\nset1_xtnPlate3_e1,hair_p3.H3_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H3,1,denvillewithaxygenbase_96_wellplate_200ul,5,H3,4\\nset1_xtnPlate3_e1,hair_p3.A4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A4,1,denvillewithaxygenbase_96_wellplate_200ul,2,A4,4\\nset1_xtnPlate3_e1,hair_p3.A4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A4,1,denvillewithaxygenbase_96_wellplate_200ul,5,A4,4\\nset1_xtnPlate3_e1,hair_p3.B4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B4,1,denvillewithaxygenbase_96_wellplate_200ul,2,B4,4\\nset1_xtnPlate3_e1,hair_p3.B4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B4,1,denvillewithaxygenbase_96_wellplate_200ul,5,B4,4\\nset1_xtnPlate3_e1,xtnNeg_p3.C4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C4,1,denvillewithaxygenbase_96_wellplate_200ul,2,C4,4\\nset1_xtnPlate3_e1,xtnNeg_p3.C4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C4,1,denvillewithaxygenbase_96_wellplate_200ul,5,C4,4\\nset1_xtnPlate3_e1,hair_p3.D4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D4,1,denvillewithaxygenbase_96_wellplate_200ul,2,D4,4\\nset1_xtnPlate3_e1,hair_p3.D4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D4,1,denvillewithaxygenbase_96_wellplate_200ul,5,D4,4\\nset1_xtnPlate3_e1,hair_p3.E4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E4,1,denvillewithaxygenbase_96_wellplate_200ul,2,E4,4\\nset1_xtnPlate3_e1,hair_p3.E4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E4,1,denvillewithaxygenbase_96_wellplate_200ul,5,E4,4\\nset1_xtnPlate3_e1,hair_p3.F4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F4,1,denvillewithaxygenbase_96_wellplate_200ul,2,F4,4\\nset1_xtnPlate3_e1,hair_p3.F4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F4,1,denvillewithaxygenbase_96_wellplate_200ul,5,F4,4\\nset1_xtnPlate3_e1,hair_p3.G4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G4,1,denvillewithaxygenbase_96_wellplate_200ul,2,G4,4\\nset1_xtnPlate3_e1,hair_p3.G4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G4,1,denvillewithaxygenbase_96_wellplate_200ul,5,G4,4\\nset1_xtnPlate3_e1,hair_p3.H4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H4,1,denvillewithaxygenbase_96_wellplate_200ul,2,H4,4\\nset1_xtnPlate3_e1,hair_p3.H4_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H4,1,denvillewithaxygenbase_96_wellplate_200ul,5,H4,4\\nset1_xtnPlate3_e1,hair_p3.B5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B5,1,denvillewithaxygenbase_96_wellplate_200ul,2,B5,4\\nset1_xtnPlate3_e1,hair_p3.B5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B5,1,denvillewithaxygenbase_96_wellplate_200ul,5,B5,4\\nset1_xtnPlate3_e1,hair_p3.C5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C5,1,denvillewithaxygenbase_96_wellplate_200ul,2,C5,4\\nset1_xtnPlate3_e1,hair_p3.C5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C5,1,denvillewithaxygenbase_96_wellplate_200ul,5,C5,4\\nset1_xtnPlate3_e1,hair_p3.D5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D5,1,denvillewithaxygenbase_96_wellplate_200ul,2,D5,4\\nset1_xtnPlate3_e1,hair_p3.D5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D5,1,denvillewithaxygenbase_96_wellplate_200ul,5,D5,4\\nset1_xtnPlate3_e1,hair_p3.E5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E5,1,denvillewithaxygenbase_96_wellplate_200ul,2,E5,4\\nset1_xtnPlate3_e1,hair_p3.E5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E5,1,denvillewithaxygenbase_96_wellplate_200ul,5,E5,4\\nset1_xtnPlate3_e1,hair_p3.F5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F5,1,denvillewithaxygenbase_96_wellplate_200ul,2,F5,4\\nset1_xtnPlate3_e1,hair_p3.F5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F5,1,denvillewithaxygenbase_96_wellplate_200ul,5,F5,4\\nset1_xtnPlate3_e1,hair_p3.G5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G5,1,denvillewithaxygenbase_96_wellplate_200ul,2,G5,4\\nset1_xtnPlate3_e1,hair_p3.G5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G5,1,denvillewithaxygenbase_96_wellplate_200ul,5,G5,4\\nset1_xtnPlate3_e1,hair_p3.H5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H5,1,denvillewithaxygenbase_96_wellplate_200ul,2,H5,4\\nset1_xtnPlate3_e1,hair_p3.H5_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H5,1,denvillewithaxygenbase_96_wellplate_200ul,5,H5,4\\nset1_xtnPlate3_e1,hair_p3.A6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A6,1,denvillewithaxygenbase_96_wellplate_200ul,2,A6,4\\nset1_xtnPlate3_e1,hair_p3.A6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A6,1,denvillewithaxygenbase_96_wellplate_200ul,5,A6,4\\nset1_xtnPlate3_e1,hair_p3.B6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B6,1,denvillewithaxygenbase_96_wellplate_200ul,2,B6,4\\nset1_xtnPlate3_e1,hair_p3.B6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B6,1,denvillewithaxygenbase_96_wellplate_200ul,5,B6,4\\nset1_xtnPlate3_e1,hair_p3.C6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C6,1,denvillewithaxygenbase_96_wellplate_200ul,2,C6,4\\nset1_xtnPlate3_e1,hair_p3.C6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C6,1,denvillewithaxygenbase_96_wellplate_200ul,5,C6,4\\nset1_xtnPlate3_e1,hair_p3.D6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D6,1,denvillewithaxygenbase_96_wellplate_200ul,2,D6,4\\nset1_xtnPlate3_e1,hair_p3.D6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D6,1,denvillewithaxygenbase_96_wellplate_200ul,5,D6,4\\nset1_xtnPlate3_e1,hair_p3.E6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E6,1,denvillewithaxygenbase_96_wellplate_200ul,2,E6,4\\nset1_xtnPlate3_e1,hair_p3.E6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E6,1,denvillewithaxygenbase_96_wellplate_200ul,5,E6,4\\nset1_xtnPlate3_e1,hair_p3.G6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G6,1,denvillewithaxygenbase_96_wellplate_200ul,2,G6,4\\nset1_xtnPlate3_e1,hair_p3.G6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G6,1,denvillewithaxygenbase_96_wellplate_200ul,5,G6,4\\nset1_xtnPlate3_e1,hair_p3.H6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H6,1,denvillewithaxygenbase_96_wellplate_200ul,2,H6,4\\nset1_xtnPlate3_e1,hair_p3.H6_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H6,1,denvillewithaxygenbase_96_wellplate_200ul,5,H6,4\\nset1_xtnPlate3_e1,hair_p3.A7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A7,1,denvillewithaxygenbase_96_wellplate_200ul,2,A7,4\\nset1_xtnPlate3_e1,hair_p3.A7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A7,1,denvillewithaxygenbase_96_wellplate_200ul,5,A7,4\\nset1_xtnPlate3_e1,hair_p3.B7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B7,1,denvillewithaxygenbase_96_wellplate_200ul,2,B7,4\\nset1_xtnPlate3_e1,hair_p3.B7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B7,1,denvillewithaxygenbase_96_wellplate_200ul,5,B7,4\\nset1_xtnPlate3_e1,hair_p3.C7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C7,1,denvillewithaxygenbase_96_wellplate_200ul,2,C7,4\\nset1_xtnPlate3_e1,hair_p3.C7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C7,1,denvillewithaxygenbase_96_wellplate_200ul,5,C7,4\\nset1_xtnPlate3_e1,hair_p3.D7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D7,1,denvillewithaxygenbase_96_wellplate_200ul,2,D7,4\\nset1_xtnPlate3_e1,hair_p3.D7_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D7,1,denvillewithaxygenbase_96_wellplate_200ul,5,D7,4\\nset1_xtnPlate3_e1,hair_p3.A8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A8,1,denvillewithaxygenbase_96_wellplate_200ul,2,A8,4\\nset1_xtnPlate3_e1,hair_p3.A8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A8,1,denvillewithaxygenbase_96_wellplate_200ul,5,A8,4\\nset1_xtnPlate3_e1,hair_p3.B8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B8,1,denvillewithaxygenbase_96_wellplate_200ul,2,B8,4\\nset1_xtnPlate3_e1,hair_p3.B8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B8,1,denvillewithaxygenbase_96_wellplate_200ul,5,B8,4\\nset1_xtnPlate3_e1,hair_p3.C8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C8,1,denvillewithaxygenbase_96_wellplate_200ul,2,C8,4\\nset1_xtnPlate3_e1,hair_p3.C8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C8,1,denvillewithaxygenbase_96_wellplate_200ul,5,C8,4\\nset1_xtnPlate3_e1,hair_p3.D8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D8,1,denvillewithaxygenbase_96_wellplate_200ul,2,D8,4\\nset1_xtnPlate3_e1,hair_p3.D8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D8,1,denvillewithaxygenbase_96_wellplate_200ul,5,D8,4\\nset1_xtnPlate3_e1,hair_p3.E8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E8,1,denvillewithaxygenbase_96_wellplate_200ul,2,E8,4\\nset1_xtnPlate3_e1,hair_p3.E8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E8,1,denvillewithaxygenbase_96_wellplate_200ul,5,E8,4\\nset1_xtnPlate3_e1,hair_p3.F8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F8,1,denvillewithaxygenbase_96_wellplate_200ul,2,F8,4\\nset1_xtnPlate3_e1,hair_p3.F8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F8,1,denvillewithaxygenbase_96_wellplate_200ul,5,F8,4\\nset1_xtnPlate3_e1,hair_p3.G8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G8,1,denvillewithaxygenbase_96_wellplate_200ul,2,G8,4\\nset1_xtnPlate3_e1,hair_p3.G8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G8,1,denvillewithaxygenbase_96_wellplate_200ul,5,G8,4\\nset1_xtnPlate3_e1,hair_p3.H8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H8,1,denvillewithaxygenbase_96_wellplate_200ul,2,H8,4\\nset1_xtnPlate3_e1,hair_p3.H8_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H8,1,denvillewithaxygenbase_96_wellplate_200ul,5,H8,4\\nset1_xtnPlate3_e1,xtnNeg_p3.F9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F9,1,denvillewithaxygenbase_96_wellplate_200ul,2,F9,4\\nset1_xtnPlate3_e1,xtnNeg_p3.F9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F9,1,denvillewithaxygenbase_96_wellplate_200ul,5,F9,4\\nset1_xtnPlate3_e1,hair_p3.G9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G9,1,denvillewithaxygenbase_96_wellplate_200ul,2,G9,4\\nset1_xtnPlate3_e1,hair_p3.G9_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G9,1,denvillewithaxygenbase_96_wellplate_200ul,5,G9,4\\nset1_xtnPlate3_e1,hair_p3.A10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A10,1,denvillewithaxygenbase_96_wellplate_200ul,2,A10,4\\nset1_xtnPlate3_e1,hair_p3.A10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,A10,1,denvillewithaxygenbase_96_wellplate_200ul,5,A10,4\\nset1_xtnPlate3_e1,hair_p3.B10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B10,1,denvillewithaxygenbase_96_wellplate_200ul,2,B10,4\\nset1_xtnPlate3_e1,hair_p3.B10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B10,1,denvillewithaxygenbase_96_wellplate_200ul,5,B10,4\\nset1_xtnPlate3_e1,hair_p3.C10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C10,1,denvillewithaxygenbase_96_wellplate_200ul,2,C10,4\\nset1_xtnPlate3_e1,hair_p3.C10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C10,1,denvillewithaxygenbase_96_wellplate_200ul,5,C10,4\\nset1_xtnPlate3_e1,hair_p3.D10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D10,1,denvillewithaxygenbase_96_wellplate_200ul,2,D10,4\\nset1_xtnPlate3_e1,hair_p3.D10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D10,1,denvillewithaxygenbase_96_wellplate_200ul,5,D10,4\\nset1_xtnPlate3_e1,hair_p3.E10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E10,1,denvillewithaxygenbase_96_wellplate_200ul,2,E10,4\\nset1_xtnPlate3_e1,hair_p3.E10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E10,1,denvillewithaxygenbase_96_wellplate_200ul,5,E10,4\\nset1_xtnPlate3_e1,hair_p3.F10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F10,1,denvillewithaxygenbase_96_wellplate_200ul,2,F10,4\\nset1_xtnPlate3_e1,hair_p3.F10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F10,1,denvillewithaxygenbase_96_wellplate_200ul,5,F10,4\\nset1_xtnPlate3_e1,hair_p3.G10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G10,1,denvillewithaxygenbase_96_wellplate_200ul,2,G10,4\\nset1_xtnPlate3_e1,hair_p3.G10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G10,1,denvillewithaxygenbase_96_wellplate_200ul,5,G10,4\\nset1_xtnPlate3_e1,hair_p3.H10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H10,1,denvillewithaxygenbase_96_wellplate_200ul,2,H10,4\\nset1_xtnPlate3_e1,hair_p3.H10_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H10,1,denvillewithaxygenbase_96_wellplate_200ul,5,H10,4\\nset1_xtnPlate3_e1,hair_p3.B11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B11,1,denvillewithaxygenbase_96_wellplate_200ul,2,B11,4\\nset1_xtnPlate3_e1,hair_p3.B11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,B11,1,denvillewithaxygenbase_96_wellplate_200ul,5,B11,4\\nset1_xtnPlate3_e1,hair_p3.C11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C11,1,denvillewithaxygenbase_96_wellplate_200ul,2,C11,4\\nset1_xtnPlate3_e1,hair_p3.C11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,C11,1,denvillewithaxygenbase_96_wellplate_200ul,5,C11,4\\nset1_xtnPlate3_e1,hair_p3.D11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D11,1,denvillewithaxygenbase_96_wellplate_200ul,2,D11,4\\nset1_xtnPlate3_e1,hair_p3.D11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D11,1,denvillewithaxygenbase_96_wellplate_200ul,5,D11,4\\nset1_xtnPlate3_e1,hair_p3.E11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E11,1,denvillewithaxygenbase_96_wellplate_200ul,2,E11,4\\nset1_xtnPlate3_e1,hair_p3.E11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E11,1,denvillewithaxygenbase_96_wellplate_200ul,5,E11,4\\nset1_xtnPlate3_e1,hair_p3.F11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F11,1,denvillewithaxygenbase_96_wellplate_200ul,2,F11,4\\nset1_xtnPlate3_e1,hair_p3.F11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F11,1,denvillewithaxygenbase_96_wellplate_200ul,5,F11,4\\nset1_xtnPlate3_e1,hair_p3.G11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G11,1,denvillewithaxygenbase_96_wellplate_200ul,2,G11,4\\nset1_xtnPlate3_e1,hair_p3.G11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,G11,1,denvillewithaxygenbase_96_wellplate_200ul,5,G11,4\\nset1_xtnPlate3_e1,hair_p3.H11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H11,1,denvillewithaxygenbase_96_wellplate_200ul,2,H11,4\\nset1_xtnPlate3_e1,hair_p3.H11_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H11,1,denvillewithaxygenbase_96_wellplate_200ul,5,H11,4\\nset1_xtnPlate3_e1,hair_p3.D12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D12,1,denvillewithaxygenbase_96_wellplate_200ul,2,D12,4\\nset1_xtnPlate3_e1,hair_p3.D12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,D12,1,denvillewithaxygenbase_96_wellplate_200ul,5,D12,4\\nset1_xtnPlate3_e1,hair_p3.E12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E12,1,denvillewithaxygenbase_96_wellplate_200ul,2,E12,4\\nset1_xtnPlate3_e1,hair_p3.E12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,E12,1,denvillewithaxygenbase_96_wellplate_200ul,5,E12,4\\nset1_xtnPlate3_e1,hair_p3.F12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F12,1,denvillewithaxygenbase_96_wellplate_200ul,2,F12,4\\nset1_xtnPlate3_e1,hair_p3.F12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,F12,1,denvillewithaxygenbase_96_wellplate_200ul,5,F12,4\\nset1_xtnPlate3_e1,hair_p3.H12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H12,1,denvillewithaxygenbase_96_wellplate_200ul,2,H12,4\\nset1_xtnPlate3_e1,hair_p3.H12_e1,nest_96_wellplate_100ul_pcr_full_skirt,7,H12,1,denvillewithaxygenbase_96_wellplate_200ul,5,H12,4\\nset2.1_xtnPlate3_e2,hair_p3.G1_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,G1,1,denvillewithaxygenbase_96_wellplate_200ul,2,G1,4\\nset2.1_xtnPlate3_e2,hair_p3.G1_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,G1,1,denvillewithaxygenbase_96_wellplate_200ul,5,G1,4\\nset2.1_xtnPlate3_e2,hair_p3.B2_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,B2,1,denvillewithaxygenbase_96_wellplate_200ul,2,B2,4\\nset2.1_xtnPlate3_e2,hair_p3.B2_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,B2,1,denvillewithaxygenbase_96_wellplate_200ul,5,B2,4\\nset2.1_xtnPlate3_e2,hair_p3.D2_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,D2,1,denvillewithaxygenbase_96_wellplate_200ul,2,D2,4\\nset2.1_xtnPlate3_e2,hair_p3.D2_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,D2,1,denvillewithaxygenbase_96_wellplate_200ul,5,D2,4\\nset2.1_xtnPlate3_e2,hair_p3.G2_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,G2,1,denvillewithaxygenbase_96_wellplate_200ul,2,G2,4\\nset2.1_xtnPlate3_e2,hair_p3.G2_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,G2,1,denvillewithaxygenbase_96_wellplate_200ul,5,G2,4\\nset2.1_xtnPlate3_e2,hair_p3.H2_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,H2,1,denvillewithaxygenbase_96_wellplate_200ul,2,H2,4\\nset2.1_xtnPlate3_e2,hair_p3.H2_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,H2,1,denvillewithaxygenbase_96_wellplate_200ul,5,H2,4\\nset2.1_xtnPlate3_e2,hair_p3.A5_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,A5,1,denvillewithaxygenbase_96_wellplate_200ul,2,A5,4\\nset2.1_xtnPlate3_e2,hair_p3.A5_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,A5,1,denvillewithaxygenbase_96_wellplate_200ul,5,A5,4\\nset2.1_xtnPlate3_e2,hair_p3.F6_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,F6,1,denvillewithaxygenbase_96_wellplate_200ul,2,F6,4\\nset2.1_xtnPlate3_e2,hair_p3.F6_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,F6,1,denvillewithaxygenbase_96_wellplate_200ul,5,F6,4\\nset2.1_xtnPlate3_e2,hair_p3.E7_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,E7,1,denvillewithaxygenbase_96_wellplate_200ul,2,E7,4\\nset2.1_xtnPlate3_e2,hair_p3.E7_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,E7,1,denvillewithaxygenbase_96_wellplate_200ul,5,E7,4\\nset2.1_xtnPlate3_e2,hair_p3.F7_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,F7,1,denvillewithaxygenbase_96_wellplate_200ul,2,F7,4\\nset2.1_xtnPlate3_e2,hair_p3.F7_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,F7,1,denvillewithaxygenbase_96_wellplate_200ul,5,F7,4\\nset2.1_xtnPlate3_e2,hair_p3.G7_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,G7,1,denvillewithaxygenbase_96_wellplate_200ul,2,G7,4\\nset2.1_xtnPlate3_e2,hair_p3.G7_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,G7,1,denvillewithaxygenbase_96_wellplate_200ul,5,G7,4\\nset2.1_xtnPlate3_e2,hair_p3.H7_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,H7,1,denvillewithaxygenbase_96_wellplate_200ul,2,H7,4\\nset2.1_xtnPlate3_e2,hair_p3.H7_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,H7,1,denvillewithaxygenbase_96_wellplate_200ul,5,H7,4\\nset2.1_xtnPlate3_e2,hair_p3.A9_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,A9,1,denvillewithaxygenbase_96_wellplate_200ul,2,A9,4\\nset2.1_xtnPlate3_e2,hair_p3.A9_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,A9,1,denvillewithaxygenbase_96_wellplate_200ul,5,A9,4\\nset2.1_xtnPlate3_e2,hair_p3.B9_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,B9,1,denvillewithaxygenbase_96_wellplate_200ul,2,B9,4\\nset2.1_xtnPlate3_e2,hair_p3.B9_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,B9,1,denvillewithaxygenbase_96_wellplate_200ul,5,B9,4\\nset2.1_xtnPlate3_e2,hair_p3.D9_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,D9,1,denvillewithaxygenbase_96_wellplate_200ul,2,D9,4\\nset2.1_xtnPlate3_e2,hair_p3.D9_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,D9,1,denvillewithaxygenbase_96_wellplate_200ul,5,D9,4\\nset2.1_xtnPlate3_e2,hair_p3.E9_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,E9,1,denvillewithaxygenbase_96_wellplate_200ul,2,E9,4\\nset2.1_xtnPlate3_e2,hair_p3.E9_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,E9,1,denvillewithaxygenbase_96_wellplate_200ul,5,E9,4\\nset2.1_xtnPlate3_e2,hair_p3.H9_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,H9,1,denvillewithaxygenbase_96_wellplate_200ul,2,H9,4\\nset2.1_xtnPlate3_e2,hair_p3.H9_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,H9,1,denvillewithaxygenbase_96_wellplate_200ul,5,H9,4\\nset2.1_xtnPlate3_e2,hair_p3.G12_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,G12,1,denvillewithaxygenbase_96_wellplate_200ul,2,G12,4\\nset2.1_xtnPlate3_e2,hair_p3.G12_e2,nest_96_wellplate_100ul_pcr_full_skirt,7,G12,1,denvillewithaxygenbase_96_wellplate_200ul,5,G12,4\\nset2.2_xtnPlate3.tubes,hair_t76_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A1,1,denvillewithaxygenbase_96_wellplate_200ul,2,B1,4\\nset2.2_xtnPlate3.tubes,hair_t76_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A1,1,denvillewithaxygenbase_96_wellplate_200ul,5,B1,4\\nset2.2_xtnPlate3.tubes,hair_t86_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B1,1,denvillewithaxygenbase_96_wellplate_200ul,2,D1,4\\nset2.2_xtnPlate3.tubes,hair_t86_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B1,1,denvillewithaxygenbase_96_wellplate_200ul,5,D1,4\\nset2.2_xtnPlate3.tubes,hair_t62_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C1,1,denvillewithaxygenbase_96_wellplate_200ul,2,A2,4\\nset2.2_xtnPlate3.tubes,hair_t62_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C1,1,denvillewithaxygenbase_96_wellplate_200ul,5,A2,4\\nset2.2_xtnPlate3.tubes,hair_t96_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D1,1,denvillewithaxygenbase_96_wellplate_200ul,2,D3,4\\nset2.2_xtnPlate3.tubes,hair_t96_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D1,1,denvillewithaxygenbase_96_wellplate_200ul,5,D3,4\\nset2.2_xtnPlate3.tubes,hair_t110_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A2,1,denvillewithaxygenbase_96_wellplate_200ul,2,A12,4\\nset2.2_xtnPlate3.tubes,hair_t110_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A2,1,denvillewithaxygenbase_96_wellplate_200ul,5,A12,4\\nset2.2_xtnPlate3.tubes,hair_t23_e2,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B2,1,denvillewithaxygenbase_96_wellplate_200ul,2,C12,4\\nset2.2_xtnPlate3.tubes,hair_t23_e2,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B2,1,denvillewithaxygenbase_96_wellplate_200ul,5,C12,4\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A1,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A2,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A3,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A4,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A5,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A6,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A7,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A8,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A9,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A10,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A11,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A12,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A1,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A2,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A3,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A4,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A5,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A6,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A7,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A8,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A9,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A10,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A11,6\\nset3_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A12,6\\n","pipette_type_s20":"p20_single_gen2","pipette_mount_s20":"left","tip_type_s20":"opentrons_96_filtertiprack_20ul","tip_reuse_s20":"always", "pipette_type_m20":"p20_multi_gen2","pipette_mount_m20":"right","tip_type_m20":"opentrons_96_filtertiprack_20ul","tip_reuse_m20":"always"}""")
    return [_all_values[n] for n in names]


metadata = {
    'apiLevel': '2.8',
    'protocolName': 'tamGenetics_pcr1setup_p3ab',
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

    # transfers for SET 1: xtnPlate3_e1
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

    # PAUSE 1: switch to xtnPlate3_e2 + hair xtn tubes
    protocol.pause("PAUSE 1: i) Remove xtnPlate3_e1 and set aside. ii) Place xtnPlate1_e2 on magblock & hair xtn tubes on tuberack and resume run.")

    # transfers for SET 2: xtnPlate3_e2 + hair xtn tubes
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
    protocol.pause("PAUSE 2: i) Remove xtnPlate3_e2 & hair xtn tubes. ii) Check pcr plates to ensure that sufficient xtn volume was transfered AND that no beads were transferred. iii) For any wells with insufficient volume and/or beads, remove beads and/or manually transfer the sample. iv) Seal xtnPlate3_e1/e2 and place on ice. Place mastermix and resume run.")

    # Transfers for SET 3: mastermix for pcr1Plate3a/b
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