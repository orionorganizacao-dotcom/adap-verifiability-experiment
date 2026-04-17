# A-DAP Verifiability Experiment

This is a minimal experiment to demonstrate independent reconstruction of an AI decision.

## Files

- `data/input.json` → original input  
- `logs/verifiable_trace.json` → decision + hashes  
- `scripts/verify_reconstruction.py` → independent verifier  

## How to verify

Run:

```bash
python scripts/verify_reconstruction.py
