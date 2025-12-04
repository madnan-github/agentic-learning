/sp.constitution

Project: AI/Spec-Driven Book Creation using Docusaurus and GitHub Pages

Core principles:

* Spec-first content generation (no chapter written without prior specification)
* AI-assisted writing with mandatory human review
* Technical accuracy through official documentation verification
* Clear, beginner-to-intermediate friendly instructional writing
* Open-source transparency and community reusability
* Automation-oriented publishing workflow

Key standards:

* Every chapter must originate from an approved written spec
* All technical claims must be verifiable from official or trusted sources
* Code examples must be runnable and tested before publishing
* Documentation must conform to Docusaurus best practices
* Repository standards:

  * Full Git version history
  * Clear commit messages
  * Public issue tracking enabled
* Writing must follow structured instructional flow
* AI-generated content must be reviewed, edited, and validated

Constraints:

* Book format: Static documentation website (Docusaurus)
* Hosting: GitHub Pages only
* Source control: GitHub mandatory
* AI tools: Claude Code + Spec-Kit Plus only
* Content pipeline: Spec → Draft → Review → Publish
* All content must be original and free from copyright violation
* No hallucinated tools, APIs, libraries, or frameworks
* Markdown-only content format
* SEO-friendly headings and front-matter required

Success criteria:

* Live, fully functional book deployed via GitHub Pages
* 100% of chapters derived from approved specs
* Zero broken links across the site
* All code examples execute without errors
* Clean Docusaurus production build with zero warnings
* Repository is reusable as an open-source learning template
* Book is fully self-learnable without external guidance
________________________________________________

/sp.specify  High-Level Book Layout – Physical AI & Humanoid Robotics (Official 4 Modules)

Book Title:
Physical AI & Humanoid Robotics: From Simulation to Embodied Intelligence

Primary Objective:
To guide learners from zero robotics knowledge to building a fully autonomous humanoid system using ROS 2, simulation, NVIDIA Isaac, and Vision-Language-Action intelligence.

Teaching Philosophy:
Spec-first → Sim-first → AI-first → Hardware-last

---

Module 1: The Robotic Nervous System (ROS 2)

Objective:
Teach the foundational software backbone required to control physical and humanoid robots using ROS 2.

Learning Outcomes:

* Understand Physical AI and embodied intelligence concepts
* Master ROS 2 core architecture and communication models
* Build ROS 2 packages using Python
* Model humanoid robots using URDF
* Integrate basic robot sensors

Content Scope:

* Physical AI vs Digital AI
* ROS 2 architecture
* Nodes, Topics, Services, Actions
* rclpy Python robotics
* Launch systems & parameters
* URDF for humanoid modeling
* Sensors: LiDAR, RGB & Depth Cameras, IMUs, Force/Torque

Practical Lab:

* Build a ROS 2 workspace
* Create ROS 2 publisher/subscriber nodes
* Simulate a URDF humanoid skeleton
* Attach virtual sensors to the robot

Teaching Style:

* Concept → Visualization → Demo → Hands-on lab
* Beginner-friendly, command-driven robotics

Success Criteria:

* Learner successfully runs ROS 2 nodes
* Humanoid URDF loads correctly
* Sensor data streams inside ROS

Not in Scope:

* AI perception
* Navigation
* Machine learning
* Real hardware deployment

---

Module 2: The Digital Twin (Gazebo & Unity)

Objective:
Enable learners to create realistic simulation environments for humanoid robots.

Learning Outcomes:

* Build Gazebo simulations
* Apply robot physics and dynamics
* Simulate humanoid sensors
* Visualize robots using Unity
* Validate robot behaviors safely

Content Scope:

* Gazebo environment setup
* Rigid body physics
* URDF & SDF formats
* Sensor simulation (LiDAR, depth, IMU)
* Humanoid behavior testing
* Unity rendering & visualization
* Sim-based human-robot interaction

Practical Lab:

* Simulate a humanoid robot in Gazebo
* Add gravity, collisions, sensors
* Visualize motion using Unity

Teaching Style:

* Simulation-first learning
* Visual debugging through virtual worlds

Success Criteria:

* Robot behaves correctly in simulation
* Sensors output realistic data
* Unity visualization is synchronized

Not in Scope:

* AI training
* Reinforcement learning
* Real-world sensor drivers

---

Module 3: The AI-Robot Brain (NVIDIA Isaac™)

Objective:
Endow humanoid robots with perception, navigation, and learning intelligence.

Learning Outcomes:

* Understand NVIDIA Isaac ecosystem
* Perform AI-based perception using Isaac ROS
* Implement Visual SLAM
* Deploy Nav2 navigation
* Train robots using reinforcement learning
* Perform sim-to-real transfer
* Deploy AI on Jetson Orin

Content Scope:

* Isaac Sim
* Synthetic data generation
* Isaac ROS acceleration
* VSLAM
* Nav2 navigation stack
* AI perception pipelines
* Reinforcement learning
* Sim-to-real techniques
* Edge AI with Jetson

Practical Lab:

* Train a robot using synthetic data
* Deploy VSLAM + Nav2 in simulation
* Run perception models on Jetson

Teaching Style:

* AI system pipeline learning
* Performance-driven robotics engineering

