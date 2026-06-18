---
date: 2026-06-18
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "iam", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-18  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking to GitRepositoryLink resources for machine-based authentication in GitRemoteSettings.

## Details

The GitRemoteSettings schema has been updated with an optional gitRepositoryLink string field. This field allows developers to reference a specific connection resource (using the format projects/*/locations/*/connections/*/gitRepositoryLinks/*) for handling machine credentials, likely integrating with Google Cloud's Developer Connect for more secure and centralized Git authentication management.

**Tags:** `dataform` `git` `iam` `devops`
