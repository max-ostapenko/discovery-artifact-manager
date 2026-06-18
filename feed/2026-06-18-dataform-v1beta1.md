---
date: 2026-06-18
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "authentication", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-18  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports `gitRepositoryLink` in Git remote settings, allowing developers to use centralized repository connections for machine-based authentication.

## Details

The `GitRemoteSettings` schema has been updated with a new optional field: `gitRepositoryLink`. This field accepts a resource name in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`. This change enables more robust machine credential management by leveraging existing repository links instead of relying solely on manual Git configuration within the Dataform environment.

**Tags:** `dataform` `git` `authentication` `devops`
