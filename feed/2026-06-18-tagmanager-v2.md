---
date: 2026-06-18
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Destination methods in Tag Manager"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager"]
interesting_score: 5
---

# Deprecation of Destination methods in Tag Manager

**Date:** 2026-06-18  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has officially marked the 'get' and 'link' methods for the Destinations resource as deprecated.

## Details

The API discovery document now flags accounts.containers.destinations.get and accounts.containers.destinations.link as deprecated. While these methods remain functional for now, this is a clear signal to developers to begin auditing their integrations and prepare for a future removal or replacement of these specific destination management endpoints.

**Tags:** `deprecation` `tag-manager`
