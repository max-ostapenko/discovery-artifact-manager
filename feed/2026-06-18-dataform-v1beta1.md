---
date: 2026-06-18
api: dataform.v1beta1
service: Dataform
title: "Machine credentials via GitRepositoryLink"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "credentials"]
interesting_score: 5
---

# Machine credentials via GitRepositoryLink

**Date:** 2026-06-18  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports gitRepositoryLink in Git remote settings, allowing for more structured machine credential management.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*. This allows developers to link Dataform workspaces to specific Git repository connection resources for machine-based authentication, likely integrating with Google Cloud's Developer Connect or similar connection services.

**Tags:** `dataform` `git` `security` `credentials`
