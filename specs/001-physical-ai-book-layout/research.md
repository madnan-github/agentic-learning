---
title: Research Findings for Physical AI & Humanoid Robotics Book
description: Documenting ongoing research, key technical decisions, trusted sources, and constraints for the book.
slug: /specs/physical-ai-book-layout/research
---

# Research Findings: Physical AI & Humanoid Robotics Book

This document serves as a living repository for research findings, technical investigations, and key decisions made during the development of the "Physical AI & Humanoid Robotics" book. It aligns with the "Research-Concurrent Strategy" outlined in the implementation plan.

## 1. Key Primary and Trusted Sources

-   **ROS 2**: Official ROS 2 documentation, ROS Industrial, OSRF resources.
-   **NVIDIA Isaac**: NVIDIA developer documentation, Isaac Sim/ROS/Nav2 official guides, Jetson documentation.
-   **Gazebo**: Gazebo official documentation, Open Robotics resources.
-   **Unity**: Unity documentation for Robotics, simulation packages.
-   **Docusaurus**: Official Docusaurus documentation.
-   **Python**: Official Python documentation, PEPs.

## 2. Technical Decisions and Rationale

### 2.1. ROS 2 Distribution Choice

-   **Decision**: Use ROS 2 Humble Hawksbill as the primary distribution.
-   **Rationale**: Humble is an LTS (Long Term Support) release, offering stability and a longer support window, which is crucial for a book with code examples that need to remain functional over time. It also has broad community support and good compatibility with other tools like NVIDIA Isaac.

### 2.2. Python Version

-   **Decision**: Target Python 3.8+.
-   **Rationale**: This provides a balance between modern Python features and compatibility with existing robotics frameworks. Many ROS 2 packages are developed with Python 3.8 or newer.

### 2.3. Docusaurus Version

-   **Decision**: Use Docusaurus v3.
-   **Rationale**: Docusaurus v3 offers the latest features, performance improvements, and ongoing support, ensuring the book's platform remains modern.

## 3. Constraints and Assumptions

-   **Markdown-only content**: All book content will be written in Markdown.
-   **SEO-friendly**: Content will be optimized for search engines.
-   **Original Content**: All content must be original or properly attributed to avoid copyright issues.
-   **AI-assisted writing with human review**: AI will assist in content generation, but human review is mandatory for accuracy and quality.
-   **Runnable Code Examples**: All code examples will be tested for correctness and executability.

## 4. Ongoing Research Areas

-   Specific versions of NVIDIA Isaac components (Isaac Sim, Isaac ROS, Nav2) and their compatibility with ROS 2 Humble.
-   Best practices for integrating Unity with ROS 2 for robot visualization.
-   Detailed setup procedures for Jetson Orin devices for AI deployment.
-   Effective methods for sim-to-real transfer in humanoid robotics.
