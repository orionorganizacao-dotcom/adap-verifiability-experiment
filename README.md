# A-DAP Verifiability Experiment

This is a minimal experiment to demonstrate independent reconstruction of an AI decision.

## Files

- `data/input.json` → original input  
- `logs/verifiable_trace.json` → decision + hashes  
- `scripts/verify_reconstruction.py` → independent verifier  

## How to verify
## Expected result

If everything is correct, the script should output:## Tamper test

Modify any value in `data/input.json` and run again.

The verification will fail.

## What this proves

This demonstrates that the decision can be independently reconstructed and verified without access to the original system.
Run:

```bash
python scripts/verify_reconstruction.py
