from recordclass import recordclass

from pyxenoverse.bac.types import BaseType

BACEffect = recordclass('BACEffect', [
    'start_time',
    'duration',
    'u_04',
    'character_type',
    'eepk_type',
    'bone_link',
    'skill_id',
    'use_skill_id',
    'effect_id',
    'u_14',
    'u_18',
    'u_1c',
    'u_20',
    'u_24',
    'u_28',
    'on_off_switch'
])


# Type 8
class Effect(BaseType):
    type = 8
    bac_record = BACEffect
    byte_order = 'HHHHHHHHIffffffI'
    size = 48
    dependencies = {
        ('skill_id', 'use_skill_id'): {0x0: 'Yes'}
    }

    eepk_type_dict = {0x0 : "Global",
                      0x1 : "Stage BG",
                      0x2 : "Player",
                      0x3 : "Awoken",
                      0x5 : "Super",
                      0x6 : "Ultimate",
                      0x7 : "Evasive",
                      0x8 : "Unknown (0x8)",
                      0x9 : "Ki blast",
                      0xa : "Unknown (0xa)",
                      0xb : "Stage (0xb)"}



    def __init__(self, index):
        super().__init__(index)
