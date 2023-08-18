def get_values(*names):
    import json
    _all_values = json.loads("""{"transfer_csv":"ot2set,reagent,source_labware,source_slot,source_well,asp_height,dest_labware,dest_slot,dest_well,disp_height,transfer_volume\\nset1_water.pcr1.dilutionPlate.pcr2,water.pcr1.dilution,nest_96_wellplate_100ul_pcr_full_skirt,6,A1,1,denvillewithaxygenbase_96_wellplate_200ul,2,A1,1,8\\nset1_water.pcr1.dilutionPlate.pcr2,water.pcr1.dilution,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,denvillewithaxygenbase_96_wellplate_200ul,2,A2,1,8\\nset1_water.pcr1.dilutionPlate.pcr2,water.pcr1.dilution,nest_96_wellplate_100ul_pcr_full_skirt,6,A3,1,denvillewithaxygenbase_96_wellplate_200ul,2,A3,1,8\\nset1_water.pcr1.dilutionPlate.pcr2,water.pcr1.dilution,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,denvillewithaxygenbase_96_wellplate_200ul,2,A4,1,8\\nset1_water.pcr1.dilutionPlate.pcr2,water.pcr1.dilution,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,denvillewithaxygenbase_96_wellplate_200ul,2,A5,1,8\\nset1_water.pcr1.dilutionPlate.pcr2,water.pcr1.dilution,nest_96_wellplate_100ul_pcr_full_skirt,6,A6,1,denvillewithaxygenbase_96_wellplate_200ul,2,A6,1,8\\nset1_water.pcr1.dilutionPlate.pcr2,water.pcr1.dilution,nest_96_wellplate_100ul_pcr_full_skirt,6,A7,1,denvillewithaxygenbase_96_wellplate_200ul,2,A7,1,8\\nset1_water.pcr1.dilutionPlate.pcr2,water.pcr1.dilution,nest_96_wellplate_100ul_pcr_full_skirt,6,A8,1,denvillewithaxygenbase_96_wellplate_200ul,2,A8,1,8\\nset1_water.pcr1.dilutionPlate.pcr2,water.pcr1.dilution,nest_96_wellplate_100ul_pcr_full_skirt,6,A9,1,denvillewithaxygenbase_96_wellplate_200ul,2,A9,1,8\\nset1_water.pcr1.dilutionPlate.pcr2,water.pcr1.dilution,nest_96_wellplate_100ul_pcr_full_skirt,6,A10,1,denvillewithaxygenbase_96_wellplate_200ul,2,A10,1,8\\nset1_water.pcr1.dilutionPlate.pcr2,water.pcr1.dilution,nest_96_wellplate_100ul_pcr_full_skirt,6,A11,1,denvillewithaxygenbase_96_wellplate_200ul,2,A11,1,8\\nset1_water.pcr1.dilutionPlate.pcr2,water.pcr1.dilution,nest_96_wellplate_100ul_pcr_full_skirt,6,A12,1,denvillewithaxygenbase_96_wellplate_200ul,2,A12,1,8\\nset2_indexes.pcr2,indexPlate_setA,nest_96_wellplate_100ul_pcr_full_skirt,11,A1,3,denvillewithaxygenbase_96_wellplate_200ul,8,A1,1,4\\nset2_indexes.pcr2,indexPlate_setA,nest_96_wellplate_100ul_pcr_full_skirt,11,A2,3,denvillewithaxygenbase_96_wellplate_200ul,8,A2,1,4\\nset2_indexes.pcr2,indexPlate_setA,nest_96_wellplate_100ul_pcr_full_skirt,11,A3,3,denvillewithaxygenbase_96_wellplate_200ul,8,A3,1,4\\nset2_indexes.pcr2,indexPlate_setA,nest_96_wellplate_100ul_pcr_full_skirt,11,A4,3,denvillewithaxygenbase_96_wellplate_200ul,8,A4,1,4\\nset2_indexes.pcr2,indexPlate_setA,nest_96_wellplate_100ul_pcr_full_skirt,11,A5,3,denvillewithaxygenbase_96_wellplate_200ul,8,A5,1,4\\nset2_indexes.pcr2,indexPlate_setA,nest_96_wellplate_100ul_pcr_full_skirt,11,A6,3,denvillewithaxygenbase_96_wellplate_200ul,8,A6,1,4\\nset2_indexes.pcr2,indexPlate_setA,nest_96_wellplate_100ul_pcr_full_skirt,11,A7,3,denvillewithaxygenbase_96_wellplate_200ul,8,A7,1,4\\nset2_indexes.pcr2,indexPlate_setA,nest_96_wellplate_100ul_pcr_full_skirt,11,A8,3,denvillewithaxygenbase_96_wellplate_200ul,8,A8,1,4\\nset2_indexes.pcr2,indexPlate_setA,nest_96_wellplate_100ul_pcr_full_skirt,11,A9,3,denvillewithaxygenbase_96_wellplate_200ul,8,A9,1,4\\nset2_indexes.pcr2,indexPlate_setA,nest_96_wellplate_100ul_pcr_full_skirt,11,A10,3,denvillewithaxygenbase_96_wellplate_200ul,8,A10,1,4\\nset2_indexes.pcr2,indexPlate_setA,nest_96_wellplate_100ul_pcr_full_skirt,11,A11,3,denvillewithaxygenbase_96_wellplate_200ul,8,A11,1,4\\nset2_indexes.pcr2,indexPlate_setA,nest_96_wellplate_100ul_pcr_full_skirt,11,A12,3,denvillewithaxygenbase_96_wellplate_200ul,8,A12,1,4\\nset3_kapa.pcr2,kapa,denvillewithaxygenbase_96_wellplate_200ul,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A1,1,10\\nset3_kapa.pcr2,kapa,denvillewithaxygenbase_96_wellplate_200ul,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A2,1,10\\nset3_kapa.pcr2,kapa,denvillewithaxygenbase_96_wellplate_200ul,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A3,1,10\\nset3_kapa.pcr2,kapa,denvillewithaxygenbase_96_wellplate_200ul,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A4,1,10\\nset3_kapa.pcr2,kapa,denvillewithaxygenbase_96_wellplate_200ul,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A5,1,10\\nset3_kapa.pcr2,kapa,denvillewithaxygenbase_96_wellplate_200ul,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A6,1,10\\nset3_kapa.pcr2,kapa,denvillewithaxygenbase_96_wellplate_200ul,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A7,1,10\\nset3_kapa.pcr2,kapa,denvillewithaxygenbase_96_wellplate_200ul,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A8,1,10\\nset3_kapa.pcr2,kapa,denvillewithaxygenbase_96_wellplate_200ul,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A9,1,10\\nset3_kapa.pcr2,kapa,denvillewithaxygenbase_96_wellplate_200ul,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A10,1,10\\nset3_kapa.pcr2,kapa,denvillewithaxygenbase_96_wellplate_200ul,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A11,1,10\\nset3_kapa.pcr2,kapa,denvillewithaxygenbase_96_wellplate_200ul,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A12,1,10\\n","pipette_type":"p20_multi_gen2","pipette_mount":"right","tip_type":"opentrons_96_filtertiprack_20ul","tip_reuse":"always"}""")
    return [_all_values[n] for n in names]


