import os, sys, argparse
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from sum import add
from difference import sub
from product import mul
from divide import div, idiv, mod
from power import powi

def run_cli():
    p = argparse.ArgumentParser()
    p.add_argument("op", choices=["add","sub","mul","div","idiv","mod","pow"])
    p.add_argument("x", type=float)
    p.add_argument("y", type=float)
    a = p.parse_args()
    ops = {
        "add": lambda x,y: add(x,y),
        "sub": lambda x,y: sub(x,y),
        "mul": lambda x,y: mul(x,y),
        "div": lambda x,y: div(x,y),
        "idiv": lambda x,y: idiv(x,y),
        "mod": lambda x,y: mod(x,y),
        "pow": lambda x,y: powi(x,y),
    }
    print(ops[a.op](a.x, a.y))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_cli()
    else:
        x, y = 7, 5
        print("sum:", add(x, y))
        print("difference:", sub(x, y))
        print("product:", mul(x, y))
