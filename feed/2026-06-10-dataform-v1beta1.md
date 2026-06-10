---
date: 2026-06-10
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-10  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform's GitRemoteSettings now supports gitRepositoryLink, enabling standardized machine-to-machine authentication via Google Cloud connections.

## Details

The GitRemoteSettings schema has been updated to include a new optional field: gitRepositoryLink. This field allows developers to specify a resource name following the pattern projects/*/locations/*/connections/*/gitRepositoryLinks/*, facilitating the use of Developer Connect for managing Git credentials rather than relying solely on manual secret management.

**Tags:** `dataform` `git` `security` `devops`
