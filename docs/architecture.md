# Architecture

## Overview

The Source Control & Modernized Delivery Automation Platform provides a Git-driven automation architecture that integrates source control, workflow execution, Kubernetes orchestration, dynamic runner provisioning, and infrastructure monitoring.

The platform was designed to support both traditional self-hosted workflow execution and Kubernetes-native dynamic execution models while providing a foundation for future GitOps adoption.

---

## Architectural Principles

### Source-Control-Driven Operations

Repository events act as the operational trigger for platform automation.

```text
Source Control
        ↓
Workflow Execution
        ↓
Platform Automation
```

### Separation of Responsibilities

Platform components maintain distinct operational responsibilities.

```text
Source Control
        ↓
Execution
        ↓
Monitoring
        ↓
Visualization
```

### Dynamic Resource Utilization

Workloads should consume resources only when required.

```text
Workflow Request
        ↓
Runner Creation
        ↓
Execution
        ↓
Runner Removal
```

### Monitoring Independence

Monitoring operations should remain independent of automation inventories and secret management systems.

---

# Platform Architecture

```text
Developer
        │
        ▼

Git Push

        │
        ▼

GitHub Repository

        │
        ▼

GitHub Actions

        │
        ▼

GitHub App

        │
        ▼

Actions Runner Controller (ARC)

        │
        ▼

Runner Deployment

        │
        ▼

Dynamic GitHub Runner

        │
        ▼

Kubernetes Worker Node

        │
        ▼

Workflow Execution
```

---

# Static Runner Architecture

## Purpose

Provide persistent workflow execution using a self-hosted GitHub Actions runner.

## Architecture

```text
GitHub

        │
        ▼

Self-Hosted Runner

        │
        ▼

Management Host

        │
        ▼

Workflow Execution
```

## Administrative Workflow Path

```text
GitHub Actions

        │
        ▼

Self-Hosted Runner

        │
        ▼

SSH

        │
        ▼

Kubernetes Control Plane

        │
        ▼

Cluster Administration
```

## Characteristics

- Persistent execution environment
- Always available
- Simplified troubleshooting
- Administrative workflow support
- Remote Kubernetes administration

---

# Dynamic Runner Architecture

## Purpose

Provide Kubernetes-native workflow execution through dynamically provisioned GitHub Actions runners.

## Architecture

```text
GitHub

        │
        ▼

GitHub App

        │
        ▼

ARC Controller

        │
        ▼

Runner Deployment

        │
        ▼

Dynamic Runner

        │
        ▼

Workflow Execution
```

## Characteristics

- Ephemeral execution
- Automated provisioning
- Automated registration
- Kubernetes-native operation
- Resource-efficient execution
- Automated cleanup

---

# GitHub Identity Architecture

## Purpose

Provide secure authentication and authorization between GitHub and Kubernetes-hosted automation services.

## Components

```text
GitHub App
        ↓
Application Identity

Private Key
        ↓
Authentication

Repository Permissions
        ↓
Authorization

Installation
        ↓
Repository Access
```

## Capabilities

- Secure authentication
- Repository authorization
- Token-based access
- Application-level identity

---

# Certificate Management Architecture

## Purpose

Provide certificate lifecycle management required for controller-based services.

## Components

```text
Certificate Manager

        │
        ├── Certificate Issuance

        ├── Certificate Renewal

        └── Trust Management
```

## Supported Services

- Controller certificates
- Internal trust relationships
- Service validation

---

# Kubernetes Runner Architecture

## Components

```text
GitHub Actions

        │
        ▼

ARC Controller

        │
        ▼

Runner Deployment

        │
        ▼

Runner Pod

        │
        ▼

Kubernetes Worker
```

## Workflow

```text
Workflow Request
        ↓
Runner Creation
        ↓
Runner Registration
        ↓
Job Assignment
        ↓
Execution
        ↓
Cleanup
```

---

# Management Network Architecture

## Purpose

Provide a dedicated infrastructure management and operations network.

## Architecture

```text
Management Network

        │
        ├── Platform Operations

        ├── Automation

        ├── Monitoring

        └── Administration
```

## Benefits

- Centralized management
- Operational consistency
- Monitoring connectivity
- Administrative access

---

# Monitoring Architecture

## Design Goal

Provide monitoring independent of automation inventories and secret management systems.

## Architecture

```text
Monitoring Configuration

        │
        ▼

GitHub Actions

        │
        ▼

ARC Dynamic Runner

        │
        ▼

Validation Workflows

        │
        ▼

Results

        │
        ▼

Future Grafana Dashboards
```

## Monitoring Domains

### Infrastructure Health

- Infrastructure reachability
- Platform availability
- Service validation

### Certificate Monitoring

- Certificate discovery
- Certificate visibility
- Expiration tracking

### Runner Monitoring

- Runner availability
- Job execution visibility
- Capacity monitoring

---

# Configuration Architecture

## Automation

```text
Automation Inventory
        ↓
Infrastructure Automation
```

## Monitoring

```text
Monitoring Configuration
        ↓
Infrastructure Monitoring
```

## Benefit

Monitoring and automation remain independently managed while supporting a shared platform architecture.

---

# Future Architecture

## Observability Layer

```text
GitHub Actions
        ↓
ARC
        ↓
Monitoring
        ↓
Grafana
```

### Planned Dashboards

- Infrastructure Health
- Certificate Health
- Runner Health
- Security Action Center
- Unified Operations Dashboard

---

# GitOps Architecture (Planned)

```text
Git Push
        ↓

GitHub Actions
(Build & Validation)

        ↓

Manifest Updates

        ↓

Git Repository

        ↓

ArgoCD

        ↓

Kubernetes Deployment
```

## Objective

Establish Git as the source of truth for application and platform delivery workflows.

---

# Architectural Outcomes

✅ Source-Control-Driven Operations

✅ Static Runner Execution

✅ Dynamic Runner Execution

✅ GitHub Identity Integration

✅ ARC Integration

✅ Kubernetes Integration

✅ Certificate Management

✅ Monitoring Foundation

✅ Infrastructure Validation Framework

✅ GitOps Foundation
