def get_values(*names):
    import json
    _all_values = json.loads("""{"transfer_csv":"ot2set,reagent,source_labware,source_slot,source_well,asp_height,dest_labware,dest_slot,dest_well,disp_height,transfer_volume\\nset3_water.dilutionPlate,nf-water,nest_96_wellplate_100ul_pcr_full_skirt,6,A2,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A2,1,36\\nset3_water.dilutionPlate,nf-water,nest_96_wellplate_100ul_pcr_full_skirt,6,A3,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A3,1,36\\nset3_water.dilutionPlate,nf-water,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A4,1,36\\nset3_water.dilutionPlate,nf-water,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A5,1,36\\nset3_water.dilutionPlate,nf-water,nest_96_wellplate_100ul_pcr_full_skirt,6,A6,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A6,1,36\\nset3_water.dilutionPlate,nf-water,nest_96_wellplate_100ul_pcr_full_skirt,6,A7,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A7,1,36\\nset3_water.dilutionPlate,nf-water,nest_96_wellplate_100ul_pcr_full_skirt,6,A8,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A8,1,36\\nset3_water.dilutionPlate,nf-water,nest_96_wellplate_100ul_pcr_full_skirt,6,A9,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A9,1,36\\nset3_water.dilutionPlate,nf-water,nest_96_wellplate_100ul_pcr_full_skirt,6,A10,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A10,1,36\\nset3_water.dilutionPlate,nf-water,nest_96_wellplate_100ul_pcr_full_skirt,6,A11,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A11,1,36\\nset3_water.dilutionPlate,nf-water,nest_96_wellplate_100ul_pcr_full_skirt,6,A12,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A12,1,36\\nset4_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A1,1,6\\nset4_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A2,1,denvillewithaxygenbase_96_wellplate_200ul,8,A2,1,6\\nset4_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A3,1,denvillewithaxygenbase_96_wellplate_200ul,8,A3,1,6\\nset4_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A4,1,denvillewithaxygenbase_96_wellplate_200ul,8,A4,1,6\\nset4_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A5,1,denvillewithaxygenbase_96_wellplate_200ul,8,A5,1,6\\nset4_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A6,1,denvillewithaxygenbase_96_wellplate_200ul,8,A6,1,6\\nset4_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A7,1,denvillewithaxygenbase_96_wellplate_200ul,8,A7,1,6\\nset4_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A8,1,denvillewithaxygenbase_96_wellplate_200ul,8,A8,1,6\\nset4_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A9,1,denvillewithaxygenbase_96_wellplate_200ul,8,A9,1,6\\nset4_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A10,1,denvillewithaxygenbase_96_wellplate_200ul,8,A10,1,6\\nset4_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A11,1,denvillewithaxygenbase_96_wellplate_200ul,8,A11,1,6\\nset4_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A12,1,denvillewithaxygenbase_96_wellplate_200ul,8,A12,1,6\\nset5_indexes.pcr2,indexPlate_setC,nest_96_wellplate_100ul_pcr_full_skirt,11,A1,3,denvillewithaxygenbase_96_wellplate_200ul,8,A1,1,4\\nset5_indexes.pcr2,indexPlate_setC,nest_96_wellplate_100ul_pcr_full_skirt,11,A2,3,denvillewithaxygenbase_96_wellplate_200ul,8,A2,1,4\\nset5_indexes.pcr2,indexPlate_setC,nest_96_wellplate_100ul_pcr_full_skirt,11,A3,3,denvillewithaxygenbase_96_wellplate_200ul,8,A3,1,4\\nset5_indexes.pcr2,indexPlate_setC,nest_96_wellplate_100ul_pcr_full_skirt,11,A4,3,denvillewithaxygenbase_96_wellplate_200ul,8,A4,1,4\\nset5_indexes.pcr2,indexPlate_setC,nest_96_wellplate_100ul_pcr_full_skirt,11,A5,3,denvillewithaxygenbase_96_wellplate_200ul,8,A5,1,4\\nset5_indexes.pcr2,indexPlate_setC,nest_96_wellplate_100ul_pcr_full_skirt,11,A6,3,denvillewithaxygenbase_96_wellplate_200ul,8,A6,1,4\\nset5_indexes.pcr2,indexPlate_setC,nest_96_wellplate_100ul_pcr_full_skirt,11,A7,3,denvillewithaxygenbase_96_wellplate_200ul,8,A7,1,4\\nset5_indexes.pcr2,indexPlate_setC,nest_96_wellplate_100ul_pcr_full_skirt,11,A8,3,denvillewithaxygenbase_96_wellplate_200ul,8,A8,1,4\\nset5_indexes.pcr2,indexPlate_setC,nest_96_wellplate_100ul_pcr_full_skirt,11,A9,3,denvillewithaxygenbase_96_wellplate_200ul,8,A9,1,4\\nset5_indexes.pcr2,indexPlate_setC,nest_96_wellplate_100ul_pcr_full_skirt,11,A10,3,denvillewithaxygenbase_96_wellplate_200ul,8,A10,1,4\\nset5_indexes.pcr2,indexPlate_setC,nest_96_wellplate_100ul_pcr_full_skirt,11,A11,3,denvillewithaxygenbase_96_wellplate_200ul,8,A11,1,4\\nset5_indexes.pcr2,indexPlate_setC,nest_96_wellplate_100ul_pcr_full_skirt,11,A12,3,denvillewithaxygenbase_96_wellplate_200ul,8,A12,1,4\\nset6_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A1,1,10\\nset6_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A2,1,10\\nset6_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A3,1,10\\nset6_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A4,1,10\\nset6_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A5,1,10\\nset6_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A6,1,10\\nset6_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A7,1,10\\nset6_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A8,1,10\\nset6_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A9,1,10\\nset6_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A10,1,10\\nset6_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A11,1,10\\nset6_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A12,1,10\\n","pipette_type":"p20_multi_gen2","pipette_mount":"right","tip_type":"opentrons_96_filtertiprack_20ul","tip_reuse":"always"}""")
    return [_all_values[n] for n in names]


