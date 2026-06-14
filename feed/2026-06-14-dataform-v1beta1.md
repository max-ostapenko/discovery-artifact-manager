---
date: 2026-06-14
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "authentication"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-14  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking GitRepositoryLink resources for machine-based authentication to remote repositories.

## Details

The GitRemoteSettings schema now includes an optional gitRepositoryLink field. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, enabling developers to leverage managed connection resources for Git authentication instead of manual credential handling.

**Tags:** `dataform` `git` `security` `authentication`
