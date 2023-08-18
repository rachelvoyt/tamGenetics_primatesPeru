def get_values(*names):
    import json
    _all_values = json.loads("""{"transfer_csv":"ot2set,reagent,source_labware,source_slot,source_well,asp_height,dest_labware,dest_slot,dest_well,transfer_volume\\nset1_tubes1to24,hair_t8_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A1,1,denvillewithaxygenbase_96_wellplate_200ul,2,A1,4\\nset1_tubes1to24,hair_t9_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B1,1,denvillewithaxygenbase_96_wellplate_200ul,2,B1,4\\nset1_tubes1to24,hair_t16_e2,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C1,1,denvillewithaxygenbase_96_wellplate_200ul,2,C1,4\\nset1_tubes1to24,hair_tx8A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D1,1,denvillewithaxygenbase_96_wellplate_200ul,2,D1,4\\nset1_tubes1to24,hair_tx15B_e2,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A2,1,denvillewithaxygenbase_96_wellplate_200ul,2,E1,4\\nset1_tubes1to24,hair_tx17A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B2,1,denvillewithaxygenbase_96_wellplate_200ul,2,F1,4\\nset1_tubes1to24,hair_tx19A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C2,1,denvillewithaxygenbase_96_wellplate_200ul,2,G1,4\\nset1_tubes1to24,hair_tx20B_e2,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D2,1,denvillewithaxygenbase_96_wellplate_200ul,2,H1,4\\nset1_tubes1to24,hair_tx23A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A3,1,denvillewithaxygenbase_96_wellplate_200ul,2,A2,4\\nset1_tubes1to24,hair_tx24A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B3,1,denvillewithaxygenbase_96_wellplate_200ul,2,B2,4\\nset1_tubes1to24,hair_tx25B_e2,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C3,1,denvillewithaxygenbase_96_wellplate_200ul,2,C2,4\\nset1_tubes1to24,hair_tx28A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D3,1,denvillewithaxygenbase_96_wellplate_200ul,2,D2,4\\nset1_tubes1to24,hair_tx29A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A4,1,denvillewithaxygenbase_96_wellplate_200ul,2,E2,4\\nset1_tubes1to24,hair_tx30A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B4,1,denvillewithaxygenbase_96_wellplate_200ul,2,F2,4\\nset1_tubes1to24,hair_tx31A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C4,1,denvillewithaxygenbase_96_wellplate_200ul,2,G2,4\\nset1_tubes1to24,hair_tx32A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D4,1,denvillewithaxygenbase_96_wellplate_200ul,2,H2,4\\nset1_tubes1to24,hair_tx35A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A5,1,denvillewithaxygenbase_96_wellplate_200ul,2,A3,4\\nset1_tubes1to24,hair_tx38A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B5,1,denvillewithaxygenbase_96_wellplate_200ul,2,B3,4\\nset1_tubes1to24,hair_tx39A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C5,1,denvillewithaxygenbase_96_wellplate_200ul,2,C3,4\\nset1_tubes1to24,hair_tx40A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D5,1,denvillewithaxygenbase_96_wellplate_200ul,2,D3,4\\nset1_tubes1to24,hair_tx41A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A6,1,denvillewithaxygenbase_96_wellplate_200ul,2,E3,4\\nset1_tubes1to24,hair_tx42A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B6,1,denvillewithaxygenbase_96_wellplate_200ul,2,F3,4\\nset1_tubes1to24,hair_tx43A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C6,1,denvillewithaxygenbase_96_wellplate_200ul,2,G3,4\\nset1_tubes1to24,hair_tx44A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D6,1,denvillewithaxygenbase_96_wellplate_200ul,2,H3,4\\nset2_tubes25to48,hair_tx45A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A1,1,denvillewithaxygenbase_96_wellplate_200ul,2,A4,4\\nset2_tubes25to48,hair_tx47A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B1,1,denvillewithaxygenbase_96_wellplate_200ul,2,B4,4\\nset2_tubes25to48,hair_pcr1Neg,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C1,1,denvillewithaxygenbase_96_wellplate_200ul,2,C4,4\\nset2_tubes25to48,hair_tx48B_e2,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D1,1,denvillewithaxygenbase_96_wellplate_200ul,2,D4,4\\nset2_tubes25to48,hair_tx50A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A2,1,denvillewithaxygenbase_96_wellplate_200ul,2,E4,4\\nset2_tubes25to48,hair_tx52A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B2,1,denvillewithaxygenbase_96_wellplate_200ul,2,F4,4\\nset2_tubes25to48,hair_tx53A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C2,1,denvillewithaxygenbase_96_wellplate_200ul,2,G4,4\\nset2_tubes25to48,hair_tx57A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D2,1,denvillewithaxygenbase_96_wellplate_200ul,2,H4,4\\nset2_tubes25to48,hair_tx59A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A3,1,denvillewithaxygenbase_96_wellplate_200ul,2,A5,4\\nset2_tubes25to48,hair_tx60A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B3,1,denvillewithaxygenbase_96_wellplate_200ul,2,B5,4\\nset2_tubes25to48,hair_tx67A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C3,1,denvillewithaxygenbase_96_wellplate_200ul,2,C5,4\\nset2_tubes25to48,hair_tx69A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D3,1,denvillewithaxygenbase_96_wellplate_200ul,2,D5,4\\nset2_tubes25to48,hair_tx70A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A4,1,denvillewithaxygenbase_96_wellplate_200ul,2,E5,4\\nset2_tubes25to48,hair_tx73B_e2,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B4,1,denvillewithaxygenbase_96_wellplate_200ul,2,F5,4\\nset2_tubes25to48,hair_tx75A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C4,1,denvillewithaxygenbase_96_wellplate_200ul,2,G5,4\\nset2_tubes25to48,hair_tx76A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D4,1,denvillewithaxygenbase_96_wellplate_200ul,2,H5,4\\nset2_tubes25to48,hair_tx77A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A5,1,denvillewithaxygenbase_96_wellplate_200ul,2,A6,4\\nset2_tubes25to48,hair_tx84A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B5,1,denvillewithaxygenbase_96_wellplate_200ul,2,B6,4\\nset2_tubes25to48,hair_tx85A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C5,1,denvillewithaxygenbase_96_wellplate_200ul,2,C6,4\\nset2_tubes25to48,hair_tx87A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D5,1,denvillewithaxygenbase_96_wellplate_200ul,2,D6,4\\nset2_tubes25to48,hair_tx89A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A6,1,denvillewithaxygenbase_96_wellplate_200ul,2,E6,4\\nset2_tubes25to48,hair_tx91A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B6,1,denvillewithaxygenbase_96_wellplate_200ul,2,F6,4\\nset2_tubes25to48,hair_tx93A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,C6,1,denvillewithaxygenbase_96_wellplate_200ul,2,G6,4\\nset2_tubes25to48,hair_tx104A_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,D6,1,denvillewithaxygenbase_96_wellplate_200ul,2,H6,4\\nset3_tubes49up,hair_tx105B_e2,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,A1,1,denvillewithaxygenbase_96_wellplate_200ul,2,A7,4\\nset3_tubes49up,hair_txWBO_e1,opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap,3,B1,1,denvillewithaxygenbase_96_wellplate_200ul,2,B7,4\\nset4_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A1,6\\nset4_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A2,6\\nset4_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A3,6\\nset4_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A4,6\\nset4_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A5,6\\nset4_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A6,6\\nset4_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A4,1,nest_96_wellplate_100ul_pcr_full_skirt,2,A7,6\\nset4_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A1,6\\nset4_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A2,6\\nset4_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A3,6\\nset4_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A4,6\\nset4_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A5,6\\nset4_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A6,6\\nset4_mm,mastermix,nest_96_wellplate_100ul_pcr_full_skirt,6,A5,1,nest_96_wellplate_100ul_pcr_full_skirt,5,A7,6\\n","pipette_type_s20":"p20_single_gen2","pipette_mount_s20":"left","tip_type_s20":"opentrons_96_filtertiprack_20ul","tip_reuse_s20":"always", "pipette_type_m20":"p20_multi_gen2","pipette_mount_m20":"right","tip_type_m20":"opentrons_96_filtertiprack_20ul","tip_reuse_m20":"always"}""")
    return [_all_values[n] for n in names]

