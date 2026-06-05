---
date: 2026-06-05
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: low
breaking: false
tags: ["dataform", "git", "authentication", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-05  
**API:** `dataform.v1beta1`  
**Impact:** Low  

## Summary

Dataform's Git remote settings now support a gitRepositoryLink field, allowing developers to reference centralized connection resources for machine-based authentication.

## Details

The GitRemoteSettings schema has been updated with a new optional string field: gitRepositoryLink. This field expects a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*. This addition enables Dataform to leverage standardized GCP connection resources for Git operations, likely simplifying credential management for automated workflows and machine-to-machine interactions.

**Tags:** `dataform` `git` `authentication` `devops`
