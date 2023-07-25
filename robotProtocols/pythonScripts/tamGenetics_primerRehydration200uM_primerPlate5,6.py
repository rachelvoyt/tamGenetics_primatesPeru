def get_values(*names):
    import json
    _all_values = json.loads("""{"transfer_csv":"\"source_labware\",\"source_slot\",\"source_well\",\"asp_height\",\"dest_labware\",\"dest_slot\",\"dest_well\",\"transfer_volume\"\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"A1\",84.6\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"B1\",111.5\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"C1\",103.8\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"D1\",136.5\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"E1\",108.2\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"F1\",113.5\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"G1\",119.3\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"H1\",108.4\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"A2\",91.8\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"B2\",115.6\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"C2\",108.8\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"D2\",115.4\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"E2\",103.6\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"F2\",137.1\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"G2\",134.6\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"H2\",124.8\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"A3\",120\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"B3\",98.4\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"C3\",132.3\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"D3\",139.8\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"E3\",126.6\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"F3\",136.3\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"G3\",126\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"H3\",141\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"A4\",108.9\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"B4\",100.1\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"C4\",131.5\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"D4\",119.7\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"E4\",119.2\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"F4\",100.4\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"G4\",139.9\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"H4\",110\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"A5\",110.2\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"B5\",102.3\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"C5\",101.8\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"D5\",126.6\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"E5\",127.3\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"F5\",124.9\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"G5\",109.6\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"H5\",138.6\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"A6\",103.6\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"B6\",102.5\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"C6\",114\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"D6\",112.5\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"E6\",130.9\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"F6\",119.2\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"G6\",134.1\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"H6\",117\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"A7\",108.7\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"B7\",106\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"C7\",130.3\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"D7\",104.2\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"E7\",114.4\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"F7\",139.3\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"G7\",119.8\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"H7\",129.7\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"A8\",89.2\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"B8\",112.2\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"C8\",100.8\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"D8\",120\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"E8\",130.5\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"F8\",134.1\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"G8\",130.3\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"H8\",131\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"A9\",98.5\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"B9\",119.4\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"C9\",117.1\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"D9\",119.8\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"E9\",136.3\\n\"nest_12_reservoir_15ml\",2,\"A3\",1,\"vwr_96_wellplate_1000ul\",3,\"F9\",124\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"A1\",85.2\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"B1\",91.4\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"C1\",99.3\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"D1\",104.8\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"E1\",111.7\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"F1\",93.2\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"G1\",126.1\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"H1\",131.9\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"A2\",102.3\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"B2\",114.9\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"C2\",118.5\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"D2\",110.8\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"E2\",118.7\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"F2\",134.8\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"G2\",121.6\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"H2\",129.4\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"A3\",114.9\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"B3\",114.9\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"C3\",126.2\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"D3\",126.9\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"E3\",109.3\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"F3\",128.9\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"G3\",179.1\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"H3\",123.1\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"A4\",99.8\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"B4\",113.6\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"C4\",115.5\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"D4\",121.6\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"E4\",171.1\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"F4\",113.4\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"G4\",122.3\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"H4\",166.5\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"A5\",112\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"B5\",124.9\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"C5\",127.7\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"D5\",126.9\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"E5\",144.9\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"F5\",131.1\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"G5\",124.2\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"H5\",102\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"A6\",108.9\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"B6\",112.2\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"C6\",118.6\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"D6\",123.2\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"E6\",136.7\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"F6\",121.6\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"G6\",139.2\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"H6\",109.9\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"A7\",107.3\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"B7\",110.8\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"C7\",117.7\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"D7\",123.5\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"E7\",118.1\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"F7\",130.8\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"G7\",132.2\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"H7\",138.8\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"A8\",86.7\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"B8\",116.9\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"C8\",110.8\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"D8\",124.8\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"E8\",130.6\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"F8\",129.3\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"G8\",119.7\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"H8\",132.3\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"A9\",108.2\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"B9\",107\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"C9\",122\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"D9\",120.1\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"E9\",132.6\\n\"nest_12_reservoir_15ml\",2,\"A2\",1,\"vwr_96_wellplate_1000ul\",6,\"F9\",124.4\\n","pipette_type":"p300_single_gen2","pipette_mount":"right","tip_type":"standard","tip_reuse":"always"}""")
    return [_all_values[n] for n in names]


