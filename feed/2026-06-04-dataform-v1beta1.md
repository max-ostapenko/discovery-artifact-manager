---
date: 2026-06-04
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: low
breaking: false
tags: ["dataform", "git", "authentication", "security"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-04  
**API:** `dataform.v1beta1`  
**Impact:** Low  

## Summary

Dataform now supports gitRepositoryLink within GitRemoteSettings, allowing developers to use managed resource names for Git authentication.

## Details

The GitRemoteSettings schema has been updated with a new optional field: gitRepositoryLink. This field accepts a resource path in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, which points to a specific Git repository link used for machine-based authentication. This integration likely streamlines how Dataform interacts with managed Git connections in the GCP ecosystem.

**Tags:** `dataform` `git` `authentication` `security`
