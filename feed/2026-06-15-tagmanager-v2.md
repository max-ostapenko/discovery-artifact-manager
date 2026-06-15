---
date: 2026-06-15
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["tag-manager", "deprecation", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-15  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for container destinations. Developers using these methods for automated tagging setups should prepare for future removal.

## Details

The API discovery document now marks 'accounts.containers.destinations.get' and 'accounts.containers.destinations.link' with a deprecated flag. This indicates that the current approach for retrieving and linking destinations within a GTM container is being phased out, likely in favor of newer tagging or configuration workflows.

**Tags:** `tag-manager` `deprecation` `api-lifecycle`
