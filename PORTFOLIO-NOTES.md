# Engineering review

JobHunt documents a staged ATS ingestion, deterministic filtering, AI screening and drafting pipeline with human review before application. See [README](README.md) and [setup](SETUP.md).

## Review checklist

- Replace personal CVs in public repositories with synthetic examples if they contain private contact details. The current root contains `DHEERAJ_CV.pdf`; review its intended visibility. Removing a file from the current tree does not erase its history.
- Run the existing tests with a clean environment and mocked provider credentials.
- Measure filter recall, screening agreement with human labels, cost per digest and failure recovery before publishing metrics.
- Keep the human approval boundary: no automatic application submission.
