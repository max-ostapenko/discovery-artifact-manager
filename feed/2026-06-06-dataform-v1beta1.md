---
date: 2026-06-06
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "automation"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-06  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports `gitRepositoryLink` in Git remote settings, enabling the use of managed resource links for machine-based authentication.

## Details

The `GitRemoteSettings` schema has been updated with a new optional field: `gitRepositoryLink`. This field accepts a resource name in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`. This addition allows Dataform to leverage centralized repository connections for machine credentials, simplifying authentication for automated data pipelines and reducing the need for manual secret management within Git settings.

**Tags:** `dataform` `git` `security` `automation`
