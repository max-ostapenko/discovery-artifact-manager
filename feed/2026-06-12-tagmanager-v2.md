---
date: 2026-06-12
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["tag-manager", "deprecation", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-12  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for the destinations resource within containers.

## Details

The discovery document now flags 'accounts.containers.destinations.get' and 'accounts.containers.destinations.link' with a deprecated status. Developers currently using these methods to manage or retrieve destination links (often used in GA4 or server-side tagging setups) should begin looking for alternative workflows as these methods are no longer recommended and may be removed in future versions.

**Tags:** `tag-manager` `deprecation` `api-lifecycle`