metadata = {
    'apiLevel': '2.8',
    'protocolName': 'tamGenetics_dilutionsPCR2_p1Take2_kapa',
    'author': 'Rachel Voyt',
    'description': '''This protocol is to dilute PCR1 products and set up PCR2 using a p20_multi pipette.'''
}

def run(protocol):

    [pipette_type,
     pipette_mount,
     tip_type,
     tip_reuse,
     transfer_csv] = get_values(  # noqa: F821
        "pipette_type",
        "pipette_mount",
        "tip_type",
        "tip_reuse",
        "transfer_csv")

    # strip headers
    transfer_info = [[val.strip().lower() for val in line.split(',')]
                     for line in transfer_csv.splitlines()
                     if line.split(',')[0].strip()][1:]
    
    # load labware
    lw_pcr1Plate = protocol.load_labware("denvillewithaxygenbase_96_wellplate_200ul", 2)
    lw_dilutionPlate = protocol.load_labware("nest_96_wellplate_100ul_pcr_full_skirt", 5)
    lw_waterPlate = protocol.load_labware("nest_96_wellplate_100ul_pcr_full_skirt", 6)
    lw_kapaReservoir = protocol.load_labware("denvillewithaxygenbase_96_wellplate_200ul", 7)
    lw_pcr2Plate = protocol.load_labware("denvillewithaxygenbase_96_wellplate_200ul", 8)
    lw_indexPlate = protocol.load_labware("nest_96_wellplate_100ul_pcr_full_skirt", 11)

    # load tipracks
    tipracks = [protocol.load_labware(tip_type, slot)
            for slot in ['1', '4', '10']]

    # load pipettes
    m20 = protocol.load_instrument(pipette_type, pipette_mount, tip_racks=tipracks)
            
    tip_count = 0
    tip_max = len(tipracks*96)

    def pick_up():
        nonlocal tip_count
        if tip_count == tip_max:
            protocol.pause('Please refill 20 ul tipracks for m20 before resuming.')
            m20.reset_tipracks()
            tip_count = 0
        m20.pick_up_tip()
        tip_count += 8

    def parse_well(well):
        letter = well[0]
        number = well[1:]
        return letter.upper() + str(int(number))

    if tip_reuse == 'never':
        pick_up()

    # transfers for SET 3: kapa to pcr2 plate
    for line in transfer_info:
        if line[0].startswith('set3'):
            _, _, _, _, s_well, _, _, _, d_well, _, vol = line[:11]
            kapaReservoir = lw_kapaReservoir.wells_by_name()[parse_well(s_well)].bottom(1)
            pcr2Plate = lw_pcr2Plate.wells_by_name()[parse_well(d_well)].bottom(1)
            if tip_reuse == 'always':
                pick_up()
            m20.flow_rate.aspirate = 7.6
            m20.flow_rate.dispense = 7.6
            m20.transfer(float(vol),
                        kapaReservoir,
                        pcr2Plate,
                        mix_after = (10, 12),
                        new_tip = 'never')
            if tip_reuse == 'always':
                m20.drop_tip()
    if m20.hw_pipette['has_tip']:
        m20.drop_tip()