---
date: 2026-06-06
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "authentication", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-06  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports gitRepositoryLink in Git remote settings, allowing developers to use managed repository links for machine authentication.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*. This change enables more streamlined integration with GCP's managed Git connections, potentially reducing the overhead of manual credential handling for automated workflows and machine-to-machine interactions.

**Tags:** `dataform` `git` `authentication` `devops`
