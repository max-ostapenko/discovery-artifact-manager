---
date: 2026-06-14
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for managed credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "devops", "security"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for managed credentials

**Date:** 2026-06-14  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports referencing GitRepositoryLink resources for machine credentials, improving how Git remote settings handle authentication.

## Details

The GitRemoteSettings schema has been updated to include an optional gitRepositoryLink field. This field allows developers to reference a managed connection resource (using the format projects/*/locations/*/connections/*/gitRepositoryLinks/*) for machine credentials. This change facilitates more secure and centralized Git authentication by leveraging Google Cloud's managed connection services rather than manual credential configuration.

**Tags:** `dataform` `git` `devops` `security`
