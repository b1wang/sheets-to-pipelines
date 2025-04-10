# ADR 0001: Database Selection (PostgreSQL vs NoSQL)

**Date:** 2025-03-14  
**Status:** Accepted  

## Context
Need a database to transition away from spreadsheet-based workflows into structured data management. Key considerations include:

- Structured data format
- Complex querying capability
- Data integrity
- Scalability considerations for medium-term growth
- Machine learning model development and analytics

## Decision
Selected **PostgreSQL** (SQL) over NoSQL alternatives.

## Rationale
- The data currently comes from structured spreadsheet sources, making a relational schema a natural fit.
- PostgreSQL supports complex SQL queries and ensures data integrity (ACID compliance).
- The current dataset size and growth rate do not yet require the horizontal scaling capabilities provided by NoSQL solutions.

## Consequences
- **Positive:** Structured data integrity, easier complex querying, robust ecosystem and tooling.
- **Negative:** Potential future scalability challenges, limited flexibility with schema evolution.
- **Mitigation:** Future reevaluation to determine if a hybrid approach (SQL + NoSQL) becomes necessary as data grows or diversifies.