def get_values(*names):
    import json
    _all_values = json.loads("""{"transfer_csv":"ot2set,reagent,source_labware,source_slot,source_well,asp_height,dest_labware,dest_slot,dest_well,disp_height,transfer_volume\\nset1_pcr1.dilutionPlate,pcr1Plate2,denvillewithaxygenbase_96_wellplate_200ul,2,A1,0.25,nest_96_wellplate_100ul_pcr_full_skirt,5,A1,1,2\\nset1_pcr1.dilutionPlate,pcr1Plate2,denvillewithaxygenbase_96_wellplate_200ul,2,A2,0.25,nest_96_wellplate_100ul_pcr_full_skirt,5,A2,1,2\\nset1_pcr1.dilutionPlate,pcr1Plate2,denvillewithaxygenbase_96_wellplate_200ul,2,A3,0.25,nest_96_wellplate_100ul_pcr_full_skirt,5,A3,1,2\\nset1_pcr1.dilutionPlate,pcr1Plate2,denvillewithaxygenbase_96_wellplate_200ul,2,A4,0.25,nest_96_wellplate_100ul_pcr_full_skirt,5,A4,1,2\\nset1_pcr1.dilutionPlate,pcr1Plate2,denvillewithaxygenbase_96_wellplate_200ul,2,A5,0.25,nest_96_wellplate_100ul_pcr_full_skirt,5,A5,1,2\\nset1_pcr1.dilutionPlate,pcr1Plate2,denvillewithaxygenbase_96_wellplate_200ul,2,A6,0.25,nest_96_wellplate_100ul_pcr_full_skirt,5,A6,1,2\\nset1_pcr1.dilutionPlate,pcr1Plate2,denvillewithaxygenbase_96_wellplate_200ul,2,A7,0.25,nest_96_wellplate_100ul_pcr_full_skirt,5,A7,1,2\\nset1_pcr1.dilutionPlate,pcr1Plate2,denvillewithaxygenbase_96_wellplate_200ul,2,A8,0.25,nest_96_wellplate_100ul_pcr_full_skirt,5,A8,1,2\\nset1_pcr1.dilutionPlate,pcr1Plate2,denvillewithaxygenbase_96_wellplate_200ul,2,A9,0.25,nest_96_wellplate_100ul_pcr_full_skirt,5,A9,1,2\\nset1_pcr1.dilutionPlate,pcr1Plate2,denvillewithaxygenbase_96_wellplate_200ul,2,A10,0.25,nest_96_wellplate_100ul_pcr_full_skirt,5,A10,1,2\\nset1_pcr1.dilutionPlate,pcr1Plate2,denvillewithaxygenbase_96_wellplate_200ul,2,A11,0.25,nest_96_wellplate_100ul_pcr_full_skirt,5,A11,1,2\\nset1_pcr1.dilutionPlate,pcr1Plate2,denvillewithaxygenbase_96_wellplate_200ul,2,A12,0.25,nest_96_wellplate_100ul_pcr_full_skirt,5,A12,1,2\\nset2_water.dilutionPlate,nf-water,nest_12_reservoir_15ml,7,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A1,1,18\\nset2_water.dilutionPlate,nf-water,nest_12_reservoir_15ml,7,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A2,1,18\\nset2_water.dilutionPlate,nf-water,nest_12_reservoir_15ml,7,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A3,1,18\\nset2_water.dilutionPlate,nf-water,nest_12_reservoir_15ml,7,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A4,1,18\\nset2_water.dilutionPlate,nf-water,nest_12_reservoir_15ml,7,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A5,1,18\\nset2_water.dilutionPlate,nf-water,nest_12_reservoir_15ml,7,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A6,1,18\\nset2_water.dilutionPlate,nf-water,nest_12_reservoir_15ml,7,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A7,1,18\\nset2_water.dilutionPlate,nf-water,nest_12_reservoir_15ml,7,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A8,1,18\\nset2_water.dilutionPlate,nf-water,nest_12_reservoir_15ml,7,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A9,1,18\\nset2_water.dilutionPlate,nf-water,nest_12_reservoir_15ml,7,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A10,1,18\\nset2_water.dilutionPlate,nf-water,nest_12_reservoir_15ml,7,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A11,1,18\\nset2_water.dilutionPlate,nf-water,nest_12_reservoir_15ml,7,A1,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A12,1,18\\nset3_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A1,1,denvillewithaxygenbase_96_wellplate_200ul,8,A1,1,6\\nset3_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A2,1,denvillewithaxygenbase_96_wellplate_200ul,8,A2,1,6\\nset3_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A3,1,denvillewithaxygenbase_96_wellplate_200ul,8,A3,1,6\\nset3_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A4,1,denvillewithaxygenbase_96_wellplate_200ul,8,A4,1,6\\nset3_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A5,1,denvillewithaxygenbase_96_wellplate_200ul,8,A5,1,6\\nset3_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A6,1,denvillewithaxygenbase_96_wellplate_200ul,8,A6,1,6\\nset3_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A7,1,denvillewithaxygenbase_96_wellplate_200ul,8,A7,1,6\\nset3_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A8,1,denvillewithaxygenbase_96_wellplate_200ul,8,A8,1,6\\nset3_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A9,1,denvillewithaxygenbase_96_wellplate_200ul,8,A9,1,6\\nset3_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A10,1,denvillewithaxygenbase_96_wellplate_200ul,8,A10,1,6\\nset3_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A11,1,denvillewithaxygenbase_96_wellplate_200ul,8,A11,1,6\\nset3_dilutionPlate.pcr2,dilutionPlate,nest_96_wellplate_100ul_pcr_full_skirt,5,A12,1,denvillewithaxygenbase_96_wellplate_200ul,8,A12,1,6\\nset4_indexes.pcr2,indexPlate_setB,nest_96_wellplate_100ul_pcr_full_skirt,11,A1,3,denvillewithaxygenbase_96_wellplate_200ul,8,A1,1,4\\nset4_indexes.pcr2,indexPlate_setB,nest_96_wellplate_100ul_pcr_full_skirt,11,A2,3,denvillewithaxygenbase_96_wellplate_200ul,8,A2,1,4\\nset4_indexes.pcr2,indexPlate_setB,nest_96_wellplate_100ul_pcr_full_skirt,11,A3,3,denvillewithaxygenbase_96_wellplate_200ul,8,A3,1,4\\nset4_indexes.pcr2,indexPlate_setB,nest_96_wellplate_100ul_pcr_full_skirt,11,A4,3,denvillewithaxygenbase_96_wellplate_200ul,8,A4,1,4\\nset4_indexes.pcr2,indexPlate_setB,nest_96_wellplate_100ul_pcr_full_skirt,11,A5,3,denvillewithaxygenbase_96_wellplate_200ul,8,A5,1,4\\nset4_indexes.pcr2,indexPlate_setB,nest_96_wellplate_100ul_pcr_full_skirt,11,A6,3,denvillewithaxygenbase_96_wellplate_200ul,8,A6,1,4\\nset4_indexes.pcr2,indexPlate_setB,nest_96_wellplate_100ul_pcr_full_skirt,11,A7,3,denvillewithaxygenbase_96_wellplate_200ul,8,A7,1,4\\nset4_indexes.pcr2,indexPlate_setB,nest_96_wellplate_100ul_pcr_full_skirt,11,A8,3,denvillewithaxygenbase_96_wellplate_200ul,8,A8,1,4\\nset4_indexes.pcr2,indexPlate_setB,nest_96_wellplate_100ul_pcr_full_skirt,11,A9,3,denvillewithaxygenbase_96_wellplate_200ul,8,A9,1,4\\nset4_indexes.pcr2,indexPlate_setB,nest_96_wellplate_100ul_pcr_full_skirt,11,A10,3,denvillewithaxygenbase_96_wellplate_200ul,8,A10,1,4\\nset4_indexes.pcr2,indexPlate_setB,nest_96_wellplate_100ul_pcr_full_skirt,11,A11,3,denvillewithaxygenbase_96_wellplate_200ul,8,A11,1,4\\nset4_indexes.pcr2,indexPlate_setB,nest_96_wellplate_100ul_pcr_full_skirt,11,A12,3,denvillewithaxygenbase_96_wellplate_200ul,8,A12,1,4\\nset5_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A4,1,denvillewithaxygenbase_96_wellplate_200ul,8,A1,1,10\\nset5_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A4,1,denvillewithaxygenbase_96_wellplate_200ul,8,A2,1,10\\nset5_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A4,1,denvillewithaxygenbase_96_wellplate_200ul,8,A3,1,10\\nset5_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A4,1,denvillewithaxygenbase_96_wellplate_200ul,8,A4,1,10\\nset5_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A4,1,denvillewithaxygenbase_96_wellplate_200ul,8,A5,1,10\\nset5_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A4,1,denvillewithaxygenbase_96_wellplate_200ul,8,A6,1,10\\nset5_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A4,1,denvillewithaxygenbase_96_wellplate_200ul,8,A7,1,10\\nset5_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A4,1,denvillewithaxygenbase_96_wellplate_200ul,8,A8,1,10\\nset5_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A4,1,denvillewithaxygenbase_96_wellplate_200ul,8,A9,1,10\\nset5_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A4,1,denvillewithaxygenbase_96_wellplate_200ul,8,A10,1,10\\nset5_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A4,1,denvillewithaxygenbase_96_wellplate_200ul,8,A11,1,10\\nset5_kapa.pcr2,kapa,nest_12_reservoir_15ml,7,A4,1,denvillewithaxygenbase_96_wellplate_200ul,8,A12,1,10\\n","pipette_type":"p20_multi_gen2","pipette_mount":"right","tip_type":"opentrons_96_filtertiprack_20ul","tip_reuse":"always"}""")
    return [_all_values[n] for n in names]


