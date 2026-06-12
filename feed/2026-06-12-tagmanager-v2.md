---
date: 2026-06-12
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Destination methods in GTM"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Destination methods in GTM

**Date:** 2026-06-12  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for the destinations resource within containers.

## Details

The API discovery document now flags 'accounts.containers.destinations.get' and 'accounts.containers.destinations.link' as deprecated. This signals that the current implementation for managing destinations is being phased out, and developers should look for alternative ways to manage tag destinations in future integrations.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
