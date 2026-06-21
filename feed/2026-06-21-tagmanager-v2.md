---
date: 2026-06-21
api: tagmanager.v2
service: Tag Manager
title: "Tag Manager Deprecates Destination Methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "containers"]
interesting_score: 5
---

# Tag Manager Deprecates Destination Methods

**Date:** 2026-06-21  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the get and link methods for the destinations resource within containers.

## Details

The API discovery document now explicitly flags `accounts.containers.destinations.get` and `accounts.containers.destinations.link` as deprecated. While these methods remain functional for now, this change signals a future removal or a shift in how GTM handles destination configurations. Developers using these methods for automated container management or auditing should begin looking for alternative workflows.

**Tags:** `deprecation` `tag-manager` `containers`
