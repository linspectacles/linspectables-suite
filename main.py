#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Linspectacles - Linux Inspection Suite
# Copyright (C) 2026 brunonlinespace
# GPL-3.0-or-later

import json
import sys
from pathlib import Path

PROGRAM_ROOT = Path(__file__).resolve().parent


def component_info():
    path = PROGRAM_ROOT / "suite-pythoine-extension.json"
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    if "--component-info" in sys.argv:
        print(json.dumps(component_info(), ensure_ascii=False))
        return 0
    if "--suite-pythoine" in sys.argv:
        sys.argv.remove("--suite-pythoine")
    from linspectacles.host import run
    return run(PROGRAM_ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
