# verify_env.py
import json, torch
try:
    import bitsandbytes as bnb
    bnb_ver = bnb.__version__
except Exception as e:
    bnb_ver = f"ERROR: {e}"
info = {
  "torch_version": torch.__version__,
  "cuda_available": torch.cuda.is_available(),
  "cuda_device_count": torch.cuda.device_count(),
  "bitsandbytes": bnb_ver
}
print(json.dumps(info))
