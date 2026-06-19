---
date: 2026-06-19
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["tag-manager", "deprecation", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-19  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for container destinations. Developers should begin auditing automation scripts that rely on these endpoints.

## Details

The discovery document now flags 'accounts.containers.destinations.get' and 'accounts.containers.destinations.link' as deprecated. This indicates that the current mechanism for retrieving and linking destinations within GTM containers is being phased out, likely in favor of a different resource model or consolidated tagging configuration.

**Tags:** `tag-manager` `deprecation` `api-lifecycle`
