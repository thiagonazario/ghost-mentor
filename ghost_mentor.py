import re
import sys

class GhostMentorMVP:
    def __init__(self):
        # Knowledge Base: The core intelligence of the Mentor
        # Hardened by Design patterns for common infrastructure failures
        self.rules = [
            {
                "id": "IAM_ACCESS_DENIED",
                "pattern": r"AccessDenied.*calling the (.*?) operation",
                "message": "🚨 Security Alert: IAM Permission Gap",
                "fix": "Your IAM Role lacks permissions for the '{0}' operation. Update your Terraform/CloudFormation policy.",
                "hardened_tip": "Least Privilege Principle: Avoid 'Resource: *'. Always specify the exact ARN to minimize the attack surface."
            },
            {
                "id": "S3_BUCKET_NOT_FOUND",
                "pattern": r"NoSuchBucket.*bucket (.*)",
                "message": "📍 Infrastructure Alert: Missing Target",
                "fix": "The bucket '{0}' was not found. Verify the naming convention and region configuration in your IaC.",
                "hardened_tip": "Immutability: Use Environment Variables for bucket names to prevent hardcoding between Staging and Production."
            },
            {
                "id": "DOCKER_AUTH_FAIL",
                "pattern": r"denied: requested access to the resource is denied",
                "message": "🔑 Registry Alert: Auth Failure",
                "fix": "Docker authentication failed. Verify your ECR/DockerHub credentials and login lifecycle.",
                "hardened_tip": "Secrets Management: Use AWS Secrets Manager or Parameter Store. Never inject plain-text credentials into your pipeline."
            },
            {
                "id": "K8S_IMAGE_PULL_ERR",
                "pattern": r"ImagePullBackOff|ErrImagePull",
                "message": "☸️ Kubernetes Alert: Container Startup Failure",
                "fix": "The cluster cannot pull your Docker image. Check if the image name/tag is correct and if the 'imagePullSecrets' are configured.",
                "hardened_tip": "Standardization: Always use a specific version tag (e.g., :v1.0.2) instead of ':latest'. This ensures predictable deployments and easier rollbacks."
            },
            {
                "id": "K8S_CRASH_LOOP",
                "pattern": r"CrashLoopBackOff",
                "message": "🔄 Kubernetes Alert: Application Instability",
                "fix": "Your container started but crashed immediately. Check the application logs using 'kubectl logs [pod_name]'.",
                "hardened_tip": "Resilience: Configure 'Liveness' and 'Readiness' probes correctly. A crashing app usually points to missing Environment Variables or DB connection issues."
            }
        ]

    def analyze(self, log_content):
        """
        Scans the log content against Hardened rules to provide actionable insights.
        """
        for rule in self.rules:
            match = re.search(rule["pattern"], log_content, re.IGNORECASE)
            if match:
                # Capture the context (operation name or resource) if available
                context = match.group(1) if match.groups() else "resource"
                return self.format_output(rule, context)
        
        return "⚠️ Ghost Mentor: Unmapped error detected. Review detailed logs or escalate to SRE."

    def format_output(self, rule, context):
        """
        Formats the mentor feedback using the Ghost-Architect signature style.
        """
        return f"""
---
### 👻 {rule['message']}
**Resolution:** {rule['fix'].format(context)}

**🛡️ Hardened by Design Tip:** _{rule['hardened_tip']}_

*Solving Complex Problems with Elegance & Without Drama.*
---
"""

if __name__ == "__main__":
    mentor = GhostMentorMVP()
    
    # Check if data is being piped (|) into the script
    if not sys.stdin.isatty():
        # Read from pipeline input (e.g., stderr redirection)
        error_input = sys.stdin.read()
    elif len(sys.argv) > 1:
        # Read from command line argument
        error_input = sys.argv[1]
    else:
        # Default usage hint
        error_input = "Usage: [command] 2>&1 | python3 ghost_mentor.py"

    # Execution and output to terminal/PR
    print(mentor.analyze(error_input))