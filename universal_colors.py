from collections import OrderedDict

'''
アクセントカラー
'''
accent_colors = OrderedDict((
    ('red', (255, 49, 0)),
    ('yellow', (250, 245, 0)),
    ('green', (53, 161, 107)),
    ('blue', (0, 65, 255)),
    ('sky', (102, 204, 255)),
    ('pink', (255, 153, 160)),
    ('purple', (154, 0, 121)),
    ('brown', (102, 51, 0)),
))

'''
ベースカラー
'''
base_colors = OrderedDict((
    ('light pink', (255, 209, 209)),
    ('cream', (255, 255, 153)),
    ('light yellow-green', (203, 242, 102)),
    ('light sky', (180, 235, 250)),
    ('beige', (237, 197, 143)),
    ('light green', (135, 231, 176)),
    ('light purple', (199, 178, 222)),
))

'''
無彩色
'''
achromatic_colors = OrderedDict((
    ('white', (255, 255, 255)),
    ('light gray', (200, 200, 200)),
    ('gray', (127, 135, 143)),
    ('black', (0, 0, 0)),
))

'''
全色入り
'''
colors = OrderedDict()
colors.update(accent_colors)
colors.update(base_colors)
colors.update(achromatic_colors)