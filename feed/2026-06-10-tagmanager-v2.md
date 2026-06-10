---
date: 2026-06-10
api: tagmanager.v2
service: Google Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["tag-manager", "deprecation", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-10  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the get and link methods for container destinations. Developers should begin planning migrations away from these endpoints.

## Details

The tagmanager.v2 API has marked the accounts.containers.destinations.get and accounts.containers.destinations.link methods as deprecated. While these methods are still currently functional, the deprecation flag indicates they are no longer recommended for use and may be removed in a future revision of the API.

**Tags:** `tag-manager` `deprecation` `api-lifecycle`
