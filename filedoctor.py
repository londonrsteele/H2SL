import sys
import os
# Below function is from Stack Overflow: 
# https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/13790741#13790741
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

assets_dir = resource_path("assets")
browser_mw_path = resource_path("browser_mw.py")
EOMdashapp_path = resource_path("EOM_dashapp.py")
CARdashapp_path = resource_path("CAR_dashapp.py")
dashapp_path = resource_path("dashapp.py")