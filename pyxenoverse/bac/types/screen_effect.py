from recordclass import recordclass

from pyxenoverse.bac.types import BaseType
from yabac.panels.types import screen_effect_panel

BACScreenEffect = recordclass('BACScreenEffect', [
    'start_time',
    'duration',
    'u_04',
    'character_type',
    'bpe_effect_id',
    'u_0c',
    'u_10',
    'u_14',
    'u_18',
    'u_1c'
])


# Type 16
class ScreenEffect(BaseType):
    type = 16
    bac_record = BACScreenEffect
    byte_order = 'HHHHIIIIII'
    size = 32

    bpe_effect_id_dict = screen_effect_panel.IDs
    def __init__(self, index):
        super().__init__(index)
