---
date: 2026-06-14
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-14  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports gitRepositoryLink within GitRemoteSettings, allowing developers to use managed repository links for machine authentication.

## Details

The GitRemoteSettings schema has been updated with a new optional gitRepositoryLink field. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, enabling more robust integration with Google Cloud's managed Git connection services for handling repository credentials instead of manual secret management.

**Tags:** `dataform` `git` `security` `devops`
