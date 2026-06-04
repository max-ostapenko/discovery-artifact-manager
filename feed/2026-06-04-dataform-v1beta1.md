---
date: 2026-06-04
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "iam"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-04  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking GitRepositoryLink resources for machine credentials in Git remote settings.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field allows developers to specify a resource name (following the projects/*/locations/*/connections/*/gitRepositoryLinks/* pattern) to handle machine credentials for Git operations, providing a more integrated way to manage repository access within the GCP ecosystem.

**Tags:** `dataform` `git` `security` `iam`
