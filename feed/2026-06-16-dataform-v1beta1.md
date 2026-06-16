---
date: 2026-06-16
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "authentication", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-16  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform's GitRemoteSettings now supports a gitRepositoryLink field for referencing structured Git connection resources.

## Details

The GitRemoteSettings schema has been updated to include an optional gitRepositoryLink string field. This field allows developers to provide a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, enabling more robust machine-based authentication for Git operations by leveraging Google Cloud's connection management infrastructure.

**Tags:** `dataform` `git` `authentication` `devops`
