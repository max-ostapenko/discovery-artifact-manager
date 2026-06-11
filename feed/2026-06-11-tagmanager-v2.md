---
date: 2026-06-11
api: tagmanager.v2
service: Tag Manager
title: "Tag Manager deprecates Destination get and link methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "api-lifecycle"]
interesting_score: 5
---

# Tag Manager deprecates Destination get and link methods

**Date:** 2026-06-11  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

The Tag Manager API has officially deprecated the 'get' and 'link' methods for container destinations, signaling a shift in how these resources are managed.

## Details

Within the accounts.containers.destinations resource, both the get and link methods have been marked with deprecated: true. This change suggests that developers currently relying on these endpoints for managing tagging destinations should begin auditing their code and looking for updated patterns in the Tag Manager documentation, as these methods are likely slated for eventual removal.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
