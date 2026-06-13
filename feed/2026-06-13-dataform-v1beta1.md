---
date: 2026-06-13
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "devops", "security"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-13  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking managed GitRepositoryLink resources for machine-based authentication in Git remote settings.

## Details

The GitRemoteSettings schema has been updated to include an optional gitRepositoryLink field. This allows developers to reference a managed Git repository link resource (formatted as projects/*/locations/*/connections/*/gitRepositoryLinks/*) to handle machine credentials, simplifying the authentication process for automated Git operations within Dataform.

**Tags:** `dataform` `git` `devops` `security`
