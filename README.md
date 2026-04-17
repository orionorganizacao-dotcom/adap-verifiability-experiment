# A-DAP Verifiability Experiment

This is a minimal experiment to demonstrate **independent verification of decision integrity** without access to the original system.

---

## Files

- `data/input.json` → original input  
- `logs/verifiable_trace.json` → decision + hashes  
- `scripts/verify_reconstruction.py` → independent verifier  

---

## How to verify
## Resultado esperado

Se tudo estiver correto, o script deve retornar:
Run:
## Teste de adulteração

Modifique qualquer valor em `data/input.json` e execute novamente.

A verificação irá falhar.
```bash
python scripts/verify_reconstruction.py
