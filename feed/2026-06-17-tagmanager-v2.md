---
date: 2026-06-17
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Destination methods in Tag Manager"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Destination methods in Tag Manager

**Date:** 2026-06-17  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has deprecated the get and link methods for the destinations resource within containers.

## Details

The API surface for managing container destinations is being narrowed. Specifically, the methods accounts.containers.destinations.get and accounts.containers.destinations.link have been officially marked as deprecated. Developers using these methods for GA4 or server-side tagging automation should begin looking for alternative workflows or prepare for these endpoints to be phased out in future revisions.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
