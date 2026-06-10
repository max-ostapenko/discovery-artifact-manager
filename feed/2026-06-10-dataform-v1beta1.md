---
date: 2026-06-10
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "authentication", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-10  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking GitRepositoryLink resources directly to Git remote settings, streamlining machine credential management.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, allowing developers to leverage managed Git connections for authentication instead of manual credential handling. This is particularly useful for machine-to-machine workflows where traditional secret management might be cumbersome.

**Tags:** `dataform` `git` `authentication` `devops`
