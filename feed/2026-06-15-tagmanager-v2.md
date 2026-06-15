---
date: 2026-06-15
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-15  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the get and link methods for container destinations, signaling a shift in how external destinations are managed.

## Details

The API discovery document now flags accounts.containers.destinations.get and accounts.containers.destinations.link as deprecated. While these methods currently remain functional, developers should audit their integrations and prepare for a future where destination management is likely handled through alternative resources or consolidated tagging workflows.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