metadata = {
    'apiLevel': '2.8',
    'protocolName': 'tamGenetics_pcr1setup_p5ab',
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
            for slot in ['1']]
    tipracks_m20 = [protocol.load_labware(tip_type_m20, slot)
            for slot in ['4', '7']]

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

    # transfers for SET 1: xtn tubes 1 to 24
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

    # PAUSE 1: switch to tubes 25 to 48
    protocol.pause("PAUSE 1: i) Remove xtns and set aside. ii) Check pcr plates to ensure that sufficient xtn volume was transfered. iii) For any wells with insufficient volume, manually transfer the sample. iv) Seal xtn plates & tubes and place on ice. Place tubes 25 to 48 on tuberack and resume run.")

    # transfers for SET 2: xtn tubes 25 to 48
    for line in transfer_info:
        if line[0].startswith('set2'):
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

    # PAUSE 2: switch to tubes 49 & up
    protocol.pause("PAUSE 2: i) Remove xtns and set aside. ii) Check pcr plates to ensure that sufficient xtn volume was transfered. iii) For any wells with insufficient volume, manually transfer the sample. iv) Seal xtn plates & tubes and place on ice. Place tubes 49 & up on tuberack and resume run.")

    # transfers for SET 3: xtn tubes 49 & up
    for line in transfer_info:
        if line[0].startswith('set3'):
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

    # PAUSE 3: switch to mastermix
    protocol.pause("PAUSE 3: i) Remove xtns and set aside. ii) Check pcr plates to ensure that sufficient xtn volume was transfered. iii) For any wells with insufficient volume, manually transfer the sample. iv) Seal xtn plates & tubes and place on ice. Place mastermix and resume run.")

    # Transfers for SET 4: mastermix for pcr1Plate5a/b
    for line in transfer_info:
        if line[0].startswith('set4'):
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