---
date: 2026-05-17
api: libraryagent.v1
service: Library Agent
title: "Library Agent API discovery document effectively removed"
impact: high
breaking: true
tags: ["decommission", "breaking-change"]
interesting_score: 8
---

# Library Agent API discovery document effectively removed

**Date:** 2026-05-17  
**API:** `libraryagent.v1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

The discovery document for the Library Agent v1 API has been gutted, removing all resources, methods, and global parameters.

## Details

The discovery surface for libraryagent.v1 has been almost entirely deleted. This includes the removal of the 'shelves' resource and its methods (e.g., shelves.get), all standard Google API query parameters (such as fields, alt, key, and prettyPrint), and the OAuth2 scope definitions. While this was primarily an example/mock API, any automated tools or client library generators relying on this discovery document will now fail.

**Tags:** `decommission` `breaking-change`
