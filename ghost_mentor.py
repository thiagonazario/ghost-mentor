import sys


class GhostMentor:
    """
    Ghost-Mentor: An architectural interceptor for DevSecOps environments.
    Designed to reduce developer friction by providing actionable 'Hardened by Design'
    insights during runtime failures.
    """

    def __init__(self):
        # Hardened by Design knowledge base for automated feedback
        self.hardened_tips = {
            "S3": "🛡️ Hardened Tip: Ensure Block Public Access is ENABLED at the account level.",
            "IAM": "🛡️ Hardened Tip: Use Permission Boundaries to limit the scope of IAM roles.",
            "K8S": "🛡️ Hardened Tip: Always use NetworkPolicies to restrict pod-to-pod communication.",
            "DOCKER": "🛡️ Hardened Tip: Run containers as non-root to prevent privilege escalation."
        }

    def intercept_error(self, exc_type, exc_value, exc_traceback):
        """
        Intercepts unhandled exceptions to inject architectural guidance
        before the standard traceback.
        """
        error_msg = str(exc_value)
        print(f"\n❌ [GHOST-ERROR DETECTED]: {error_msg}")

        # Context analysis for 'Hardened by Design' tips
        if "s3" in error_msg.lower():
            print(self.hardened_tips["S3"])
        elif "iam" in error_msg.lower():
            print(self.hardened_tips["IAM"])
        elif "kubernetes" in error_msg.lower() or "k8s" in error_msg.lower():
            print(self.hardened_tips["K8S"])
        elif "docker" in error_msg.lower():
            print(self.hardened_tips["DOCKER"])
        else:
            print("🔍 Ghost-Mentor is analyzing this unknown failure for the next paradigm...")

        # Maintain standard Python exception behavior
        sys.__excepthook__(exc_type, exc_value, exc_traceback)


def boot_mentor():
    """
    Initializes the Ghost-Mentor interceptor in the current environment.
    """
    mentor = GhostMentor()
    sys.excepthook = mentor.intercept_error
    print("🚀 Ghost-Mentor: Active & Hardening your session.")


if __name__ == "__main__":
    boot_mentor()

    # Simulation of a common cloud failure for interception testing
    print("\n--- Testing Ghost-Mentor Interception ---")

    # Example: Simulating an S3 error to trigger the Hardened Tip
    raise Exception("Access Denied on S3 Bucket: ghost-protocol-data")
