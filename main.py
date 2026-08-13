from pathlib import Path
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

import pyxcat

exe_path = None
outpath = Path("output").resolve()
xcat = pyxcat.xcat.XCAT(exe_path)

params = pyxcat.parameters.XCATParameters()
params.image_params.out_frames = 1

post_process_ops = {
    "to_nifti": True
}
os.chdir(exe_path.parent)
xcat.generate(params, outpath, "default", post_processing_options=post_process_ops)