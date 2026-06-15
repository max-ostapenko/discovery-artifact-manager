---
date: 2026-06-15
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "auth", "security"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-15  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform's GitRemoteSettings now supports a gitRepositoryLink field, allowing developers to use managed machine credentials for Git operations.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*. This integration enables more robust authentication for Git remotes by leveraging centralized repository links rather than manual credential handling, aligning Dataform with the standard GCP developer connection patterns.

**Tags:** `dataform` `git` `auth` `security`
