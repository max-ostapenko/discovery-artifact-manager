---
date: 2026-06-20
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "authentication"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-20  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking to GitRepositoryLink resources for machine-based Git authentication, simplifying credential management for remote repositories.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field allows developers to specify a resource name (following the format projects/*/locations/*/connections/*/gitRepositoryLinks/*) to handle machine credentials. This integration likely points toward better compatibility with Google Cloud's Developer Connect or similar centralized secret management for Git operations.

**Tags:** `dataform` `git` `security` `authentication`
