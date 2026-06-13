---
date: 2026-06-13
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Destinations get and link methods"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Destinations get and link methods

**Date:** 2026-06-13  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the get and link methods within the destinations resource.

## Details

The methods accounts.containers.destinations.get and accounts.containers.destinations.link have been marked as deprecated in the discovery document. While they are still available for use, this is a clear signal that developers should begin migrating away from these specific endpoints in favor of newer container configuration workflows.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
