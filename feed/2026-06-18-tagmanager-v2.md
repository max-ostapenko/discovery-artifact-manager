---
date: 2026-06-18
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Destination methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager"]
interesting_score: 5
---

# Deprecation of Destination methods

**Date:** 2026-06-18  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has deprecated the 'get' and 'link' methods for the destinations resource within containers.

## Details

The API discovery document now explicitly marks accounts.containers.destinations.get and accounts.containers.destinations.link as deprecated. This signals a shift in how GTM handles destination linking, likely moving toward a different management model for GA4 or server-side tagging configurations.

**Tags:** `deprecation` `tag-manager`
