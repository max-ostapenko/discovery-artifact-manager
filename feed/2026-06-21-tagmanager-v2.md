---
date: 2026-06-21
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "automation"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-21  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the get and link methods within the Destinations resource. Developers using these for container management should prepare for future changes.

## Details

The discovery document for Tag Manager v2 now flags accounts.containers.destinations.get and accounts.containers.destinations.link with a deprecated status. This affects workflows involving the programmatic retrieval or linking of destinations within GTM containers, typically used in server-side tagging configurations.

**Tags:** `deprecation` `tag-manager` `automation`
