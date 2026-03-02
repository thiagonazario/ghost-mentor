# 👻 Ghost-Mentor: AI-Driven DevSecOps Interceptor

![Ghost-Mentor Banner](ghost-mentor.png)

**Ghost-Mentor** is a lightweight Python-based engine designed to bridge the gap between complex infrastructure failures and developer productivity. By intercepting pipeline errors in real-time, it provides actionable, **"Hardened by Design"** guidance directly in the terminal or CI/CD logs.

> "Solving Complex Problems with Elegance & Without Drama."

---

## 🚀 Key Features

* **Real-time Interception**: Acts as a pipe interceptor for AWS, Docker, and Kubernetes logs.
* **Actionable Mentorship**: Instead of cryptic logs, developers receive clear resolution steps.
* **Hardened by Design**: Every suggestion reinforces industry best practices (Least Privilege, Immutability, and Secrets Management).
* **Zero Dependencies**: Pure Python implementation, ready for any CI/CD environment (Jenkins, GitHub Actions, GitLab CI).

## 🛠️ Supported Patterns

| Domain | Error Pattern | Mentor Guidance |
| :--- | :--- | :--- |
| **AWS IAM** | `AccessDenied` | Permission Gap Analysis & Policy Snippets |
| **AWS S3** | `NoSuchBucket` | Region & Naming Convention Validation |
| **Docker** | `Auth Failures` | Registry Lifecycle & Secrets Management |
| **Kubernetes** | `ImagePullBackOff` | Tag Standardization & PullSecrets Check |
| **Kubernetes** | `CrashLoopBackOff` | Stability Analysis & Probe Configuration |

---

## 📦 How it Works (The Feedback Loop)

```mermaid
sequenceDiagram
    participant D as Developer
    participant P as CI/CD Pipeline
    participant AWS as AWS/K8s Log
    box rgb(40, 44, 52) Ghost-Architect Engine
    participant GM as Ghost-Mentor
    end
    participant Terminal as Developer Terminal

    D->>P: git push (Start Deployment)
    P->>AWS: Execute aws/kubectl command
    alt Error Occurs
        AWS-->>GM: pipe stderr (AccessDenied/ImagePull)
        activate GM
        GM->>GM: Analyze Pattern via Regex
        GM->>GM: Inject "Hardened by Design" Tip
        GM-->>Terminal: Format & Output Actionable Fix 🛡️
        deactivate GM
        Terminal-->>D: Clear Guidance (No Googling)
        D->>D: Quick Fix & Learning
    else Success
        AWS-->>P: Continue Deployment 🚀
    end
```
## 💻 Quick Start
1. Integration via Pipe
Integrate Ghost-Mentor into your existing workflows by redirecting stderr (2>&1) to the script:

```bash
# Example with AWS CLI
aws s3 cp my_file.txt s3://protected-bucket/ 2>&1 | python3 ghost_mentor.py

# Example with Kubernetes Logs
kubectl logs pod/my-app 2>&1 | python3 ghost_mentor.py
```

## 🛡️ Sovereignty & Philosophy
This tool is part of the Ghost-Architect ecosystem, focused on creating self-healing infrastructure and reducing cognitive load for high-intensity engineering teams.