---
date: 2026-06-09
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: low
breaking: false
tags: ["dataform", "git", "authentication", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-09  
**API:** `dataform.v1beta1`  
**Impact:** Low  

## Summary

Dataform's GitRemoteSettings now includes a gitRepositoryLink field, enabling integration with managed Git repository connections for machine authentication.

## Details

The addition of the optional gitRepositoryLink field to the GitRemoteSettings schema allows developers to reference a specific Git repository resource using the format projects/*/locations/*/connections/*/gitRepositoryLinks/*. This update facilitates the use of machine-managed credentials, likely integrating with GCP's Developer Connect or similar connection services to streamline Git authentication for automated SQL workflows.

**Tags:** `dataform` `git` `authentication` `devops`
