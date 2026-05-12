# Linden Pain Clinic — Layer 1 Compliance Wall Demo

A runnable demonstration of the four-primitive architecture for deploying an LLM against regulated data without exposing identities. Used as the worked example in the Cognitive Shift post *Past the Compliance Wall*.

## What this is

A fictional European chronic pain clinic. The clinic wants AI assistance for patient triage, follow-up scheduling, and clinical note review. It cannot ship raw PHI to an LLM. This demo shows the architectural pattern that lets useful AI work happen anyway.

The pattern is recently named the **Reasoner-Executor-Synthesizer** ([RES](https://arxiv.org/abs/2603.22367)) pattern in the agent literature. It builds on the older **synthetic data sandbox** tradition used in privacy-preserving ML research.

## The four primitives

| Primitive | Job | Defends against |
|---|---|---|
| **Scrubber** | Microsoft Presidio + deterministic HMAC tokenizer. Pseudonymises every identifier before content enters the team brain. | LLM provider seeing raw PII |
| **Vault** | SQLite + libsodium-encrypted token-to-value mapping. Every read audit-logged with stated purpose. Refuses to construct without an audit logger. | Brain leaks (laptop, repo, screenshot) |
| **Executor** | Operation whitelist + token resolver. Applies LLM-produced plans that reference only pseudonym tokens. | Prompt-injection exfil |
| **Audit log** | Hash-chained JSONL. Tamper-evident. `verify-audit` detects exact tampered line. | Silent audit-log edits |

## Quick start

```bash
cd _infra
uv sync                                  # installs Python 3.12 + deps
uv run python -m spacy download en_core_web_lg   # Presidio's NER model

# Generate synthetic patients (Java required; ~5 min)
# Download Synthea from https://github.com/synthetichealth/synthea/releases
# Place synthea-with-dependencies.jar in _infra/synthea-raw/synthea.jar
java -jar synthea-raw/synthea.jar -p 100 -s 2026 Massachusetts

# Scrub the patients with pain conditions
uv run scrub

# Apply a sample plan against a local SQLite "prod" target
uv run apply-plan executor/examples/sample-plan-001.yaml

# Verify the audit chain
uv run verify-audit
```

## Sample patient files

`team-brain/patients/` contains three pseudonymised example notes so you can see the output without running the full pipeline. Note that tokens in those files were generated with a specific HMAC key; running the pipeline locally produces a different but functionally equivalent set of tokens.

## Sample plans

`_infra/executor/examples/` contains:

- `sample-plan-001.yaml` — a hand-written plan covering 3 patients, 5 operations
- `sample-plan-002-step4.yaml` — a follow-up plan
- `llm-generated-plan.yaml` — a plan produced by an actual Claude Code session reading only the pseudonymised brain
- `adversarial-1-unknown-op.yaml` — uses an op outside the whitelist; executor refuses atomically
- `adversarial-2-fake-token.yaml` — references tokens that don't exist in the vault

## Prod targets

The executor supports both backends:

- **SQLite** (default, local file) for development
- **PostgreSQL** for production-style deployments. Tested against Railway's EU-West region (Amsterdam) with a `connection.env` file containing `PROD_DB_URL=postgresql://...`

## Honest limits

This is Layer 1. Real production rollouts need additional hardening:

- **k-anonymity / quasi-identifier suppression**: pseudonymised content can still re-identify ("63 y/o male with rare condition X in postcode Y"). Tools: ARX, pycanon, OpenDP for differential privacy.
- **Fine-tuned NER for free-text PHI**: Presidio doesn't catch contextual leaks ("the patient I saw at the bakery"). Custom recognisers or fine-tuned medical NER models close this gap.
- **Vault behind a process boundary**: a developer with shell access can read the SQLite file directly. Move the vault behind a UNIX socket / gRPC, or swap to a managed KMS.
- **Vault metadata leakage**: counts by kind can themselves leak coarse information about a cohort.

See the post's "What this is and isn't" section for the three-rung remediation ladder mapped to each.

## License

MIT.
