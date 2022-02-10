# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

workspace = 'YOUR WORK SPACE'

a = Analysis(['카카오톡 예약전송.py'],
             pathex=[workspace],
             binaries=[],
             datas=[('img/*', 'img'), ('ui/*', 'ui'), ('icon/paper-plane.png', 'icon')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='카카오톡 예약전송',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='icon/paper_plane.ico',
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
