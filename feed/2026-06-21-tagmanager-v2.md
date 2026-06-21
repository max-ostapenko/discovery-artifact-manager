---
date: 2026-06-21
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Destination methods in GTM API"
impact: medium
breaking: false
tags: ["tag-manager", "deprecation", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Destination methods in GTM API

**Date:** 2026-06-21  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for the destinations resource within containers.

## Details

The API discovery document now flags 'accounts.containers.destinations.get' and 'accounts.containers.destinations.link' as deprecated. This indicates that the current mechanism for retrieving and linking destinations (often used in GA4 or server-side tagging setups) is being phased out in favor of newer workflows.

**Tags:** `tag-manager` `deprecation` `api-lifecycle`
