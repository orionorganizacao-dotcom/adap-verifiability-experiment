# Experimento de Verificabilidade A-DAP

Este é um experimento mínimo para demonstrar a verificação independente da integridade de uma decisão **sem acesso ao sistema original que a gerou**.

A proposta não é reexecutar a decisão, mas verificar se ela pode ser **validada de forma independente**, a partir de um rastro (trace) previamente registrado.

Em outras palavras:

- O sistema que decide não participa da verificação
- A decisão é tratada como um artefato já fechado
- A verificação valida consistência, não recalcula lógica---

## Princípio

Uma decisão só é auditável se puder ser verificada fora do sistema que a produziu.

Este experimento testa exatamente isso:

> Um terceiro, sem acesso ao código original, consegue validar a integridade da decisão?

- `data/input.json` → entrada original utilizada
- `logs/verifiable_trace.json` → decisão registrada + hashes de integridade
- `scripts/verify_reconstruction.py` → verificador independente (não executa a lógica original)

Execute:

```bash
python scripts/verify_reconstruction.py
