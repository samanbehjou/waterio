# examples/checkpoint_demo.py
from solsysgen import Sun, Planet, SolarSystem
from solsysgen.utils.checkpoint import save_checkpoint, load_checkpoint

ss = SolarSystem(
    Sun(),
    [
        Planet("Earth", 5.972e24, 1.496e11, 6.371e6),
        Planet("Mars", 6.39e23, 2.279e11, 3.3895e6),
    ],
)

data = {"summary": ss.summary()}
save_checkpoint("checkpoints/solsysgen_demo.npz", data)
loaded = load_checkpoint("checkpoints/solsysgen_demo.npz")
print(loaded["summary"])

