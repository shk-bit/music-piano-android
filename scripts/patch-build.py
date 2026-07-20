#!/usr/bin/env python3
"""Patch Capacitor-generated build.gradle to add release signing config."""
import os, re

build_file = os.path.join(os.environ.get("GITHUB_WORKSPACE", "."), "android", "app", "build.gradle")

with open(build_file, "r") as f:
    content = f.read()

signing_block = """
    signingConfigs {
        release {
            storeFile file('release.keystore')
            storePassword System.getenv("STORE_PASSWORD") ?: ""
            keyAlias System.getenv("KEY_ALIAS") ?: ""
            keyPassword System.getenv("KEY_PASSWORD") ?: ""
        }
    }
"""

# Insert signingConfigs block before buildTypes
if "signingConfigs" not in content:
    content = content.replace(
        "    buildTypes {",
        signing_block + "\n    buildTypes {",
        1
    )

# Add signingConfig to release buildType
if "signingConfig signingConfigs.release" not in content:
    content = content.replace(
        "minifyEnabled false",
        "minifyEnabled false\n            signingConfig signingConfigs.release"
    )

with open(build_file, "w") as f:
    f.write(content)

print("build.gradle patched successfully for release signing")
