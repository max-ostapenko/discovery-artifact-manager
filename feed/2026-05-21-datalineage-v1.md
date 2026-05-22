---
date: 2026-05-21
api: datalineage.v1
service: Data Lineage
title: "Granular OAuth scopes for Lineage Streaming"
impact: low
breaking: false
tags: ["security", "iam", "datalineage"]
interesting_score: 4
---

# Granular OAuth scopes for Lineage Streaming

**Date:** 2026-05-21  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

The Data Lineage API now supports more granular OAuth scopes for the searchLineageStreaming method, enabling better least-privilege access control.

## Details

The searchLineageStreaming method in the projects.locations resource has been updated to explicitly include the datalineage.read-write and datalineage.readonly OAuth scopes. This allows developers to configure applications with specific permissions for lineage data rather than relying on broader, more permissive scopes like cloud-platform.

**Tags:** `security` `iam` `datalineage`
