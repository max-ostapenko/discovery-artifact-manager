---
date: 2026-06-14
api: tagmanager.v2
service: Tag Manager
title: "Deprecation of Destination methods in Tag Manager"
impact: medium
breaking: false
tags: ["deprecation", "tag-manager", "api-lifecycle"]
interesting_score: 5
---

# Deprecation of Destination methods in Tag Manager

**Date:** 2026-06-14  
**API:** `tagmanager.v2`  
**Impact:** Medium  

## Summary

Google Tag Manager has deprecated the get and link methods for the Destinations resource, signaling a shift in how container destinations are managed.

## Details

The discovery document now explicitly marks accounts.containers.destinations.get and accounts.containers.destinations.link as deprecated. While these methods remain functional for the time being, developers should audit their implementations and prepare for these endpoints to be phased out in favor of newer tagging configurations.

**Tags:** `deprecation` `tag-manager` `api-lifecycle`