metadata = {
    'apiLevel': '2.8',
    'protocolName': 'tamGenetics_dilutionsPCR2_p2',
    'author': 'Rachel Voyt',
    'source': 'Custom Protocol Request',
    'description': '''This protocol is a modified version of the 'Custom CSV Transfer' protocol from OT2. The protocol includes steps to transfer mastermix & samples, with adjustments to add a blowout after each transfer as well as a mix step after the water/mastermix transfer. The protocol also allows for the use of two pipette types (p20_single and p20_multi, both with filter tips) and includes pauses to switch out xtn plates & tubes.'''
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

    # transfers for SET 1: pcr1 to dilution plate
    for line in transfer_info:
        if line[0].startswith('set1'):
            _, _, _, s_slot, s_well, asp_h, _, d_slot, d_well, disp_h, vol = line[:11]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(asp_h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)].bottom(float(disp_h))
            if tip_reuse == 'always':
                pick_up()
            m20.distribute(float(vol),
                        source,
                        dest,
                        disposal_volume = 1,
                        touch_tip = True,
                        blow_out = True,
                        blowout_location = 'source well',
                        new_tip = 'never')
            if tip_reuse == 'always':
                m20.drop_tip()
    if m20.hw_pipette['has_tip']:
        m20.drop_tip()

    # PAUSE 1: check pcr1 transfers
    protocol.pause("PAUSE 1: Check the dilution plate to ensure that all PCR1 products were transferred. Manually transfer any that are missing or low. Resume run.")

    # transfers for SET 2: water to dilution plate
    for line in transfer_info:
        if line[0].startswith('set2'):
            _, _, _, s_slot, s_well, asp_h, _, d_slot, d_well, disp_h, vol = line[:11]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(asp_h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)].bottom(float(disp_h))
            if tip_reuse == 'always':
                pick_up()
            m20.transfer(float(vol),
                        source,
                        dest,
                        new_tip = 'never')
            if tip_reuse == 'always':
                m20.drop_tip()
    if m20.hw_pipette['has_tip']:
        m20.drop_tip()

    # transfers for SET 3: dilutions to pcr2 plate
    for line in transfer_info:
        if line[0].startswith('set3'):
            _, _, _, s_slot, s_well, asp_h, _, d_slot, d_well, disp_h, vol = line[:11]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(asp_h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)].bottom(float(disp_h))
            if tip_reuse == 'always':
                pick_up()
            m20.transfer(float(vol),
                        source,
                        dest,
                        mix_before = (10, 12),
                        new_tip = 'never')
            if tip_reuse == 'always':
                m20.drop_tip()
    if m20.hw_pipette['has_tip']:
        m20.drop_tip()

    # transfers for SET 4: index primers to pcr2 plate
    for line in transfer_info:
        if line[0].startswith('set4'):
            _, _, _, s_slot, s_well, asp_h, _, d_slot, d_well, disp_h, vol = line[:11]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(asp_h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)].bottom(float(disp_h))
            if tip_reuse == 'always':
                pick_up()
            m20.transfer(float(vol),
                        source,
                        dest,
                        mix_before = (10, 12),
                        new_tip = 'never')
            if tip_reuse == 'always':
                m20.drop_tip()
    if m20.hw_pipette['has_tip']:
        m20.drop_tip()

    # PAUSE 2: add kapa to reservoir
    protocol.pause("PAUSE 2: Add kapa to column 4 of reservoir. Resume run.")

    # transfers for SET 5: kapa to pcr2 plate
    for line in transfer_info:
        if line[0].startswith('set5'):
            _, _, _, s_slot, s_well, asp_h, _, d_slot, d_well, disp_h, vol = line[:11]
            source = protocol.loaded_labwares[
                int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(asp_h))
            dest = protocol.loaded_labwares[
                int(d_slot)].wells_by_name()[parse_well(d_well)].bottom(float(disp_h))
            if tip_reuse == 'always':
                pick_up()
            m20.transfer(float(vol),
                        source,
                        dest,
                        mix_after = (10, 6),
                        new_tip = 'never')
            if tip_reuse == 'always':
                m20.drop_tip()
    if m20.hw_pipette['has_tip']:
        m20.drop_tip()