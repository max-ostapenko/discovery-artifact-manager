---
date: 2026-06-10
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Destination methods in GTM API"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Destination methods in GTM API

**Date:** 2026-06-10  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the get and link methods for the destinations resource. Developers should audit their integrations to move away from these endpoints.

## Details

The API discovery document now flags accounts.containers.destinations.get and accounts.containers.destinations.link as deprecated. While these methods remain functional for now, their deprecation signals that they are no longer the recommended path for managing container destinations and may be removed in a future update.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
