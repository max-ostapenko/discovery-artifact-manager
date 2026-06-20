---
date: 2026-06-20
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Destination methods in Tag Manager API"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Destination methods in Tag Manager API

**Date:** 2026-06-20  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for the destinations resource within containers.

## Details

The discovery document for Tag Manager v2 now flags 'accounts.containers.destinations.get' and 'accounts.containers.destinations.link' as deprecated. While these methods remain functional for now, their deprecation signals that developers should begin auditing their integrations and look for alternative ways to manage container destinations as these endpoints may be removed in a future update.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
