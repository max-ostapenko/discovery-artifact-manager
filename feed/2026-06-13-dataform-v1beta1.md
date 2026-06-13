---
date: 2026-06-13
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "authentication"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-13  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking GitRepositoryLink resources for machine credentials in Git remote settings, improving how repositories are authenticated.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, allowing developers to leverage managed connections for Git authentication instead of manual credential handling. This is particularly useful for CI/CD pipelines and machine-to-machine interactions.

**Tags:** `dataform` `git` `security` `authentication`
