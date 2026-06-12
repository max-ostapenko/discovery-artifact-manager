---
date: 2026-06-12
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "authentication"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-12  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform's Git settings now support a gitRepositoryLink field, allowing developers to use centralized machine credentials via Google Cloud connections.

## Details

The GitRemoteSettings schema now includes an optional gitRepositoryLink string field. This field points to a resource in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, enabling more robust integration with managed Git connections for authentication instead of manual token management.

**Tags:** `dataform` `git` `security` `authentication`
