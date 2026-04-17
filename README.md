# A-DAP Verifiability Experiment

## From Documentation to Verifiability

This repository implements a controlled experiment to test a simple but critical claim:

> An automated decision is only auditable if it can be independently reconstructed outside the system that produced it.

---

## Problem

Most AI systems are considered "auditable" based on:
- internal logs
- internal explanations
- internal documentation

But this raises a fundamental question:

Can a third party reconstruct the decision independently?

---

## Hypothesis

Traditional logs appear sufficient internally, but fail under independent reconstruction.

A structured, verifiable decision trace enables consistent and independent reconstruction.

---

## Experimental Design

Two conditions:

**A — Traditional Logging**
- Standard logs
- Internal context dependent

**B — Verifiable Trace (A-DAP-inspired)**
- Pre-commit structure
- Hash-linked trace
- Independent reconstruction possible

---

## Metrics

- Reconstruction time
- Dependency on original operator
- Ambiguity level
- Consistency across evaluators

---

## Minimal Flow

commit_pre → execution → result → hash_chain → verify

---

## Why This Matters

If auditability depends on internal context, it is not auditability.

It is documentation.

---

## Status

Experimental — open to validation and collaboration.

---

## Author

Ezio v.s. Santos  
AI Governance & Verifiability
