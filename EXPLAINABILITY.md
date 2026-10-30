# Candidate Matching Advisor Explainability

## Decision and Reasoning Process

The agent's decision support maps candidate evidence to essential and preferred role criteria. Its reasoning shows the basis for each match, partial match, gap, or unresolved item.

## Inputs and Data Sources Used

Input data consists of the approved role profile, recruiter criteria, and candidate-submitted information. The agent does not use inferred demographic data, social profiles, or undisclosed data sources.

## Outputs and Supporting Evidence

The output is a match matrix with evidence, gaps, questions, and a non-binding summary. Supporting evidence is traceable to the role profile and candidate materials.

## Limits, Constraints, and Known Issues

One limitation is that matching cannot establish future performance or cultural contribution. The agent is constrained from automatically ranking, rejecting, or selecting candidates.

## Uncertainty and Human Review

Uncertainty is shown for missing, inconsistent, or unverifiable claims. Human review is required before shortlisting or any other hiring action.

## Implementation in This Repository

The repository implements a declarative OpenGAP worker through `agent.yaml`, `SOUL.md`, this explainability file, and its `README.md`. The manifest describes the candidate-and-role evidence accepted by the worker and the structured comparison it may return, while the policy files prohibit autonomous hiring decisions.

There is no applicant-tracking integration or trained ranking model in this repository. Execution depends on a compatible host, and every result must retain the cited input evidence, uncertainty, and a human-review requirement.
