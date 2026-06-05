---
date: 2026-06-05
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: low
breaking: false
tags: ["dataform", "git", "iam", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-05  
**API:** `dataform.v1beta1`  
**Impact:** Low  

## Summary

Dataform's GitRemoteSettings now supports a gitRepositoryLink field, allowing developers to use centralized connection resources for machine-based Git authentication.

## Details

The GitRemoteSettings schema has been updated with an optional gitRepositoryLink string field. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, enabling integration with Google Cloud's connection management service (Developer Connect) for handling Git credentials instead of manual configuration.

**Tags:** `dataform` `git` `iam` `devops`
