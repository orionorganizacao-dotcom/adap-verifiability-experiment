# Experimento de Verificabilidade A-DAP

Este é um experimento mínimo para demonstrar a verificação independente da integridade de uma decisão sem acesso ao sistema original que a gerou.

A proposta não é reexecutar a decisão, mas verificar se ela pode ser validada de forma independente, a partir de um rastro (trace) previamente registrado.

Em outras palavras:

- O sistema que decide não participa da verificação
- A decisão é tratada como um artefato já fechado
- A verificação valida consistência, não recalcula lógica

---

## Princípio

Uma decisão só é auditável se puder ser verificada fora do sistema que a produziu.

Este experimento testa exatamente isso:

> Um terceiro, sem acesso ao código original, consegue validar a integridade da decisão?

---

## O que é verificado

O verificador não reexecuta a lógica de decisão.

Ele valida:

- Se o input utilizado corresponde ao hash registrado
- Se a decisão registrada corresponde ao hash do resultado
- Se o trace não foi alterado após a geração

Ou seja:

A verificação garante que o artefato da decisão é íntegro e consistente com os dados originais, sem depender do sistema que a produziu.

---

## Arquivos

- `data/input.json`
- `logs/verifiable_trace.json`
- `scripts/verify_reconstruction.py`

---

## Como verificar

Execute:

```bash
python scripts/verify_reconstruction.py
