---
date: 2026-06-20
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Container Destination methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Container Destination methods

**Date:** 2026-06-20  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for the destinations resource within containers.

## Details

The methods `accounts.containers.destinations.get` and `accounts.containers.destinations.link` have been marked as deprecated in the discovery document. This indicates that the underlying functionality for managing destinations via these specific endpoints is being phased out, likely in favor of newer tagging or GA4-integrated configuration workflows.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
