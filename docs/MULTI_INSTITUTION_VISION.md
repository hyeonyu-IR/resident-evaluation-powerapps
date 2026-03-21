# Multi-Institution Vision for a Resident Evaluation App

This document is a strategic interpretation of how a resident-evaluation app could be deployed across multiple institutions, including scenarios in which a professional society, specialty committee, or workgroup wants to encourage broader adoption.

It is not a strict technical specification. It is meant to provide a practical vision, a shared vocabulary, and a realistic set of recommendations for people imagining this kind of workflow across institutions.

## Purpose

The main question is not whether an app can be built. That is the easy part.

The harder and more important question is:

How should the app, user management, and evaluation data be deployed across institutions in a way that is secure, realistic, and sustainable?

For educational evaluation workflows, especially in graduate medical education, the app itself can be shared broadly, but the underlying data usually should not be centralized casually.

## Core Interpretation

For this type of app, the most realistic operating model is usually:

- one shared app design
- many institution-owned deployments

That means:

- the app concept can be common
- the evaluation framework can be common
- the user experience can be common
- but the confidential institutional data should usually remain local

This is especially important when the data includes:

- resident names
- faculty names
- role mappings
- comments and evaluations
- institutional performance records

## Why a Central National Database Is Usually the Wrong Default

A central database managed by a national society or committee may sound efficient at first, but it creates immediate governance problems.

Common concerns include:

- confidentiality of resident and faculty evaluation data
- institutional ownership of educational records
- local legal and compliance review
- data retention requirements
- permission management across institutions
- support burden if a central body becomes the system owner

Unless the central organization is prepared to operate like a true software and data platform, with clear legal, security, privacy, and operational responsibilities, central data hosting is usually not the right starting model.

## Recommended Default Model

The recommended default model is:

- central sharing of the app framework and documentation
- local hosting of institutional data

In practical terms, that means:

- a shared application pattern or codebase can be distributed
- each institution manages its own resident, faculty, and evaluation data
- each institution controls its own backend
- each institution determines its own local governance and support model

This approach keeps the shared work reusable while avoiding unnecessary centralization of confidential data.

## Three Realistic Architecture Models

### 1. Institution-Local Deployment

This is the most conservative and most realistic model.

In this model:

- the app is distributed centrally
- each institution deploys its own backend
- each institution stores its own user lists and evaluation records
- each institution manages authentication and permissions locally

Advantages:

- strongest institutional control
- lowest central governance burden
- easier to align with local privacy expectations
- easiest model to justify for confidential educational workflows

Challenges:

- each institution needs some technical setup capacity
- local implementations may diverge over time
- documentation must be strong enough to support semi-independent deployment

This is the closest analogue to the current Power Apps plus SharePoint model.

### 2. Centrally Managed Multi-Tenant Platform

In this model:

- one central platform exists
- each institution gets its own logically isolated tenant or environment
- the central organization manages infrastructure and application updates

Advantages:

- more standardized user experience
- easier centralized updates
- less local engineering burden if the central platform team is strong

Challenges:

- much higher governance burden
- central organization becomes more like a software vendor
- legal, privacy, support, and security responsibilities expand dramatically
- institutions may hesitate to place evaluation data into a centrally controlled system

This model is possible, but it should be treated as a major product and governance commitment, not a casual committee project.

### 3. Hybrid Local Data with Optional Aggregate Reporting

This is often the most strategically attractive long-term model.

In this model:

- institutions keep identifiable evaluation data locally
- optional aggregate, de-identified, or summary metrics may be shared centrally
- the central organization receives only what institutions explicitly agree to share

Advantages:

- preserves local control of sensitive data
- still enables cross-institution insight at a national level
- creates a path toward benchmarking without forcing central custody of raw evaluations

Challenges:

- requires careful definition of what is truly de-identified
- requires clear participation rules
- aggregate standards must be stable and interpretable

This model is often a better strategic target than full centralization.

## What a Society or Committee Could Realistically Provide

A central body such as SIR could contribute a great deal without becoming the holder of all institutional data.

Useful central contributions could include:

- a reference app design
- recommended data model
- backend schema guidance
- implementation guides
- security and governance recommendations
- sample deployment architectures
- reference resident and faculty import templates
- optional reporting standards
- optional de-identified export format for benchmarking

In other words, the central body can provide the blueprint, standards, and shared tooling, while institutions remain the owners of their own operational data.

## Predicted Adoption Workflow Across Institutions

A realistic cross-institution workflow would likely look like this:

1. A central group publishes the app framework and implementation guidance.
2. An interested institution evaluates the documentation and deployment model.
3. The institution provisions its own backend environment.
4. The institution imports local resident and faculty lists.
5. Local leadership tests permissions, reporting, and workflow behavior.
6. The app is adopted locally.
7. Optional aggregate reporting may later be shared outward if governance allows it.

That model is much more realistic than assuming that every institution would directly connect to one central national database.

## Recommendations

### Recommendation 1

Treat the app as a shared framework, not a shared database.

This keeps the design portable while preserving institutional control over confidential data.

### Recommendation 2

Keep the first deployment model simple.

The first successful multi-institution model should emphasize:

- local backend ownership
- clear setup documentation
- stable data fields
- role-based local governance

It is better to have a modest but adoptable model than an ambitious central platform that institutions are reluctant to trust.

### Recommendation 3

Standardize the data model before trying to standardize the infrastructure.

The most useful common ground across institutions is often:

- field definitions
- evaluation categories
- user-role structure
- report structure
- export format

If those are stable, institutions can implement the workflow in different technical stacks without losing conceptual alignment.

### Recommendation 4

Do not centralize identifiable evaluation data unless there is a deliberate governance framework.

If a central body ever wants to hold identifiable data, that should happen only after:

- clear legal review
- security review
- privacy policy
- support model
- long-term maintenance plan

Without those pieces, central data custody creates more risk than value.

### Recommendation 5

If national benchmarking is a long-term goal, start with local-first deployments and optional aggregate reporting.

That path is much more realistic and much easier for institutions to accept.

## Suggestions for Future Planning

If a central group wants to explore this seriously, the next practical planning questions should be:

1. What data must remain institution-local?
2. What data, if any, could be shared centrally in de-identified form?
3. What minimum common data model should all institutions use?
4. Who is expected to support local deployments?
5. Is the central organization trying to distribute a toolkit, or operate a true platform?

Those questions should be answered before large-scale technical development decisions are made.

## Final Recommendation

For a resident-evaluation app used across multiple institutions, the safest and most realistic vision is:

- a shared app concept
- a shared implementation model
- institution-local backends
- institution-local confidential data
- optional future aggregate reporting if governance supports it

That model is practical, scalable, and much easier to defend than immediate centralization.

It also aligns well with how institutions usually want to handle confidential educational workflows: local control first, broader collaboration second.
