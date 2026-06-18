---
date: 2026-06-18
api: dataform.v1beta1
service: Dataform
title: "New GitRepositoryLink support for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "auth", "cicd"]
interesting_score: 5
---

# New GitRepositoryLink support for machine credentials

**Date:** 2026-06-18  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking GitRepositoryLink resources for machine-based authentication in Git remote settings.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, enabling developers to use managed connections for machine credentials instead of manual configuration. This is particularly useful for setting up secure, automated workflows without managing raw Git tokens directly within Dataform.

**Tags:** `dataform` `git` `auth` `cicd`
