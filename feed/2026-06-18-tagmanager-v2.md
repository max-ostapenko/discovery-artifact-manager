---
date: 2026-06-18
api: tagmanager.v2
service: Google Tag Manager
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

Google Tag Manager has officially deprecated the get and link methods for the destinations resource within containers.

## Details

The discovery document now explicitly flags accounts.containers.destinations.get and accounts.containers.destinations.link as deprecated. While these methods remain functional for the time being, developers using these endpoints to manage container destinations should begin auditing their integrations and look for alternative management workflows as these may be removed in a future revision.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
