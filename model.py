"""
Compatibility module for the backend import.

The project currently stores the model implementation in `model (1).py`,
which cannot be imported as a standard Python module name. This shim loads
that file and exposes FoodCostPredictor under the expected `model` module.
"""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


_MODEL_PATH = Path(__file__).with_name("model (1).py")
_SPEC = spec_from_file_location("food_model_impl", _MODEL_PATH)
if _SPEC is None or _SPEC.loader is None:
    raise ImportError(f"Could not load model implementation from {_MODEL_PATH}")

_MODULE = module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)

FoodCostPredictor = _MODULE.FoodCostPredictor

