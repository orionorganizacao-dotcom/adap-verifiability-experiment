# Experimento de Verificabilidade A-DAP

Este é um experimento mínimo para demonstrar a verificação independente da integridade de uma decisão sem acesso ao sistema original.

---

## Arquivos

- `data/input.json` → entrada original  
- `logs/verifiable_trace.json` → decisão + hashes  
- `scripts/verify_reconstruction.py` → verificador independente  

---

## Como verificar

Execute:

```bash
python scripts/verify_reconstruction.py
