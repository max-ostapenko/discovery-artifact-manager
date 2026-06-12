---
date: 2026-06-12
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "authentication", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-12  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking to managed Git repository connections for machine-based authentication via a new gitRepositoryLink field.

## Details

The GitRemoteSettings schema has been updated to include an optional gitRepositoryLink string field. This field allows developers to specify a resource name (formatted as projects/*/locations/*/connections/*/gitRepositoryLinks/*) to handle machine credentials, likely integrating with Google Cloud's broader connection management infrastructure for more secure and centralized Git authentication.

**Tags:** `dataform` `git` `authentication` `devops`
