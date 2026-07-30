---
date: 2026-07-30
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI: Task Stores, ASR Config, and HTTP Proxying"
impact: medium
breaking: false
tags: ["AI", "Vertex AI", "Agents", "Generative AI", "Reasoning Engine"]
interesting_score: 7
---

# Vertex AI: Task Stores, ASR Config, and HTTP Proxying

**Date:** 2026-07-30  
**API:** `aiplatform.v1beta1`  
**Impact:** Medium  

## Summary

Vertex AI introduces Task Stores for agent task management, adds native ASR configuration to GenAI generation, and provides a new HTTP proxy method for model responses.

## Details

Reasoning Engine tasks (a2aTasks) now support a new parent resource, TaskStore, allowing tasks to be managed at `projects/{project}/locations/{location}/taskStores/{task_store}/a2aTasks/{a2a_task}`. The GenaiVertexV1beta1GenerationConfig schema now includes a transcriptionConfig field, enabling developers to toggle Automatic Speech Recognition (ASR) directly within the generation configuration. 

Additionally, a new publishers.v1.responses.compact method has been added to forward arbitrary HTTP requests to deployed models, supporting both streaming and non-streaming use cases. Other updates include a new 'QUEUED' status for interactions, a 'view' parameter for a2aTasks.get to filter between basic headers and full materialized state, and an exrColorSpaceOverride for video generation experiments.

**Tags:** `AI` `Vertex AI` `Agents` `Generative AI` `Reasoning Engine`
