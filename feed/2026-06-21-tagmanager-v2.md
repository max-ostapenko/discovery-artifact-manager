---
date: 2026-06-21
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Destination methods in GTM API"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Destination methods in GTM API

**Date:** 2026-06-21  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has deprecated the get and link methods for the Destinations resource. Developers should audit their integrations to move away from these endpoints.

## Details

The tagmanager.v2 API now explicitly marks accounts.containers.destinations.get and accounts.containers.destinations.link as deprecated. While the methods remain functional for the time being, the deprecation flag signals that these specific destination management workflows are being phased out in favor of newer patterns.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
