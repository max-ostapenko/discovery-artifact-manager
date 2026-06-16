---
date: 2026-06-16
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Destination methods in Tag Manager"
impact: medium
breaking: false
tags: ["tag-manager", "deprecation", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Destination methods in Tag Manager

**Date:** 2026-06-16  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for the destinations resource within containers.

## Details

The API surface for managing destinations is being phased out. Specifically, the methods accounts.containers.destinations.get and accounts.containers.destinations.link have been marked as deprecated. Developers currently relying on these methods to retrieve or link destinations to containers should begin looking for alternative workflows as these may be removed in a future update.

**Tags:** `tag-manager` `deprecation` `api-lifecycle`
