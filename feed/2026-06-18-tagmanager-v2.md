---
date: 2026-06-18
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Destination methods in Tag Manager"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Destination methods in Tag Manager

**Date:** 2026-06-18  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially marked the 'get' and 'link' methods for the Destinations resource as deprecated.

## Details

The discovery document now flags accounts.containers.destinations.get and accounts.containers.destinations.link with a deprecated status. Developers currently relying on these methods for managing container destinations should look for alternative integration paths, as these endpoints are no longer recommended for new implementations.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
