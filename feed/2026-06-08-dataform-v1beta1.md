---
date: 2026-06-08
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["Dataform", "Git", "Authentication", "BigQuery"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-08  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform's GitRemoteSettings now supports gitRepositoryLink, allowing developers to use managed Git repository links for machine-based authentication.

## Details

The GitRemoteSettings schema has been updated with an optional gitRepositoryLink field. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, enabling a more streamlined approach to handling Git credentials through Google Cloud's connectivity resources instead of manual secret management.

**Tags:** `Dataform` `Git` `Authentication` `BigQuery`
