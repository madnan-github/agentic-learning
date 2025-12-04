---
title: Content Guidelines
description: Guidelines for writing Markdown content for the Physical AI & Humanoid Robotics book.
slug: /architecture/content-guidelines
---

# Markdown Content Guidelines

This document outlines the guidelines for creating Markdown content for the "Physical AI & Humanoid Robotics" book. Adhering to these guidelines ensures consistency, readability, and maintainability across all chapters and lessons.

## 1. Front Matter

Every Markdown file **must** begin with front matter, enclosed by `---` at the top and bottom. The following fields are mandatory:

-   `title`: The title of the chapter/lesson. This will appear as the page title.
-   `description`: A brief summary of the content (1-2 sentences). Used for SEO and page previews.
-   `slug`: The unique URL path for the document (e.g., `/module1/chapter1/lesson1`).
-   `sidebar_label`: (Optional) A concise label for the sidebar navigation. If not provided, `title` is used.

**Example Front Matter:**

```markdown
---
title: ROS 2 Core Concepts
description: An introduction to the fundamental concepts of ROS 2, including nodes, topics, services, and actions.
slug: /module1/chapter1/ros2-core-concepts
sidebar_label: ROS 2 Basics
---
```

## 2. Headings

Use semantic headings to structure your content:

-   `#` for the main title (should match the `title` in front matter).
-   `##` for major sections.
-   `###` for subsections.
-   Do not skip heading levels (e.g., jump from `#` to `###`).

## 3. Code Blocks

-   Use fenced code blocks with language identifiers for syntax highlighting (e.g., ````python`, ````cpp`, ````bash`).
-   Ensure code examples are runnable and follow the project's coding standards.
-   Reference code files in `code_examples/` where applicable.

## 4. Internal and External Links

-   **Internal Links**: Use relative paths for links within the Docusaurus site. Example: `[ROS 2 Basics](/docs/module1/chapter1/ros2-basics)`.
-   **External Links**: Use full URLs. All external technical claims **must** be cited in APA style, with a corresponding entry in `docs/references.md` (to be created).

## 5. Images and Media

-   Store images in the `static/` directory or within module-specific subdirectories (e.g., `static/img/module1/`).
-   Use Markdown image syntax: `![Alt text](/img/path/to/image.png)`.
-   Provide descriptive alt text for accessibility and SEO.

## 6. Content Style

-   **Clarity and Conciseness**: Write clearly and avoid jargon where possible. Explain technical terms.
-   **Technical Accuracy**: All technical information **must** be accurate and verifiable. Reference trusted sources.
-   **Instructional Tone**: Maintain an instructional and encouraging tone suitable for learners.
-   **No Copyright Violations**: Ensure all content is original or properly attributed.

## 7. Versioning

-   Specify exact versions for tools and frameworks (e.g., ROS 2 Humble, Python 3.8).
-   Note any version-specific considerations.
