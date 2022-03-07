# coding=utf-8
import argparse
import datetime as dt
import logging
import numpy as np
import os
import sys
from typing import Any, Dict, Tuple, Optional

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from section2_1 import calc_E_T


def main():
    # コマンドライン引数の処理
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename",
        type=str,
        help="設備条件JSONファイル"
    )
    args = parser.parse_args()

    import json
    with open(args.filename, 'r') as fin:
        d = json.load(fin)
        E_T, E_H, E_C, E_V, E_L, E_W, E_S, E_M, UPL, E_gen, E_E_gen, E_E_PV_h_d_t, E_E, E_G, E_K = calc_E_T(d)
        result = {
            "E_T": E_T,
            "E_H": E_H,
            "E_C": E_C,
            "E_V": E_V,
            "E_L": E_L,
            "E_W": E_W,
            "E_S": E_S,
            "E_M": E_M,
            "UPL": str(UPL),
            "E_gen": E_gen,
            "E_E_gen": E_E_gen,
            "E_E": str(E_E),
            "E_G": str(E_G),
            "E_K": str(E_K),
        }
        print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
