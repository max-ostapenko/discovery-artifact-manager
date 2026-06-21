---
date: 2026-06-21
api: tagmanager.v2
service: Google Tag Manager
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

Google Tag Manager has deprecated the get and link methods for the Destinations resource, signaling a shift in how container destinations are managed.

## Details

The API discovery document now explicitly marks accounts.containers.destinations.get and accounts.containers.destinations.link as deprecated. While these methods remain functional for the time being, developers should audit their integrations—particularly those involving server-side tagging or GA4 destination linking—to prepare for future removal or replacement of these endpoints.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
