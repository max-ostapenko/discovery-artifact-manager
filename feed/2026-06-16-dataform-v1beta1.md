---
date: 2026-06-16
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "iam"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-16  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform's GitRemoteSettings now supports gitRepositoryLink, allowing developers to use managed Git repository connections for machine-based authentication.

## Details

The GitRemoteSettings schema has been updated with a new optional gitRepositoryLink field. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, enabling more robust integration with GCP's managed connection services for Git-based workflows instead of relying solely on manual credential handling.

**Tags:** `dataform` `git` `security` `iam`
