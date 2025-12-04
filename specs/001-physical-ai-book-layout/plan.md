# Implementation Plan: High-Level Book Layout – Physical AI & Humanoid Robotics

**Branch**: `001-physical-ai-book-layout` | **Date**: 2025-12-04 | **Spec**: specs/001-physical-ai-book-layout/spec.md
**Input**: Feature specification from `/specs/001-physical-ai-book-layout/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan outlines the comprehensive technical strategy for developing the "Teaching Physical AI & Humanoid Robotics" book. It defines the architecture, content pipeline, research, quality validation, and key decisions for a Docusaurus-based, AI-assisted, and GitHub Pages-deployed project, aligning with a 4-module curriculum.

## Technical Context

**Language/Version**: Python (for ROS 2, simulation scripting, AI models), JavaScript/TypeScript (for Docusaurus, React components).
**Primary Dependencies**: Docusaurus, GitHub Pages, Claude Code, Spec-Kit Plus, ROS 2, Gazebo, Unity, NVIDIA Isaac (Isaac Sim, Isaac ROS, Nav2), Whisper (for speech-to-text).
**Storage**: Markdown files (book content), Git repository (source control), static assets (images, videos).
**Testing**: Docusaurus build validation (zero warnings/errors), automated code example execution, broken link checking, lab reproducibility checks.
**Target Platform**: Web (Static site via GitHub Pages), Linux (for local ROS 2, Gazebo, Unity, NVIDIA Isaac development/labs), Jetson Orin (Edge AI deployment).
**Project Type**: Single project (Docusaurus documentation site).
**Performance Goals**: Docusaurus build times: Target < 2 minutes for full production build, responsive website performance (e.g., Largest Contentful Paint < 2.5s, First Input Delay < 100ms), real-time AI pipeline execution for labs, low-latency robot control in simulation (e.g., control loop latency < 50ms).
**Constraints**: Markdown-only content, SEO-friendly headings/front-matter, all content original and copyright-free, spec-first content generation, AI-assisted writing with mandatory human review, technical accuracy verifiable from trusted sources.
**Scale/Scope**: 4 Modules, ~20 Chapters, ~60 Lessons, ~20 Labs; guiding learners from zero robotics knowledge to building a fully autonomous humanoid system.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

This plan adheres to the project's Constitution, ensuring:

*   [ ] **Spec-first Content Generation**: Every chapter will originate from an approved written spec.
*   [ ] **AI-Assisted Writing with Human Review**: All AI-generated content will undergo mandatory human review.
*   [ ] **Technical Accuracy**: All technical claims will be verifiable from official documentation or trusted sources.
*   [ ] **Clear Instructional Writing**: Content will be accessible to a beginner-to-intermediate audience.
*   [ ] **Open-Source Transparency**: The project will maintain open-source transparency and reusability.
*   [ ] **Automation-Oriented Publishing**: The publishing workflow will be highly automated.

Furthermore, this plan adheres to the key standards and constraints:

*   [ ] **Docusaurus Best Practices**: Documentation will conform to Docusaurus best practices.
*   [ ] **Runnable Code Examples**: All code examples will be runnable and tested.
*   [ ] **GitHub Standards**: Repository will follow full Git version history, clear commit messages, and public issue tracking.
*   [ ] **No Copyright Violations**: All content will be original and free from copyright violation.
*   [ ] **Markdown-only Content**: Content will be in Markdown format.
*   [ ] **SEO-friendly**: Headings and front-matter will be SEO-friendly.

## Project Structure

### Documentation (this feature)

```text
specs/001-physical-ai-book-layout/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
.github/                     # GitHub Actions workflows for CI/CD
docs/                        # All book content (modules, chapters, lessons, labs) as Markdown files
├── module1/                 # The Robotic Nervous System (ROS 2)
│   ├── chapter1/
│   │   ├── lesson1.md
│   │   └── labs/
│   │       └── lab1.py
│   └── ...
├── module2/                 # The Digital Twin (Gazebo & Unity)
├── module3/                 # The AI-Robot Brain (NVIDIA Isaac™)
├── module4/                 # Vision-Language-Action (VLA) & The Autonomous Humanoid Capstone
└── architecture/            # Infrastructure & Lab Architecture documentation
docusaurus.config.js         # Docusaurus configuration
sidebars.js                  # Docusaurus sidebar navigation configuration
src/                         # Docusaurus theme overrides and custom React components
├── css/
├── components/
└── pages/
static/                      # Static assets (images, videos, diagrams)
code_examples/               # Centralized directory for all runnable code examples (Python, C++)
├── module1/
├── module2/
├── module3/
└── module4/
```

**Structure Decision**: The project will follow a Docusaurus-centric structure, with book content organized under `docs/` by module, chapter, lesson, and lab. Common Docusaurus configuration and custom components will reside in their standard locations. A `code_examples/` directory will centralize all runnable code for testing and verification. GitHub Actions will handle CI/CD for publishing.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | N/A | N/A |

## Deliverables

### 1. Architecture Sketch

- **Content Pipeline**:
    - **Spec**: Feature specifications (like the book layout) are created first using Claude Code and Spec-Kit Plus, defining user stories, requirements, and success criteria.
    - **Draft**: AI-assisted content generation (Claude Code) produces initial drafts for chapters and lessons based on approved specs.
    - **Review**: Mandatory human review for technical accuracy, clarity, instructional quality, and alignment with constitution.
    - **Publish**: Content is deployed via Docusaurus to GitHub Pages, triggered by automated CI/CD workflows.
- **Integration with Docusaurus and GitHub Pages**:
    - Docusaurus will serve as the static site generator, converting Markdown content (`docs/`) into HTML.
    - GitHub Pages will host the compiled Docusaurus site, enabling automated deployment upon merges to the main branch.
    - Version control and collaboration will be managed entirely through GitHub.
- **AI-assisted Writing Workflow (Claude Code + Spec-Kit Plus)**:
    - Claude Code assists in generating detailed specifications, drafting chapter content, and creating runnable code examples.
    - Spec-Kit Plus templates and scripts standardize the development process (spec, plan, tasks, PHR, ADR).
    - AI is used for content generation, not as a final authority; human review is mandatory.
- **Code Example Management (Run, Test, Validate)**:
    - All code examples (`code_examples/`) will be version-controlled and tested.
    - Automated scripts (e.g., Python `pytest`, ROS 2 `colcon test`) will verify code correctness and executability within a Dockerized environment (or similar consistent setup).
    - Code will be linked directly from lessons within Docusaurus documentation.
- **Infrastructure for Lab Simulations, Edge AI, and Optional Cloud Resources**:
    - **Simulation**: Docker containers pre-configured with ROS 2, Gazebo, Unity (via headless rendering or client access) for reproducible lab environments.
    - **Edge AI**: Guidance and setup for Jetson Orin devices, including flashing OS, installing NVIDIA Isaac SDKs, and deploying trained models.
    - **Cloud**: Optional cloud resources (e.g., AWS EC2, NVIDIA Omniverse Cloud) for running demanding simulations or AI training, with clear instructions for setup and cost management.
- **Repository Structure**: As detailed in "Source Code (repository root)" above.

### 2. Section Structure (Modules → Chapters → Lessons → Labs)

- **Mapping Business Requirements to Technical Sections**:
    - Each of the 4 Modules in `spec.md` will map to a top-level directory under `docs/` (e.g., `docs/module1-ros2/`).
    - Within each module, distinct Chapters will be created as subdirectories or Markdown files (e.g., `docs/module1-ros2/chapter1-ros2-basics/`).
    - Lessons will be individual Markdown files within chapters (e.g., `docs/module1-ros2/chapter1-ros2-basics/lesson1-nodes-topics.md`).
    - Practical Labs will be associated with specific lessons or chapters, linked directly from the Markdown and having their code in `code_examples/`.
- **Dependencies Between Chapters and Modules**:
    - **Module 1 (ROS 2)** is foundational; subsequent modules depend on its concepts.
    - **Module 2 (Simulation)** builds on Module 1's ROS 2 knowledge.
    - **Module 3 (NVIDIA Isaac)** depends on both ROS 2 and simulation concepts.
    - **Module 4 (VLA Capstone)** integrates all prior modules.
    - Explicit `prerequisites` will be noted in chapter/lesson front-matter where applicable.
- **Metadata, SEO Strategy, and Content Tagging for Docusaurus**:
    - Each Markdown file will include Docusaurus front-matter for `title`, `description` (for SEO), `keywords`, and `sidebar_label`.
    - `docusaurus.config.js` will be configured for SEO (sitemap, robots.txt, canonical URLs).
    - Content will use semantic headings (H1, H2, H3) for clarity and SEO.
    - Custom tags will be explored for filtering/categorization (e.g., `ros2`, `gazebo`, `isaac`, `lab`).

### 3. Research Approach

- **Research-Concurrent Strategy**: Research will be conducted iteratively alongside content generation, rather than a monolithic upfront phase. This allows for dynamic integration of the latest information and deep dives as specific content needs arise.
- **Identify Key Primary and Trusted Sources**:
    - **ROS 2**: Official ROS 2 documentation, ROS Industrial, OSRF resources.
    - **NVIDIA Isaac**: NVIDIA developer documentation, Isaac Sim/ROS/Nav2 official guides, Jetson documentation.
    - **Gazebo**: Gazebo official documentation, Open Robotics resources.
    - **Unity**: Unity documentation for Robotics, simulation packages.
    - **Docusaurus**: Official Docusaurus documentation.
- **Citation Management (APA Style)**:
    - All external technical claims and facts will be cited using APA style, typically through footnotes or inline references to maintain readability within Markdown.
    - A dedicated `references.md` file (or similar) will aggregate all citations.
- **Verification of Technical Accuracy Before Publishing**:
    - Every technical claim will be cross-referenced with at least two trusted primary sources.
    - Code examples will be executed in a verified environment to confirm functionality.
    - Technical content will undergo peer review by subject matter experts if available.

### 4. Quality Validation / Testing Strategy

- **Ensure all Code Examples are Runnable and Tested**:
    - A CI/CD pipeline (GitHub Actions) will include jobs to clone the `code_examples/` repository.
    - Automated scripts will run all Python, C++, or ROS 2 specific examples.
    - Test failures will block content publication.
    - Output of successful runs will be captured and potentially included in documentation.
- **Validate that Docusaurus Build Produces Zero Warnings/Errors**:
    - The CI/CD pipeline will execute `npm install && npm run build` for the Docusaurus site.
    - Any build warnings or errors will fail the CI/CD pipeline, preventing deployment.
- **Check for Broken Links, Missing Images, and Incomplete References**:
    - Docusaurus provides built-in link checking during build; this will be enabled and strictly enforced.
    - Custom scripts may be developed to verify image paths and external links more robustly if needed.
    - Regular manual review will supplement automated checks.
- **Validate Alignment with Learning Objectives and Success Criteria in Constitution**:
    - Manual review against `spec.md` and `.specify/memory/constitution.md` will confirm content covers learning outcomes.
    - Success criteria from `spec.md` and the Constitution (`SC-001` to `SC-007`) will form a checklist for each module/chapter during review.
- **Include Lab Reproducibility Checks**:
    - Lab instructions will be tested end-to-end by an independent party (or automated script in a clean environment).
    - Dockerfiles or virtual machine configurations for lab environments will be version-controlled and verified.

### 5. Decisions Needing Documentation (ADRs)

- **Hardware vs. Cloud-based Simulation Strategy**:
    - **Options**: Pure on-premise, pure cloud, hybrid.
    - **Trade-offs**: Cost, accessibility, performance, ease of setup, reproducibility.
    - **Rationale**: Balance high-fidelity requirements with student accessibility and cost-effectiveness.
- **Edge Device Selection (Jetson Variants, Sensors)**:
    - **Options**: Jetson Nano, Xavier NX, Orin Nano/NX. Specific sensor models (e.g., Intel RealSense, LiDAR).
    - **Trade-offs**: Processing power, cost, power consumption, ecosystem support.
    - **Rationale**: Select devices that offer a good balance for learning while being capable of running practical AI applications.
- **Choice of Humanoid Robots (Proxy vs Miniature vs Premium)**:
    - **Options**: Simulated-only, mini-humanoids (e.g., OpenCR), proxy robot arms, full-size humanoids.
    - **Trade-offs**: Cost, complexity, accessibility, physical safety, realism.
    - **Rationale**: Start with simulation, then introduce conceptual understanding of hardware categories, possibly focusing on proxy/miniature for affordable hands-on labs.
- **ROS 2 Versions, Python Versions, and Simulation Environment Setup**:
    - **Options**: Specific ROS 2 distros (e.g., Humble, Iron), Python 3.8+, Ubuntu LTS versions.
    - **Trade-offs**: Stability, feature set, community support, compatibility with NVIDIA Isaac/Gazebo/Unity.
    - **Rationale**: Select stable LTS versions with good community support and proven compatibility across the toolchain.
- **Tradeoffs between Fidelity, Cost, and Student Accessibility**:
    - **Options**: High-fidelity, high-cost; medium-fidelity, medium-cost; lower-fidelity, low-cost.
    - **Trade-offs**: Realism of simulations, hardware requirements, budget for students, ease of setup.
    - **Rationale**: Prioritize student accessibility and learning outcomes, using high-fidelity only when critical for demonstrating concepts.
- **Lab Workflow Design (On-premise vs Cloud, Latency Management)**:
    - **Options**: Fully local Docker-based setup, cloud-based VMs/services, combination.
    - **Trade-offs**: Ease of setup, required internet bandwidth, cost of cloud, latency for real-time interaction.
    - **Rationale**: Provide clear guidance for both local and cloud options, emphasizing reproducible setups and strategies to mitigate latency in interactive labs.

## Technical Details (Phased Approach)

- **Organize by phases: Research → Foundation → Analysis → Synthesis**:
    1.  **Phase 0: Research (Concurrent)**: Ongoing research into primary sources, latest versions of ROS 2, NVIDIA Isaac, Gazebo, Unity. Capture findings in `specs/001-physical-ai-book-layout/research.md`.
    2.  **Phase 1: Foundation (Architecture & Structure)**: Define the initial Docusaurus project structure, configure CI/CD for build/deployment, establish Markdown content guidelines, and finalize module/chapter/lesson/lab mapping. Capture data models (if any) in `data-model.md` and initial quickstart instructions in `quickstart.md`.
    3.  **Phase 2: Analysis (Content Generation & Drafts)**: AI-assisted generation of initial chapter/lesson drafts based on `spec.md` and research findings. Focus on core concepts and initial code examples.
    4.  **Phase 3: Synthesis (Review, Refine & Test)**: Human review for technical accuracy, clarity, and instructional quality. Integration of runnable code examples, comprehensive testing (Docusaurus build, link checking, code execution), and refinement based on feedback.
- **Use concurrent research approach for technical accuracy while writing**: Integrate new research findings directly into the content and update existing sections as needed, ensuring the book remains current.
- **Follow APA citation style from Constitution**: Implement a consistent citation mechanism across all content.
- **Include risk assessment for reproducibility and infrastructure**:
    - **Risk**: Environment setup complexity for labs.
    - **Mitigation**: Provide Dockerfiles, pre-configured VMs, or cloud templates; clearly document minimum hardware requirements.
    - **Risk**: Outdated dependencies or breaking changes in robotics/AI frameworks.
    - **Mitigation**: Specify exact version numbers for all tools; implement a versioning strategy and update policy for the book; include automated dependency checks in CI/CD.
- **Provide actionable steps for automation-first workflow and publishing**:
    - Automate Docusaurus build and deployment via GitHub Actions.
    - Automate testing of all code examples.
    - Automate broken link checking.
    - Implement scripts for content generation/validation where appropriate (e.g., checking front-matter adherence).

## Success Criteria

- Plan is complete and executable as a technical roadmap.
- All infrastructure, lab, and software decisions documented with rationale.
- Section structure aligns 100% with 4-module curriculum.
- Plan is ready for `/sp.specify` creation per module and chapter.
- Clear validation strategy for code, Docusaurus build, and lab reproducibility.
