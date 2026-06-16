---
date: 2026-06-16
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "iam", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-16  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports `gitRepositoryLink` in Git remote settings, enabling structured machine-based authentication via GCP connection resources.

## Details

The `GitRemoteSettings` object has been updated with a new `gitRepositoryLink` field. This field accepts a resource path in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`, allowing developers to link Dataform to specific Git repository connection resources for machine-to-machine authentication rather than relying solely on manual credential configuration.

**Tags:** `dataform` `git` `iam` `devops`
