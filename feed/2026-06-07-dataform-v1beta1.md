---
date: 2026-06-07
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "authentication"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-07  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking GitRepositoryLink resources for machine credentials in Git remote settings.

## Details

The GitRemoteSettings schema has been updated to include a new optional field, gitRepositoryLink. This field allows developers to specify a resource name (following the format projects/*/locations/*/connections/*/gitRepositoryLinks/*) to handle machine credentials for Git operations, likely integrating with Google Cloud's Developer Connect or similar managed connection services.

**Tags:** `dataform` `git` `security` `authentication`
