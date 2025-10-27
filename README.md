# waterio

Read/write NumPy arrays to/from a compressed checkpoint (.npz).

## Install
```bash
python3 -m pip install --no-build-isolation -v .
from waterio import save_checkpoint, load_checkpoint
import numpy as np

save_checkpoint("ckpt.npz", a=np.arange(5), b=np.ones((2,3)))
data = load_checkpoint("ckpt.npz")
print(data["a"], data["b"].shape)

