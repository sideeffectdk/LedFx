# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:\\Users\\Shaun\\ledfx-env\\LedFx\\ledfx\\__main__.py'],
             pathex=['C:\\Users\\Shaun\\ledfx-env\\LedFx', 'C:\\Users\\Shaun\\ledfx-env\\LedFx'],
             binaries=[],
             datas=[('C:/Users/shaun/ledfx-env/LedFx/ledfx_frontend', 'ledfx_frontend/'), ('C:/Users/shaun/ledfx-env/LedFx/ledfx', 'ledfx/')],
             hiddenimports=['sacn', 'pyaudio', 'aubio', 'numpy', 'math', 'voluptuous', 'numpy', 'aiohttp', 'aiohttp_jinja2'],
             hookspath=['c:\\users\\shaun\\ledfx-env\\lib\\site-packages\\pyupdater\\hooks'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='win',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='C:\\Users\\shaun\\ledfx-env\\LedFx\\icons\\discord.ico')