metadata = {
    'apiLevel': '2.8',
    'protocolName': 'tamGenetics_dilutionsPCR2_p3ab_waterAdjust',
    'author': 'Rachel Voyt',
    'source': 'Custom Protocol Request',
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
    pcr2Plate = protocol.load_labware("denvillewithaxygenbase_96_wellplate_200ul", 8)
    for line in transfer_info:
        s_lw, s_slot, d_lw, d_slot = line[2:4] + line[6:8]
        for slot, lw in zip([s_slot, d_slot], [s_lw, d_lw]):
            if not int(slot) in protocol.loaded_labwares:
                protocol.load_labware(lw.lower(), slot)

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

    # transfers for SETS 3 & 4: water to dilution plate + dilutions to pcr2 plate
    for line in transfer_info:
        if line[0].startswith('set3'):
            _, _, _, s_slot, s_well, asp_h, _, d_slot, d_well, disp_h, vol = line[:11]
            source1 = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(asp_h))
            dest1 = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)].bottom(float(disp_h))
            source2 = dest1
            dest2 = pcr2Plate.wells_by_name()[parse_well(d_well)].bottom(float(disp_h))
            if tip_reuse == 'always':
                pick_up()
            m20.flow_rate.aspirate = 7.6
            m20.flow_rate.dispense = 7.6
            m20.transfer(float(vol),
                        source1,
                        dest1,
                        new_tip = 'never')
            m20.transfer(6,
                        source2,
                        dest2,
                        mix_before = (10, 12),
                        new_tip = 'never')
            if tip_reuse == 'always':
                m20.drop_tip()
    if m20.hw_pipette['has_tip']:
        m20.drop_tip()

    # transfers for SET 5: index primers to pcr2 plate
    for line in transfer_info:
        if line[0].startswith('set5'):
            _, _, _, s_slot, s_well, asp_h, _, d_slot, d_well, disp_h, vol = line[:11]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(asp_h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)].bottom(float(disp_h))
            if tip_reuse == 'always':
                pick_up()
            m20.flow_rate.aspirate = 7.6
            m20.flow_rate.dispense = 7.6
            m20.transfer(float(vol),
                        source,
                        dest,
                        mix_before = (10, 20),
                        new_tip = 'never')
            if tip_reuse == 'always':
                m20.drop_tip()
    if m20.hw_pipette['has_tip']:
        m20.drop_tip()

    # PAUSE 3: add kapa to reservoir
    protocol.pause("PAUSE 3: Add kapa to column 1 of reservoir. Resume run.")

    # transfers for SET 6: kapa to pcr2 plate
    for line in transfer_info:
        if line[0].startswith('set6'):
            _, _, _, s_slot, s_well, asp_h, _, d_slot, d_well, disp_h, vol = line[:11]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(asp_h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)].bottom(float(disp_h))
            if tip_reuse == 'always':
                pick_up()
            m20.flow_rate.aspirate = 7.6
            m20.flow_rate.dispense = 7.6
            m20.transfer(float(vol),
                        source,
                        dest,
                        mix_after = (10, 12),
                        new_tip = 'never')
            if tip_reuse == 'always':
                m20.drop_tip()
    if m20.hw_pipette['has_tip']:
        m20.drop_tip()