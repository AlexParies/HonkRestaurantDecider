# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['/Users/ap1048141/Desktop/HonkRestaurantDecider/main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['_tkinter', 'Tkinter', 'enchant', 'twisted'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='touchtracer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(exe, Tree('/Users/ap1048141/Desktop/HonkRestaurantDecider/'),
              a.binaries,
              a.zipfiles,
              a.datas,
              strip=None,
              upx=True,
              name='touchtracer')
)
app = BUNDLE(
    coll,
    name='touchtracer.app',
    icon=None,
    bundle_identifier=None,
)
