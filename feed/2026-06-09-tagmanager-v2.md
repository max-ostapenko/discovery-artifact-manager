---
date: 2026-06-09
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Destination methods in Tag Manager"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Destination methods in Tag Manager

**Date:** 2026-06-09  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially deprecated the 'get' and 'link' methods for the destinations resource within containers.

## Details

The API discovery document now explicitly marks accounts.containers.destinations.get and accounts.containers.destinations.link as deprecated. While these methods currently remain functional, this change signals that they are slated for future removal. Developers using these endpoints to manage or retrieve destination links should begin auditing their integrations and look for alternative management patterns.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
