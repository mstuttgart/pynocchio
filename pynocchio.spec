# -*- mode: python -*-

block_cipher = None

a = Analysis(['pynocchio_comic_reader/main.py'],
             pathex=['/home/michell/Documents/Projects/pynocchio-comic-reader/pynocchio_comic_reader'],
             binaries=None,
             datas=[('pynocchio_comic_reader/locale/pynocchio_*.qm', '/usr/share/pynocchio-comic-reader/locale')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pynocchio-comic-reader',
          debug=False,
          strip=False,
          upx=True,
          console=True )

