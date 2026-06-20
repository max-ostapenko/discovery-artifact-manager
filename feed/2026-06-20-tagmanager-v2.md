---
date: 2026-06-20
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Destination methods in GTM API"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Destination methods in GTM API

**Date:** 2026-06-20  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for the destinations resource within containers.

## Details

The discovery document now flags 'accounts.containers.destinations.get' and 'accounts.containers.destinations.link' with a deprecated status. This signals that programmatic management of destination links via these specific endpoints is being phased out, likely in favor of newer Google Tag management workflows.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
