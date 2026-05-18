---
date: 2026-05-18
api: libraryagent.v1
service: Library Agent
title: "Library Agent API Discovery Document Removed"
impact: high
breaking: true
tags: ["deprecation", "removal", "example-api"]
interesting_score: 8
---

# Library Agent API Discovery Document Removed

**Date:** 2026-05-18  
**API:** `libraryagent.v1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

The discovery document for the Library Agent API (v1) has been completely removed, effectively ending its public availability via the Discovery Service.

## Details

This update reflects a total removal of the Library Agent API's discovery surface. All resources (such as `shelves`), methods, OAuth scopes, and global parameters (like `access_token`, `fields`, and `key`) have been deleted from the document. As this was primarily a Google Example API used for documentation and testing, this likely signals its formal retirement.

**Tags:** `deprecation` `removal` `example-api`
