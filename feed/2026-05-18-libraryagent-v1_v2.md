---
date: 2026-05-18
api: libraryagent.v1
service: Library Agent API
title: "Library Agent v1 discovery surface effectively removed"
impact: high
breaking: true
tags: ["decommissioned", "breaking-change"]
interesting_score: 8
---

# Library Agent v1 discovery surface effectively removed

**Date:** 2026-05-18  
**API:** `libraryagent.v1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

The discovery document for the Library Agent v1 API has been stripped of nearly all content, including resources, methods, and global parameters.

## Details

In a massive cleanup, 169 elements were removed from the discovery document. This includes the entire 'shelves' resource and its associated methods (like shelves.get), all OAuth2 scopes, and standard global parameters such as 'access_token', 'fields', and 'key'. This effectively renders the API unreachable via discovery-based client libraries.

**Tags:** `decommissioned` `breaking-change`
