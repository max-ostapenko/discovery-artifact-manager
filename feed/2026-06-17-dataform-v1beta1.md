---
date: 2026-06-17
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "devops", "security"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-17  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform's Git settings now support a gitRepositoryLink field, enabling integration with managed connection resources for machine-based authentication.

## Details

The GitRemoteSettings schema now includes a new optional field, gitRepositoryLink. This field accepts a resource name string in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*. This update allows developers to leverage centralized Google Cloud connection resources for Git authentication, moving away from manual credential management within Dataform itself.

**Tags:** `dataform` `git` `devops` `security`