metadata = {
    'protocolName': 'Custom CSV Transfer Protocol',
    'author': 'Nick <protocols@opentrons.com>',
    'source': 'Custom Protocol Request',
    'apiLevel': '2.3'
}


def run(ctx):

    [pipette_type, pipette_mount, tip_type,
     tip_reuse, transfer_csv] = get_values(  # noqa: F821
        "pipette_type", "pipette_mount", "tip_type", "tip_reuse",
        "transfer_csv")

    tiprack_map = {
        'p10_single': {
            'standard': 'opentrons_96_tiprack_10ul',
            'filter': 'opentrons_96_filtertiprack_20ul'
        },
        'p50_single': {
            'standard': 'opentrons_96_tiprack_300ul',
            'filter': 'opentrons_96_filtertiprack_200ul'
        },
        'p300_single': {
            'standard': 'opentrons_96_tiprack_300ul',
            'filter': 'opentrons_96_filtertiprack_200ul'
        },
        'p1000_single': {
            'standard': 'opentrons_96_tiprack_1000ul',
            'filter': 'opentrons_96_filtertiprack_1000ul'
        },
        'p20_single_gen2': {
            'standard': 'opentrons_96_tiprack_20ul',
            'filter': 'opentrons_96_filtertiprack_20ul'
        },
        'p300_single_gen2': {
            'standard': 'opentrons_96_tiprack_300ul',
            'filter': 'opentrons_96_filtertiprack_200ul'
        },
        'p1000_single_gen2': {
            'standard': 'opentrons_96_tiprack_1000ul',
            'filter': 'opentrons_96_filtertiprack_1000ul'
        }
    }

    # load labware
    transfer_info = [[val.strip().lower() for val in line.split(',')]
                     for line in transfer_csv.splitlines()
                     if line.split(',')[0].strip()][1:]
    for line in transfer_info:
        s_lw, s_slot, d_lw, d_slot = line[:2] + line[4:6]
        for slot, lw in zip([s_slot, d_slot], [s_lw, d_lw]):
            if not int(slot) in ctx.loaded_labwares:
                ctx.load_labware(lw.lower(), slot)

    # load tipracks in remaining slots
    tiprack_type = tiprack_map[pipette_type][tip_type]
    tipracks = []
    for slot in range(1, 13):
        if slot not in ctx.loaded_labwares:
            tipracks.append(ctx.load_labware(tiprack_type, str(slot)))

    # load pipette
    pip = ctx.load_instrument(pipette_type, pipette_mount, tip_racks=tipracks)

    tip_count = 0
    tip_max = len(tipracks*96)

    def pick_up():
        nonlocal tip_count
        if tip_count == tip_max:
            ctx.pause('Please refill tipracks before resuming.')
            pip.reset_tipracks()
            tip_count = 0
        pip.pick_up_tip()
        tip_count += 1

    def parse_well(well):
        letter = well[0]
        number = well[1:]
        return letter.upper() + str(int(number))

    if tip_reuse == 'never':
        pick_up()
    for line in transfer_info:
        _, s_slot, s_well, h, _, d_slot, d_well, vol = line[:8]
        source = ctx.loaded_labwares[
            int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(h))
        dest = ctx.loaded_labwares[
            int(d_slot)].wells_by_name()[parse_well(d_well)]
        if tip_reuse == 'always':
            pick_up()
        pip.transfer(float(vol), source, dest, new_tip='never')
        if tip_reuse == 'always':
            pip.drop_tip()
    if pip.hw_pipette['has_tip']:
        pip.drop_tip()
