---
date: 2026-06-11
api: tagmanager.v2
service: Google Tag Manager
title: "Deprecation of Destination methods in Tag Manager"
impact: medium
breaking: false
tags: ["tagmanager", "deprecation", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Destination methods in Tag Manager

**Date:** 2026-06-11  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for the Destinations resource within containers.

## Details

The API discovery document now flags 'accounts.containers.destinations.get' and 'accounts.containers.destinations.link' as deprecated. While these methods currently remain functional, this change signals that developers should begin migrating away from these specific endpoints for managing container destinations to avoid future service disruptions.

**Tags:** `tagmanager` `deprecation` `api-lifecycle`
