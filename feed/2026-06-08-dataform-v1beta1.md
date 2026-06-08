---
date: 2026-06-08
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "iam", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-08  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking to managed GitRepositoryLink resources for authentication, simplifying how machine credentials are handled for remote repositories.

## Details

The GitRemoteSettings schema includes a new optional gitRepositoryLink field. This allows developers to specify a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, facilitating integration with Google Cloud's managed connection services for Git operations and credential management.

**Tags:** `dataform` `git` `iam` `devops`