Success Criteria:

* Robot navigates autonomously in simulation
* Perception model detects objects
* AI pipeline runs in real time

Not in Scope:

* LLM task planning
* Speech & natural language control

---

Module 4: Vision-Language-Action (VLA) & The Autonomous Humanoid Capstone

Objective:
Fuse language, vision, and robotics into a fully autonomous humanoid system.

Learning Outcomes:

* Convert voice into robot actions
* Use LLMs for robot task planning
* Implement multimodal robot cognition
* Build a full autonomous humanoid pipeline

Content Scope:

* Vision-Language-Action architecture
* Speech-to-text using Whisper
* Natural language understanding
* LLM-based task planning
* ROS 2 action graph automation
* Multimodal interaction (speech + vision + gestures)
* End-to-end humanoid system integration

Practical Lab:

* Issue voice commands to a humanoid
* Perform object detection + navigation
* Execute manipulation tasks
* Run full autonomous mission in simulation

Teaching Style:

* System integration engineering
* Real-world autonomy workflow

Success Criteria:

* Robot obeys spoken commands
* Robot navigates, detects, and manipulates objects autonomously
* Full autonomous demo completes successfully

Not in Scope:

* Advanced humanoid biomechanics research
* Military-grade robotics systems

---

Infrastructure & Lab Architecture (Applies to All Modules)

Objective:
Define the computing and hardware environment for Physical AI development.

Learning Outcomes:

* Design on-prem and cloud-based Physical AI labs
* Select edge devices and sensors correctly
* Plan sim-to-real deployment safely

Content Scope:

* RTX workstations
* Ubuntu robotics setups
* Cloud Isaac Sim
* Jetson Orin edge deployment
* Sensor kits
* Proxy robots, mini humanoids, full humanoids
* Safety, latency, and cost strategy

Practical Lab:

* Build a virtual Physical AI lab architecture
* Validate hardware + cloud workflows

Teaching Style:

* Infrastructure-first systems engineering

Success Criteria:

* Lab architecture supports full pipeline
* Simulation, AI, and deployment all function cohesively

Not in Scope:

* Vendor-specific procurement contracts

---

Scope Control Note:
This is the **high-level instructional constitution for the Physical AI book**.
All upcoming `/sp.specify` prompts will expand each module into **chapters → lessons → labs** in the second iteration.


----------------------------------------------------------------

/sp.plan

Create a comprehensive technical plan for the book **"Teaching Physical AI & Humanoid Robotics"** using Docusaurus, Claude Code, and Spec-Kit Plus.

---

Objectives:

- Define the full technical architecture and structure for the book project.
- Identify research approach, section layout, and technical dependencies.
- Establish quality validation and testing strategy aligned with Constitution success criteria.
- Document important technical decisions with options, tradeoffs, and reasoning.
- Ensure the plan aligns with the 4-module course curriculum and hands-on labs.

---

Deliverables:

1. **Architecture Sketch**
   - Diagram/description of the content pipeline:
     - Spec → Draft → Review → Publish
     - Integration with Docusaurus and GitHub Pages
     - AI-assisted writing workflow (Claude Code + Spec-Kit Plus)
     - Code example management (run, test, validate)
   - Infrastructure for lab simulations, Edge AI, and optional cloud resources
   - Repository structure (chapters, modules, labs, assets, code)

2. **Section Structure**
   - Modules → Chapters → Lessons → Labs
   - Mapping of business requirements (learning outcomes, teaching style, practical labs) to technical sections
   - Highlight dependencies between chapters and modules
   - Include metadata, SEO strategy, and content tagging for Docusaurus

3. **Research Approach**
   - Research-concurrent strategy (research while writing, not all upfront)
   - Identify key primary and trusted sources (official documentation, NVIDIA Isaac, ROS 2, Gazebo, Unity)
   - Citation management (APA style)
   - Verification of technical accuracy before publishing

4. **Quality Validation / Testing Strategy**
   - Ensure all code examples are runnable and tested
   - Validate that Docusaurus build produces zero warnings/errors
   - Check for broken links, missing images, and incomplete references
   - Validate alignment with learning objectives and success criteria in Constitution
   - Include lab reproducibility checks

5. **Decisions Needing Documentation**
   - Hardware vs. Cloud-based simulation strategy
   - Edge device selection (Jetson variants, sensors)
   - Choice of humanoid robots (proxy vs miniature vs premium)
   - ROS 2 versions, Python versions, and simulation environment setup
   - Tradeoffs between fidelity, cost, and student accessibility
   - Lab workflow design (on-premise vs cloud, latency management)

---

Technical Details:

- Organize by phases: **Research → Foundation → Analysis → Synthesis**
- Use concurrent research approach for technical accuracy while writing
- Follow APA citation style from Constitution
- Include risk assessment for reproducibility and infrastructure
- Provide actionable steps for automation-first workflow and publishing

---

Success Criteria:

- Plan is complete and executable as a technical roadmap
- All infrastructure, lab, and software decisions documented with rationale
- Section structure aligns 100% with 4-module curriculum
- Plan is ready for `/sp.specify` creation per module and chapter
- Clear validation strategy for code, Docusaurus build, and lab reproducibility

