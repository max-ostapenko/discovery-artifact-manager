---
date: 2026-05-17
api: libraryagent.v1
service: Library Agent
title: "Library Agent API v1 has been decommissioned"
impact: high
breaking: true
tags: ["decommissioned", "breaking-change", "example-api"]
interesting_score: 9
---

# Library Agent API v1 has been decommissioned

**Date:** 2026-05-17  
**API:** `libraryagent.v1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

The Library Agent API, a sample service for Google Cloud, has had its entire resource and parameter definition removed from the discovery document.

## Details

The discovery document for libraryagent.v1 has been effectively emptied. All core resources, including the 'shelves' resource and its methods (e.g., shelves.get), have been removed. Additionally, all global parameters, authentication scopes, and metadata like mtlsRootUrl and discoveryVersion are gone. This represents a total removal of the API surface.

**Tags:** `decommissioned` `breaking-change` `example-api`
