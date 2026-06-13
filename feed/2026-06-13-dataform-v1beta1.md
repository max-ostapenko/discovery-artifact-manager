---
date: 2026-06-13
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: low
breaking: false
tags: ["dataform", "git", "security"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-13  
**API:** `dataform.v1beta1`  
**Impact:** Low  

## Summary

Dataform's Git settings now support gitRepositoryLink, allowing developers to link machine credentials via standard GCP connection resources.

## Details

The GitRemoteSettings schema now includes an optional gitRepositoryLink field. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, enabling more streamlined integration with managed Git connections for automated workflows and machine-based authentication.

**Tags:** `dataform` `git` `security`
