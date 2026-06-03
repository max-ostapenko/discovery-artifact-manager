---
date: 2026-06-03
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-03  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking to Git repositories using managed connection resources, simplifying machine credential management.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, allowing developers to leverage centralized Google Cloud connection resources for machine-based Git authentication instead of manual secret handling.

**Tags:** `dataform` `git` `security` `devops`
