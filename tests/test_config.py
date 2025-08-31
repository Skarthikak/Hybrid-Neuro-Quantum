from src.utils.config import load_config

def test_config_load():
    cfg = load_config("configs/mnist_classical.json")
    assert "dataset" in cfg
